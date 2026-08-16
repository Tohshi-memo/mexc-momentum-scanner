# Decision Report

- generated_at: 2026-08-16T04:36:30.739768+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11715**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.63% / filled 20/20。**
- 全期間 MARKET基準: n=11715, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.63%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.63% | **+0.63%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 18/20 | 90.0% | +1.96% | **+1.76%** |
| LIMIT_ATR | 15/20 | 75.0% | +1.85% | **+1.39%** |
| LIMIT_3PCT | 14/20 | 70.0% | +1.65% | **+1.16%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.03% | **+0.98%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.57% | **+0.71%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.95% | **+0.98%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.31% | **+0.52%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.44% | **+0.37%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.65% | **+0.36%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.36% | **+0.27%** |

## 2. $100 Live Portfolio

- 残高: **$121.53** / 初期 $100.00 (+21.53%)
- 確定トレード: 183件 (TP 71 / SL 107 / EXP 5)
- 最新: MOVR/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.53
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$627.16** / 初期 $100.00 (+527.16%)
- 確定: 4181件 (Win 1292 / Loss 1361 / Flat 1528) / skip 4095件
- 成長率目線: 平均log +0.000439 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEMI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $627.16

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.79** / 初期 $100.00 (+54.79%)
- 確定: 1769件 (Win 493 / Loss 416 / Flat 860) / skip 3357件
- 成長率目線: 平均log +0.000247 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HEMI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $154.79

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.28** / 初期 $100.00 (+19.28%)
- 確定: 1626件 (Win 495 / Loss 618 / Flat 513) / pending 0件 / skip 1559件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000093 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: H/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $119.28

## 6. Latest Market Context

- 更新: 2026-08-16T04:36:22.326828+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=63090.9
- Funnel: target 986 → liquid 135 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEMI/USDT:USDT | +24.14% | $5,653,700.13 |
| SPORTFUN/USDT:USDT | +17.29% | $4,297,351.59 |
| CROSS/USDT:USDT | +16.97% | $1,229,706.77 |
| H/USDT:USDT | +15.23% | $6,888,668.56 |
| BASED/USDT:USDT | +12.84% | $2,131,991.17 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HEMI/USDT:USDT | below_1h_threshold | +3.80% | +3.81% |
| ANTHROPIC/USDT:USDT | below_1h_threshold | +2.33% | +2.34% |
| BICO/USDT:USDT | below_1h_threshold | +1.82% | +1.83% |
| H/USDT:USDT | below_1h_threshold | +1.65% | +1.66% |
| PRL/USDT:USDT | below_1h_threshold | +1.60% | +1.61% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
