# Decision Report

- generated_at: 2026-05-21T22:04:09.024853+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4654**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.17% / filled 20/20。**
- 全期間 MARKET基準: n=4654, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+1.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.17% | **+1.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.17% | **+1.17%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.92% | **+0.83%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.10% | **+0.72%** |
| ASK | 20/20 | 100.0% | +0.69% | **+0.69%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.74% | **+0.56%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.18% | **+0.16%** |
| MARKET_LONG | 20/20 | 100.0% | +0.03% | **+0.03%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$95.25** / 初期 $100.00 (-4.75%)
- 確定トレード: 60件 (TP 15 / SL 42 / EXP 3)
- 最新: STXSTOCK/USDT:USDT SL_HIT PnL -1.86% 残高後 $95.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定: 547件 (Win 138 / Loss 185 / Flat 224) / skip 668件
- 成長率目線: 平均log +0.000355 / 幾何平均 +0.035% per trade / maxDD +4.21%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SPOTSTOCK/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $121.41

## 4. Latest Market Context

- 更新: 2026-05-21T22:04:06.635508+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=77697.3
- Funnel: target 762 → liquid 139 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PLUME/USDT:USDT | +13.17% | $1,275,165.66 |
| GRASS/USDT:USDT | +12.29% | $2,305,592.87 |
| RIVER/USDT:USDT | +8.50% | $9,445,913.44 |
| BILL/USDT:USDT | +8.27% | $14,660,959.00 |
| PEAQ/USDT:USDT | +7.33% | $1,511,361.98 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GRASS/USDT:USDT | below_1h_threshold | +1.15% | +1.07% |
| PEAQ/USDT:USDT | below_1h_threshold | +0.79% | +0.71% |
| LIT/USDT:USDT | below_1h_threshold | +0.79% | +0.71% |
| PLUME/USDT:USDT | below_1h_threshold | +0.62% | +0.54% |
| BEAT/USDT:USDT | below_1h_threshold | +0.46% | +0.38% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
