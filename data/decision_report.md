# Decision Report

- generated_at: 2026-05-15T08:53:18.466106+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4329**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.32% / filled 20/20。**
- 全期間 MARKET基準: n=4329, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+2.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.32% | **+2.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.38% | **+2.38%** |
| MARKET | 20/20 | 100.0% | +2.32% | **+2.32%** |
| LIMIT_1PCT | 17/20 | 85.0% | +2.62% | **+2.23%** |
| LIMIT_2PCT | 14/20 | 70.0% | +2.56% | **+1.79%** |
| LIMIT_ATR | 13/20 | 65.0% | +2.25% | **+1.46%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +2.52% | **+1.26%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +1.77% | **+0.88%** |
| LIMIT_BB3S_LONG | 5/5 | 100.0% | +0.45% | **+0.45%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.71% | **+0.43%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.00% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$96.72** / 初期 $100.00 (-3.28%)
- 確定トレード: 45件 (TP 11 / SL 31 / EXP 3)
- 最新: SNDKSTOCK/USDT:USDT SL_HIT PnL -3.19% 残高後 $96.72
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.42** / 初期 $100.00 (+20.42%)
- 確定: 381件 (Win 97 / Loss 131 / Flat 153) / skip 509件
- 成長率目線: 平均log +0.000488 / 幾何平均 +0.049% per trade / maxDD +4.21%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FF/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $120.42

## 4. Latest Market Context

- 更新: 2026-05-15T08:53:14.520255+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.31% price=80529.3
- Funnel: target 763 → liquid 161 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PEAQ/USDT:USDT | +25.60% | $3,775,318.93 |
| GWEI/USDT:USDT | +25.58% | $1,422,831.52 |
| UP/USDT:USDT | +23.09% | $4,358,584.01 |
| BILL/USDT:USDT | +14.86% | $22,186,236.19 |
| TAC/USDT:USDT | +14.06% | $2,288,469.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| COLLECT/USDT:USDT | below_1h_threshold | +3.14% | +3.45% |
| TAC/USDT:USDT | below_1h_threshold | +2.52% | +2.83% |
| UP/USDT:USDT | below_1h_threshold | +2.42% | +2.73% |
| USOIL/USDT:USDT | below_1h_threshold | +1.29% | +1.61% |
| RIVER/USDT:USDT | below_1h_threshold | +1.21% | +1.53% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
