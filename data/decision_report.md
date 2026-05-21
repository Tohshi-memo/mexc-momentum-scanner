# Decision Report

- generated_at: 2026-05-21T16:33:59.198562+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4649**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.25% / filled 20/20。**
- 全期間 MARKET基準: n=4649, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=+0.25%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.25% | **+0.25%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 14/20 | 70.0% | +0.96% | **+0.67%** |
| ASK | 20/20 | 100.0% | +0.33% | **+0.33%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| MARKET | 20/20 | 100.0% | +0.25% | **+0.25%** |
| LIMIT_5PCT | 3/20 | 15.0% | +0.95% | **+0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +0.53% | **+0.29%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +0.22% | **+0.12%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.19% | **+0.08%** |

## 2. $100 Live Portfolio

- 残高: **$95.25** / 初期 $100.00 (-4.75%)
- 確定トレード: 60件 (TP 15 / SL 42 / EXP 3)
- 最新: STXSTOCK/USDT:USDT SL_HIT PnL -1.86% 残高後 $95.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定: 547件 (Win 138 / Loss 185 / Flat 224) / skip 663件
- 成長率目線: 平均log +0.000355 / 幾何平均 +0.035% per trade / maxDD +4.21%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SPOTSTOCK/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $121.41

## 4. Latest Market Context

- 更新: 2026-05-21T16:33:56.910736+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=77249.9
- Funnel: target 766 → liquid 140 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +6.29% | $74,275,216.44 |
| B/USDT:USDT | +2.41% | $2,193,968.57 |
| BANANAS31/USDT:USDT | +2.33% | $2,993,176.87 |
| MUSTOCK/USDT:USDT | +1.74% | $6,913,361.72 |
| PENDLE/USDT:USDT | +1.60% | $1,863,114.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| B/USDT:USDT | below_1h_threshold | +2.42% | +2.39% |
| BANANAS31/USDT:USDT | below_1h_threshold | +2.34% | +2.30% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +1.72% | +1.69% |
| PENDLE/USDT:USDT | below_1h_threshold | +1.61% | +1.57% |
| BABY/USDT:USDT | below_1h_threshold | +1.24% | +1.21% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
