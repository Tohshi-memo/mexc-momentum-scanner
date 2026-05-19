# Decision Report

- generated_at: 2026-05-19T04:33:42.142540+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4460**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.42% / filled 20/20。**
- 全期間 MARKET基準: n=4460, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.42%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.42% | **+0.42%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.14% | **+1.14%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.42% | **+0.92%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.66% | **+0.56%** |
| MARKET | 20/20 | 100.0% | +0.42% | **+0.42%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.87% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +2.37% | **+0.83%** |
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | +1.85% | **+0.56%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.56% | **+0.42%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.44% | **+0.24%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +0.27% | **+0.13%** |

## 2. $100 Live Portfolio

- 残高: **$96.70** / 初期 $100.00 (-3.30%)
- 確定トレード: 54件 (TP 14 / SL 37 / EXP 3)
- 最新: DASH/USDT:USDT TP_HIT PnL +5.37% 残高後 $96.70
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.88** / 初期 $100.00 (+19.88%)
- 確定: 457件 (Win 119 / Loss 158 / Flat 180) / skip 564件
- 成長率目線: 平均log +0.000397 / 幾何平均 +0.040% per trade / maxDD +4.21%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RAVE/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $119.88

## 4. Latest Market Context

- 更新: 2026-05-19T04:33:37.748347+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=76762.5
- Funnel: target 768 → liquid 139 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RON/USDT:USDT | +31.93% | $8,453,579.87 |
| ONDO/USDT:USDT | +12.16% | $46,697,691.99 |
| AKT/USDT:USDT | +11.22% | $1,312,379.17 |
| INJ/USDT:USDT | +11.06% | $26,872,768.30 |
| ZEC/USDT:USDT | +6.98% | $586,987,652.83 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SIREN/USDT:USDT | below_1h_threshold | +2.66% | +2.65% |
| RAVE/USDT:USDT | below_1h_threshold | +1.40% | +1.39% |
| ASTEROID/USDT:USDT | below_1h_threshold | +1.12% | +1.11% |
| TONCOIN/USDT:USDT | below_1h_threshold | +0.96% | +0.94% |
| LUNC/USDT:USDT | below_1h_threshold | +0.93% | +0.91% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
