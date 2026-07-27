# Decision Report

- generated_at: 2026-07-27T19:01:12.347299+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9645**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9645, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.13%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.13% | **-0.13%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +0.88% | **+0.88%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.48% | **+0.40%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.25% | **+0.17%** |
| LIMIT_5PCT | 4/20 | 20.0% | -0.29% | **-0.06%** |
| LIMIT_4PCT | 12/20 | 60.0% | -0.16% | **-0.10%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/6 | 33.3% | +8.00% | **+2.67%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.76% | **+1.24%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.30% | **+0.72%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.44% | **+0.57%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.59% | **+0.32%** |

## 2. $100 Live Portfolio

- 残高: **$106.92** / 初期 $100.00 (+6.92%)
- 確定トレード: 145件 (TP 50 / SL 90 / EXP 5)
- 最新: ON/USDT:USDT SL_HIT PnL -4.00% 残高後 $106.92
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$459.29** / 初期 $100.00 (+359.29%)
- 確定: 3432件 (Win 1087 / Loss 1117 / Flat 1228) / skip 2774件
- 成長率目線: 平均log +0.000444 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LA/USDT:USDT `LIMIT_BB3S_LONG` TP_HIT account +1.00% 残高後 $459.29

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1224件 (Win 338 / Loss 275 / Flat 611) / skip 1832件
- 成長率目線: 平均log +0.000259 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0092 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOXS/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$108.66** / 初期 $100.00 (+8.66%)
- 確定: 665件 (Win 219 / Loss 253 / Flat 193) / pending 2件 / skip 447件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000332 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $108.66

## 6. Latest Market Context

- 更新: 2026-07-27T19:01:06.063075+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=64852.2
- Funnel: target 902 → liquid 173 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LA/USDT:USDT | +45.81% | $3,132,038.99 |
| RIF/USDT:USDT | +15.55% | $5,167,763.12 |
| AEON1/USDT:USDT | +12.51% | $1,174,858.49 |
| JIMOTHY/USDT:USDT | +12.48% | $1,967,314.27 |
| ALLO/USDT:USDT | +7.52% | $4,339,353.16 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MUU/USDT:USDT | below_1h_threshold | +2.66% | +2.66% |
| SOXL/USDT:USDT | below_1h_threshold | +2.50% | +2.50% |
| KORU/USDT:USDT | below_1h_threshold | +2.32% | +2.33% |
| RIF/USDT:USDT | below_1h_threshold | +1.41% | +1.42% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +1.37% | +1.38% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
