# Decision Report

- generated_at: 2026-08-16T16:56:28.883743+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11755**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.10% / filled 20/20。**
- 全期間 MARKET基準: n=11755, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.10% | **+1.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.40% | **+1.26%** |
| MARKET | 20/20 | 100.0% | +1.10% | **+1.10%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.10% | **+0.71%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.64% | **+0.49%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.50% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/8 | 62.5% | +4.27% | **+2.67%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +1.24% | **+0.80%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +0.67% | **+0.47%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$121.53** / 初期 $100.00 (+21.53%)
- 確定トレード: 183件 (TP 71 / SL 107 / EXP 5)
- 最新: MOVR/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.53
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$620.90** / 初期 $100.00 (+520.90%)
- 確定: 4183件 (Win 1292 / Loss 1363 / Flat 1528) / skip 4133件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CROSS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $620.90

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.89** / 初期 $100.00 (+54.89%)
- 確定: 1784件 (Win 495 / Loss 417 / Flat 872) / skip 3382件
- 成長率目線: 平均log +0.000245 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CROSS/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $154.89

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.47** / 初期 $100.00 (+19.47%)
- 確定: 1652件 (Win 500 / Loss 625 / Flat 527) / pending 3件 / skip 1572件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000117 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: COTI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $119.47

## 6. Latest Market Context

- 更新: 2026-08-16T16:56:18.250814+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.18% price=63229.8
- Funnel: target 986 → liquid 145 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.7 >= 65=1, 4h RSI 81.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIO/USDT:USDT | +7.40% | $6,939,011.57 |
| PORTAL/USDT:USDT | +6.36% | $6,917,683.35 |
| RIVER/USDT:USDT | +3.64% | $1,382,359.91 |
| ROBO/USDT:USDT | +3.22% | $1,445,791.89 |
| TUT/USDT:USDT | +2.89% | $6,155,102.79 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RIVER/USDT:USDT | below_1h_threshold | +3.65% | +3.46% |
| ROBO/USDT:USDT | below_1h_threshold | +3.22% | +3.04% |
| TUT/USDT:USDT | below_1h_threshold | +2.90% | +2.71% |
| PRL/USDT:USDT | below_1h_threshold | +2.62% | +2.44% |
| WLD/USDT:USDT | below_1h_threshold | +2.48% | +2.30% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
