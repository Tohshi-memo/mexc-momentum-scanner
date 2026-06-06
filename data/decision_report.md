# Decision Report

- generated_at: 2026-06-06T21:14:41.044149+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5905**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5905, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| LIMIT_FIB1272 | 2/20 | 10.0% | +5.39% | **+0.54%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.95% | **+0.48%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/8 | 75.0% | +6.19% | **+4.64%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +2.21% | **+1.77%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.22% | **+1.33%** |
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| ASK_LONG | 20/20 | 100.0% | +1.02% | **+1.02%** |

## 2. $100 Live Portfolio

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定トレード: 2件 (TP 0 / SL 2 / EXP 0)
- 最新: PORTAL/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.00
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$137.07** / 初期 $100.00 (+37.07%)
- 確定: 1038件 (Win 249 / Loss 319 / Flat 470) / skip 1428件
- 成長率目線: 平均log +0.000304 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `LIMIT_BB3S_LONG` TP_HIT account +1.00% 残高後 $137.07

## 4. Latest Market Context

- 更新: 2026-06-06T21:14:35.212010+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.20% price=60797.0
- Funnel: target 771 → liquid 125 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +63.99% | $57,055,933.24 |
| FIDA/USDT:USDT | +28.87% | $2,206,243.61 |
| SKYAI/USDT:USDT | +22.47% | $21,227,386.74 |
| BTW/USDT:USDT | +17.00% | $13,962,513.10 |
| BABY/USDT:USDT | +8.32% | $3,462,824.17 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_1h_threshold | +1.60% | +1.40% |
| BABY/USDT:USDT | below_1h_threshold | +1.13% | +0.93% |
| HOME/USDT:USDT | below_1h_threshold | +1.00% | +0.80% |
| FIDA/USDT:USDT | below_1h_threshold | +0.91% | +0.72% |
| TONCOIN/USDT:USDT | below_1h_threshold | +0.82% | +0.63% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
