# Decision Report

- generated_at: 2026-06-06T13:47:22.636366+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5835**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5835, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_BB3S | 5/18 | 27.8% | +0.99% | **+0.27%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.46% | **+0.23%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |
| ASK | 20/20 | 100.0% | +0.15% | **+0.15%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +1.31% | **+1.31%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.14% | **+0.97%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +2.40% | **+0.84%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.20% | **+0.84%** |
| ASK_LONG | 20/20 | 100.0% | +0.68% | **+0.68%** |

## 2. $100 Live Portfolio

- 残高: **$99.50** / 初期 $100.00 (-0.50%)
- 確定トレード: 1件 (TP 0 / SL 1 / EXP 0)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.50
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.54** / 初期 $100.00 (+30.54%)
- 確定: 1014件 (Win 239 / Loss 313 / Flat 462) / skip 1382件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ALLO/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $130.54

## 4. Latest Market Context

- 更新: 2026-06-06T13:47:18.868053+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.18% price=60887.9
- Funnel: target 771 → liquid 148 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.9 >= 65=1, 4h RSI 76.4 >= 65=1, 4h RSI 70.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ALLO/USDT:USDT | +116.11% | $62,509,796.98 |
| BLUAI/USDT:USDT | +67.67% | $4,514,778.42 |
| VELVET/USDT:USDT | +49.79% | $3,563,330.26 |
| HEI/USDT:USDT | +41.07% | $3,285,395.18 |
| CLO/USDT:USDT | +32.10% | $2,552,073.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_1h_threshold | +3.40% | +3.59% |
| GUA/USDT:USDT | below_1h_threshold | +2.96% | +3.15% |
| POL/USDT:USDT | below_1h_threshold | +1.52% | +1.71% |
| HOME/USDT:USDT | below_1h_threshold | +1.47% | +1.65% |
| TONCOIN/USDT:USDT | below_1h_threshold | +1.29% | +1.48% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
