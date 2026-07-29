# Decision Report

- generated_at: 2026-07-29T03:46:44.265797+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9764**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.58% / filled 20/20。**
- 全期間 MARKET基準: n=9764, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+3.58%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.58% | **+3.58%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.58% | **+3.58%** |
| LIMIT_1PCT | 17/20 | 85.0% | +3.50% | **+2.98%** |
| LIMIT_ATR | 14/20 | 70.0% | +3.81% | **+2.66%** |
| LIMIT_2PCT | 13/20 | 65.0% | +3.37% | **+2.19%** |
| LIMIT_3PCT | 9/20 | 45.0% | +3.29% | **+1.48%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 15/20 | 75.0% | +1.59% | **+1.19%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +5.46% | **+0.55%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | +0.95% | **+0.52%** |
| LIMIT_6PCT_LONG | 15/20 | 75.0% | +0.03% | **+0.02%** |
| LIMIT_FIB1618_LONG | 10/20 | 50.0% | -0.59% | **-0.30%** |

## 2. $100 Live Portfolio

- 残高: **$119.87** / 初期 $100.00 (+19.87%)
- 確定トレード: 161件 (TP 63 / SL 93 / EXP 5)
- 最新: MUSTOCK/USDT:USDT TP_HIT PnL +7.86% 残高後 $119.87
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$494.05** / 初期 $100.00 (+394.05%)
- 確定: 3519件 (Win 1113 / Loss 1147 / Flat 1259) / skip 2806件
- 成長率目線: 平均log +0.000454 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $494.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1227件 (Win 338 / Loss 275 / Flat 614) / skip 1948件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0337 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EUL/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$110.16** / 初期 $100.00 (+10.16%)
- 確定: 760件 (Win 246 / Loss 291 / Flat 223) / pending 0件 / skip 477件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000458 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: STXSTOCK/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $110.16

## 6. Latest Market Context

- 更新: 2026-07-29T03:46:30.514033+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.31% price=63758.0
- Funnel: target 904 → liquid 170 → pre 50 → checked 50 → surge 4 → strict 3
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.6 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +43.95% | $1,400,788.07 |
| BTW/USDT:USDT | +29.87% | $6,918,070.57 |
| BEAT/USDT:USDT | +12.73% | $44,982,153.93 |
| KAITO/USDT:USDT | +12.20% | $9,818,922.05 |
| SOXS/USDT:USDT | +10.20% | $8,268,907.45 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RIF/USDT:USDT | below_1h_threshold | +4.31% | +4.62% |
| UB/USDT:USDT | below_1h_threshold | +1.68% | +1.99% |
| CXMTSTOCK/USDT:USDT | below_1h_threshold | +0.79% | +1.10% |
| O/USDT:USDT | below_1h_threshold | +0.73% | +1.03% |
| RCATSTOCK/USDT:USDT | below_1h_threshold | +0.65% | +0.95% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
