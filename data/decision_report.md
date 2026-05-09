# Decision Report

- generated_at: 2026-05-09T07:03:12.805355+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3862**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.68% / filled 20/20。**
- 全期間 MARKET基準: n=3862, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.68%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.68% | **+0.68%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 14/20 | 70.0% | +1.29% | **+0.91%** |
| ASK | 20/20 | 100.0% | +0.83% | **+0.83%** |
| MARKET | 20/20 | 100.0% | +0.68% | **+0.68%** |
| LIMIT_5PCT | 6/20 | 30.0% | +1.04% | **+0.31%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +2.33% | **+0.93%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.58% | **+0.40%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| MARKET_LONG | 20/20 | 100.0% | +0.23% | **+0.23%** |

## 2. $100 Live Portfolio

- 残高: **$98.71** / 初期 $100.00 (-1.29%)
- 確定トレード: 29件 (TP 7 / SL 19 / EXP 3)
- 最新: LUNC/USDT:USDT EXPIRED PnL +3.11% 残高後 $98.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 194件 (Win 48 / Loss 64 / Flat 82) / skip 229件
- 成長率目線: 平均log +0.000416 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PHAROS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-09T07:03:09.918398+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=80205.1
- Funnel: target 767 → liquid 173 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DYM/USDT:USDT | +29.50% | $2,436,006.06 |
| ZEREBRO/USDT:USDT | +27.71% | $1,217,775.62 |
| CORE/USDT:USDT | +25.76% | $2,623,787.31 |
| SATO/USDT:USDT | +20.17% | $3,806,624.61 |
| REZ/USDT:USDT | +20.10% | $1,558,480.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| COLLECT/USDT:USDT | below_1h_threshold | +2.09% | +2.10% |
| REZ/USDT:USDT | below_1h_threshold | +1.09% | +1.10% |
| BILL/USDT:USDT | below_1h_threshold | +0.87% | +0.88% |
| BRETT/USDT:USDT | below_1h_threshold | +0.70% | +0.71% |
| CORE/USDT:USDT | below_1h_threshold | +0.64% | +0.65% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
