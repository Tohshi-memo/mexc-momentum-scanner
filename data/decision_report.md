# Decision Report

- generated_at: 2026-11-19T07:06:42.115660+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19182**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.01% / filled 20/20。**
- 全期間 MARKET基準: n=19182, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.01%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.01% | **+2.01%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +2.14% | **+2.03%** |
| MARKET | 20/20 | 100.0% | +2.01% | **+2.01%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.18% | **+0.89%** |
| LIMIT_BB3S | 6/14 | 42.9% | +1.55% | **+0.67%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.90% | **+0.58%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.89% | **+0.40%** |
| LIMIT_BB3S_LONG | 4/6 | 66.7% | +0.51% | **+0.34%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.45% | **+0.29%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 282件 (TP 102 / SL 172 / EXP 8)
- 最新: KORU/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,753.58** / 初期 $100.00 (+1653.58%)
- 確定: 7371件 (Win 2118 / Loss 2367 / Flat 2886) / skip 8372件
- 成長率目線: 平均log +0.000389 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `MARKET` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EVAA/USDT:USDT `MARKET` TP_HIT account +1.00% 残高後 $1,753.58

## 4. Robust Adaptive DryRun ($100)

- 残高: **$430.70** / 初期 $100.00 (+330.70%)
- 確定: 5023件 (Win 1335 / Loss 1087 / Flat 2601) / skip 7570件
- 成長率目線: 平均log +0.000291 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOXL/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $430.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7342件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000246 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-19T07:06:25.983966+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=63765.4
- Funnel: target 1081 → liquid 143 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IRYS/USDT:USDT | +37.04% | $9,915,221.50 |
| LUNC/USDT:USDT | +26.00% | $3,575,252.22 |
| VELVET/USDT:USDT | +24.25% | $5,164,706.88 |
| ARIA/USDT:USDT | +14.16% | $2,262,392.50 |
| ETHFI/USDT:USDT | +12.90% | $1,252,114.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXL/USDT:USDT | below_1h_threshold | +3.68% | +3.61% |
| MVLL/USDT:USDT | below_1h_threshold | +3.46% | +3.39% |
| SNXX/USDT:USDT | below_1h_threshold | +2.87% | +2.81% |
| CSOPSKHYNIX2L/USDT:USDT | below_1h_threshold | +2.26% | +2.19% |
| MUU/USDT:USDT | below_1h_threshold | +2.04% | +1.98% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
