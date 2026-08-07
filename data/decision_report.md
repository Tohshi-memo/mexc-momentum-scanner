# Decision Report

- generated_at: 2026-08-07T04:36:26.771476+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10672**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.48% / filled 20/20。**
- 全期間 MARKET基準: n=10672, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.48%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.48% | **+1.48%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.48% | **+1.48%** |
| LIMIT_3PCT | 16/20 | 80.0% | +1.74% | **+1.39%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.12% | **+0.90%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.87% | **+0.74%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.70% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +2.55% | **+0.76%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.80% | **+0.40%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +0.46% | **+0.09%** |
| MARKET_LONG | 20/20 | 100.0% | -0.08% | **-0.08%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$595.60** / 初期 $100.00 (+495.60%)
- 確定: 3797件 (Win 1203 / Loss 1250 / Flat 1344) / skip 3436件
- 成長率目線: 平均log +0.000470 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: KMNO/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $595.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$144.37** / 初期 $100.00 (+44.37%)
- 確定: 1454件 (Win 406 / Loss 342 / Flat 706) / skip 2629件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AXTISTOCK/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $144.37

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.56** / 初期 $100.00 (+16.56%)
- 確定: 1157件 (Win 369 / Loss 455 / Flat 333) / pending 2件 / skip 992件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000270 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: RIVER/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $116.56

## 6. Latest Market Context

- 更新: 2026-08-07T04:36:17.511968+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=64313.6
- Funnel: target 958 → liquid 192 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STG/USDT:USDT | +40.31% | $7,408,193.21 |
| ON/USDT:USDT | +24.34% | $9,069,386.85 |
| CATE/USDT:USDT | +22.49% | $4,066,653.00 |
| SKYAI/USDT:USDT | +18.41% | $59,262,795.68 |
| ZHIPUSTOCK/USDT:USDT | +17.65% | $1,771,276.47 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CATE/USDT:USDT | below_1h_threshold | +4.95% | +4.88% |
| AAOISTOCK/USDT:USDT | below_1h_threshold | +3.34% | +3.26% |
| STG/USDT:USDT | below_1h_threshold | +2.80% | +2.72% |
| ON/USDT:USDT | below_1h_threshold | +2.61% | +2.53% |
| BTW/USDT:USDT | below_1h_threshold | +2.05% | +1.97% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
