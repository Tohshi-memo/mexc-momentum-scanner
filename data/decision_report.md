# Decision Report

- generated_at: 2026-05-14T11:58:04.506840+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4286**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.73% / filled 20/20。**
- 全期間 MARKET基準: n=4286, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=+0.73%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.73% | **+0.73%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/13 | 46.2% | +5.18% | **+2.39%** |
| LIMIT_ATR | 15/20 | 75.0% | +1.52% | **+1.14%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.18% | **+1.06%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| ASK | 20/20 | 100.0% | +0.78% | **+0.78%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/7 | 71.4% | +3.24% | **+2.32%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.61% | **+0.73%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.28% | **+0.33%** |
| MARKET_LONG | 20/20 | 100.0% | +0.22% | **+0.22%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.34% | **+0.14%** |

## 2. $100 Live Portfolio

- 残高: **$96.73** / 初期 $100.00 (-3.27%)
- 確定トレード: 42件 (TP 10 / SL 29 / EXP 3)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.73
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.18** / 初期 $100.00 (+19.18%)
- 確定: 344件 (Win 94 / Loss 125 / Flat 125) / skip 503件
- 成長率目線: 平均log +0.000510 / 幾何平均 +0.051% per trade / maxDD +4.21%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GIGA/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $119.18

## 4. Latest Market Context

- 更新: 2026-05-14T11:57:58.912150+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.33% price=79269.4
- Funnel: target 763 → liquid 167 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIGENSYN/USDT:USDT | +55.95% | $6,442,499.96 |
| UP/USDT:USDT | +28.90% | $1,806,757.70 |
| TROLLSOL/USDT:USDT | +25.72% | $2,245,811.01 |
| PIEVERSE/USDT:USDT | +19.00% | $2,614,959.88 |
| CSCOSTOCK/USDT:USDT | +18.03% | $5,542,548.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_1h_threshold | +2.32% | +2.65% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +1.64% | +1.97% |
| RIVER/USDT:USDT | below_1h_threshold | +1.04% | +1.37% |
| JTO/USDT:USDT | below_1h_threshold | +0.97% | +1.30% |
| TRIA/USDT:USDT | below_1h_threshold | +0.88% | +1.20% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
