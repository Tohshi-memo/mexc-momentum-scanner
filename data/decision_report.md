# Decision Report

- generated_at: 2026-08-22T08:11:21.102364+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12356**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.20% / filled 20/20。**
- 全期間 MARKET基準: n=12356, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+3.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.20% | **+3.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.20% | **+3.20%** |
| LIMIT_1PCT | 15/20 | 75.0% | +1.87% | **+1.41%** |
| LIMIT_3PCT | 11/20 | 55.0% | +1.20% | **+0.66%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.18% | **+0.65%** |
| LIMIT_2PCT | 12/20 | 60.0% | +1.02% | **+0.61%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +0.30% | **+0.18%** |
| LIMIT_7PCT_LONG | 12/20 | 60.0% | +0.22% | **+0.13%** |
| LIMIT_9PCT_LONG | 8/20 | 40.0% | -0.36% | **-0.15%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | -0.51% | **-0.48%** |
| LIMIT_10PCT_LONG | 7/20 | 35.0% | -1.40% | **-0.49%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$716.07** / 初期 $100.00 (+616.07%)
- 確定: 4447件 (Win 1364 / Loss 1453 / Flat 1630) / skip 4470件
- 成長率目線: 平均log +0.000443 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PEPE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $716.07

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.53** / 初期 $100.00 (+56.53%)
- 確定: 1934件 (Win 533 / Loss 465 / Flat 936) / skip 3833件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PEPE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $156.53

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.04** / 初期 $100.00 (+17.04%)
- 確定: 1862件 (Win 549 / Loss 705 / Flat 608) / pending 0件 / skip 1971件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000630 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ZAMA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $117.04

## 6. Latest Market Context

- 更新: 2026-08-22T08:11:12.272396+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=77371.4
- Funnel: target 1018 → liquid 245 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BASECAT/USDT:USDT | +215.25% | $5,625,239.80 |
| TRUMPOFFICIAL/USDT:USDT | +52.05% | $111,600,191.00 |
| CATE/USDT:USDT | +46.46% | $11,346,940.98 |
| ZAMA/USDT:USDT | +33.69% | $2,862,115.84 |
| AGI/USDT:USDT | +32.62% | $2,172,108.91 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MELANIA/USDT:USDT | below_1h_threshold | +4.63% | +4.52% |
| TRB/USDT:USDT | below_1h_threshold | +1.80% | +1.69% |
| STX/USDT:USDT | below_1h_threshold | +1.65% | +1.54% |
| POPCAT/USDT:USDT | below_1h_threshold | +1.55% | +1.44% |
| ZEC/USDT:USDT | below_1h_threshold | +1.17% | +1.06% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
