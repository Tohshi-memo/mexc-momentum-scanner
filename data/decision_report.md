# Decision Report

- generated_at: 2026-05-21T23:08:02.444267+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4656**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.51% / filled 20/20。**
- 全期間 MARKET基準: n=4656, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+1.51%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.51% | **+1.51%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.51% | **+1.51%** |
| ASK | 20/20 | 100.0% | +1.03% | **+1.03%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.96% | **+0.81%** |
| LIMIT_3PCT | 12/20 | 60.0% | +1.28% | **+0.77%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.08% | **+0.76%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
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
- 確定: 547件 (Win 138 / Loss 185 / Flat 224) / skip 670件
- 成長率目線: 平均log +0.000355 / 幾何平均 +0.035% per trade / maxDD +4.21%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SPOTSTOCK/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $121.41

## 4. Latest Market Context

- 更新: 2026-05-21T23:08:00.806552+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=77666.1
- Funnel: target 763 → liquid 137 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| GRASS/USDT:USDT | +13.02% | $2,849,449.66 |
| PEAQ/USDT:USDT | +12.18% | $1,539,898.66 |
| PLUME/USDT:USDT | +12.09% | $1,402,744.45 |
| LIT/USDT:USDT | +7.83% | $9,016,426.13 |
| NEAR/USDT:USDT | +7.80% | $41,293,278.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PEAQ/USDT:USDT | below_1h_threshold | +4.55% | +4.45% |
| LIT/USDT:USDT | below_1h_threshold | +0.88% | +0.78% |
| BABY/USDT:USDT | below_1h_threshold | +0.78% | +0.69% |
| NEAR/USDT:USDT | below_1h_threshold | +0.72% | +0.63% |
| IBMSTOCK/USDT:USDT | below_1h_threshold | +0.65% | +0.55% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
