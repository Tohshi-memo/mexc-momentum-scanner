# Decision Report

- generated_at: 2026-09-22T12:31:30.707061+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15325**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15325, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 9/16 | 56.2% | +2.11% | **+1.19%** |
| LIMIT_2PCT | 18/20 | 90.0% | +1.02% | **+0.92%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.80% | **+0.76%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.62% | **+0.40%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +0.43% | **+0.43%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.54% | **+0.27%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.29% | **+0.13%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +0.02% | **+0.01%** |
| MARKET_LONG | 20/20 | 100.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,174.97** / 初期 $100.00 (+1074.97%)
- 確定: 5816件 (Win 1726 / Loss 1872 / Flat 2218) / skip 6070件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: KERNEL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,174.97

## 4. Robust Adaptive DryRun ($100)

- 残高: **$249.51** / 初期 $100.00 (+149.51%)
- 確定: 3353件 (Win 926 / Loss 781 / Flat 1646) / skip 5383件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KERNEL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $249.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.36** / 初期 $100.00 (+22.36%)
- 確定: 3095件 (Win 908 / Loss 1211 / Flat 976) / pending 4件 / skip 3697件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000157 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: KERNEL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $122.36

## 6. Latest Market Context

- 更新: 2026-09-22T12:31:20.655945+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.21% price=86127.8
- Funnel: target 1058 → liquid 176 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=1, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| 4STOCK/USDT:USDT | +62.27% | $3,476,696.03 |
| MUBARAK/USDT:USDT | +48.30% | $4,967,900.73 |
| KERNEL/USDT:USDT | +28.96% | $5,297,797.75 |
| NIL/USDT:USDT | +27.60% | $3,571,372.54 |
| AGT/USDT:USDT | +24.41% | $1,883,676.08 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIL/USDT:USDT | below_relative_strength | +5.20% | +4.99% |
| WIF/USDT:USDT | below_1h_threshold | +3.48% | +3.28% |
| UNI/USDT:USDT | below_1h_threshold | +3.32% | +3.11% |
| BCH/USDT:USDT | below_1h_threshold | +3.24% | +3.03% |
| 4STOCK/USDT:USDT | below_1h_threshold | +2.17% | +1.96% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
