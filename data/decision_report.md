# Decision Report

- generated_at: 2026-07-02T22:13:20.246331+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8113**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.81% / filled 20/20。**
- 全期間 MARKET基準: n=8113, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.81%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.81% | **+0.81%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.88% | **+0.88%** |
| MARKET | 20/20 | 100.0% | +0.81% | **+0.81%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.77% | **+0.44%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.51% | **+0.41%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.13% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +2.70% | **+1.48%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.47% | **+0.35%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.39% | **+0.21%** |
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +0.14% | **+0.11%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.11% | **+0.10%** |

## 2. $100 Live Portfolio

- 残高: **$102.62** / 初期 $100.00 (+2.62%)
- 確定トレード: 53件 (TP 19 / SL 33 / EXP 1)
- 最新: GUA/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.62
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$284.67** / 初期 $100.00 (+184.67%)
- 確定: 2444件 (Win 754 / Loss 816 / Flat 874) / skip 2230件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $284.67

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.39** / 初期 $100.00 (+6.39%)
- 確定: 571件 (Win 139 / Loss 133 / Flat 299) / skip 953件
- 成長率目線: 平均log +0.000109 / 幾何平均 +0.011% per trade / maxDD +3.55%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0735 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: GUA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.52% 残高後 $106.39

## 5. Latest Market Context

- 更新: 2026-07-02T22:13:15.237146+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=61502.1
- Funnel: target 834 → liquid 172 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| THE/USDT:USDT | +34.75% | $1,318,802.62 |
| MAGMA/USDT:USDT | +18.77% | $4,762,318.71 |
| PIPPIN/USDT:USDT | +15.34% | $4,306,346.60 |
| GUA/USDT:USDT | +13.87% | $8,802,960.87 |
| LAB/USDT:USDT | +12.48% | $12,777,477.03 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| THE/USDT:USDT | below_1h_threshold | +3.68% | +3.79% |
| TAIKO/USDT:USDT | below_1h_threshold | +2.26% | +2.37% |
| SYN/USDT:USDT | below_1h_threshold | +2.24% | +2.35% |
| SLX/USDT:USDT | below_1h_threshold | +0.89% | +1.00% |
| BEAT/USDT:USDT | below_1h_threshold | +0.87% | +0.98% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
