# Decision Report

- generated_at: 2026-09-29T05:16:20.326554+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15755**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15755, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.19% | **+0.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 2/20 | 10.0% | +4.25% | **+0.42%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.48% | **+0.39%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.54% | **+0.35%** |
| MARKET | 20/20 | 100.0% | +0.19% | **+0.19%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.11% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +1.63% | **+1.06%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.27% | **+0.89%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.70% | **+0.85%** |
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +0.49% | **+0.49%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.81% | **+0.45%** |

## 2. $100 Live Portfolio

- 残高: **$120.75** / 初期 $100.00 (+20.75%)
- 確定トレード: 225件 (TP 82 / SL 136 / EXP 7)
- 最新: XLM/USDT:USDT SL_HIT PnL -2.52% 残高後 $120.75
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,227.24** / 初期 $100.00 (+1127.24%)
- 確定: 5984件 (Win 1766 / Loss 1925 / Flat 2293) / skip 6332件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NMR/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $1,227.24

## 4. Robust Adaptive DryRun ($100)

- 残高: **$263.08** / 初期 $100.00 (+163.08%)
- 確定: 3534件 (Win 974 / Loss 812 / Flat 1748) / skip 5632件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: QNT/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $263.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 3913件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `見送り` (no_strategy_passed_causal_filters) / causal_score n/a / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-09-29T05:16:09.084367+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=83240.0
- Funnel: target 1069 → liquid 171 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| GRASS/USDT:USDT | +27.40% | $5,924,415.48 |
| NMR/USDT:USDT | +24.79% | $9,724,747.13 |
| BTW/USDT:USDT | +21.18% | $18,271,753.25 |
| 0G/USDT:USDT | +20.01% | $1,442,611.35 |
| CRV/USDT:USDT | +18.57% | $13,496,927.59 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MARSCOIN/USDT:USDT | below_1h_threshold | +3.87% | +3.79% |
| MUBARAK/USDT:USDT | below_1h_threshold | +2.71% | +2.62% |
| GRASS/USDT:USDT | below_1h_threshold | +2.65% | +2.56% |
| QNT/USDT:USDT | below_1h_threshold | +2.23% | +2.14% |
| PHA/USDT:USDT | below_1h_threshold | +1.95% | +1.86% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
