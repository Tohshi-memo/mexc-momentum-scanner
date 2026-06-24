# Decision Report

- generated_at: 2026-06-24T06:12:49.866840+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7463**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.30% / filled 20/20。**
- 全期間 MARKET基準: n=7463, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.30%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.30% | **+0.30%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.54% | **+0.54%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| MARKET | 20/20 | 100.0% | +0.30% | **+0.30%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| ASK_LONG | 20/20 | 100.0% | +0.78% | **+0.78%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.61% | **+0.52%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.30% | **+0.22%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$101.93** / 初期 $100.00 (+1.93%)
- 確定トレード: 32件 (TP 12 / SL 20 / EXP 0)
- 最新: ID/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.93
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$229.07** / 初期 $100.00 (+129.07%)
- 確定: 2094件 (Win 620 / Loss 695 / Flat 779) / skip 1930件
- 成長率目線: 平均log +0.000396 / 幾何平均 +0.040% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BICO/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $229.07

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.36** / 初期 $100.00 (+6.36%)
- 確定: 328件 (Win 92 / Loss 88 / Flat 148) / skip 546件
- 成長率目線: 平均log +0.000188 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0264 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: G/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $106.36

## 5. Latest Market Context

- 更新: 2026-06-24T06:12:44.053495+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=62820.0
- Funnel: target 807 → liquid 163 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +47.33% | $13,265,228.83 |
| SLX/USDT:USDT | +41.38% | $1,645,941.92 |
| CLO/USDT:USDT | +29.42% | $5,100,342.29 |
| BEAT/USDT:USDT | +27.84% | $73,743,866.59 |
| ID/USDT:USDT | +14.26% | $1,346,310.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SLX/USDT:USDT | below_1h_threshold | +3.14% | +3.21% |
| BASED/USDT:USDT | below_1h_threshold | +1.60% | +1.66% |
| ID/USDT:USDT | below_1h_threshold | +0.96% | +1.02% |
| MVLL/USDT:USDT | below_1h_threshold | +0.67% | +0.73% |
| JTO/USDT:USDT | below_1h_threshold | +0.61% | +0.68% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
