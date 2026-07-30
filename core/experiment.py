"""
core/experiment.py
シャドウトレード追跡: フィルター粒度別 PnL 実験用

スキャナーが拾った全候補（STRICT フィルター confirmed/rejected 問わず）を
仮想エントリーとして追跡し、各候補のフィルター値・outcome・PnL を
data/experiments.json に蓄積する。

これにより、後から「もし RSI 閾値を 70 に下げていたら？」「4h フィルターを
無効にしていたら？」のような re-evaluation が同じデータセットから可能になる。
実トレード（StatsManager）には影響しない。完全に独立した実験データ。

設計のポイント:
    - confirmed_strict フラグで現行フィルター通過の有無を記録
    - filters スナップショットで全指標値を保存（後で任意の閾値で再評価可能）
    - 古い記録は MAX_CLOSED_RECORDS で自動的に切り捨て（ファイルサイズ抑制）
"""
from __future__ import annotations

import json
import logging
import os
from dataclasses import asdict, dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import TYPE_CHECKING

from core.experiment_archive import append_records as _archive_append
from core.live_policy import live_policy_fingerprint

if TYPE_CHECKING:
    from utils.mexc_client import MEXCClient

logger = logging.getLogger(__name__)

EXPERIMENT_FILE = Path("data/experiments.json")

OUTCOME_ACTIVE  = "ACTIVE"
OUTCOME_TP_HIT  = "TP_HIT"
OUTCOME_SL_HIT  = "SL_HIT"
OUTCOME_EXPIRED = "EXPIRED"


@dataclass
class FilterSnapshot:
    """検出時の全フィルター指標値。後から任意の閾値で再評価できる。"""
    rsi:               float | None
    rsi_4h:            float | None
    bb_upper:          float | None
    price_vs_bb:       float           # price / bb_upper (1.0 超で BB break)
    volume_ratio:      float           # 直近1足 vol / 過去N足平均
    volume_trend:      str             # RISING / FLAT / DECLINING
    atr_pct:           float | None
    change_1h:         float
    relative_strength: float           # alt_1h - btc_1h
    btc_change_1h:     float
    funding_rate:      float | None = None  # ファンディングレート (%) 記録のみ
    obv_divergence:    str | None = None    # BEARISH_DIV / BULLISH_DIV / NONE 記録のみ
    open_interest_usd:   float | None = None  # OI の USDT 建て総額 記録のみ
    oi_change_pct:       float | None = None  # 直近1h OI 変化率 (%) 記録のみ
    long_short_ratio:    float | None = None  # ロング/ショート比率 記録のみ
    upper_wick_ratio_1h: float | None = None  # 直前1h足の上ヒゲ比率 記録のみ
    consecutive_green_1h: int | None  = None  # 1h連続陽線数 記録のみ
    consecutive_green_4h: int | None  = None  # 4h連続陽線数 記録のみ
    bb_width_pct:       float | None = None   # BBバンド幅% = (upper-lower)/middle×100 記録のみ
    ma20_deviation_pct: float | None = None   # 20MA乖離率 = (price-MA20)/MA20×100 記録のみ
    candle_body_ratio:  float | None = None   # 実体比率 = |close-open|/(high-low) 記録のみ
    rsi_15m:            float | None = None   # 15m足RSI(14) 記録のみ
    daily_direction:    str | None   = None   # GREEN / RED / DOJI 記録のみ


@dataclass
class EntryVariant:
    """エントリー戦略バリアントの追跡結果。

    同一の検出タイミングに対して複数のエントリー戦略を仮想的に追跡し、
    「指値で入っていたら？」「スプレッド考慮したら？」を比較できる。

    戦略一覧:
        MARKET      — 検出時の last price (成行の理想値)
        ASK         — 検出時の ask price (成行ショートの実質コスト)
        LIMIT_1PCT〜10PCT — last × 1.01〜1.10 (任意の +1〜10%: ベースライン)
        LIMIT_BB3S  — BB中心 + 3σ  (統計的な極限ゾーン)
        LIMIT_ATR   — last + ATR×0.5 (ボラティリティ半分だけ上)
        LIMIT_FIB1272 — フィボナッチ 1.272 エクステンション
        LIMIT_FIB1618 — フィボナッチ 1.618 エクステンション (黄金比)
    """
    strategy: str          # 上記戦略名
    entry_price: float     # 実際のエントリー仮想価格
    sl_price: float
    tp_price: float
    filled: bool = True    # 指値が約定したか (LIMIT は後で価格到達で True に)
    filled_at: str | None = None

    outcome: str = OUTCOME_ACTIVE
    outcome_price: float | None = None
    pnl_pct: float | None = None


