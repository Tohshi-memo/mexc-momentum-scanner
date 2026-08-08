# Decision Report

- generated_at: 2026-08-08T14:11:21.361738+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10849**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10849, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.86%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.86% | **-0.86%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.31% | **+0.20%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +0.74% | **+0.15%** |
| LIMIT_BB3S | 5/18 | 27.8% | -0.68% | **-0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.67% | **+1.58%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.14% | **+1.28%** |
| MARKET_LONG | 20/20 | 100.0% | +0.96% | **+0.96%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.25% | **+0.62%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.50% | **+0.50%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$628.01** / 初期 $100.00 (+528.01%)
- 確定: 3850件 (Win 1212 / Loss 1253 / Flat 1385) / skip 3560件
- 成長率目線: 平均log +0.000477 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $628.01

## 4. Robust Adaptive DryRun ($100)

- 残高: **$142.00** / 初期 $100.00 (+42.00%)
- 確定: 1510件 (Win 424 / Loss 360 / Flat 726) / skip 2750件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0504 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $142.00

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.42** / 初期 $100.00 (+18.42%)
- 確定: 1217件 (Win 385 / Loss 469 / Flat 363) / pending 6件 / skip 1099件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000236 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SYN/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $118.42

## 6. Latest Market Context

- 更新: 2026-08-08T14:11:11.967594+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=65004.4
- Funnel: target 961 → liquid 164 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +223.93% | $11,321,063.36 |
| TUT/USDT:USDT | +88.99% | $9,307,259.52 |
| BLUAI/USDT:USDT | +33.86% | $4,360,943.38 |
| BEAT/USDT:USDT | +31.83% | $28,469,098.23 |
| MMT/USDT:USDT | +27.64% | $6,785,871.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TST/USDT:USDT | below_1h_threshold | +3.01% | +2.98% |
| ACE/USDT:USDT | below_1h_threshold | +2.04% | +2.01% |
| DODO/USDT:USDT | below_1h_threshold | +1.99% | +1.96% |
| TUT/USDT:USDT | below_1h_threshold | +1.96% | +1.93% |
| CAP/USDT:USDT | below_1h_threshold | +1.80% | +1.77% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
