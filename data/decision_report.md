# Decision Report

- generated_at: 2026-07-03T00:07:24.109286+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8116**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.81% / filled 20/20。**
- 全期間 MARKET基準: n=8116, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.81%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.81% | **+0.81%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.86% | **+0.86%** |
| MARKET | 20/20 | 100.0% | +0.81% | **+0.81%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.77% | **+0.44%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.13% | **+0.40%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.32% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +2.14% | **+1.28%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +1.02% | **+0.61%** |
| LIMIT_3PCT_LONG | 17/20 | 85.0% | +0.65% | **+0.55%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.93% | **+0.46%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.65% | **+0.42%** |

## 2. $100 Live Portfolio

- 残高: **$102.62** / 初期 $100.00 (+2.62%)
- 確定トレード: 53件 (TP 19 / SL 33 / EXP 1)
- 最新: GUA/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.62
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$284.67** / 初期 $100.00 (+184.67%)
- 確定: 2444件 (Win 754 / Loss 816 / Flat 874) / skip 2233件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $284.67

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.20** / 初期 $100.00 (+6.20%)
- 確定: 574件 (Win 140 / Loss 135 / Flat 299) / skip 953件
- 成長率目線: 平均log +0.000105 / 幾何平均 +0.010% per trade / maxDD +3.55%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0566 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BIRB/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $106.20

## 5. Latest Market Context

- 更新: 2026-07-03T00:07:17.986602+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.18% price=61428.6
- Funnel: target 834 → liquid 170 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| THE/USDT:USDT | +33.73% | $1,782,630.59 |
| MAGMA/USDT:USDT | +18.00% | $5,044,753.40 |
| RPL/USDT:USDT | +16.53% | $1,151,123.34 |
| PIPPIN/USDT:USDT | +14.79% | $5,888,238.24 |
| GUA/USDT:USDT | +11.70% | $9,216,894.51 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| THE/USDT:USDT | below_1h_threshold | +3.98% | +4.16% |
| GUA/USDT:USDT | below_1h_threshold | +2.77% | +2.95% |
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +2.59% | +2.77% |
| RENDER/USDT:USDT | below_1h_threshold | +1.95% | +2.13% |
| NOM/USDT:USDT | below_1h_threshold | +1.73% | +1.91% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
