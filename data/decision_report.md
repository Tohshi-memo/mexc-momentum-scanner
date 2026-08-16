# Decision Report

- generated_at: 2026-08-16T15:06:21.993039+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11750**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.73% / filled 20/20。**
- 全期間 MARKET基準: n=11750, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.73%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.73% | **+0.73%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 15/20 | 75.0% | +1.42% | **+1.07%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.99% | **+0.89%** |
| MARKET | 20/20 | 100.0% | +0.73% | **+0.73%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.44% | **+0.51%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.48% | **+0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/8 | 62.5% | +4.27% | **+2.67%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +1.81% | **+1.18%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.47% | **+0.66%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.87% | **+0.65%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.32% | **+0.53%** |

## 2. $100 Live Portfolio

- 残高: **$121.53** / 初期 $100.00 (+21.53%)
- 確定トレード: 183件 (TP 71 / SL 107 / EXP 5)
- 最新: MOVR/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.53
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$620.90** / 初期 $100.00 (+520.90%)
- 確定: 4183件 (Win 1292 / Loss 1363 / Flat 1528) / skip 4128件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CROSS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $620.90

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.89** / 初期 $100.00 (+54.89%)
- 確定: 1784件 (Win 495 / Loss 417 / Flat 872) / skip 3377件
- 成長率目線: 平均log +0.000245 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CROSS/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $154.89

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.48** / 初期 $100.00 (+19.48%)
- 確定: 1648件 (Win 499 / Loss 623 / Flat 526) / pending 2件 / skip 1572件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000135 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BOME/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $119.48

## 6. Latest Market Context

- 更新: 2026-08-16T15:06:12.392231+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=63085.1
- Funnel: target 986 → liquid 140 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +29.43% | $5,595,610.45 |
| MARSCOIN/USDT:USDT | +27.67% | $1,149,382.87 |
| DOLO/USDT:USDT | +25.89% | $1,125,226.56 |
| AIO/USDT:USDT | +22.06% | $5,782,233.71 |
| BICO/USDT:USDT | +17.35% | $4,705,352.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +1.89% | +1.88% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +1.67% | +1.66% |
| ON/USDT:USDT | below_1h_threshold | +1.41% | +1.39% |
| ROBO/USDT:USDT | below_1h_threshold | +1.28% | +1.26% |
| WLFI/USDT:USDT | below_1h_threshold | +1.02% | +1.00% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
