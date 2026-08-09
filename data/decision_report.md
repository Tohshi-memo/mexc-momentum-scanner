# Decision Report

- generated_at: 2026-08-09T04:51:31.653786+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10937**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.03% / filled 20/20。**
- 全期間 MARKET基準: n=10937, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.03% | **+1.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 11/20 | 55.0% | +2.17% | **+1.19%** |
| MARKET | 20/20 | 100.0% | +1.03% | **+1.03%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.87% | **+0.74%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.10% | **+0.71%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.71% | **+0.64%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +1.80% | **+0.27%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.17% | **+0.07%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | -0.27% | **-0.11%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | -0.29% | **-0.12%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | -0.49% | **-0.32%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$631.27** / 初期 $100.00 (+531.27%)
- 確定: 3930件 (Win 1230 / Loss 1280 / Flat 1420) / skip 3568件
- 成長率目線: 平均log +0.000469 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TST/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $631.27

## 4. Robust Adaptive DryRun ($100)

- 残高: **$142.00** / 初期 $100.00 (+42.00%)
- 確定: 1511件 (Win 424 / Loss 360 / Flat 727) / skip 2837件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0134 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CAT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $142.00

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.44** / 初期 $100.00 (+17.44%)
- 確定: 1248件 (Win 390 / Loss 480 / Flat 378) / pending 0件 / skip 1166件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `見送り` (no_strategy_passed_causal_filters) / causal_score n/a / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CAP/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account -0.10% 残高後 $117.44

## 6. Latest Market Context

- 更新: 2026-08-09T04:51:19.253980+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=64760.0
- Funnel: target 961 → liquid 156 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.9 >= 65=1, 4h RSI 75.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TUT/USDT:USDT | +101.02% | $31,608,562.41 |
| SAGA/USDT:USDT | +50.59% | $2,300,837.98 |
| BLUAI/USDT:USDT | +37.21% | $8,147,335.27 |
| IOTX/USDT:USDT | +32.54% | $3,182,006.66 |
| BICO/USDT:USDT | +23.10% | $28,905,382.25 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BICO/USDT:USDT | below_1h_threshold | +4.52% | +4.52% |
| TUT/USDT:USDT | below_1h_threshold | +2.81% | +2.80% |
| BANK/USDT:USDT | below_1h_threshold | +1.96% | +1.96% |
| PIXEL/USDT:USDT | below_1h_threshold | +1.24% | +1.24% |
| UB/USDT:USDT | below_1h_threshold | +1.17% | +1.17% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
