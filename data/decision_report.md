# Decision Report

- generated_at: 2026-09-29T12:11:13.522273+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15764**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15764, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.80% | **-0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 8/17 | 47.1% | +1.94% | **+0.91%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.32% | **+0.26%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.08% | **+0.07%** |
| LIMIT_6PCT | 3/20 | 15.0% | -0.08% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +6.32% | **+4.22%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.98% | **+1.29%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.95% | **+1.07%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.31% | **+0.59%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.29% | **+0.58%** |

## 2. $100 Live Portfolio

- 残高: **$120.75** / 初期 $100.00 (+20.75%)
- 確定トレード: 225件 (TP 82 / SL 136 / EXP 7)
- 最新: XLM/USDT:USDT SL_HIT PnL -2.52% 残高後 $120.75
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,227.24** / 初期 $100.00 (+1127.24%)
- 確定: 5985件 (Win 1766 / Loss 1925 / Flat 2294) / skip 6340件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GRASS/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,227.24

## 4. Robust Adaptive DryRun ($100)

- 残高: **$263.08** / 初期 $100.00 (+163.08%)
- 確定: 3534件 (Win 974 / Loss 812 / Flat 1748) / skip 5641件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: QNT/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $263.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 3925件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000076 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-09-29T12:11:04.423970+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=84283.8
- Funnel: target 1067 → liquid 164 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +33.85% | $16,226,603.70 |
| 0G/USDT:USDT | +32.73% | $2,243,227.96 |
| GRASS/USDT:USDT | +26.74% | $8,165,704.02 |
| CRV/USDT:USDT | +18.72% | $19,108,424.98 |
| SYRUP/USDT:USDT | +18.63% | $3,058,946.74 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PHA/USDT:USDT | below_1h_threshold | +1.95% | +1.98% |
| POL/USDT:USDT | below_1h_threshold | +1.42% | +1.45% |
| PENGU/USDT:USDT | below_1h_threshold | +1.25% | +1.28% |
| QNT/USDT:USDT | below_1h_threshold | +0.92% | +0.95% |
| SOXL/USDT:USDT | below_1h_threshold | +0.79% | +0.82% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
