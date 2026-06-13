# Decision Report

- generated_at: 2026-06-13T22:49:20.324942+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6616**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=6616, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.89% | **+0.89%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.07% | **+0.27%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.60% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +1.96% | **+1.08%** |
| LIMIT_6PCT_LONG | 13/20 | 65.0% | +1.34% | **+0.87%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +0.90% | **+0.72%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +1.33% | **+0.60%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |

## 2. $100 Live Portfolio

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定トレード: 0件 (TP 0 / SL 0 / EXP 0)

## 3. Safe Adaptive DryRun ($100)

- 残高: **$167.72** / 初期 $100.00 (+67.72%)
- 確定: 1489件 (Win 401 / Loss 476 / Flat 612) / skip 1688件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TRADOOR/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $167.72

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.92** / 初期 $100.00 (-1.08%)
- 確定: 27件 (Win 9 / Loss 10 / Flat 8) / skip 0件
- 成長率目線: 平均log -0.000402 / 幾何平均 -0.040% per trade / maxDD +1.93%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0213 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TRADOOR/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $98.92

## 5. Latest Market Context

- 更新: 2026-06-13T22:49:15.557826+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=64459.4
- Funnel: target 770 → liquid 131 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RIF/USDT:USDT | +26.29% | $11,752,953.24 |
| TRADOOR/USDT:USDT | +25.71% | $1,567,824.15 |
| MEGA/USDT:USDT | +16.62% | $2,587,123.14 |
| BTW/USDT:USDT | +11.22% | $1,886,923.70 |
| JASMY/USDT:USDT | +8.54% | $2,235,891.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RIF/USDT:USDT | below_1h_threshold | +4.94% | +4.90% |
| TRADOOR/USDT:USDT | below_1h_threshold | +4.78% | +4.74% |
| MEGA/USDT:USDT | below_1h_threshold | +2.99% | +2.95% |
| JASMY/USDT:USDT | below_1h_threshold | +2.67% | +2.63% |
| BILL/USDT:USDT | below_1h_threshold | +2.25% | +2.21% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
