# Decision Report

- generated_at: 2026-05-11T05:57:43.088809+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4008**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.55% / filled 20/20。**
- 全期間 MARKET基準: n=4008, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+1.55%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.55% | **+1.55%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.55% | **+1.55%** |
| ASK | 20/20 | 100.0% | +1.51% | **+1.51%** |
| LIMIT_BB3S | 5/11 | 45.5% | +2.89% | **+1.31%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.20% | **+0.96%** |
| LIMIT_ATR | 14/20 | 70.0% | +1.28% | **+0.90%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 15/20 | 75.0% | +1.15% | **+0.86%** |
| LIMIT_3PCT_LONG | 18/20 | 90.0% | +0.96% | **+0.86%** |
| LIMIT_ATR_LONG | 17/20 | 85.0% | +0.17% | **+0.15%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.33% | **+0.13%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +0.29% | **+0.07%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.95** / 初期 $100.00 (+8.95%)
- 確定: 214件 (Win 54 / Loss 74 / Flat 86) / skip 355件
- 成長率目線: 平均log +0.000400 / 幾何平均 +0.040% per trade / maxDD +4.09%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SATO/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $108.95

## 4. Latest Market Context

- 更新: 2026-05-11T05:57:39.768416+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=80788.2
- Funnel: target 776 → liquid 180 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +32.50% | $10,596,426.33 |
| JELLYJELLY/USDT:USDT | +22.79% | $1,049,287.71 |
| TROLLSOL/USDT:USDT | +19.79% | $5,252,543.42 |
| ALCH/USDT:USDT | +18.61% | $4,457,413.80 |
| FOLKS/USDT:USDT | +11.87% | $1,883,902.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JELLYJELLY/USDT:USDT | below_1h_threshold | +4.40% | +4.39% |
| VVV/USDT:USDT | below_1h_threshold | +4.13% | +4.12% |
| GIGA/USDT:USDT | below_1h_threshold | +2.88% | +2.88% |
| JTO/USDT:USDT | below_1h_threshold | +2.86% | +2.86% |
| ZRO/USDT:USDT | below_1h_threshold | +2.66% | +2.66% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
