# Decision Report

- generated_at: 2026-05-15T00:38:16.326928+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4314**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.54% / filled 20/20。**
- 全期間 MARKET基準: n=4314, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=+0.54%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.54% | **+0.54%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/14 | 35.7% | +4.35% | **+1.55%** |
| ASK | 20/20 | 100.0% | +0.59% | **+0.59%** |
| MARKET | 20/20 | 100.0% | +0.54% | **+0.54%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/6 | 66.7% | +3.19% | **+2.12%** |
| MARKET_LONG | 20/20 | 100.0% | +0.55% | **+0.55%** |
| ASK_LONG | 20/20 | 100.0% | +0.51% | **+0.51%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.91% | **+0.41%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.35% | **+0.27%** |

## 2. $100 Live Portfolio

- 残高: **$96.24** / 初期 $100.00 (-3.76%)
- 確定トレード: 43件 (TP 10 / SL 30 / EXP 3)
- 最新: PLAY/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.24
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.48** / 初期 $100.00 (+20.48%)
- 確定: 366件 (Win 96 / Loss 129 / Flat 141) / skip 509件
- 成長率目線: 平均log +0.000509 / 幾何平均 +0.051% per trade / maxDD +4.21%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TROLLSOL/USDT:USDT `LIMIT_BB3S` EXPIRED account +0.00% 残高後 $120.48

## 4. Latest Market Context

- 更新: 2026-05-15T00:38:12.338049+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.62% price=81550.9
- Funnel: target 760 → liquid 165 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.3 >= 65=1, 4h RSI 67.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| UP/USDT:USDT | +18.62% | $3,786,795.51 |
| TAC/USDT:USDT | +17.45% | $1,883,185.60 |
| PEAQ/USDT:USDT | +15.91% | $1,741,065.14 |
| FIGSTOCK/USDT:USDT | +14.90% | $3,062,869.14 |
| TROLLSOL/USDT:USDT | +11.59% | $1,572,031.27 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| WLFI/USDT:USDT | below_1h_threshold | +3.77% | +3.15% |
| BILL/USDT:USDT | below_1h_threshold | +3.11% | +2.49% |
| CC/USDT:USDT | below_1h_threshold | +2.31% | +1.69% |
| PENDLE/USDT:USDT | below_1h_threshold | +2.28% | +1.66% |
| PNUT/USDT:USDT | below_1h_threshold | +2.26% | +1.64% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