@dataclass
class ExperimentTrade:
    """シャドウトレード（仮想エントリーの追跡）"""
    symbol: str
    detected_at: str
    expires_at: str
    entry_price: float
    sl_price: float
    tp_price: float
    sl_pct: float
    tp_pct: float

    market_regime: str
    confirmed_strict: bool             # 現行 STRICT フィルター通過したか
    filters: FilterSnapshot

    # ファンダメンタル情報 (confirmed のみ。rejected は UNKNOWN)
    catalyst_type: str = "UNKNOWN"         # NONE / POSITIVE / NEGATIVE / WEAK / UNKNOWN
    short_conviction: str = "UNKNOWN"      # HIGH / MEDIUM / LOW / AVOID / UNKNOWN
    news_count: int = -1                   # -1 = 未取得
    # 実弾判定ポリシーを固定した後に収集したOOS標本かを識別する。
    policy_version: str = "unversioned"
    policy_fingerprint: str = ""
    # 取引所の確定1h足と当時の却下理由を保持し、未来情報なしで
    # signal/decision/outcome を後から結合できるようにする。
    signal_candle_at: str | None = None
    strict_reject_reasons: list[str] | None = None

    # スプレッド情報 (検出時点)
    ask_price: float | None = None         # 売り気配 (成行ショートの実質エントリー)
    bid_price: float | None = None         # 買い気配
    spread_pct: float | None = None        # (ask - bid) / mid × 100

    # エントリー戦略バリアント (各戦略ごとの仮想結果)
    entry_variants: list[EntryVariant] | None = None

    # 状態 (MARKET 戦略のメイン outcome。後方互換のため残す)
    outcome: str = OUTCOME_ACTIVE
    outcome_at: str | None = None
    outcome_price: float | None = None
    pnl_pct: float | None = None
    hours_held: float | None = None

    # 期間中の最大値（追加分析用）
    max_favorable_pct: float = 0.0     # ショート視点の最大利益（最大下落%）
    max_adverse_pct: float = 0.0       # ショート視点の最大損失（最大上昇%）
    last_price: float | None = None


