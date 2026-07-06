# Decision Report

- generated_at: 2026-07-06T17:11:07.416284+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8402**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8402, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 11/20 | 55.0% | +0.36% | **+0.20%** |
| LIMIT_8PCT | 5/20 | 25.0% | +0.62% | **+0.16%** |
| LIMIT_9PCT | 4/20 | 20.0% | +0.29% | **+0.06%** |
| LIMIT_7PCT | 5/20 | 25.0% | +0.08% | **+0.02%** |
| LIMIT_6PCT | 6/20 | 30.0% | -0.08% | **-0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.71% | **+1.71%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.71% | **+1.49%** |
| MARKET_LONG | 20/20 | 100.0% | +1.26% | **+1.26%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.93% | **+1.25%** |
| LIMIT_BB3S_LONG | 4/7 | 57.1% | +2.00% | **+1.14%** |

## 2. $100 Live Portfolio

- 残高: **$101.57** / 初期 $100.00 (+1.57%)
- 確定トレード: 67件 (TP 23 / SL 43 / EXP 1)
- 最新: EPIC/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.57
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$317.13** / 初期 $100.00 (+217.13%)
- 確定: 2624件 (Win 832 / Loss 887 / Flat 905) / skip 2339件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_8PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ANSEM/USDT:USDT `LIMIT_8PCT` EXPIRED account +0.00% 残高後 $317.13

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.48** / 初期 $100.00 (+5.48%)
- 確定: 639件 (Win 152 / Loss 158 / Flat 329) / skip 1174件
- 成長率目線: 平均log +0.000084 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BASED/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.26% 残高後 $105.48

## 5. Latest Market Context

- 更新: 2026-07-06T17:11:02.107606+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=63784.9
- Funnel: target 841 → liquid 178 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLUR/USDT:USDT | +29.15% | $1,543,017.00 |
| ANSEM/USDT:USDT | +13.33% | $3,501,034.98 |
| ALLO/USDT:USDT | +9.52% | $10,758,838.73 |
| HMSTR/USDT:USDT | +8.18% | $3,805,496.33 |
| CAP/USDT:USDT | +5.17% | $6,882,121.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HMSTR/USDT:USDT | below_1h_threshold | +4.55% | +4.44% |
| GOAT/USDT:USDT | below_1h_threshold | +1.88% | +1.76% |
| EPIC/USDT:USDT | below_1h_threshold | +1.11% | +0.99% |
| B/USDT:USDT | below_1h_threshold | +1.08% | +0.96% |
| ZRO/USDT:USDT | below_1h_threshold | +1.07% | +0.95% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
