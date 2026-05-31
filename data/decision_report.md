# Decision Report

- generated_at: 2026-05-31T08:49:46.826859+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5177**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.56% / filled 20/20。**
- 全期間 MARKET基準: n=5177, expectancy=-0.05%
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
| LIMIT_ATR | 12/20 | 60.0% | +0.77% | **+0.46%** |
| LIMIT_1PCT | 15/20 | 75.0% | +0.50% | **+0.37%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.46% | **+0.32%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +0.92% | **+0.14%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.11% | **+0.08%** |

## 2. $100 Live Portfolio

- 残高: **$97.61** / 初期 $100.00 (-2.39%)
- 確定トレード: 79件 (TP 23 / SL 53 / EXP 3)
- 最新: ID/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$122.91** / 初期 $100.00 (+22.91%)
- 確定: 812件 (Win 184 / Loss 243 / Flat 385) / skip 926件
- 成長率目線: 平均log +0.000254 / 幾何平均 +0.025% per trade / maxDD +6.32%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PORTAL/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $122.91

## 4. Latest Market Context

- 更新: 2026-05-31T08:49:44.041665+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=73823.8
- Funnel: target 773 → liquid 125 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIA/USDT:USDT | +33.65% | $1,695,807.32 |
| PORTAL/USDT:USDT | +29.18% | $11,810,180.56 |
| TA/USDT:USDT | +19.79% | $2,490,037.67 |
| MYX/USDT:USDT | +14.40% | $3,026,064.15 |
| HIVE/USDT:USDT | +14.17% | $2,615,578.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIA/USDT:USDT | below_1h_threshold | +2.44% | +2.46% |
| NIGHT/USDT:USDT | below_1h_threshold | +2.32% | +2.34% |
| VVV/USDT:USDT | below_1h_threshold | +2.21% | +2.23% |
| H/USDT:USDT | below_1h_threshold | +2.19% | +2.21% |
| UP/USDT:USDT | below_1h_threshold | +1.51% | +1.52% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
