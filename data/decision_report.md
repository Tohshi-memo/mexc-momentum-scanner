# Decision Report

- generated_at: 2026-05-30T01:19:42.892047+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5084**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.31% / filled 20/20。**
- 全期間 MARKET基準: n=5084, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+0.31%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.31% | **+0.31%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.40% | **+0.40%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.66% | **+0.33%** |
| MARKET | 20/20 | 100.0% | +0.31% | **+0.31%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| MARKET_LONG | 20/20 | 100.0% | +0.29% | **+0.29%** |
| ASK_LONG | 20/20 | 100.0% | +0.24% | **+0.24%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +0.24% | **+0.11%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +0.31% | **+0.09%** |

## 2. $100 Live Portfolio

- 残高: **$98.10** / 初期 $100.00 (-1.90%)
- 確定トレード: 75件 (TP 22 / SL 50 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.68** / 初期 $100.00 (+25.68%)
- 確定: 744件 (Win 175 / Loss 226 / Flat 343) / skip 901件
- 成長率目線: 平均log +0.000307 / 幾何平均 +0.031% per trade / maxDD +4.72%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ALLO/USDT:USDT `LIMIT_BB3S` EXPIRED account +0.00% 残高後 $125.68

## 4. Latest Market Context

- 更新: 2026-05-30T01:19:40.416121+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=73562.6
- Funnel: target 773 → liquid 148 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| XLM/USDT:USDT | +25.98% | $409,482,028.79 |
| OL/USDT:USDT | +20.96% | $1,490,625.40 |
| HBAR/USDT:USDT | +18.70% | $36,873,990.79 |
| BASED/USDT:USDT | +16.04% | $2,491,156.68 |
| LAB/USDT:USDT | +15.72% | $132,062,079.51 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ALGO/USDT:USDT | below_1h_threshold | +2.83% | +2.70% |
| JTO/USDT:USDT | below_1h_threshold | +2.28% | +2.15% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.94% | +1.81% |
| HEI/USDT:USDT | below_1h_threshold | +1.92% | +1.79% |
| RAVE/USDT:USDT | below_1h_threshold | +1.71% | +1.59% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
