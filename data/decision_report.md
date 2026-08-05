# Decision Report

- generated_at: 2026-08-05T15:01:28.882748+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10414**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.58% / filled 20/20。**
- 全期間 MARKET基準: n=10414, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.58%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.58% | **+0.58%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 18/20 | 90.0% | +1.16% | **+1.04%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.75% | **+0.71%** |
| MARKET | 20/20 | 100.0% | +0.58% | **+0.58%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.65% | **+0.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.93% | **+0.69%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.69% | **+0.45%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.50% | **+0.45%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$605.31** / 初期 $100.00 (+505.31%)
- 確定: 3769件 (Win 1195 / Loss 1236 / Flat 1338) / skip 3206件
- 成長率目線: 平均log +0.000478 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $605.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$143.05** / 初期 $100.00 (+43.05%)
- 確定: 1321件 (Win 374 / Loss 311 / Flat 636) / skip 2504件
- 成長率目線: 平均log +0.000271 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0645 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ON/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $143.05

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.94** / 初期 $100.00 (+17.94%)
- 確定: 1141件 (Win 365 / Loss 443 / Flat 333) / pending 1件 / skip 748件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000172 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ALLO/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $117.94

## 6. Latest Market Context

- 更新: 2026-08-05T15:01:16.349801+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=64475.6
- Funnel: target 948 → liquid 180 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +86.39% | $29,422,281.72 |
| BLESS/USDT:USDT | +78.67% | $63,376,996.82 |
| HFT/USDT:USDT | +61.53% | $4,555,810.75 |
| ON/USDT:USDT | +32.32% | $4,063,727.05 |
| CYS/USDT:USDT | +29.01% | $30,943,530.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AAPU/USDT:USDT | below_1h_threshold | +2.11% | +2.06% |
| EVAA/USDT:USDT | below_1h_threshold | +0.90% | +0.85% |
| GGLL/USDT:USDT | below_1h_threshold | +0.78% | +0.73% |
| BKNGSTOCK/USDT:USDT | below_1h_threshold | +0.72% | +0.67% |
| AMGNSTOCK/USDT:USDT | below_1h_threshold | +0.48% | +0.43% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
