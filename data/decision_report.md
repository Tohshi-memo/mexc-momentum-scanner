# Decision Report

- generated_at: 2026-05-13T21:17:59.276780+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4253**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.24% / filled 20/20。**
- 全期間 MARKET基準: n=4253, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.24% | **+0.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 3/14 | 21.4% | +1.42% | **+0.30%** |
| MARKET | 20/20 | 100.0% | +0.24% | **+0.24%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.21% | **+0.19%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +2.81% | **+0.98%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.09% | **+0.98%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.03% | **+0.77%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.99% | **+0.64%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |

## 2. $100 Live Portfolio

- 残高: **$97.70** / 初期 $100.00 (-2.30%)
- 確定トレード: 40件 (TP 10 / SL 27 / EXP 3)
- 最新: IRYS/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.70
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.18** / 初期 $100.00 (+19.18%)
- 確定: 342件 (Win 94 / Loss 125 / Flat 123) / skip 472件
- 成長率目線: 平均log +0.000513 / 幾何平均 +0.051% per trade / maxDD +4.21%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: COS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $119.18

## 4. Latest Market Context

- 更新: 2026-05-13T21:17:56.112919+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.37% price=79378.2
- Funnel: target 759 → liquid 170 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TROLLSOL/USDT:USDT | +21.18% | $1,530,206.44 |
| CSCOSTOCK/USDT:USDT | +17.37% | $2,921,931.79 |
| BEAT/USDT:USDT | +15.70% | $2,867,245.66 |
| UP/USDT:USDT | +14.56% | $4,705,046.69 |
| BB/USDT:USDT | +12.01% | $1,905,251.30 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IRYS/USDT:USDT | below_1h_threshold | +4.38% | +4.75% |
| CSCOSTOCK/USDT:USDT | below_1h_threshold | +2.29% | +2.66% |
| UB/USDT:USDT | below_1h_threshold | +2.13% | +2.50% |
| TROLLSOL/USDT:USDT | below_1h_threshold | +2.10% | +2.47% |
| COLLECT/USDT:USDT | below_1h_threshold | +1.83% | +2.20% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
