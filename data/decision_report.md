# Decision Report

- generated_at: 2026-06-03T17:11:19.573671+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5565**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5565, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.10% | **-0.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.39% | **+0.25%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.09% | **+0.07%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.09% | **+0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/7 | 42.9% | +4.71% | **+2.02%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.91% | **+0.77%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.18% | **+0.77%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.92% | **+0.38%** |

## 2. $100 Live Portfolio

- 残高: **$96.13** / 初期 $100.00 (-3.87%)
- 確定トレード: 91件 (TP 26 / SL 62 / EXP 3)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.13
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.20** / 初期 $100.00 (+31.20%)
- 確定: 1004件 (Win 239 / Loss 312 / Flat 453) / skip 1122件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $131.20

## 4. Latest Market Context

- 更新: 2026-06-03T17:11:16.161724+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.38% price=65786.1
- Funnel: target 771 → liquid 146 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BP/USDT:USDT | +18.56% | $1,341,055.49 |
| OPN/USDT:USDT | +17.93% | $3,942,995.23 |
| EDEN/USDT:USDT | +16.97% | $1,229,786.92 |
| HEI/USDT:USDT | +6.26% | $1,001,060.30 |
| US/USDT:USDT | +4.11% | $5,598,760.94 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PIEVERSE/USDT:USDT | below_1h_threshold | +4.92% | +5.29% |
| BP/USDT:USDT | below_1h_threshold | +2.82% | +3.20% |
| APR/USDT:USDT | below_1h_threshold | +1.38% | +1.75% |
| H/USDT:USDT | below_1h_threshold | +1.15% | +1.53% |
| US/USDT:USDT | below_1h_threshold | +0.78% | +1.16% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
