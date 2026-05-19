# Decision Report

- generated_at: 2026-05-19T02:48:56.527478+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4458**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.41% / filled 20/20。**
- 全期間 MARKET基準: n=4458, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.41%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.41% | **+0.41%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 14/20 | 70.0% | +1.86% | **+1.30%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.75% | **+0.56%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.65% | **+0.56%** |
| ASK | 20/20 | 100.0% | +0.53% | **+0.53%** |
| LIMIT_ATR | 16/20 | 80.0% | +0.60% | **+0.48%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.53% | **+0.84%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.36% | **+0.68%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.56% | **+0.42%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.10% | **+0.39%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +0.66% | **+0.17%** |

## 2. $100 Live Portfolio

- 残高: **$96.70** / 初期 $100.00 (-3.30%)
- 確定トレード: 54件 (TP 14 / SL 37 / EXP 3)
- 最新: DASH/USDT:USDT TP_HIT PnL +5.37% 残高後 $96.70
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.48** / 初期 $100.00 (+20.48%)
- 確定: 455件 (Win 119 / Loss 157 / Flat 179) / skip 564件
- 成長率目線: 平均log +0.000410 / 幾何平均 +0.041% per trade / maxDD +4.21%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIGENSYN/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $120.48

## 4. Latest Market Context

- 更新: 2026-05-19T02:48:54.610890+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=76681.4
- Funnel: target 768 → liquid 140 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RON/USDT:USDT | +32.86% | $8,231,123.38 |
| ONDO/USDT:USDT | +14.39% | $45,181,858.06 |
| AKT/USDT:USDT | +10.81% | $1,384,210.67 |
| INJ/USDT:USDT | +10.22% | $26,388,636.62 |
| ZEC/USDT:USDT | +6.23% | $597,280,542.08 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ONDO/USDT:USDT | below_1h_threshold | +2.44% | +2.38% |
| AKT/USDT:USDT | below_1h_threshold | +1.72% | +1.66% |
| VVV/USDT:USDT | below_1h_threshold | +1.59% | +1.53% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +1.09% | +1.03% |
| APE/USDT:USDT | below_1h_threshold | +0.98% | +0.92% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
