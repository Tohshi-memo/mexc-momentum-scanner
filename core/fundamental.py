"""
core/fundamental.py
ファンダメンタル考察: 急騰に材料(Catalyst)があるかを判定する

無料ソースのみを使用 (APIキー不要):
    1. RSS フィード (CoinDesk / CoinTelegraph / Decrypt / BeInCrypto)
    2. Reddit JSON 検索 (認証不要)

判定フロー:
    1. 複数の無料ソースから直近 FUNDAMENTAL_LOOKBACK_HOURS 以内のニュースを収集
    2. ヘッドラインをキーワード分類
       - 正材料: listing, partnership, mainnet launch, upgrade... → AVOID
       - 悪材料: hack, exploit, rug, scam...                    → MEDIUM
       - ニュースなし                                            → HIGH (材料なし急騰)
    3. ショート確信度 (short_conviction) を返す

小規模アルトはニュースに出ないことが多いが、
「ニュースなし = 材料なし急騰」として HIGH conviction で扱うため問題なし。
"""
from __future__ import annotations

import logging
import time
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from typing import Any
import os

import requests

logger = logging.getLogger(__name__)

# ───────────────────────────────────────────────
# RSS フィード一覧 (無料・認証不要)
# ───────────────────────────────────────────────

_RSS_FEEDS: list[str] = [
    "https://www.coindesk.com/arc/outboundfeeds/rss/",
    "https://cointelegraph.com/rss",
    "https://decrypt.co/feed",
    "https://beincrypto.com/feed/",
]

# ───────────────────────────────────────────────
# キーワード辞書
# ───────────────────────────────────────────────

_POSITIVE_KEYWORDS: list[str] = [
    "listing", "listed", "exchange listing", "partnership", "collaboration",
    "integration", "strategic",
    "mainnet", "launch", "upgrade", "v2", "v3", "migration",
    "airdrop", "staking", "burn", "buyback",
    "etf", "institutional", "fund", "investment",
]

_NEGATIVE_KEYWORDS: list[str] = [
    "hack", "hacked", "exploit", "exploited",
    "rug", "rug pull", "scam", "fraud",
    "lawsuit", "sec", "ban", "seized",
    "ponzi", "exit scam",
]


# ───────────────────────────────────────────────
# データクラス
# ───────────────────────────────────────────────

@dataclass
class FundamentalResult:
    """ファンダメンタル考察の結果。"""

    symbol: str
    base_currency: str

    news_count: int             # 検出記事数 (-1 = スキップ)
    top_headlines: list[str] = field(default_factory=list)

    catalyst_type: str = "UNKNOWN"
    # "NONE"     → 材料なし → 根拠のない急騰の可能性が高い
    # "POSITIVE" → 正材料あり → 上昇に正当性がある可能性
    # "NEGATIVE" → 悪材料あり → 悪材料での逆張り急騰
    # "WEAK"     → ニュースはあるが明確な材料なし
    # "UNKNOWN"  → データ取得不可

    short_conviction: str = "MEDIUM"
    # "HIGH"   → 強い確信 (材料なし急騰)
    # "MEDIUM" → 中程度 (悪材料 or データ不足)
    # "LOW"    → 弱い確信
    # "AVOID"  → ショート非推奨 (正材料あり)

    reason: str = ""
    sources_checked: int = 0    # 参照ソース数
    sources_succeeded: int = 0  # 正常応答を確認できたソース数


# ───────────────────────────────────────────────
# アナライザー
# ───────────────────────────────────────────────

