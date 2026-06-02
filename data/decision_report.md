# Decision Report

- generated_at: 2026-06-02T04:29:23.120348+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5404**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.44% / filled 20/20。**
- 全期間 MARKET基準: n=5404, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.44%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.44% | **+0.44%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.48% | **+0.48%** |
| MARKET | 20/20 | 100.0% | +0.44% | **+0.44%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.56% | **+0.23%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +1.67% | **+1.00%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.92% | **+0.87%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.29% | **+0.80%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.68% | **+0.48%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.62% | **+0.37%** |

## 2. $100 Live Portfolio

- 残高: **$96.63** / 初期 $100.00 (-3.37%)
- 確定トレード: 84件 (TP 24 / SL 57 / EXP 3)
- 最新: PORTAL/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.63
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$133.60** / 初期 $100.00 (+33.60%)
- 確定: 916件 (Win 214 / Loss 273 / Flat 429) / skip 1049件
- 成長率目線: 平均log +0.000316 / 幾何平均 +0.032% per trade / maxDD +7.25%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EPIC/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $133.60

## 4. Latest Market Context

- 更新: 2026-06-02T04:29:17.738883+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=70978.8
- Funnel: target 777 → liquid 146 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SKYAI/USDT:USDT | +28.96% | $4,762,903.39 |
| ESPORTS/USDT:USDT | +24.52% | $11,026,835.28 |
| LAB/USDT:USDT | +21.30% | $203,006,629.97 |
| WLD/USDT:USDT | +19.74% | $141,318,201.04 |
| MRVLSTOCK/USDT:USDT | +18.92% | $1,570,329.94 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +3.85% | +3.77% |
| BIANRENSHENG/USDT:USDT | below_1h_threshold | +3.67% | +3.59% |
| H/USDT:USDT | below_1h_threshold | +2.68% | +2.60% |
| XPL/USDT:USDT | below_1h_threshold | +2.01% | +1.93% |
| STG/USDT:USDT | below_1h_threshold | +1.85% | +1.76% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
