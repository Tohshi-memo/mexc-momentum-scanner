# Decision Report

- generated_at: 2026-06-12T16:29:11.739068+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6523**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.57% / filled 20/20。**
- 全期間 MARKET基準: n=6523, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+0.57%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.57% | **+0.57%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.57% | **+0.57%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| ASK | 20/20 | 100.0% | +0.34% | **+0.34%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_BB3S | 4/16 | 25.0% | +1.30% | **+0.33%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +3.65% | **+1.82%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.46% | **+0.80%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.11% | **+0.42%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.47% | **+0.33%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.37% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$95.64** / 初期 $100.00 (-4.36%)
- 確定トレード: 19件 (TP 3 / SL 15 / EXP 1)
- 最新: UB/USDT:USDT TP_HIT PnL +8.00% 残高後 $95.64
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$165.50** / 初期 $100.00 (+65.50%)
- 確定: 1396件 (Win 385 / Loss 455 / Flat 556) / skip 1688件
- 成長率目線: 平均log +0.000361 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIN/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $165.50

## 4. Latest Market Context

- 更新: 2026-06-12T16:29:03.411548+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.50% price=63876.2
- Funnel: target 774 → liquid 159 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=45, below_relative_strength=2, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +7.98% | $2,679,021.32 |
| RKLBSTOCK/USDT:USDT | +6.86% | $1,151,953.50 |
| NAORIS/USDT:USDT | +5.93% | $7,052,562.82 |
| ESPORTS/USDT:USDT | +5.17% | $65,412,992.36 |
| COAI/USDT:USDT | +4.77% | $4,180,308.83 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_relative_strength | +5.48% | +4.98% |
| COAI/USDT:USDT | below_relative_strength | +5.07% | +4.57% |
| AIO/USDT:USDT | below_1h_threshold | +3.46% | +2.96% |
| SOXL/USDT:USDT | below_1h_threshold | +3.35% | +2.85% |
| PLSTOCK/USDT:USDT | below_1h_threshold | +3.33% | +2.83% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