class FundamentalAnalyzer:
    """急騰銘柄のファンダメンタル考察を行い、ショート確信度を返す。

    無料 RSS フィードと Reddit JSON API を使用。APIキー不要。
    """

    _REDDIT_SEARCH = "https://www.reddit.com/search.json"
    _REDDIT_SUBS   = "https://www.reddit.com/r/{sub}/search.json"

    def __init__(self) -> None:
        self._lookback_hours: int = int(
            os.getenv("FUNDAMENTAL_LOOKBACK_HOURS", "48")
        )
        self._use_reddit: bool = (
            os.getenv("USE_REDDIT_NEWS", "true").lower() != "false"
        )
        self._sources_attempted: int = 0
        self._sources_succeeded: int = 0
        logger.info(
            "FundamentalAnalyzer: RSS + Reddit mode "
            "(lookback=%dh, reddit=%s)",
            self._lookback_hours, self._use_reddit,
        )

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def analyze(self, symbol: str) -> FundamentalResult:
        """単一銘柄のファンダメンタル考察を実行する。"""
        base = self._extract_base(symbol)
        articles = self._collect_news(base)
        result = self._evaluate(symbol, base, articles)
        self._log_result(result)
        return result

    def analyze_batch(self, symbols: list[str]) -> dict[str, FundamentalResult]:
        return {s: self.analyze(s) for s in symbols}

    # ------------------------------------------------------------------
    # News Collection
    # ------------------------------------------------------------------

    def _collect_news(self, currency: str) -> list[dict[str, Any]]:
        """RSS + Reddit から記事を収集し、cutoff 以内のものだけ返す。"""
        self._sources_attempted = 0
        self._sources_succeeded = 0
        cutoff = datetime.now(timezone.utc) - timedelta(hours=self._lookback_hours)
        articles: list[dict[str, Any]] = []

        # RSS フィード
        rss_articles = self._fetch_rss(currency, cutoff)
        articles.extend(rss_articles)
        logger.debug("RSS: %d article(s) found for %s", len(rss_articles), currency)

        # Reddit
        if self._use_reddit:
            reddit_articles = self._fetch_reddit(currency, cutoff)
            articles.extend(reddit_articles)
            logger.debug("Reddit: %d post(s) found for %s", len(reddit_articles), currency)

        return articles

    def _fetch_rss(
        self, currency: str, cutoff: datetime
    ) -> list[dict[str, Any]]:
        """複数の RSS フィードを取得し、通貨名を含む記事を返す。"""
        try:
            import feedparser  # noqa: PLC0415
        except ImportError:
            logger.warning("feedparser not installed. Skipping RSS. Run: pip install feedparser")
            return []

        results: list[dict[str, Any]] = []
        search_term = currency.lower()

        for feed_url in _RSS_FEEDS:
            self._sources_attempted += 1
            try:
                feed = feedparser.parse(feed_url)
                status = getattr(feed, "status", None)
                if status is not None and int(status) >= 400:
                    raise RuntimeError(f"HTTP {status}")
                if getattr(feed, "bozo", False) and not getattr(feed, "entries", []):
                    raise RuntimeError(
                        str(getattr(feed, "bozo_exception", "invalid RSS feed"))
                    )
                self._sources_succeeded += 1
                for entry in feed.entries:
                    title   = entry.get("title", "")
                    summary = entry.get("summary", "")
                    combined = (title + " " + summary).lower()

                    if search_term not in combined:
                        continue

                    # 日時パース
                    pub_dt = self._parse_rss_date(entry)
                    if pub_dt and pub_dt < cutoff:
                        continue

                    results.append({
                        "title":  title,
                        "body":   summary,
                        "source": feed_url,
                        "published_at": pub_dt.isoformat() if pub_dt else "",
                    })

                time.sleep(0.3)  # RSS サーバへの負荷軽減

            except Exception as e:
                logger.debug("RSS fetch failed (%s): %s", feed_url, e)

        return results

    def _fetch_reddit(
        self, currency: str, cutoff: datetime
    ) -> list[dict[str, Any]]:
        """Reddit の JSON 検索 API (認証不要) で投稿を取得する。"""
        results: list[dict[str, Any]] = []
        subreddits = ["CryptoCurrency", "CryptoMoonShots", "altcoin"]

        headers = {"User-Agent": "mexc-momentum-scanner/1.0"}

        for sub in subreddits:
            self._sources_attempted += 1
            try:
                resp = requests.get(
                    self._REDDIT_SUBS.format(sub=sub),
                    params={
                        "q":      currency,
                        "sort":   "new",
                        "t":      "day",
                        "limit":  10,
                        "restrict_sr": "true",
                    },
                    headers=headers,
                    timeout=8,
                )
                if resp.status_code != 200:
                    continue
                self._sources_succeeded += 1

                for post in resp.json().get("data", {}).get("children", []):
                    data  = post.get("data", {})
                    title = data.get("title", "")
                    body  = data.get("selftext", "")

                    # 投稿日時チェック
                    created = data.get("created_utc")
                    if created:
                        pub_dt = datetime.fromtimestamp(created, tz=timezone.utc)
                        if pub_dt < cutoff:
                            continue

                    results.append({
                        "title":  title,
                        "body":   body,
                        "source": f"reddit/r/{sub}",
                        "published_at": "",
                    })

                time.sleep(0.5)  # Reddit レートリミット対策

            except Exception as e:
                logger.debug("Reddit fetch failed (r/%s): %s", sub, e)

        return results

    # ------------------------------------------------------------------
    # Evaluation
    # ------------------------------------------------------------------

    def _evaluate(
        self,
        symbol: str,
        base: str,
        articles: list[dict[str, Any]],
    ) -> FundamentalResult:
        """記事リストを解析し catalyst 判定と conviction を返す。"""
        headlines = [a.get("title", "") for a in articles[:5]]
        sources_checked = self._sources_attempted

        if self._sources_succeeded == 0:
            return FundamentalResult(
                symbol=symbol,
                base_currency=base,
                news_count=-1,
                top_headlines=[],
                catalyst_type="UNKNOWN",
                short_conviction="UNKNOWN",
                reason=(
                    "All configured news sources failed or were unavailable. "
                    "Live short conviction cannot be established."
                ),
                sources_checked=sources_checked,
                sources_succeeded=0,
            )

        if not articles:
            return FundamentalResult(
                symbol=symbol,
                base_currency=base,
                news_count=0,
                top_headlines=[],
                catalyst_type="NONE",
                short_conviction="HIGH",
                reason=(
                    f"No news in last {self._lookback_hours}h across "
                    f"{sources_checked} free sources. "
                    "Pump has no visible fundamental catalyst → HIGH conviction short."
                ),
                sources_checked=sources_checked,
                sources_succeeded=self._sources_succeeded,
            )

        all_text = " ".join(
            (a.get("title", "") + " " + a.get("body", "")).lower()
            for a in articles
        )

        has_positive = any(kw in all_text for kw in _POSITIVE_KEYWORDS)
        has_negative = any(kw in all_text for kw in _NEGATIVE_KEYWORDS)

        if has_negative:
            return FundamentalResult(
                symbol=symbol, base_currency=base,
                news_count=len(articles), top_headlines=headlines,
                catalyst_type="NEGATIVE", short_conviction="MEDIUM",
                reason=(
                    f"Negative news detected ({len(articles)} article(s)). "
                    "Bad-news-driven pump tends to be short-lived → MEDIUM conviction."
                ),
                sources_checked=sources_checked,
                sources_succeeded=self._sources_succeeded,
            )

        if has_positive:
            return FundamentalResult(
                symbol=symbol, base_currency=base,
                news_count=len(articles), top_headlines=headlines,
                catalyst_type="POSITIVE", short_conviction="AVOID",
                reason=(
                    f"Positive catalyst found ({len(articles)} article(s)). "
                    "Pump may be fundamentally justified → AVOID short."
                ),
                sources_checked=sources_checked,
                sources_succeeded=self._sources_succeeded,
            )

        return FundamentalResult(
            symbol=symbol, base_currency=base,
            news_count=len(articles), top_headlines=headlines,
            catalyst_type="WEAK", short_conviction="MEDIUM",
            reason=(
                f"{len(articles)} article(s) found but no clear catalyst keyword. "
                "Proceed with caution → MEDIUM conviction."
            ),
            sources_checked=sources_checked,
            sources_succeeded=self._sources_succeeded,
        )

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _extract_base(symbol: str) -> str:
        """'LAB/USDT:USDT' → 'LAB'"""
        return symbol.split("/")[0]

    @staticmethod
    def _parse_rss_date(entry: Any) -> datetime | None:
        """feedparser エントリから datetime を取得する。"""
        import time as time_module  # noqa: PLC0415
        try:
            if hasattr(entry, "published_parsed") and entry.published_parsed:
                return datetime(
                    *entry.published_parsed[:6], tzinfo=timezone.utc
                )
            if hasattr(entry, "updated_parsed") and entry.updated_parsed:
                return datetime(
                    *entry.updated_parsed[:6], tzinfo=timezone.utc
                )
        except Exception:
            pass
        return None

    @staticmethod
    def _log_result(result: FundamentalResult) -> None:
        label = {
            "HIGH":   "[FUND HIGH  ]",
            "MEDIUM": "[FUND MED   ]",
            "LOW":    "[FUND LOW   ]",
            "AVOID":  "[FUND AVOID ]",
        }.get(result.short_conviction, "[FUND ???   ]")

        logger.info(
            "%s %s | catalyst=%s news=%d sources=%d",
            label, result.symbol,
            result.catalyst_type, result.news_count, result.sources_checked,
        )
        logger.info("  %s", result.reason)
        for headline in result.top_headlines[:3]:
            logger.info("  > %s", headline)
