# Decision Report

- generated_at: 2026-05-22T00:53:52.176600+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4658**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.85% / filled 20/20。**
- 全期間 MARKET基準: n=4658, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+1.85%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.85% | **+1.85%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.85% | **+1.85%** |
| ASK | 20/20 | 100.0% | +1.32% | **+1.32%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.14% | **+0.91%** |
| LIMIT_2PCT | 13/20 | 65.0% | +1.32% | **+0.86%** |
| LIMIT_3PCT | 11/20 | 55.0% | +1.48% | **+0.82%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/5 | 40.0% | +1.63% | **+0.65%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.02% | **+0.02%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$95.25** / 初期 $100.00 (-4.75%)
- 確定トレード: 60件 (TP 15 / SL 42 / EXP 3)
- 最新: STXSTOCK/USDT:USDT SL_HIT PnL -1.86% 残高後 $95.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定: 547件 (Win 138 / Loss 185 / Flat 224) / skip 672件
- 成長率目線: 平均log +0.000355 / 幾何平均 +0.035% per trade / maxDD +4.21%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SPOTSTOCK/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $121.41

## 4. Latest Market Context

- 更新: 2026-05-22T00:53:50.058246+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.26% price=77384.9
- Funnel: target 764 → liquid 138 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| GRASS/USDT:USDT | +13.18% | $3,228,741.87 |
| PEAQ/USDT:USDT | +12.56% | $1,853,347.05 |
| PLUME/USDT:USDT | +10.85% | $1,515,251.94 |
| IBMSTOCK/USDT:USDT | +9.60% | $2,088,700.34 |
| NEAR/USDT:USDT | +8.47% | $43,431,028.37 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SATO/USDT:USDT | below_1h_threshold | +3.81% | +4.07% |
| IBMSTOCK/USDT:USDT | below_1h_threshold | +3.60% | +3.86% |
| VVV/USDT:USDT | below_1h_threshold | +2.89% | +3.15% |
| NEAR/USDT:USDT | below_1h_threshold | +1.82% | +2.08% |
| JTO/USDT:USDT | below_1h_threshold | +1.54% | +1.80% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
