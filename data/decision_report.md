# Decision Report

- generated_at: 2026-05-08T05:07:33.440214+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3735**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.26% / filled 20/20。**
- 全期間 MARKET基準: n=3735, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+2.26%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.26% | **+2.26%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.26% | **+2.26%** |
| LIMIT_1PCT | 16/20 | 80.0% | +2.25% | **+1.80%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.87% | **+1.31%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +3.01% | **+1.20%** |
| LIMIT_3PCT | 11/20 | 55.0% | +2.02% | **+1.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.35% | **+0.68%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +0.92% | **+0.51%** |
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | +0.96% | **+0.29%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.70% | **+0.25%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$98.83** / 初期 $100.00 (-1.17%)
- 確定トレード: 24件 (TP 6 / SL 16 / EXP 2)
- 最新: PENGUIN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.83
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 190件 (Win 48 / Loss 64 / Flat 78) / skip 106件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.043% per trade / maxDD +3.48%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PENGUIN/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-08T05:07:30.673509+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=79590.0
- Funnel: target 772 → liquid 180 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +36.17% | $2,669,869.02 |
| DYDX/USDT:USDT | +22.61% | $13,087,766.70 |
| BSB/USDT:USDT | +21.65% | $3,788,427.38 |
| LAB/USDT:USDT | +20.14% | $211,395,708.09 |
| NOT/USDT:USDT | +18.72% | $10,364,635.90 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +2.06% | +2.10% |
| PLAY/USDT:USDT | below_1h_threshold | +1.77% | +1.80% |
| NOT/USDT:USDT | below_1h_threshold | +1.71% | +1.74% |
| HIGH/USDT:USDT | below_1h_threshold | +1.23% | +1.27% |
| DYDX/USDT:USDT | below_1h_threshold | +0.84% | +0.88% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
