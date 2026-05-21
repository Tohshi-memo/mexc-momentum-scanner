# Decision Report

- generated_at: 2026-05-21T12:03:50.920709+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4621**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.66% / filled 20/20。**
- 全期間 MARKET基準: n=4621, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.66%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.66% | **+0.66%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 7/19 | 36.8% | +2.03% | **+0.75%** |
| MARKET | 20/20 | 100.0% | +0.66% | **+0.66%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.67% | **+0.61%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.16% | **+0.40%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +0.42% | **+0.17%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +0.32% | **+0.14%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.29% | **+0.13%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.23% | **+0.08%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 58件 (TP 15 / SL 40 / EXP 3)
- 最新: SKYAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定: 546件 (Win 138 / Loss 185 / Flat 223) / skip 636件
- 成長率目線: 平均log +0.000355 / 幾何平均 +0.036% per trade / maxDD +4.21%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PROVE/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $121.41

## 4. Latest Market Context

- 更新: 2026-05-21T12:03:46.073249+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=77199.4
- Funnel: target 766 → liquid 135 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PROVE/USDT:USDT | +43.53% | $5,366,347.68 |
| EDEN/USDT:USDT | +37.33% | $30,609,402.65 |
| PEAQ/USDT:USDT | +35.20% | $1,077,879.11 |
| ROAM/USDT:USDT | +33.74% | $2,239,921.35 |
| FIDA/USDT:USDT | +29.62% | $12,520,063.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FIDA/USDT:USDT | below_1h_threshold | +4.69% | +4.63% |
| SKYAI/USDT:USDT | below_1h_threshold | +3.36% | +3.31% |
| EDEN/USDT:USDT | below_1h_threshold | +1.47% | +1.41% |
| PEAQ/USDT:USDT | below_1h_threshold | +0.81% | +0.75% |
| NIL/USDT:USDT | below_1h_threshold | +0.72% | +0.67% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
