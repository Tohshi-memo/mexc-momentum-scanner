# Decision Report

- generated_at: 2026-08-10T14:01:25.103502+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11169**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11169, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.62% | **+0.41%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.29% | **+0.20%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |
| LIMIT_BB3S | 4/18 | 22.2% | +0.03% | **+0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.19% | **+1.07%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +0.22% | **+0.13%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$622.98** / 初期 $100.00 (+522.98%)
- 確定: 3934件 (Win 1230 / Loss 1283 / Flat 1421) / skip 3796件
- 成長率目線: 平均log +0.000465 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ACT/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.32% 残高後 $622.98

## 4. Robust Adaptive DryRun ($100)

- 残高: **$141.89** / 初期 $100.00 (+41.89%)
- 確定: 1513件 (Win 424 / Loss 361 / Flat 728) / skip 3067件
- 成長率目線: 平均log +0.000231 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TST/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.08% 残高後 $141.89

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.05** / 初期 $100.00 (+17.05%)
- 確定: 1302件 (Win 403 / Loss 506 / Flat 393) / pending 1件 / skip 1338件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000052 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CYS/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $117.05

## 6. Latest Market Context

- 更新: 2026-08-10T14:01:14.637268+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=64574.4
- Funnel: target 962 → liquid 177 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| GUA/USDT:USDT | +75.97% | $5,629,414.96 |
| LONGXIA/USDT:USDT | +60.54% | $2,465,346.76 |
| TST/USDT:USDT | +31.65% | $4,896,095.65 |
| GRVT/USDT:USDT | +23.65% | $5,407,260.25 |
| SQD/USDT:USDT | +23.60% | $1,659,633.06 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLTRSTOCK/USDT:USDT | below_1h_threshold | +4.60% | +4.53% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +4.18% | +4.12% |
| AAOISTOCK/USDT:USDT | below_1h_threshold | +3.33% | +3.27% |
| SOXS/USDT:USDT | below_1h_threshold | +1.71% | +1.64% |
| MSFTSTOCK/USDT:USDT | below_1h_threshold | +1.56% | +1.50% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
