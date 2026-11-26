# Decision Report

- generated_at: 2026-11-26T15:11:22.592816+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19699**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.92% / filled 20/20。**
- 全期間 MARKET基準: n=19699, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.92% | **+0.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.92% | **+0.92%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.00% | **+0.00%** |
| LIMIT_ATR | 12/20 | 60.0% | -0.03% | **-0.02%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | -0.16% | **-0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.21% | **+1.02%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.78% | **+0.54%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.10% | **+0.27%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.29% | **+0.27%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$121.73** / 初期 $100.00 (+21.73%)
- 確定トレード: 290件 (TP 106 / SL 176 / EXP 8)
- 最新: MONAD/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.73
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,977.67** / 初期 $100.00 (+1877.67%)
- 確定: 7633件 (Win 2199 / Loss 2456 / Flat 2978) / skip 8627件
- 成長率目線: 平均log +0.000391 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SSV/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,977.67

## 4. Robust Adaptive DryRun ($100)

- 残高: **$466.63** / 初期 $100.00 (+366.63%)
- 確定: 5226件 (Win 1392 / Loss 1125 / Flat 2709) / skip 7884件
- 成長率目線: 平均log +0.000295 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0108 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SSV/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $466.63

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7861件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000315 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-26T15:11:11.149041+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.83% price=60200.0
- Funnel: target 1097 → liquid 138 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BULLA/USDT:USDT | +72.39% | $7,588,747.35 |
| SI/USDT:USDT | +59.96% | $1,849,091.43 |
| NES/USDT:USDT | +49.80% | $1,170,552.27 |
| INIT/USDT:USDT | +47.96% | $4,991,463.98 |
| SSV/USDT:USDT | +36.76% | $2,630,496.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EVAA/USDT:USDT | below_1h_threshold | +1.75% | +2.59% |
| JCT/USDT:USDT | below_1h_threshold | +0.20% | +1.03% |
| INIT/USDT:USDT | below_1h_threshold | +0.11% | +0.94% |
| TQQQ/USDT:USDT | below_1h_threshold | +0.09% | +0.92% |
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +0.05% | +0.89% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
