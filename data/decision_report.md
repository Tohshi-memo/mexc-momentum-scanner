# Decision Report

- generated_at: 2026-06-09T23:24:16.493055+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6164**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=6164, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| ASK | 20/20 | 100.0% | +0.79% | **+0.79%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.63% | **+0.41%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +0.87% | **+0.57%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +4.93% | **+0.49%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.62% | **+0.40%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +0.62% | **+0.37%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.54% | **+0.35%** |

## 2. $100 Live Portfolio

- 残高: **$95.66** / 初期 $100.00 (-4.34%)
- 確定トレード: 13件 (TP 1 / SL 11 / EXP 1)
- 最新: PIPPIN/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.66
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$148.01** / 初期 $100.00 (+48.01%)
- 確定: 1188件 (Win 297 / Loss 374 / Flat 517) / skip 1537件
- 成長率目線: 平均log +0.000330 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EPIC/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $148.01

## 4. Latest Market Context

- 更新: 2026-06-09T23:24:13.715605+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=61715.0
- Funnel: target 778 → liquid 152 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +31.86% | $8,834,041.35 |
| HOME/USDT:USDT | +17.70% | $4,571,155.53 |
| STG/USDT:USDT | +17.05% | $2,318,353.83 |
| BLESS/USDT:USDT | +12.53% | $4,409,702.40 |
| LIT/USDT:USDT | +8.23% | $4,127,483.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_1h_threshold | +3.93% | +3.88% |
| CHZ/USDT:USDT | below_1h_threshold | +2.26% | +2.21% |
| ORDI/USDT:USDT | below_1h_threshold | +1.43% | +1.38% |
| ZRO/USDT:USDT | below_1h_threshold | +1.32% | +1.28% |
| UB/USDT:USDT | below_1h_threshold | +1.31% | +1.26% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
