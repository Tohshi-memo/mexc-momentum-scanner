# Decision Report

- generated_at: 2026-07-28T15:01:33.784365+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9702**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9702, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/19 | 21.1% | +2.70% | **+0.57%** |
| LIMIT_ATR | 9/20 | 45.0% | +0.87% | **+0.39%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +1.62% | **+0.32%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +2.40% | **+2.04%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +1.13% | **+1.13%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.28% | **+0.57%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.93% | **+0.56%** |

## 2. $100 Live Portfolio

- 残高: **$106.38** / 初期 $100.00 (+6.38%)
- 確定トレード: 149件 (TP 51 / SL 93 / EXP 5)
- 最新: BANK/USDT:USDT SL_HIT PnL -4.00% 残高後 $106.38
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$477.29** / 初期 $100.00 (+377.29%)
- 確定: 3472件 (Win 1096 / Loss 1126 / Flat 1250) / skip 2791件
- 成長率目線: 平均log +0.000450 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SOONNETWORK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $477.29

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1225件 (Win 338 / Loss 275 / Flat 612) / skip 1888件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0966 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: COTI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$109.39** / 初期 $100.00 (+9.39%)
- 確定: 721件 (Win 235 / Loss 275 / Flat 211) / pending 6件 / skip 448件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000383 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SOONNETWORK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $109.39

## 6. Latest Market Context

- 更新: 2026-07-28T15:01:24.346246+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=63403.7
- Funnel: target 904 → liquid 174 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COTI/USDT:USDT | +55.43% | $22,998,194.15 |
| SOONNETWORK/USDT:USDT | +36.51% | $2,828,380.60 |
| ON/USDT:USDT | +33.88% | $19,622,454.13 |
| BULLA/USDT:USDT | +26.36% | $2,119,605.23 |
| DEXE/USDT:USDT | +25.82% | $15,667,142.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +3.06% | +3.03% |
| MSFU/USDT:USDT | below_1h_threshold | +2.14% | +2.11% |
| INFQSTOCK/USDT:USDT | below_1h_threshold | +2.02% | +1.99% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +1.89% | +1.86% |
| GGLL/USDT:USDT | below_1h_threshold | +1.80% | +1.77% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
