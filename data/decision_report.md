# Decision Report

- generated_at: 2026-09-21T10:21:40.591601+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15248**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15248, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.17% | **-0.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.96% | **+0.69%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.33% | **+0.20%** |
| LIMIT_BB3S | 5/13 | 38.5% | +0.50% | **+0.19%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.18% | **+0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/6 | 66.7% | +2.61% | **+1.74%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.56% | **+0.78%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.73% | **+0.62%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +2.02% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,174.95** / 初期 $100.00 (+1074.95%)
- 確定: 5739件 (Win 1710 / Loss 1846 / Flat 2183) / skip 6070件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PHA/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.12% 残高後 $1,174.95

## 4. Robust Adaptive DryRun ($100)

- 残高: **$247.51** / 初期 $100.00 (+147.51%)
- 確定: 3310件 (Win 915 / Loss 765 / Flat 1630) / skip 5349件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0157 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PHA/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $247.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.69** / 初期 $100.00 (+22.69%)
- 確定: 3026件 (Win 892 / Loss 1186 / Flat 948) / pending 6件 / skip 3689件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000122 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PHA/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.04% 残高後 $122.69

## 6. Latest Market Context

- 更新: 2026-09-21T10:21:30.326271+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=84641.5
- Funnel: target 1050 → liquid 156 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 96.0 >= 65=1, 4h RSI 71.1 >= 65=1, 4h RSI 67.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ZETA/USDT:USDT | +69.47% | $6,284,255.96 |
| PHA/USDT:USDT | +61.54% | $1,870,028.78 |
| NIL/USDT:USDT | +30.47% | $7,437,269.98 |
| PTB/USDT:USDT | +29.51% | $1,154,394.20 |
| UAI/USDT:USDT | +25.16% | $1,628,828.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MARSCOIN/USDT:USDT | below_1h_threshold | +3.45% | +3.43% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +2.94% | +2.92% |
| EGLD/USDT:USDT | below_1h_threshold | +1.76% | +1.74% |
| SEI/USDT:USDT | below_1h_threshold | +1.70% | +1.68% |
| NEAR/USDT:USDT | below_1h_threshold | +1.69% | +1.67% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
