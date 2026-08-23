# Decision Report

- generated_at: 2026-08-23T19:21:23.849585+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12468**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12468, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.64%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.64% | **-1.64%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 16/20 | 80.0% | +0.28% | **+0.22%** |
| LIMIT_BB3S | 9/14 | 64.3% | +0.25% | **+0.16%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |
| LIMIT_FIB1272 | 11/20 | 55.0% | -0.22% | **-0.12%** |
| LIMIT_4PCT | 13/20 | 65.0% | -0.28% | **-0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +5.60% | **+4.48%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +3.14% | **+1.73%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +3.39% | **+1.70%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +4.12% | **+1.65%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +2.09% | **+1.15%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$707.63** / 初期 $100.00 (+607.63%)
- 確定: 4495件 (Win 1371 / Loss 1470 / Flat 1654) / skip 4534件
- 成長率目線: 平均log +0.000435 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FF/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account +0.00% 残高後 $707.63

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.63** / 初期 $100.00 (+56.63%)
- 確定: 1944件 (Win 534 / Loss 468 / Flat 942) / skip 3935件
- 成長率目線: 平均log +0.000231 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SPK/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $156.63

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.91** / 初期 $100.00 (+16.91%)
- 確定: 1865件 (Win 550 / Loss 707 / Flat 608) / pending 0件 / skip 2081件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000084 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HEMI/USDT:USDT `MARKET` EXPIRED account +0.24% 残高後 $116.91

## 6. Latest Market Context

- 更新: 2026-08-23T19:21:14.942774+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=77345.0
- Funnel: target 1018 → liquid 168 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SPK/USDT:USDT | +11.11% | $3,646,355.25 |
| PENGU/USDT:USDT | +9.67% | $13,335,297.59 |
| BASECAT/USDT:USDT | +8.62% | $2,911,159.69 |
| 1000RATS/USDT:USDT | +8.60% | $1,468,509.35 |
| BRETT/USDT:USDT | +6.88% | $1,090,399.06 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| 1000RATS/USDT:USDT | below_1h_threshold | +3.58% | +3.53% |
| ZAMA/USDT:USDT | below_1h_threshold | +3.29% | +3.24% |
| STX/USDT:USDT | below_1h_threshold | +1.93% | +1.89% |
| MELANIA/USDT:USDT | below_1h_threshold | +1.64% | +1.59% |
| MORPHO/USDT:USDT | below_1h_threshold | +1.48% | +1.43% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
