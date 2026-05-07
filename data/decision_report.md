# Decision Report

- generated_at: 2026-05-07T15:22:48.351346+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3648**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.40% / filled 20/20。**
- 全期間 MARKET基準: n=3648, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.40% | **+0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.89% | **+0.71%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +2.46% | **+1.60%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +2.89% | **+1.59%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +2.70% | **+1.48%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +2.99% | **+1.35%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.98% | **+1.09%** |

## 2. $100 Live Portfolio

- 残高: **$100.83** / 初期 $100.00 (+0.83%)
- 確定トレード: 20件 (TP 6 / SL 12 / EXP 2)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.83
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$109.95** / 初期 $100.00 (+9.95%)
- 確定: 142件 (Win 44 / Loss 53 / Flat 45) / skip 67件
- 成長率目線: 平均log +0.000668 / 幾何平均 +0.067% per trade / maxDD +2.62%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `LIMIT_6PCT_LONG` SL_HIT account -0.50% 残高後 $109.95

## 4. Latest Market Context

- 更新: 2026-05-07T15:22:45.420722+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.37% price=79833.6
- Funnel: target 771 → liquid 182 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B3/USDT:USDT | +86.41% | $10,195,821.54 |
| PENGUIN/USDT:USDT | +76.43% | $4,410,278.07 |
| SATO/USDT:USDT | +65.35% | $3,807,694.77 |
| NIL/USDT:USDT | +51.59% | $5,556,522.21 |
| DOGS/USDT:USDT | +47.32% | $17,860,368.11 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JTO/USDT:USDT | below_1h_threshold | +4.66% | +5.03% |
| D/USDT:USDT | below_1h_threshold | +3.72% | +4.09% |
| QCOMSTOCK/USDT:USDT | below_1h_threshold | +3.19% | +3.56% |
| BILL/USDT:USDT | below_1h_threshold | +1.43% | +1.80% |
| DYDX/USDT:USDT | below_1h_threshold | +1.27% | +1.64% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
