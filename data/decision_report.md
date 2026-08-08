# Decision Report

- generated_at: 2026-08-08T06:26:37.668888+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10817**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10817, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 6/20 | 30.0% | +4.00% | **+1.20%** |
| LIMIT_8PCT | 8/20 | 40.0% | +1.46% | **+0.59%** |
| LIMIT_9PCT | 6/20 | 30.0% | +1.43% | **+0.43%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_BB3S | 5/14 | 35.7% | +0.11% | **+0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +5.30% | **+1.85%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +4.00% | **+1.80%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +6.84% | **+1.71%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +2.00% | **+1.40%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +2.37% | **+1.19%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$615.31** / 初期 $100.00 (+515.31%)
- 確定: 3818件 (Win 1208 / Loss 1252 / Flat 1358) / skip 3560件
- 成長率目線: 平均log +0.000476 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $615.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$142.00** / 初期 $100.00 (+42.00%)
- 確定: 1510件 (Win 424 / Loss 360 / Flat 726) / skip 2718件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1126 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $142.00

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.02** / 初期 $100.00 (+18.02%)
- 確定: 1187件 (Win 381 / Loss 468 / Flat 338) / pending 4件 / skip 1098件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000298 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $118.02

## 6. Latest Market Context

- 更新: 2026-08-08T06:26:23.974153+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=64953.1
- Funnel: target 961 → liquid 176 → pre 50 → checked 50 → surge 4 → strict 2
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.2 >= 65=1, 4h RSI 78.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +285.52% | $7,377,599.76 |
| BLESS/USDT:USDT | +48.95% | $91,951,214.22 |
| MMT/USDT:USDT | +34.10% | $2,174,906.03 |
| CYS/USDT:USDT | +24.70% | $16,366,754.50 |
| TUT/USDT:USDT | +23.75% | $2,730,241.17 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SLX/USDT:USDT | below_1h_threshold | +4.61% | +4.63% |
| BICO/USDT:USDT | below_1h_threshold | +3.51% | +3.53% |
| PENGU/USDT:USDT | below_1h_threshold | +0.93% | +0.95% |
| PI/USDT:USDT | below_1h_threshold | +0.83% | +0.85% |
| 1000BONK/USDT:USDT | below_1h_threshold | +0.53% | +0.55% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
