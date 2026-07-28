# Decision Report

- generated_at: 2026-07-28T17:51:47.012919+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9716**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9716, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.53%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.53% | **-0.53%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.83% | **+0.73%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.58% | **+0.55%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.37% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +3.27% | **+1.31%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +2.32% | **+0.93%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.28% | **+0.83%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.68% | **+0.58%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.05% | **+0.53%** |

## 2. $100 Live Portfolio

- 残高: **$107.44** / 初期 $100.00 (+7.44%)
- 確定トレード: 150件 (TP 52 / SL 93 / EXP 5)
- 最新: DEXE/USDT:USDT TP_HIT PnL +8.00% 残高後 $107.44
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$485.71** / 初期 $100.00 (+385.71%)
- 確定: 3486件 (Win 1101 / Loss 1131 / Flat 1254) / skip 2791件
- 成長率目線: 平均log +0.000453 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $485.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1226件 (Win 338 / Loss 275 / Flat 613) / skip 1901件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1127 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SPCXSTOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$109.57** / 初期 $100.00 (+9.57%)
- 確定: 734件 (Win 238 / Loss 280 / Flat 216) / pending 5件 / skip 450件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000414 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $109.57

## 6. Latest Market Context

- 更新: 2026-07-28T17:51:37.919407+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.66% price=63600.1
- Funnel: target 904 → liquid 175 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.1 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +18.18% | $1,290,493.66 |
| ON/USDT:USDT | +10.17% | $27,728,843.57 |
| BTW/USDT:USDT | +8.60% | $6,551,421.36 |
| BULLA/USDT:USDT | +7.10% | $2,740,784.77 |
| ZIL/USDT:USDT | +4.45% | $1,729,695.08 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RIF/USDT:USDT | below_1h_threshold | +2.75% | +3.40% |
| REZ/USDT:USDT | below_1h_threshold | +2.05% | +2.70% |
| BEAT/USDT:USDT | below_1h_threshold | +1.72% | +2.37% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +1.28% | +1.93% |
| BILL/USDT:USDT | below_1h_threshold | +1.21% | +1.87% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
