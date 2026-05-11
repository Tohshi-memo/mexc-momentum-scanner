# Decision Report

- generated_at: 2026-05-11T12:00:43.862412+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4028**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4028, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.89%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.89% | **-0.89%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 17/20 | 85.0% | +0.74% | **+0.63%** |
| LIMIT_5PCT | 5/20 | 25.0% | +2.36% | **+0.59%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.63% | **+0.44%** |
| LIMIT_FIB1272 | 14/20 | 70.0% | +0.17% | **+0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 8/8 | 100.0% | +0.70% | **+0.70%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.32% | **+0.59%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.19% | **+0.54%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.78% | **+0.47%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.71% | **+0.37%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 33件 (TP 8 / SL 22 / EXP 3)
- 最新: SIREN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.86** / 初期 $100.00 (+7.86%)
- 確定: 218件 (Win 54 / Loss 76 / Flat 88) / skip 371件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +4.09%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $107.86

## 4. Latest Market Context

- 更新: 2026-05-11T12:00:40.667226+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=81172.9
- Funnel: target 762 → liquid 182 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +38.65% | $13,569,053.04 |
| PENGUIN/USDT:USDT | +33.84% | $1,209,990.93 |
| B/USDT:USDT | +30.06% | $11,219,404.45 |
| SAGA/USDT:USDT | +28.71% | $3,206,255.71 |
| TROLLSOL/USDT:USDT | +21.70% | $4,427,324.70 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PENGUIN/USDT:USDT | below_1h_threshold | +0.84% | +0.83% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +0.46% | +0.45% |
| SAGA/USDT:USDT | below_1h_threshold | +0.41% | +0.40% |
| B/USDT:USDT | below_1h_threshold | +0.37% | +0.36% |
| ZRO/USDT:USDT | below_1h_threshold | +0.33% | +0.32% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
