# Decision Report

- generated_at: 2026-06-15T02:20:08.442075+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6723**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.87% / filled 20/20。**
- 全期間 MARKET基準: n=6723, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.87%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.87% | **+0.87%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.08% | **+0.97%** |
| MARKET | 20/20 | 100.0% | +0.87% | **+0.87%** |
| ASK | 20/20 | 100.0% | +0.63% | **+0.63%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +5.51% | **+1.65%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +2.34% | **+0.82%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.71% | **+0.60%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.83% | **+0.33%** |
| MARKET_LONG | 20/20 | 100.0% | +0.05% | **+0.05%** |

## 2. $100 Live Portfolio

- 残高: **$100.99** / 初期 $100.00 (+0.99%)
- 確定トレード: 4件 (TP 2 / SL 2 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.99
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$175.11** / 初期 $100.00 (+75.11%)
- 確定: 1596件 (Win 423 / Loss 499 / Flat 674) / skip 1688件
- 成長率目線: 平均log +0.000351 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CLO/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $175.11

## 4. Robust Adaptive DryRun ($100)

- 残高: **$99.53** / 初期 $100.00 (-0.47%)
- 確定: 91件 (Win 22 / Loss 15 / Flat 54) / skip 43件
- 成長率目線: 平均log -0.000052 / 幾何平均 -0.005% per trade / maxDD +2.07%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0660 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CLO/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $99.53

## 5. Latest Market Context

- 更新: 2026-06-15T02:20:04.053537+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.28% price=65661.2
- Funnel: target 770 → liquid 139 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +37.44% | $16,815,249.78 |
| CLO/USDT:USDT | +27.28% | $1,812,422.00 |
| RIF/USDT:USDT | +24.44% | $4,385,128.89 |
| EDEN/USDT:USDT | +17.32% | $1,512,026.88 |
| BABY/USDT:USDT | +16.53% | $2,554,317.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CLO/USDT:USDT | below_1h_threshold | +3.53% | +3.26% |
| SKYAI/USDT:USDT | below_1h_threshold | +3.26% | +2.98% |
| JUP/USDT:USDT | below_1h_threshold | +3.11% | +2.83% |
| BABY/USDT:USDT | below_1h_threshold | +1.76% | +1.48% |
| EDEN/USDT:USDT | below_1h_threshold | +1.62% | +1.34% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
