# Decision Report

- generated_at: 2026-06-07T10:39:45.454175+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5947**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5947, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=-1.79%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.79% | **-1.79%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.60% | **+0.24%** |
| LIMIT_BB3S | 10/18 | 55.6% | +0.39% | **+0.22%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +2.73% | **+2.05%** |
| MARKET_LONG | 20/20 | 100.0% | +1.99% | **+1.99%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +3.11% | **+1.40%** |
| ASK_LONG | 20/20 | 100.0% | +1.29% | **+1.29%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +2.28% | **+1.25%** |

## 2. $100 Live Portfolio

- 残高: **$99.49** / 初期 $100.00 (-0.51%)
- 確定トレード: 4件 (TP 1 / SL 3 / EXP 0)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.49
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$143.50** / 初期 $100.00 (+43.50%)
- 確定: 1064件 (Win 259 / Loss 324 / Flat 481) / skip 1444件
- 成長率目線: 平均log +0.000339 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $143.50

## 4. Latest Market Context

- 更新: 2026-06-07T10:39:42.150048+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.30% price=62319.9
- Funnel: target 768 → liquid 123 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FIDA/USDT:USDT | +61.74% | $7,241,247.34 |
| EDEN/USDT:USDT | +44.06% | $4,177,648.03 |
| LAB/USDT:USDT | +39.18% | $63,113,257.39 |
| BSB/USDT:USDT | +29.22% | $6,908,067.47 |
| ESPORTS/USDT:USDT | +25.55% | $2,033,283.83 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_1h_threshold | +4.58% | +4.88% |
| FIDA/USDT:USDT | below_1h_threshold | +4.11% | +4.41% |
| VELVET/USDT:USDT | below_1h_threshold | +3.48% | +3.78% |
| EDEN/USDT:USDT | below_1h_threshold | +3.21% | +3.51% |
| UB/USDT:USDT | below_1h_threshold | +2.82% | +3.12% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
