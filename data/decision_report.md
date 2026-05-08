# Decision Report

- generated_at: 2026-05-08T01:07:33.400446+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3717**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.53% / filled 20/20。**
- 全期間 MARKET基準: n=3717, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.53%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.53% | **+0.53%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_8PCT | 4/20 | 20.0% | +2.85% | **+0.57%** |
| LIMIT_ATR | 7/20 | 35.0% | +1.59% | **+0.56%** |
| MARKET | 20/20 | 100.0% | +0.53% | **+0.53%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.73% | **+0.51%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.90% | **+0.59%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.05% | **+0.53%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.87% | **+0.48%** |
| MARKET_LONG | 20/20 | 100.0% | +0.41% | **+0.41%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$99.32** / 初期 $100.00 (-0.68%)
- 確定トレード: 23件 (TP 6 / SL 15 / EXP 2)
- 最新: D/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.32
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 189件 (Win 48 / Loss 64 / Flat 77) / skip 89件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +3.48%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FHE/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-08T01:07:30.666020+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=79749.9
- Funnel: target 767 → liquid 185 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +21.98% | $6,128,029.06 |
| LAB/USDT:USDT | +18.40% | $211,725,522.45 |
| NIL/USDT:USDT | +18.23% | $30,892,576.06 |
| SATO/USDT:USDT | +17.54% | $8,597,922.95 |
| NOT/USDT:USDT | +16.84% | $10,910,857.32 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SATO/USDT:USDT | below_1h_threshold | +4.44% | +4.50% |
| M/USDT:USDT | below_1h_threshold | +2.86% | +2.92% |
| NIL/USDT:USDT | below_1h_threshold | +1.52% | +1.58% |
| BASED/USDT:USDT | below_1h_threshold | +1.25% | +1.31% |
| B3/USDT:USDT | below_1h_threshold | +1.24% | +1.30% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
