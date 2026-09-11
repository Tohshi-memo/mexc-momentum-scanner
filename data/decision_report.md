# Decision Report

- generated_at: 2026-09-11T09:36:20.257655+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14205**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.42% / filled 20/20。**
- 全期間 MARKET基準: n=14205, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.42%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.42% | **+0.42%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.42% | **+0.42%** |
| LIMIT_5PCT | 3/20 | 15.0% | +0.95% | **+0.14%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.12% | **+0.04%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.04% | **+0.02%** |
| LIMIT_ATR | 13/20 | 65.0% | -0.23% | **-0.15%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +1.61% | **+1.61%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.65% | **+0.62%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.47% | **+0.35%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.49% | **+0.34%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.57% | **+0.34%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 208件 (TP 78 / SL 125 / EXP 5)
- 最新: EIGEN/USDT:USDT SL_HIT PnL -3.25% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,066.75** / 初期 $100.00 (+966.75%)
- 確定: 5370件 (Win 1616 / Loss 1736 / Flat 2018) / skip 5396件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: 4STOCK/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.12% 残高後 $1,066.75

## 4. Robust Adaptive DryRun ($100)

- 残高: **$208.37** / 初期 $100.00 (+108.37%)
- 確定: 2799件 (Win 769 / Loss 650 / Flat 1380) / skip 4817件
- 成長率目線: 平均log +0.000262 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0058 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: 4STOCK/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $208.37

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.66** / 初期 $100.00 (+22.66%)
- 確定: 2708件 (Win 799 / Loss 1036 / Flat 873) / pending 3件 / skip 2964件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000151 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: 4STOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $122.66

## 6. Latest Market Context

- 更新: 2026-09-11T09:36:09.688022+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.40% price=77013.9
- Funnel: target 1068 → liquid 164 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIULAI/USDT:USDT | +63.22% | $14,140,078.83 |
| RAY/USDT:USDT | +22.54% | $18,179,082.04 |
| LSK/USDT:USDT | +22.45% | $2,137,877.11 |
| PONS/USDT:USDT | +16.45% | $8,803,568.56 |
| MARSCOIN/USDT:USDT | +13.87% | $3,033,259.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIULAI/USDT:USDT | below_1h_threshold | +4.37% | +4.77% |
| UAI/USDT:USDT | below_1h_threshold | +3.79% | +4.19% |
| THETA/USDT:USDT | below_1h_threshold | +1.50% | +1.90% |
| 4/USDT:USDT | below_1h_threshold | +1.43% | +1.83% |
| CNPY/USDT:USDT | below_1h_threshold | +1.26% | +1.66% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
