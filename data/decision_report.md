# Decision Report

- generated_at: 2026-05-31T08:34:53.638214+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5176**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.56% / filled 20/20。**
- 全期間 MARKET基準: n=5176, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.56%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.56% | **+1.56%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.56% | **+1.56%** |
| ASK | 20/20 | 100.0% | +0.87% | **+0.87%** |
| LIMIT_1PCT | 15/20 | 75.0% | +0.43% | **+0.32%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.40% | **+0.26%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.32% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +2.69% | **+0.54%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.31% | **+0.14%** |

## 2. $100 Live Portfolio

- 残高: **$97.61** / 初期 $100.00 (-2.39%)
- 確定トレード: 79件 (TP 23 / SL 53 / EXP 3)
- 最新: ID/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$122.91** / 初期 $100.00 (+22.91%)
- 確定: 811件 (Win 184 / Loss 243 / Flat 384) / skip 926件
- 成長率目線: 平均log +0.000254 / 幾何平均 +0.025% per trade / maxDD +6.32%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HIVE/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $122.91

## 4. Latest Market Context

- 更新: 2026-05-31T08:34:51.118266+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=73889.9
- Funnel: target 773 → liquid 123 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIA/USDT:USDT | +33.58% | $1,643,789.99 |
| PORTAL/USDT:USDT | +24.69% | $11,642,897.77 |
| TA/USDT:USDT | +20.26% | $2,485,773.50 |
| HIVE/USDT:USDT | +15.25% | $2,555,435.06 |
| MYX/USDT:USDT | +14.94% | $2,966,914.40 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIA/USDT:USDT | below_1h_threshold | +2.32% | +2.24% |
| UP/USDT:USDT | below_1h_threshold | +2.05% | +1.97% |
| H/USDT:USDT | below_1h_threshold | +1.91% | +1.84% |
| ALGO/USDT:USDT | below_1h_threshold | +1.65% | +1.58% |
| VVV/USDT:USDT | below_1h_threshold | +1.22% | +1.15% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
