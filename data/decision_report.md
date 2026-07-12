# Decision Report

- generated_at: 2026-07-12T17:51:14.775029+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8603**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.18% / filled 20/20。**
- 全期間 MARKET基準: n=8603, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.18%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.18% | **+2.18%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +2.72% | **+2.58%** |
| MARKET | 20/20 | 100.0% | +2.18% | **+2.18%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.94% | **+1.45%** |
| LIMIT_BB3S | 5/12 | 41.7% | +1.75% | **+0.73%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.00% | **+0.65%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +1.47% | **+0.88%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.66% | **+0.36%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +0.26% | **+0.14%** |

## 2. $100 Live Portfolio

- 残高: **$102.22** / 初期 $100.00 (+2.22%)
- 確定トレード: 89件 (TP 30 / SL 57 / EXP 2)
- 最新: BSB/USDT:USDT EXPIRED PnL +5.08% 残高後 $102.22
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$319.81** / 初期 $100.00 (+219.81%)
- 確定: 2784件 (Win 875 / Loss 922 / Flat 987) / skip 2380件
- 成長率目線: 平均log +0.000418 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MAGMA/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $319.81

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.11** / 初期 $100.00 (+5.11%)
- 確定: 644件 (Win 152 / Loss 159 / Flat 333) / skip 1370件
- 成長率目線: 平均log +0.000077 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VANRY/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $105.11

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定: 27件 (Win 9 / Loss 18 / Flat 0) / pending 0件 / skip 49件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000410 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $99.00

## 6. Latest Market Context

- 更新: 2026-07-12T17:51:07.518990+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=64103.9
- Funnel: target 863 → liquid 132 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PIPPIN/USDT:USDT | +7.08% | $2,324,034.79 |
| T/USDT:USDT | +3.87% | $19,972,235.47 |
| ZEC/USDT:USDT | +2.58% | $200,680,712.73 |
| TAC/USDT:USDT | +2.14% | $2,117,642.62 |
| ALLO/USDT:USDT | +2.04% | $14,505,246.86 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TRIA/USDT:USDT | below_1h_threshold | +3.14% | +3.21% |
| TAC/USDT:USDT | below_1h_threshold | +2.93% | +3.00% |
| FHE/USDT:USDT | below_1h_threshold | +2.36% | +2.42% |
| CAP/USDT:USDT | below_1h_threshold | +1.78% | +1.85% |
| PYTH/USDT:USDT | below_1h_threshold | +1.64% | +1.71% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