class ExperimentTracker:
    """全候補を仮想追跡してフィルター粒度別の PnL データを蓄積する。

    実トレード（SymbolTracker / StatsManager）から完全に独立しており、
    confirmed/rejected 問わず全候補を記録する。

    使い方:
        exp = ExperimentTracker()
        exp.add_candidate(symbol, entry, sl, tp, ..., filters, confirmed_strict)
        exp.update(client)  # 各サイクルで価格更新 + outcome 確定
        exp.save()
    """

    # ホットファイル (experiments.json) に保持する closed 件数の上限。
    # これを超えたら古いものから data/archive/experiments_YYYY-MM.json.gz に
    # 月単位で gzip アーカイブし、ホットは軽量に保つ。
    # 分析 (tools/analyze_experiments.py) はホット + 全アーカイブを結合するため
    # 分析精度は落ちない。
    DEFAULT_HOT_MAX = 500

    # hot + archive を足したトータル上限 (主にディスク肥大の緊急ブレーキ)。
    # 通常は archive が無限に伸びる設計だが、セーフティネットとして。
    MAX_CLOSED_RECORDS = 5000  # legacy 名残 (アーカイブ移行後は hot のみに適用)

    def __init__(self, file_path: Path = EXPERIMENT_FILE) -> None:
        self._file = file_path
        self._tracking_hours = int(os.getenv("EXPERIMENT_TRACKING_HOURS", "8"))
        self._hot_max = int(os.getenv("EXPERIMENT_HOT_MAX", str(self.DEFAULT_HOT_MAX)))
        self._policy_version = (
            os.getenv("LIVE_POLICY_VERSION", "unversioned").strip()
            or "unversioned"
        )
        self._policy_fingerprint = live_policy_fingerprint()
        self._active: dict[str, ExperimentTrade] = {}
        self._closed: list[ExperimentTrade] = []
        self._load()

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def add_candidate(
        self,
        symbol: str,
        entry_price: float,
        sl_price: float,
        tp_price: float,
        sl_pct: float,
        tp_pct: float,
        market_regime: str,
        filters: FilterSnapshot,
        confirmed_strict: bool,
        signal_candle_at: str | None = None,
        strict_reject_reasons: list[str] | None = None,
        detected_at: str | None = None,
        catalyst_type: str = "UNKNOWN",
        short_conviction: str = "UNKNOWN",
        news_count: int = -1,
        ask_price: float | None = None,
        bid_price: float | None = None,
        # テクニカル指値計算用
        bb_upper: float | None = None,
        bb_middle: float | None = None,
        atr_pct: float | None = None,
        swing_low_1h: float | None = None,
    ) -> bool:
        """新規シャドウトレードを登録。同銘柄追跡中なら何もしない。

        ask_price / bid_price が渡された場合、スプレッド情報を記録し、
        複数のエントリー戦略バリアントを自動生成する。
        """
        if symbol in self._active:
            return False

        if detected_at:
            now = datetime.fromisoformat(detected_at)
            if now.tzinfo is None or now.utcoffset() is None:
                raise ValueError("detected_at must be timezone-aware")
            now = now.astimezone(timezone.utc)
        else:
            now = datetime.now(timezone.utc)
        expires = now + timedelta(hours=self._tracking_hours)

        # スプレッド計算
        spread_pct: float | None = None
        if ask_price and bid_price and bid_price > 0:
            mid = (ask_price + bid_price) / 2
            spread_pct = (ask_price - bid_price) / mid * 100 if mid > 0 else None

        # エントリー戦略バリアントを生成
        variants = self._build_entry_variants(
            entry_price, ask_price, sl_pct, tp_pct,
            bb_upper=bb_upper,
            bb_middle=bb_middle,
            atr_pct=atr_pct,
            swing_low_1h=swing_low_1h,
        )

        self._active[symbol] = ExperimentTrade(
            symbol=symbol,
            detected_at=now.isoformat(),
            expires_at=expires.isoformat(),
            entry_price=entry_price,
            sl_price=sl_price,
            tp_price=tp_price,
            sl_pct=sl_pct,
            tp_pct=tp_pct,
            market_regime=market_regime,
            confirmed_strict=confirmed_strict,
            filters=filters,
            catalyst_type=catalyst_type,
            short_conviction=short_conviction,
            news_count=news_count,
            policy_version=self._policy_version,
            policy_fingerprint=self._policy_fingerprint,
            signal_candle_at=signal_candle_at,
            strict_reject_reasons=list(strict_reject_reasons or []),
            ask_price=ask_price,
            bid_price=bid_price,
            spread_pct=spread_pct,
            entry_variants=variants,
            last_price=entry_price,
        )
        logger.debug(
            "Shadow trade added: %s (strict=%s, regime=%s, spread=%.3f%%)",
            symbol, confirmed_strict, market_regime,
            spread_pct or 0.0,
        )
        return True

    @staticmethod
    def _build_entry_variants(
        last_price: float,
        ask_price: float | None,
        sl_pct: float,
        tp_pct: float,
        bb_upper: float | None = None,
        bb_middle: float | None = None,
        atr_pct: float | None = None,
        swing_low_1h: float | None = None,
    ) -> list[EntryVariant]:
        """エントリー戦略ごとの仮想エントリー価格 + SL/TP を生成する。

        指値戦略は filled=False で初期化し、update() で価格到達時に
        filled=True に切り替える。到達しなければ outcome は EXPIRED (unfilled)。
        """
        variants: list[EntryVariant] = []

        def _make(strategy: str, price: float, filled: bool = True) -> EntryVariant:
            """ショート用バリアント: SL は上、TP は下。"""
            sl = price * (1 + sl_pct / 100)
            tp = price * (1 - tp_pct / 100)
            return EntryVariant(
                strategy=strategy,
                entry_price=price,
                sl_price=sl,
                tp_price=tp,
                filled=filled,
            )

        def _make_long(strategy: str, price: float, filled: bool = True) -> EntryVariant:
            """ロング用バリアント: SL は下、TP は上。"""
            sl = price * (1 - sl_pct / 100)
            tp = price * (1 + tp_pct / 100)
            return EntryVariant(
                strategy=strategy,
                entry_price=price,
                sl_price=sl,
                tp_price=tp,
                filled=filled,
            )

        # ── ショート: 即時約定 ───────────────────────────────────────────
        # MARKET: last price (成行の理想値)
        variants.append(_make("MARKET", last_price))

        # ASK: 実際の成行ショートは ask 価格で約定する
        if ask_price and ask_price > 0:
            variants.append(_make("ASK", ask_price))

        # ── ショート: 任意 % 指値 (ベースライン) ────────────────────────
        for pct in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
            variants.append(_make(
                f"LIMIT_{pct}PCT", last_price * (1 + pct / 100), filled=False,
            ))

        # ── テクニカル指値 ───────────────────────────────────────────────
        # LIMIT_BB3S: ボリンジャーバンド 3σ (統計的な極限ゾーン)
        # 価格が 2σ を超えて 3σ まで伸びたところでショート
        if bb_upper and bb_middle and bb_upper > bb_middle:
            sigma = (bb_upper - bb_middle) / 2
            bb_3s = bb_middle + 3 * sigma
            if bb_3s > last_price:          # 現値より上にある場合のみ有効
                variants.append(_make("LIMIT_BB3S", bb_3s, filled=False))

        # LIMIT_ATR: 現値 + ATR × 0.5
        # 急騰後に ATR 半分だけ追加で上がったところが「売られ始め」と仮定
        if atr_pct and atr_pct > 0:
            atr_limit = last_price * (1 + atr_pct * 0.5 / 100)
            if atr_limit > last_price * 1.001:  # 最低 0.1% 上でないと意味なし
                variants.append(_make("LIMIT_ATR", atr_limit, filled=False))

        # LIMIT_FIB1272 / LIMIT_FIB1618: フィボナッチ・エクステンション
        # 急騰直前のスイング安値からの波を基準にエクステンションを計算
        # 1.272 と 1.618 (黄金比) が典型的な反転ゾーン
        if swing_low_1h and swing_low_1h < last_price:
            move = last_price - swing_low_1h
            fib1272 = last_price + move * 0.272
            fib1618 = last_price + move * 0.618
            if fib1272 > last_price * 1.001:
                variants.append(_make("LIMIT_FIB1272", fib1272, filled=False))
            if fib1618 > last_price * 1.001:
                variants.append(_make("LIMIT_FIB1618", fib1618, filled=False))

        # ── ロング方向（同一検出イベントでの逆方向記録）────────────────
        # 同じ急騰を「継続トレンドのブレイクアウト」として捉えた場合の仮想成績。
        # ショートと並べて比較することで「この相場はロング/ショートどちらが有効か」
        # を定量的に判断できる。

        # MARKET_LONG: 即時ロング (MARKET ショートと同価格・逆方向)
        variants.append(_make_long("MARKET_LONG", last_price))

        # ASK_LONG: ask 価格で即時ロング (実際の成行ロストコスト)
        if ask_price and ask_price > 0:
            variants.append(_make_long("ASK_LONG", ask_price))

        # LIMIT_1〜10PCT_LONG: 1〜10% 押した水準でロング (押し目買い)
        for pct in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
            variants.append(_make_long(
                f"LIMIT_{pct}PCT_LONG", last_price * (1 - pct / 100), filled=False,
            ))

        # LIMIT_BB3S_LONG: BB中心+3σ水準でロング
        # ショートのLIMIT_BB3Sと同価格・逆方向 → 「同じ水準でL/Sどちらが有利か」の比較
        if bb_upper and bb_middle and bb_upper > bb_middle:
            sigma = (bb_upper - bb_middle) / 2
            bb_3s = bb_middle + 3 * sigma
            if bb_3s < last_price * 0.999:  # 現値より下にある場合のみ (押し目)
                variants.append(_make_long("LIMIT_BB3S_LONG", bb_3s, filled=False))

        # LIMIT_ATR_LONG: 現値 - ATR×0.5 (ATR半分だけ押したところでロング)
        if atr_pct and atr_pct > 0:
            atr_limit_long = last_price * (1 - atr_pct * 0.5 / 100)
            if atr_limit_long < last_price * 0.999:
                variants.append(_make_long("LIMIT_ATR_LONG", atr_limit_long, filled=False))

        # LIMIT_FIB1272_LONG / LIMIT_FIB1618_LONG: フィボナッチ・リトレースメント
        # ショートのエクステンション（上方）と対称に、上昇幅の0.272/0.618戻した水準でロング
        # FIB1272_LONG = 上昇幅の27.2%押し戻し (浅い押し目)
        # FIB1618_LONG = 上昇幅の61.8%押し戻し (深い押し目 = 黄金比リトレース)
        if swing_low_1h and swing_low_1h < last_price:
            move = last_price - swing_low_1h
            fib1272_long = last_price - move * 0.272
            fib1618_long = last_price - move * 0.618
            if fib1272_long < last_price * 0.999:
                variants.append(_make_long("LIMIT_FIB1272_LONG", fib1272_long, filled=False))
            if fib1618_long < last_price * 0.999:
                variants.append(_make_long("LIMIT_FIB1618_LONG", fib1618_long, filled=False))

        return variants

    def update_fundamental(
        self,
        symbol: str,
        catalyst_type: str,
        short_conviction: str,
        news_count: int,
    ) -> None:
        """アクティブなシャドウトレードにファンダメンタル情報を後付けする。

        シャドウ登録はテクニカル分析直後（ファンダ前）に行われるため、
        confirmed シグナルのファンダ分析が完了した後にこのメソッドで補完する。
        """
        trade = self._active.get(symbol)
        if trade is None:
            return
        trade.catalyst_type = catalyst_type
        trade.short_conviction = short_conviction
        trade.news_count = news_count

    def update(self, client: "MEXCClient") -> list[ExperimentTrade]:
        """全アクティブシャドウの outcome を更新。新規確定したものを返す。

        直近 6 本の 1 分足 OHLCV の high/low を使って、チェック間隔中の
        SL/TP 通過を分単位で検出する。5 分間で起きた高値・安値を正確に把握。
        """
        if not self._active:
            return []

        symbols_list = list(self._active.keys())

        # 直近6本の 1m 足を銘柄ごとに取得して high/low/close を得る
        candle_data: dict[str, dict] = {}
        for symbol in symbols_list:
            try:
                ohlcv = client.fetch_ohlcv(symbol, timeframe="1m", limit=6)
                if ohlcv and len(ohlcv) >= 1:
                    candle_data[symbol] = {
                        "high":  max(float(c[2]) for c in ohlcv),
                        "low":   min(float(c[3]) for c in ohlcv),
                        "close": float(ohlcv[-1][4]),
                    }
            except Exception as e:
                logger.debug("1m OHLCV unavailable for %s: %s", symbol, e)

        newly_closed: list[ExperimentTrade] = []
        now = datetime.now(timezone.utc)
        now_str = now.isoformat()

        for symbol in symbols_list:
            trade = self._active[symbol]
            candle = candle_data.get(symbol)

            if candle is None:
                # OHLCV 取得失敗時は期限切れチェックのみ
                if datetime.fromisoformat(trade.expires_at) <= now:
                    self._close(
                        trade, OUTCOME_EXPIRED,
                        trade.last_price or trade.entry_price, now_str,
                    )
                    newly_closed.append(trade)
                continue

            high  = candle["high"]
            low   = candle["low"]
            close = candle["close"]

            expired = datetime.fromisoformat(trade.expires_at) <= now

            trade.last_price = close

            # MFE / MAE 更新（5分足の high/low で正確に追跡）
            # ショート視点：価格下落 = 利益
            favorable_pct = (trade.entry_price - low) / trade.entry_price * 100
            adverse_pct   = (trade.entry_price - high) / trade.entry_price * 100
            if favorable_pct > trade.max_favorable_pct:
                trade.max_favorable_pct = favorable_pct
            if adverse_pct < trade.max_adverse_pct:
                trade.max_adverse_pct = adverse_pct

            # エントリーバリアントの更新（high/low で指値約定判定 + SL/TP 判定）
            self._update_variants_ohlcv(trade, high, low, close, now_str)

            # outcome 判定（5分足の high/low で SL/TP 通過を検出）
            sl_hit = high >= trade.sl_price
            tp_hit = low  <= trade.tp_price

            if sl_hit and tp_hit:
                # 同一足内で両方通過した場合は SL 優先（保守的判定）
                self._close(trade, OUTCOME_SL_HIT, trade.sl_price, now_str)
                newly_closed.append(trade)
            elif tp_hit:
                self._close(trade, OUTCOME_TP_HIT, trade.tp_price, now_str)
                newly_closed.append(trade)
            elif sl_hit:
                self._close(trade, OUTCOME_SL_HIT, trade.sl_price, now_str)
                newly_closed.append(trade)
            elif expired:
                self._close(
                    trade, OUTCOME_EXPIRED, close, now_str,
                )
                newly_closed.append(trade)

        if newly_closed:
            self._enforce_history_cap()
            self._save()
        return newly_closed

    def active_count(self) -> int:
        return len(self._active)

    def closed_count(self) -> int:
        return len(self._closed)

    def save(self) -> None:
        self._save()

    # ------------------------------------------------------------------
    # Internal
    # ------------------------------------------------------------------

    @staticmethod
    def _update_variants_ohlcv(
        trade: ExperimentTrade,
        high: float,
        low: float,
        close: float,
        now_str: str,
    ) -> None:
        """各エントリーバリアントの約定チェック + outcome 判定 (OHLCV ベース)。

        5分足の high/low を使うことで、チェック間隔中の瞬間的な
        SL/TP 通過や指値約定を正確に検出する。
        """
        if not trade.entry_variants:
            return

        for v in trade.entry_variants:
            if v.outcome != OUTCOME_ACTIVE:
                continue

            is_long = v.strategy.endswith("_LONG")

            # 指値約定チェック
            if not v.filled:
                if is_long:
                    # ロング指値: 押し目価格まで下落したら約定
                    if low <= v.entry_price:
                        v.filled = True
                        v.filled_at = now_str
                    else:
                        continue
                else:
                    # ショート指値: 吹き上げ価格まで上昇したら約定
                    if high >= v.entry_price:
                        v.filled = True
                        v.filled_at = now_str
                    else:
                        continue

            # SL/TP 判定 (5分足の high/low で通過を検出)
            if is_long:
                sl_hit = low  <= v.sl_price   # 下落で SL
                tp_hit = high >= v.tp_price   # 上昇で TP
            else:
                sl_hit = high >= v.sl_price   # 上昇で SL
                tp_hit = low  <= v.tp_price   # 下落で TP

            if sl_hit and tp_hit:
                # 同一足内で両方 → SL 優先（保守的）
                v.outcome = OUTCOME_SL_HIT
                v.outcome_price = v.sl_price
                v.pnl_pct = (
                    (v.sl_price - v.entry_price) / v.entry_price * 100 if is_long
                    else (v.entry_price - v.sl_price) / v.entry_price * 100
                )
            elif tp_hit:
                v.outcome = OUTCOME_TP_HIT
                v.outcome_price = v.tp_price
                v.pnl_pct = (
                    (v.tp_price - v.entry_price) / v.entry_price * 100 if is_long
                    else (v.entry_price - v.tp_price) / v.entry_price * 100
                )
            elif sl_hit:
                v.outcome = OUTCOME_SL_HIT
                v.outcome_price = v.sl_price
                v.pnl_pct = (
                    (v.sl_price - v.entry_price) / v.entry_price * 100 if is_long
                    else (v.entry_price - v.sl_price) / v.entry_price * 100
                )

    def _close(
        self,
        trade: ExperimentTrade,
        outcome: str,
        exit_price: float,
        now_str: str,
    ) -> None:
        trade.outcome = outcome
        trade.outcome_at = now_str
        trade.outcome_price = exit_price
        trade.pnl_pct = (trade.entry_price - exit_price) / trade.entry_price * 100

        detected = datetime.fromisoformat(trade.detected_at)
        closed   = datetime.fromisoformat(now_str)
        trade.hours_held = (closed - detected).total_seconds() / 3600

        # 未確定のバリアントも全てクローズ
        if trade.entry_variants:
            for v in trade.entry_variants:
                if v.outcome == OUTCOME_ACTIVE:
                    if not v.filled:
                        v.outcome = OUTCOME_EXPIRED
                        v.pnl_pct = 0.0
                    else:
                        is_long = v.strategy.endswith("_LONG")
                        v.outcome_price = exit_price
                        v.pnl_pct = (
                            (exit_price - v.entry_price) / v.entry_price * 100 if is_long
                            else (v.entry_price - exit_price) / v.entry_price * 100
                        )
                        # LONG と SHORT で outcome を独立判定
                        # (親トレードの outcome は SHORT 視点なので LONG には使えない)
                        if is_long:
                            if exit_price <= v.sl_price:
                                v.outcome = OUTCOME_SL_HIT
                            elif exit_price >= v.tp_price:
                                v.outcome = OUTCOME_TP_HIT
                            else:
                                v.outcome = OUTCOME_EXPIRED
                        else:
                            v.outcome = outcome

        self._closed.append(trade)
        del self._active[trade.symbol]

        logger.info(
            "[EXP %s] %s pnl=%+.2f%% (held %.1fh, regime=%s, strict=%s)",
            outcome, trade.symbol,
            trade.pnl_pct or 0.0,
            trade.hours_held or 0.0,
            trade.market_regime,
            trade.confirmed_strict,
        )

    def _enforce_history_cap(self) -> None:
        """ホット件数 > _hot_max なら古い方から月次 gzip に逃がす。

        - 分析ツールは hot + archive を結合するため、移動しても分析精度は不変。
        - archive 書き込みに失敗した場合はホットに残し、次回再試行。
        """
        overflow = len(self._closed) - self._hot_max
        if overflow <= 0:
            return

        to_archive = self._closed[:overflow]
        records = [self._serialize(t) for t in to_archive]
        try:
            _archive_append(records)
        except Exception as e:
            logger.warning(
                "Experiment archive failed (%s). Keeping %d record(s) hot.",
                e, overflow,
            )
            return

        self._closed = self._closed[overflow:]
        logger.info(
            "Rotated %d record(s) to archive. Hot file now holds %d closed.",
            overflow, len(self._closed),
        )

    def _save(self) -> None:
        self._file.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "active": [self._serialize(t) for t in self._active.values()],
            "closed": [self._serialize(t) for t in self._closed],
        }
        with self._file.open("w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2, ensure_ascii=False)
        logger.debug(
            "Experiments saved: %d active, %d closed.",
            len(self._active), len(self._closed),
        )

    @staticmethod
    def _serialize(t: ExperimentTrade) -> dict:
        return asdict(t)

    def _load(self) -> None:
        if not self._file.exists():
            return
        try:
            with self._file.open(encoding="utf-8") as f:
                data = json.load(f)

            for entry in data.get("active", []):
                trade = self._build_trade(entry)
                self._active[trade.symbol] = trade

            for entry in data.get("closed", []):
                self._closed.append(self._build_trade(entry))

            logger.info(
                "Loaded experiments: %d active, %d closed.",
                len(self._active), len(self._closed),
            )
        except Exception as e:
            logger.warning("Failed to load experiments file: %s", e)

    @staticmethod
    def _build_trade(entry: dict) -> ExperimentTrade:
        filters_dict = entry.pop("filters", {})
        # 互換性: 欠落フィールドを 0 / None で埋める
        filters_dict.setdefault("btc_change_1h", 0.0)
        filters_dict.setdefault("relative_strength", 0.0)
        # ファンダ情報の後方互換
        entry.setdefault("catalyst_type", "UNKNOWN")
        entry.setdefault("short_conviction", "UNKNOWN")
        entry.setdefault("news_count", -1)
        entry.setdefault("policy_version", "unversioned")
        entry.setdefault("policy_fingerprint", "")
        entry.setdefault("signal_candle_at", None)
        entry.setdefault("strict_reject_reasons", [])
        # スプレッド / バリアントの後方互換
        entry.setdefault("ask_price", None)
        entry.setdefault("bid_price", None)
        entry.setdefault("spread_pct", None)
        # entry_variants の復元
        variants_raw = entry.pop("entry_variants", None)
        variants: list[EntryVariant] | None = None
        if variants_raw is not None:
            variants = [EntryVariant(**v) for v in variants_raw]
        filters = FilterSnapshot(**filters_dict)
        return ExperimentTrade(filters=filters, entry_variants=variants, **entry)
