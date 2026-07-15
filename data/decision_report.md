# Decision Report

- generated_at: 2026-07-15T07:06:16.911498+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8720**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.04% / filled 20/20。**
- 全期間 MARKET基準: n=8720, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.04%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.04% | **+1.04%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.04% | **+1.04%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_3PCT | 12/20 | 60.0% | +1.04% | **+0.62%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.48% | **+0.62%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 8/11 | 72.7% | +0.99% | **+0.72%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.06% | **+0.53%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.67% | **+0.37%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$102.71** / 初期 $100.00 (+2.71%)
- 確定トレード: 97件 (TP 33 / SL 62 / EXP 2)
- 最新: DODO/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.71
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$334.81** / 初期 $100.00 (+234.81%)
- 確定: 2873件 (Win 898 / Loss 934 / Flat 1041) / skip 2408件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account -0.03% 残高後 $334.81

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.12** / 初期 $100.00 (+5.12%)
- 確定: 695件 (Win 161 / Loss 163 / Flat 371) / skip 1436件
- 成長率目線: 平均log +0.000072 / 幾何平均 +0.007% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AEHRSTOCK/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $105.12

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.75** / 初期 $100.00 (-1.25%)
- 確定: 60件 (Win 19 / Loss 39 / Flat 2) / pending 0件 / skip 133件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000164 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AEHRSTOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $98.75

## 6. Latest Market Context

- 更新: 2026-07-15T07:06:09.559547+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=64763.9
- Funnel: target 866 → liquid 171 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +120.55% | $3,482,069.96 |
| US/USDT:USDT | +33.62% | $2,827,440.71 |
| AEHRSTOCK/USDT:USDT | +31.00% | $3,234,137.74 |
| DODO/USDT:USDT | +30.73% | $8,979,030.02 |
| MAGMA/USDT:USDT | +19.91% | $2,640,262.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| INTCSTOCK/USDT:USDT | below_1h_threshold | +2.57% | +2.61% |
| MAGMA/USDT:USDT | below_1h_threshold | +2.26% | +2.29% |
| RAVE/USDT:USDT | below_1h_threshold | +1.88% | +1.92% |
| XEC/USDT:USDT | below_1h_threshold | +1.16% | +1.19% |
| FLUTSTOCK/USDT:USDT | below_1h_threshold | +0.95% | +0.99% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
