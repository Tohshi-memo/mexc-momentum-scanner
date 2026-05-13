# Decision Report

- generated_at: 2026-05-13T20:13:38.105600+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4249**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.28% / filled 20/20。**
- 全期間 MARKET基準: n=4249, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+1.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.28% | **+1.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.72% | **+1.64%** |
| MARKET | 20/20 | 100.0% | +1.28% | **+1.28%** |
| ASK | 20/20 | 100.0% | +0.66% | **+0.66%** |
| LIMIT_BB3S | 3/16 | 18.8% | +1.42% | **+0.27%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.67% | **+0.73%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.30% | **+0.58%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.32% | **+0.24%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.50% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$98.19** / 初期 $100.00 (-1.81%)
- 確定トレード: 39件 (TP 10 / SL 26 / EXP 3)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.19
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.18** / 初期 $100.00 (+19.18%)
- 確定: 342件 (Win 94 / Loss 125 / Flat 123) / skip 468件
- 成長率目線: 平均log +0.000513 / 幾何平均 +0.051% per trade / maxDD +4.21%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: COS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $119.18

## 4. Latest Market Context

- 更新: 2026-05-13T20:13:34.295112+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=79628.6
- Funnel: target 760 → liquid 171 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TROLLSOL/USDT:USDT | +24.68% | $1,420,743.30 |
| AIN/USDT:USDT | +15.06% | $1,714,413.39 |
| BB/USDT:USDT | +13.91% | $1,668,839.02 |
| GUA/USDT:USDT | +13.33% | $3,696,332.20 |
| CSCOSTOCK/USDT:USDT | +11.60% | $2,179,667.02 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKT/USDT:USDT | below_1h_threshold | +1.71% | +1.68% |
| USELESS/USDT:USDT | below_1h_threshold | +1.35% | +1.32% |
| JCT/USDT:USDT | below_1h_threshold | +1.16% | +1.13% |
| ATOM/USDT:USDT | below_1h_threshold | +1.02% | +0.99% |
| ETHFI/USDT:USDT | below_1h_threshold | +0.90% | +0.87% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
