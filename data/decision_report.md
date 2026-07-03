# Decision Report

- generated_at: 2026-07-03T02:09:01.034242+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8125**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.53% / filled 20/20。**
- 全期間 MARKET基準: n=8125, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.53%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.53% | **+1.53%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 15/20 | 75.0% | +2.06% | **+1.54%** |
| MARKET | 20/20 | 100.0% | +1.53% | **+1.53%** |
| ASK | 20/20 | 100.0% | +1.18% | **+1.18%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.48% | **+0.38%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.88% | **+0.35%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +3.26% | **+0.49%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +0.52% | **+0.28%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.18% | **+0.11%** |
| LIMIT_2PCT_LONG | 19/20 | 95.0% | +0.04% | **+0.04%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | -0.24% | **-0.06%** |

## 2. $100 Live Portfolio

- 残高: **$102.62** / 初期 $100.00 (+2.62%)
- 確定トレード: 53件 (TP 19 / SL 33 / EXP 1)
- 最新: GUA/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.62
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$285.42** / 初期 $100.00 (+185.42%)
- 確定: 2448件 (Win 755 / Loss 817 / Flat 876) / skip 2238件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RIF/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $285.42

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.09** / 初期 $100.00 (+5.09%)
- 確定: 580件 (Win 140 / Loss 138 / Flat 302) / skip 956件
- 成長率目線: 平均log +0.000086 / 幾何平均 +0.009% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RIF/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $105.09

## 5. Latest Market Context

- 更新: 2026-07-03T02:08:55.180648+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=61578.1
- Funnel: target 834 → liquid 167 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| THE/USDT:USDT | +25.79% | $1,977,711.39 |
| PIPPIN/USDT:USDT | +20.05% | $7,124,257.84 |
| RIF/USDT:USDT | +18.66% | $5,109,893.63 |
| MAGMA/USDT:USDT | +14.72% | $5,257,845.05 |
| WLD/USDT:USDT | +14.00% | $62,263,084.91 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RIF/USDT:USDT | below_1h_threshold | +4.55% | +4.53% |
| RAVE/USDT:USDT | below_1h_threshold | +2.28% | +2.26% |
| BSB/USDT:USDT | below_1h_threshold | +2.05% | +2.03% |
| TAIKO/USDT:USDT | below_1h_threshold | +1.99% | +1.97% |
| THE/USDT:USDT | below_1h_threshold | +1.17% | +1.15% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
