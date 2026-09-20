# Decision Report

- generated_at: 2026-09-20T07:51:33.061443+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15153**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.18% / filled 20/20。**
- 全期間 MARKET基準: n=15153, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.18%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.18% | **+1.18%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 14/20 | 70.0% | +2.44% | **+1.71%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.50% | **+1.20%** |
| MARKET | 20/20 | 100.0% | +1.18% | **+1.18%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.24% | **+1.12%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +3.13% | **+0.94%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.64% | **+0.90%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +2.96% | **+0.74%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.83% | **+0.37%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,193.20** / 初期 $100.00 (+1093.20%)
- 確定: 5679件 (Win 1700 / Loss 1835 / Flat 2144) / skip 6035件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CAKE/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $1,193.20

## 4. Robust Adaptive DryRun ($100)

- 残高: **$248.38** / 初期 $100.00 (+148.38%)
- 確定: 3266件 (Win 905 / Loss 762 / Flat 1599) / skip 5298件
- 成長率目線: 平均log +0.000279 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0234 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CAKE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $248.38

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.37** / 初期 $100.00 (+21.37%)
- 確定: 2978件 (Win 880 / Loss 1179 / Flat 919) / pending 0件 / skip 3646件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000306 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $121.37

## 6. Latest Market Context

- 更新: 2026-09-20T07:51:20.212832+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=80303.3
- Funnel: target 1050 → liquid 148 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CELR/USDT:USDT | +67.34% | $5,809,721.32 |
| ONE/USDT:USDT | +30.92% | $49,484,681.75 |
| OFC/USDT:USDT | +28.38% | $2,385,342.58 |
| ZIL/USDT:USDT | +25.59% | $3,805,559.85 |
| EVAA/USDT:USDT | +18.30% | $1,798,171.04 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EVAA/USDT:USDT | below_1h_threshold | +3.99% | +3.97% |
| AKE/USDT:USDT | below_1h_threshold | +2.62% | +2.59% |
| OFC/USDT:USDT | below_1h_threshold | +1.38% | +1.35% |
| HBAR/USDT:USDT | below_1h_threshold | +1.14% | +1.11% |
| ONE/USDT:USDT | below_1h_threshold | +1.04% | +1.01% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
