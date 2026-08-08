# Decision Report

- generated_at: 2026-08-08T03:56:21.565668+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10805**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10805, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.02%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.02% | **-1.02%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 9/20 | 45.0% | +0.95% | **+0.43%** |
| LIMIT_BB3S | 5/14 | 35.7% | +0.80% | **+0.29%** |
| LIMIT_10PCT | 8/20 | 40.0% | +0.50% | **+0.20%** |
| LIMIT_8PCT | 10/20 | 50.0% | +0.37% | **+0.19%** |
| LIMIT_6PCT | 11/20 | 55.0% | -0.73% | **-0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/6 | 66.7% | +5.00% | **+3.33%** |
| LIMIT_9PCT_LONG | 8/20 | 40.0% | +5.48% | **+2.19%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +4.50% | **+2.02%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +3.36% | **+1.85%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +5.79% | **+1.45%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$607.53** / 初期 $100.00 (+507.53%)
- 確定: 3807件 (Win 1206 / Loss 1252 / Flat 1349) / skip 3559件
- 成長率目線: 平均log +0.000474 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $607.53

## 4. Robust Adaptive DryRun ($100)

- 残高: **$142.00** / 初期 $100.00 (+42.00%)
- 確定: 1510件 (Win 424 / Loss 360 / Flat 726) / skip 2706件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0895 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $142.00

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.02** / 初期 $100.00 (+18.02%)
- 確定: 1182件 (Win 381 / Loss 468 / Flat 333) / pending 0件 / skip 1095件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000223 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AXTISTOCK/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $118.02

## 6. Latest Market Context

- 更新: 2026-08-08T03:56:11.767979+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=64988.8
- Funnel: target 961 → liquid 182 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.1 >= 65=1, 4h RSI 83.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +292.62% | $5,595,310.87 |
| BLESS/USDT:USDT | +27.07% | $95,544,131.61 |
| MMT/USDT:USDT | +20.48% | $1,386,115.17 |
| TUT/USDT:USDT | +15.29% | $2,413,249.14 |
| BSB/USDT:USDT | +15.29% | $3,049,747.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +4.63% | +4.47% |
| BICO/USDT:USDT | below_1h_threshold | +4.59% | +4.43% |
| RBRKSTOCK/USDT:USDT | below_1h_threshold | +4.20% | +4.05% |
| UB/USDT:USDT | below_1h_threshold | +3.97% | +3.82% |
| SLX/USDT:USDT | below_1h_threshold | +2.78% | +2.62% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
