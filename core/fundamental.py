"""
core/fundamental.py
ファンダメンタル考察: 急騰に材料(Catalyst)があるかを判定する

判定フロー:
    1. CryptoPanic API で直近 FUNDAMENTAL_LOOKBACK_HOURS 以内のニュースを取得
    2. ヘッドラインをキーワード分類
       - 正材料: listing, partnership, mainnet launch, upgrade... → AVOID
       - 悪材料: hack, exploit, rug, scam...                    → MEDIUM
       - ニュースなし                                            → HIGH (材料なし急騰)
    3. ショート確信度 (short_conviction) を返す

API キーが未設定の場合:
    ファンダ判定をスキップし conviction=MEDIUM (中立) でフォールスルーする。
    CryptoPanic 無料枠: https://cryptopanic.com/developers/api/
"""
from __future__ import annotations

import logging
import os
import time
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from typing import Any

import requests

logger = logging.getLogger(__name__)

# ───────────────────────────────────────────────
# キーワード辞書
# ───────────────────────────────────────────────

_POSITIVE_KEYWORDS: list[str] = [
    # 上場・提携
    "listing", "listed", "exchange listing", "partnership", "collaboration",
    "integration", "strategic",
    # 開発・ローンチ
    "mainnet", "launch", "upgrade", "v2", "v3", "migration",
    "airdrop", "staking", "burn", "buyback",
    # 機関系
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
    base_currency: str          # "LAB/USDT:USDT" → "LAB"

    # ニュース情報
    news_count: int             # lookback 期間内のニュース件数 (-1 = API未設定)
    top_headlines: list[str] = field(default_factory=list)

    # 判定
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


# ───────────────────────────────────────────────
# アナライザー
# ───────────────────────────────────────────────

class FundamentalAnalyzer:
    """急騰銘柄のファンダメンタル考察を行い、ショート確信度を返す。

    テクニカル確認済みシグナルに対して呼び出し、
    「なぜ上がっているか」を材料面から評価する。
    """

    CRYPTOPANIC_URL = "https://cryptopanic.com/api/v1/posts/"

    def __init__(self) -> None:
        self._api_key: str = os.getenv("CRYPTOPANIC_API_KEY", "")
        self._lookback_hours: int = int(
            os.getenv("FUNDAMENTAL_LOOKBACK_HOURS", "48")
        )
        if not self._api_key:
            logger.warning(
                "CRYPTOPANIC_API_KEY not set. Fundamental analysis will be skipped "
                "(conviction defaults to MEDIUM)."
            )

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def analyze(self, symbol: str) -> FundamentalResult:
        """単一銘柄のファンダメンタル考察を実行する。

        Args:
            symbol: 例 "LAB/USDT:USDT"
        Returns:
            FundamentalResult
        """
        base = self._extract_base(symbol)

        if not self._api_key:
            return FundamentalResult(
                symbol=symbol,
                base_currency=base,
                news_count=-1,
                catalyst_type="UNKNOWN",
                short_conviction="MEDIUM",
                reason="API key not set. Skipping fundamental check.",
            )

        news = self._fetch_news(base)
        result = self._evaluate(symbol, base, news)
        self._log_result(result)
        return result

    def analyze_batch(self, symbols: list[str]) -> dict[str, FundamentalResult]:
        """複数銘柄を一括考察する。

        Args:
            symbols: シンボルのリスト
        Returns:
            {symbol: FundamentalResult} の辞書
        """
        results: dict[str, FundamentalResult] = {}
        for symbol in symbols:
            results[symbol] = self.analyze(symbol)
        return results

    # ------------------------------------------------------------------
    # Internal
    # ------------------------------------------------------------------

    @staticmethod
    def _extract_base(symbol: str) -> str:
        """'LAB/USDT:USDT' → 'LAB'"""
        return symbol.split("/")[0]

    def _fetch_news(self, currency: str) -> list[dict[str, Any]]:
        """CryptoPanic API でニュースを取得する。

        Args:
            currency: 通貨シンボル (例: "LAB")
        Returns:
            lookback 期間内のニュース記事リスト
        """
        try:
            resp = requests.get(
                self.CRYPTOPANIC_URL,
                params={
                    "auth_token": self._api_key,
                    "currencies": currency,
                    "filter": "all",
                    "public": "true",
                },
                timeout=10,
            )
            resp.raise_for_status()
            articles: list[dict[str, Any]] = resp.json().get("results", [])

            cutoff = datetime.now(timezone.utc) - timedelta(
                hours=self._lookback_hours
            )
            recent = []
            for article in articles:
                pub = article.get("published_at", "")
                try:
                    dt = datetime.fromisoformat(pub.replace("Z", "+00:00"))
                    if dt >= cutoff:
                        recent.append(article)
                except (ValueError, TypeError):
                    pass

            # Rate limit への配慮
            time.sleep(0.5)
            return recent

        except requests.RequestException as e:
            logger.warning("CryptoPanic request failed for %s: %s", currency, e)
            return []
        except Exception as e:
            logger.error("Unexpected error in _fetch_news for %s: %s", currency, e)
            return []

    def _evaluate(
        self,
        symbol: str,
        base: str,
        news: list[dict[str, Any]],
    ) -> FundamentalResult:
        """ニュースリストを解析し、catalyst 判定と conviction を返す。"""
        headlines = [a.get("title", "") for a in news[:5]]

        # ─── ニュースなし ───────────────────────────────────
        if not news:
            return FundamentalResult(
                symbol=symbol,
                base_currency=base,
                news_count=0,
                top_headlines=[],
                catalyst_type="NONE",
                short_conviction="HIGH",
                reason=(
                    f"No news found in the last {self._lookback_hours}h. "
                    "Pump has no visible fundamental catalyst → HIGH conviction short."
                ),
            )

        # ─── キーワード分類 ───────────────────────────────────
        all_text = " ".join(
            (a.get("title", "") + " " + a.get("body", "")).lower()
            for a in news
        )

        has_positive = any(kw in all_text for kw in _POSITIVE_KEYWORDS)
        has_negative = any(kw in all_text for kw in _NEGATIVE_KEYWORDS)

        if has_negative:
            return FundamentalResult(
                symbol=symbol,
                base_currency=base,
                news_count=len(news),
                top_headlines=headlines,
                catalyst_type="NEGATIVE",
                short_conviction="MEDIUM",
                reason=(
                    f"Negative news detected ({len(news)} article(s)). "
                    "Bad-news-driven pump tends to be short-lived → MEDIUM conviction short."
                ),
            )

        if has_positive:
            return FundamentalResult(
                symbol=symbol,
                base_currency=base,
                news_count=len(news),
                top_headlines=headlines,
                catalyst_type="POSITIVE",
                short_conviction="AVOID",
                reason=(
                    f"Positive catalyst found ({len(news)} article(s)). "
                    "Pump may be fundamentally justified → AVOID short."
                ),
            )

        # ニュースはあるが明確なキーワードなし
        return FundamentalResult(
            symbol=symbol,
            base_currency=base,
            news_count=len(news),
            top_headlines=headlines,
            catalyst_type="WEAK",
            short_conviction="MEDIUM",
            reason=(
                f"{len(news)} article(s) found but no clear catalyst keyword matched. "
                "Proceed with caution → MEDIUM conviction short."
            ),
        )

    @staticmethod
    def _log_result(result: FundamentalResult) -> None:
        conviction_label = {
            "HIGH":   "[FUND HIGH  ]",
            "MEDIUM": "[FUND MED   ]",
            "LOW":    "[FUND LOW   ]",
            "AVOID":  "[FUND AVOID ]",
        }.get(result.short_conviction, "[FUND ???   ]")

        logger.info(
            "%s %s | catalyst=%s news=%d",
            conviction_label,
            result.symbol,
            result.catalyst_type,
            result.news_count,
        )
        logger.info("  %s", result.reason)
        for headline in result.top_headlines[:3]:
            logger.info("  > %s", headline)
