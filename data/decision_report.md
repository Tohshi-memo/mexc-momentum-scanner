# Decision Report

- generated_at: 2026-06-14T00:37:40.916443+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6621**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.77% / filled 20/20。**
- 全期間 MARKET基準: n=6621, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.77%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.77% | **+0.77%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.78% | **+0.78%** |
| MARKET | 20/20 | 100.0% | +0.77% | **+0.77%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.21% | **+0.49%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.57% | **+0.47%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.42% | **+0.71%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.50% | **+0.60%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.75% | **+0.52%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +0.83% | **+0.50%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定トレード: 0件 (TP 0 / SL 0 / EXP 0)

## 3. Safe Adaptive DryRun ($100)

- 残高: **$166.88** / 初期 $100.00 (+66.88%)
- 確定: 1494件 (Win 401 / Loss 477 / Flat 616) / skip 1688件
- 成長率目線: 平均log +0.000343 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SQD/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $166.88

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.71** / 初期 $100.00 (-1.29%)
- 確定: 32件 (Win 11 / Loss 11 / Flat 10) / skip 0件
- 成長率目線: 平均log -0.000405 / 幾何平均 -0.041% per trade / maxDD +1.93%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0238 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SQD/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $98.71

## 5. Latest Market Context

- 更新: 2026-06-14T00:37:35.702170+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=64512.9
- Funnel: target 770 → liquid 125 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TRADOOR/USDT:USDT | +32.89% | $2,701,685.86 |
| RIF/USDT:USDT | +20.63% | $13,162,413.74 |
| H/USDT:USDT | +18.35% | $17,924,944.88 |
| MEGA/USDT:USDT | +17.65% | $3,238,102.26 |
| BRETT/USDT:USDT | +10.94% | $1,268,464.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MEGA/USDT:USDT | below_1h_threshold | +4.84% | +4.70% |
| BRETT/USDT:USDT | below_1h_threshold | +3.25% | +3.10% |
| TRADOOR/USDT:USDT | below_1h_threshold | +2.93% | +2.79% |
| JCT/USDT:USDT | below_1h_threshold | +2.77% | +2.62% |
| ALGO/USDT:USDT | below_1h_threshold | +2.34% | +2.20% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
