# Decision Report

- generated_at: 2026-05-15T00:33:02.072555+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4313**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.14% / filled 20/20。**
- 全期間 MARKET基準: n=4313, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=+1.14%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.14% | **+1.14%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/13 | 38.5% | +4.35% | **+1.67%** |
| ASK | 20/20 | 100.0% | +1.19% | **+1.19%** |
| MARKET | 20/20 | 100.0% | +1.14% | **+1.14%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.92% | **+0.69%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.55% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/7 | 71.4% | +1.75% | **+1.25%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.35% | **+0.27%** |

## 2. $100 Live Portfolio

- 残高: **$96.24** / 初期 $100.00 (-3.76%)
- 確定トレード: 43件 (TP 10 / SL 30 / EXP 3)
- 最新: PLAY/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.24
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.48** / 初期 $100.00 (+20.48%)
- 確定: 365件 (Win 96 / Loss 129 / Flat 140) / skip 509件
- 成長率目線: 平均log +0.000511 / 幾何平均 +0.051% per trade / maxDD +4.21%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: USELESS/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $120.48

## 4. Latest Market Context

- 更新: 2026-05-15T00:32:59.186459+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.54% price=81488.0
- Funnel: target 760 → liquid 165 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.5 >= 65=1, 4h RSI 67.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| UP/USDT:USDT | +18.21% | $3,784,174.86 |
| TAC/USDT:USDT | +17.40% | $1,877,547.28 |
| PEAQ/USDT:USDT | +15.26% | $1,702,437.73 |
| FIGSTOCK/USDT:USDT | +14.50% | $3,062,489.76 |
| TROLLSOL/USDT:USDT | +10.64% | $1,557,781.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STAR/USDT:USDT | below_relative_strength | +5.25% | +4.70% |
| WLFI/USDT:USDT | below_1h_threshold | +3.05% | +2.51% |
| NAORIS/USDT:USDT | below_1h_threshold | +2.84% | +2.30% |
| BILL/USDT:USDT | below_1h_threshold | +2.24% | +1.70% |
| CC/USDT:USDT | below_1h_threshold | +2.11% | +1.57% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
