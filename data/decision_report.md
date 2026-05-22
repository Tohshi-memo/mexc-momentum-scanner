# Decision Report

- generated_at: 2026-05-22T09:03:51.308556+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4678**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.48% / filled 20/20。**
- 全期間 MARKET基準: n=4678, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.48%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.48% | **+0.48%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.74% | **+0.74%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.47% | **+0.69%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.69% | **+0.68%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/9 | 55.6% | +3.20% | **+1.78%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.56% | **+1.48%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.27% | **+0.95%** |
| ASK_LONG | 20/20 | 100.0% | +0.89% | **+0.89%** |
| MARKET_LONG | 20/20 | 100.0% | +0.52% | **+0.52%** |

## 2. $100 Live Portfolio

- 残高: **$95.25** / 初期 $100.00 (-4.75%)
- 確定トレード: 60件 (TP 15 / SL 42 / EXP 3)
- 最新: STXSTOCK/USDT:USDT SL_HIT PnL -1.86% 残高後 $95.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.55** / 初期 $100.00 (+21.55%)
- 確定: 549件 (Win 139 / Loss 185 / Flat 225) / skip 690件
- 成長率目線: 平均log +0.000355 / 幾何平均 +0.036% per trade / maxDD +4.21%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ALT/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.12% 残高後 $121.55

## 4. Latest Market Context

- 更新: 2026-05-22T09:03:48.939949+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=77256.8
- Funnel: target 768 → liquid 139 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BUILDONBOB/USDT:USDT | +43.87% | $3,273,105.37 |
| ALT/USDT:USDT | +36.26% | $1,246,985.49 |
| NEAR/USDT:USDT | +25.52% | $89,180,467.39 |
| BEAT/USDT:USDT | +22.91% | $8,960,533.68 |
| GRASS/USDT:USDT | +18.92% | $5,425,444.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EDEN/USDT:USDT | below_1h_threshold | +0.82% | +0.79% |
| NAORIS/USDT:USDT | below_1h_threshold | +0.57% | +0.55% |
| RENDER/USDT:USDT | below_1h_threshold | +0.55% | +0.52% |
| ESPORTS/USDT:USDT | below_1h_threshold | +0.55% | +0.52% |
| BEAT/USDT:USDT | below_1h_threshold | +0.54% | +0.52% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
