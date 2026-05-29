# Decision Report

- generated_at: 2026-05-29T22:24:41.844713+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5072**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.88% / filled 20/20。**
- 全期間 MARKET基準: n=5072, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+0.88%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.88% | **+0.88%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 10/18 | 55.6% | +1.92% | **+1.07%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.04% | **+0.94%** |
| ASK | 20/20 | 100.0% | +0.93% | **+0.93%** |
| MARKET | 20/20 | 100.0% | +0.88% | **+0.88%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +1.92% | **+0.67%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.42% | **+0.38%** |
| ASK_LONG | 20/20 | 100.0% | +0.32% | **+0.32%** |
| MARKET_LONG | 20/20 | 100.0% | +0.12% | **+0.12%** |

## 2. $100 Live Portfolio

- 残高: **$98.60** / 初期 $100.00 (-1.40%)
- 確定トレード: 74件 (TP 22 / SL 49 / EXP 3)
- 最新: LIT/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.60
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.68** / 初期 $100.00 (+25.68%)
- 確定: 740件 (Win 175 / Loss 226 / Flat 339) / skip 893件
- 成長率目線: 平均log +0.000309 / 幾何平均 +0.031% per trade / maxDD +4.72%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CTR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $125.68

## 4. Latest Market Context

- 更新: 2026-05-29T22:24:39.635079+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.17% price=73508.6
- Funnel: target 773 → liquid 150 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BASED/USDT:USDT | +20.73% | $2,005,683.49 |
| LAB/USDT:USDT | +15.06% | $121,382,811.92 |
| XLM/USDT:USDT | +13.45% | $363,882,665.45 |
| GRASS/USDT:USDT | +6.66% | $4,261,045.24 |
| HEI/USDT:USDT | +6.30% | $9,026,872.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BASED/USDT:USDT | below_1h_threshold | +4.23% | +4.06% |
| CTR/USDT:USDT | below_1h_threshold | +3.80% | +3.63% |
| QNTSTOCK/USDT:USDT | below_1h_threshold | +2.32% | +2.15% |
| LAB/USDT:USDT | below_1h_threshold | +2.15% | +1.98% |
| XLM/USDT:USDT | below_1h_threshold | +1.61% | +1.44% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
