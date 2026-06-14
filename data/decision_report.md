# Decision Report

- generated_at: 2026-06-14T08:16:33.388933+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6654**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=6654, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| ASK | 20/20 | 100.0% | +0.74% | **+0.74%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.91% | **+0.27%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.40% | **+0.18%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.44% | **+0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |
| ASK_LONG | 20/20 | 100.0% | +0.48% | **+0.48%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.62% | **+0.28%** |
| MARKET_LONG | 20/20 | 100.0% | +0.20% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定トレード: 0件 (TP 0 / SL 0 / EXP 0)

## 3. Safe Adaptive DryRun ($100)

- 残高: **$171.23** / 初期 $100.00 (+71.23%)
- 確定: 1527件 (Win 408 / Loss 486 / Flat 633) / skip 1688件
- 成長率目線: 平均log +0.000352 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `LIMIT_9PCT_LONG` TP_HIT account +1.00% 残高後 $171.23

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.93** / 初期 $100.00 (-1.07%)
- 確定: 55件 (Win 18 / Loss 12 / Flat 25) / skip 10件
- 成長率目線: 平均log -0.000195 / 幾何平均 -0.020% per trade / maxDD +2.00%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0277 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $98.93

## 5. Latest Market Context

- 更新: 2026-06-14T08:16:29.149447+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=64450.0
- Funnel: target 770 → liquid 121 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| H/USDT:USDT | +105.78% | $38,964,361.81 |
| TRADOOR/USDT:USDT | +24.31% | $7,044,460.10 |
| VELVET/USDT:USDT | +21.91% | $59,964,205.56 |
| MEGA/USDT:USDT | +16.77% | $4,513,623.40 |
| BTW/USDT:USDT | +12.50% | $3,028,196.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIOT/USDT:USDT | below_1h_threshold | +3.35% | +3.26% |
| LAB/USDT:USDT | below_1h_threshold | +1.18% | +1.09% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.02% | +0.93% |
| BRETT/USDT:USDT | below_1h_threshold | +0.92% | +0.83% |
| TAO/USDT:USDT | below_1h_threshold | +0.89% | +0.81% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
