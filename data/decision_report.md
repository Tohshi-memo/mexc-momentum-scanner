# Decision Report

- generated_at: 2026-09-13T04:01:21.066016+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14377**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14377, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-2.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.80% | **-2.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 11/20 | 55.0% | +0.36% | **+0.20%** |
| LIMIT_8PCT | 10/20 | 50.0% | +0.37% | **+0.19%** |
| LIMIT_6PCT | 12/20 | 60.0% | -0.00% | **-0.00%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | -0.96% | **-0.14%** |
| LIMIT_9PCT | 9/20 | 45.0% | -0.38% | **-0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.50% | **+1.12%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +1.12% | **+1.12%** |
| LIMIT_BB3S_LONG | 4/10 | 40.0% | +2.00% | **+0.80%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.62% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,080.43** / 初期 $100.00 (+980.43%)
- 確定: 5430件 (Win 1635 / Loss 1760 / Flat 2035) / skip 5508件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,080.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$221.31** / 初期 $100.00 (+121.31%)
- 確定: 2895件 (Win 803 / Loss 681 / Flat 1411) / skip 4893件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $221.31

## 5. Causal Adaptive DryRun ($100)

- 残高: **$127.11** / 初期 $100.00 (+27.11%)
- 確定: 2826件 (Win 842 / Loss 1089 / Flat 895) / pending 3件 / skip 3020件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000374 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $127.11

## 6. Latest Market Context

- 更新: 2026-09-13T04:01:07.009171+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=77165.0
- Funnel: target 1068 → liquid 124 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LSK/USDT:USDT | +302.77% | $78,943,448.57 |
| ZCAT/USDT:USDT | +45.32% | $1,196,744.56 |
| POWR/USDT:USDT | +44.46% | $1,783,232.38 |
| LONGXIA/USDT:USDT | +26.15% | $9,585,089.68 |
| STORJ/USDT:USDT | +17.47% | $18,765,166.99 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZCAT/USDT:USDT | below_1h_threshold | +2.48% | +2.48% |
| NIULAI/USDT:USDT | below_1h_threshold | +1.13% | +1.13% |
| FLOCK/USDT:USDT | below_1h_threshold | +0.26% | +0.25% |
| UKOIL/USDT:USDT | below_1h_threshold | +0.15% | +0.15% |
| ALCH/USDT:USDT | below_1h_threshold | +0.11% | +0.11% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
