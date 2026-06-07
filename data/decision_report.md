# Decision Report

- generated_at: 2026-06-07T10:34:11.833710+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5946**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5946, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=-1.79%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.79% | **-1.79%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +2.54% | **+0.76%** |
| LIMIT_BB3S | 11/19 | 57.9% | +1.09% | **+0.63%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.92% | **+0.58%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.63% | **+0.29%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.19% | **+2.19%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +2.56% | **+1.79%** |
| ASK_LONG | 20/20 | 100.0% | +1.49% | **+1.49%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +3.11% | **+1.40%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +2.28% | **+1.25%** |

## 2. $100 Live Portfolio

- 残高: **$99.49** / 初期 $100.00 (-0.51%)
- 確定トレード: 4件 (TP 1 / SL 3 / EXP 0)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.49
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$143.50** / 初期 $100.00 (+43.50%)
- 確定: 1063件 (Win 259 / Loss 324 / Flat 480) / skip 1444件
- 成長率目線: 平均log +0.000340 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JTO/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $143.50

## 4. Latest Market Context

- 更新: 2026-06-07T10:34:08.744470+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.24% price=62358.6
- Funnel: target 768 → liquid 123 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FIDA/USDT:USDT | +61.29% | $7,187,770.13 |
| EDEN/USDT:USDT | +43.40% | $4,091,644.89 |
| LAB/USDT:USDT | +39.34% | $63,060,415.74 |
| BSB/USDT:USDT | +28.46% | $6,890,990.34 |
| ESPORTS/USDT:USDT | +25.81% | $1,954,366.19 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_1h_threshold | +4.48% | +4.72% |
| FIDA/USDT:USDT | below_1h_threshold | +4.18% | +4.42% |
| VELVET/USDT:USDT | below_1h_threshold | +3.55% | +3.79% |
| EDEN/USDT:USDT | below_1h_threshold | +3.26% | +3.50% |
| BANK/USDT:USDT | below_1h_threshold | +2.91% | +3.15% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
