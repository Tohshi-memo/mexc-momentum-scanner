# Decision Report

- generated_at: 2026-05-19T04:03:35.232597+00:00
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

- 更新: 2026-05-19T04:03:33.244132+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=76701.4
- Funnel: target 768 → liquid 139 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RON/USDT:USDT | +31.82% | $8,499,350.43 |
| ONDO/USDT:USDT | +14.92% | $46,183,494.13 |
| INJ/USDT:USDT | +12.64% | $26,907,216.29 |
| AKT/USDT:USDT | +11.72% | $1,331,653.51 |
| ZEC/USDT:USDT | +7.35% | $592,844,187.82 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RAVE/USDT:USDT | below_1h_threshold | +0.73% | +0.80% |
| AKT/USDT:USDT | below_1h_threshold | +0.42% | +0.48% |
| PLAY/USDT:USDT | below_1h_threshold | +0.32% | +0.38% |
| GUA/USDT:USDT | below_1h_threshold | +0.25% | +0.32% |
| NEAR/USDT:USDT | below_1h_threshold | +0.25% | +0.31% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
