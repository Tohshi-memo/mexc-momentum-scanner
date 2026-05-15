# Decision Report

- generated_at: 2026-05-15T00:43:11.443533+00:00
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

- 更新: 2026-05-15T00:43:07.622735+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.27% price=81267.0
- Funnel: target 760 → liquid 166 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.5 >= 65=2
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| UP/USDT:USDT | +19.56% | $3,826,768.38 |
| TAC/USDT:USDT | +17.97% | $1,888,395.61 |
| PEAQ/USDT:USDT | +15.77% | $1,758,410.35 |
| FIGSTOCK/USDT:USDT | +14.55% | $3,064,433.00 |
| TROLLSOL/USDT:USDT | +13.55% | $1,589,041.87 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STAR/USDT:USDT | below_relative_strength | +5.09% | +4.82% |
| BILL/USDT:USDT | below_1h_threshold | +3.23% | +2.96% |
| NAORIS/USDT:USDT | below_1h_threshold | +2.29% | +2.02% |
| WLFI/USDT:USDT | below_1h_threshold | +2.03% | +1.76% |
| CC/USDT:USDT | below_1h_threshold | +1.92% | +1.65% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
