# Decision Report

- generated_at: 2026-10-10T19:36:13.416284+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16511**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16511, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.88%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.88% | **-0.88%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 5/20 | 25.0% | +1.04% | **+0.26%** |
| LIMIT_4PCT | 10/20 | 50.0% | +0.10% | **+0.05%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.47% | **+0.05%** |
| LIMIT_3PCT | 16/20 | 80.0% | -0.13% | **-0.11%** |
| LIMIT_BB3S | 4/9 | 44.4% | -0.33% | **-0.15%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.42% | **+1.42%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +1.52% | **+0.99%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +0.83% | **+0.29%** |
| LIMIT_2PCT_LONG | 9/20 | 45.0% | +0.59% | **+0.27%** |
| LIMIT_8PCT_LONG | 4/20 | 20.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$121.48** / 初期 $100.00 (+21.48%)
- 確定トレード: 237件 (TP 88 / SL 142 / EXP 7)
- 最新: SI/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.48
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,298.24** / 初期 $100.00 (+1198.24%)
- 確定: 6287件 (Win 1845 / Loss 2015 / Flat 2427) / skip 6785件
- 成長率目線: 平均log +0.000408 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CFX/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.39% 残高後 $1,298.24

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.04** / 初期 $100.00 (+174.04%)
- 確定: 3636件 (Win 1010 / Loss 853 / Flat 1773) / skip 6286件
- 成長率目線: 平均log +0.000277 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MINA/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $274.04

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4672件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000213 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-10T19:36:05.198291+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=83045.8
- Funnel: target 1087 → liquid 148 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CHIP/USDT:USDT | +25.40% | $8,552,525.31 |
| STRK/USDT:USDT | +8.72% | $48,980,040.11 |
| TIA/USDT:USDT | +8.28% | $24,278,199.69 |
| BR/USDT:USDT | +7.41% | $6,129,104.19 |
| RLC/USDT:USDT | +6.14% | $37,118,792.54 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CHIP/USDT:USDT | below_1h_threshold | +2.82% | +2.75% |
| TIA/USDT:USDT | below_1h_threshold | +2.00% | +1.93% |
| ZKSYNC/USDT:USDT | below_1h_threshold | +1.81% | +1.74% |
| CFX/USDT:USDT | below_1h_threshold | +1.75% | +1.68% |
| ETHFI/USDT:USDT | below_1h_threshold | +1.27% | +1.20% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
