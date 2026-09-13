# Decision Report

- generated_at: 2026-09-13T05:11:20.358126+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14389**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14389, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 10/20 | 50.0% | +3.36% | **+1.68%** |
| LIMIT_8PCT | 8/20 | 40.0% | +3.93% | **+1.57%** |
| LIMIT_9PCT | 6/20 | 30.0% | +3.43% | **+1.03%** |
| LIMIT_10PCT | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_6PCT | 10/20 | 50.0% | +0.78% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/12 | 50.0% | +5.70% | **+2.85%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.22% | **+1.16%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.83% | **+0.71%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +1.52% | **+0.38%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.44% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,080.43** / 初期 $100.00 (+980.43%)
- 確定: 5430件 (Win 1635 / Loss 1760 / Flat 2035) / skip 5520件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,080.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$224.67** / 初期 $100.00 (+124.67%)
- 確定: 2907件 (Win 808 / Loss 686 / Flat 1413) / skip 4893件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: FLOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $224.67

## 5. Causal Adaptive DryRun ($100)

- 残高: **$127.63** / 初期 $100.00 (+27.63%)
- 確定: 2836件 (Win 846 / Loss 1094 / Flat 896) / pending 5件 / skip 3020件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000310 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: VTHO/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $127.63

## 6. Latest Market Context

- 更新: 2026-09-13T05:11:09.996659+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=77204.9
- Funnel: target 1068 → liquid 125 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LSK/USDT:USDT | +315.47% | $81,661,017.59 |
| VTHO/USDT:USDT | +51.26% | $3,259,957.06 |
| POWR/USDT:USDT | +33.27% | $1,981,610.60 |
| ZCAT/USDT:USDT | +31.89% | $1,253,577.20 |
| SAGA/USDT:USDT | +23.50% | $1,029,436.76 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZCAT/USDT:USDT | below_1h_threshold | +3.28% | +3.25% |
| LAB/USDT:USDT | below_1h_threshold | +2.66% | +2.62% |
| POWR/USDT:USDT | below_1h_threshold | +1.59% | +1.56% |
| FLOCK/USDT:USDT | below_1h_threshold | +1.51% | +1.47% |
| VTHO/USDT:USDT | below_1h_threshold | +1.44% | +1.41% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
