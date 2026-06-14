# Decision Report

- generated_at: 2026-06-14T22:37:32.403293+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6707**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.51% / filled 20/20。**
- 全期間 MARKET基準: n=6707, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.51%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.51% | **+0.51%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 15/20 | 75.0% | +0.88% | **+0.66%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.82% | **+0.57%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.88% | **+0.56%** |
| MARKET | 20/20 | 100.0% | +0.51% | **+0.51%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.55% | **+1.15%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +1.17% | **+0.59%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.82% | **+0.45%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$100.99** / 初期 $100.00 (+0.99%)
- 確定トレード: 4件 (TP 2 / SL 2 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.99
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$172.74** / 初期 $100.00 (+72.74%)
- 確定: 1580件 (Win 420 / Loss 498 / Flat 662) / skip 1688件
- 成長率目線: 平均log +0.000346 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZEC/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $172.74

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.70** / 初期 $100.00 (-1.30%)
- 確定: 77件 (Win 20 / Loss 15 / Flat 42) / skip 41件
- 成長率目線: 平均log -0.000170 / 幾何平均 -0.017% per trade / maxDD +2.07%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0481 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ZEC/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $98.70

## 5. Latest Market Context

- 更新: 2026-06-14T22:37:27.533778+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=65379.1
- Funnel: target 770 → liquid 137 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| OPG/USDT:USDT | +40.72% | $4,073,998.62 |
| EVAA/USDT:USDT | +15.57% | $13,867,230.54 |
| EDEN/USDT:USDT | +15.17% | $1,262,441.38 |
| RIF/USDT:USDT | +14.27% | $7,465,856.49 |
| BABY/USDT:USDT | +13.42% | $2,082,004.91 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| OPG/USDT:USDT | below_1h_threshold | +3.27% | +3.13% |
| ZEC/USDT:USDT | below_1h_threshold | +2.79% | +2.65% |
| BABY/USDT:USDT | below_1h_threshold | +2.39% | +2.25% |
| TRUMPOFFICIAL/USDT:USDT | below_1h_threshold | +2.30% | +2.16% |
| NEAR/USDT:USDT | below_1h_threshold | +1.83% | +1.69% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
