# Decision Report

- generated_at: 2026-07-29T15:51:23.701367+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9809**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9809, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.76%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.76% | **-1.76%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +4.94% | **+0.99%** |
| LIMIT_4PCT | 15/20 | 75.0% | +1.07% | **+0.80%** |
| LIMIT_5PCT | 5/20 | 25.0% | +2.36% | **+0.59%** |
| LIMIT_ATR | 8/20 | 40.0% | +1.10% | **+0.44%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.26% | **+0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +3.46% | **+1.56%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.14% | **+1.50%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +2.78% | **+1.39%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.41% | **+1.34%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +3.10% | **+1.08%** |

## 2. $100 Live Portfolio

- 残高: **$119.27** / 初期 $100.00 (+19.27%)
- 確定トレード: 162件 (TP 63 / SL 94 / EXP 5)
- 最新: ON/USDT:USDT SL_HIT PnL -4.00% 残高後 $119.27
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$494.05** / 初期 $100.00 (+394.05%)
- 確定: 3519件 (Win 1113 / Loss 1147 / Flat 1259) / skip 2851件
- 成長率目線: 平均log +0.000454 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $494.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1227件 (Win 338 / Loss 275 / Flat 614) / skip 1993件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0582 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EUL/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$109.01** / 初期 $100.00 (+9.01%)
- 確定: 766件 (Win 246 / Loss 297 / Flat 223) / pending 0件 / skip 514件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000137 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: RIF/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $109.01

## 6. Latest Market Context

- 更新: 2026-07-29T15:51:13.333213+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.14% price=63989.5
- Funnel: target 911 → liquid 166 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.0 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +89.40% | $5,476,335.20 |
| UAI/USDT:USDT | +35.43% | $6,076,003.92 |
| COTI/USDT:USDT | +28.93% | $18,857,991.01 |
| BEAT/USDT:USDT | +28.65% | $43,011,652.59 |
| RIF/USDT:USDT | +24.33% | $3,664,343.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CAP/USDT:USDT | below_1h_threshold | +3.53% | +3.67% |
| AGT/USDT:USDT | below_1h_threshold | +2.82% | +2.96% |
| SOXS/USDT:USDT | below_1h_threshold | +2.32% | +2.46% |
| VELVET/USDT:USDT | below_1h_threshold | +2.17% | +2.31% |
| RIF/USDT:USDT | below_1h_threshold | +1.61% | +1.75% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
