# Decision Report

- generated_at: 2026-05-14T00:13:03.352917+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4258**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4258, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=+0.02%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.02% | **+0.02%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 17/20 | 85.0% | +0.19% | **+0.16%** |
| LIMIT_5PCT | 3/20 | 15.0% | +0.95% | **+0.14%** |
| MARKET | 20/20 | 100.0% | +0.02% | **+0.02%** |
| LIMIT_4PCT | 10/20 | 50.0% | +0.01% | **+0.01%** |
| ASK | 20/20 | 100.0% | -0.01% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.36% | **+1.22%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +2.81% | **+0.98%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.29% | **+0.97%** |
| LIMIT_BB3S_LONG | 3/6 | 50.0% | +0.56% | **+0.28%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.44% | **+0.27%** |

## 2. $100 Live Portfolio

- 残高: **$97.70** / 初期 $100.00 (-2.30%)
- 確定トレード: 40件 (TP 10 / SL 27 / EXP 3)
- 最新: IRYS/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.70
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.18** / 初期 $100.00 (+19.18%)
- 確定: 343件 (Win 94 / Loss 125 / Flat 124) / skip 476件
- 成長率目線: 平均log +0.000512 / 幾何平均 +0.051% per trade / maxDD +4.21%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IRYS/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $119.18

## 4. Latest Market Context

- 更新: 2026-05-14T00:13:00.114967+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.19% price=79439.9
- Funnel: target 760 → liquid 168 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TROLLSOL/USDT:USDT | +31.48% | $1,754,577.79 |
| CSCOSTOCK/USDT:USDT | +20.87% | $4,368,228.76 |
| UP/USDT:USDT | +19.01% | $4,849,578.05 |
| AIN/USDT:USDT | +14.88% | $2,433,863.57 |
| BB/USDT:USDT | +12.86% | $2,153,876.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GUA/USDT:USDT | below_1h_threshold | +3.00% | +2.80% |
| GIGA/USDT:USDT | below_1h_threshold | +1.85% | +1.66% |
| BASED/USDT:USDT | below_1h_threshold | +1.70% | +1.51% |
| AKT/USDT:USDT | below_1h_threshold | +1.62% | +1.43% |
| TRUTH/USDT:USDT | below_1h_threshold | +1.45% | +1.26% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
