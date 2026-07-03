# Decision Report

- generated_at: 2026-07-03T00:26:27.193700+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8119**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.54% / filled 20/20。**
- 全期間 MARKET基準: n=8119, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.54%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.54% | **+1.54%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.59% | **+1.59%** |
| MARKET | 20/20 | 100.0% | +1.54% | **+1.54%** |
| LIMIT_2PCT | 13/20 | 65.0% | +1.32% | **+0.86%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.82% | **+0.37%** |
| LIMIT_5PCT | 5/20 | 25.0% | +1.21% | **+0.30%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +1.45% | **+0.95%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +1.40% | **+0.77%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +2.39% | **+0.48%** |
| LIMIT_FIB1272_LONG | 14/20 | 70.0% | +0.40% | **+0.28%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.48% | **+0.19%** |

## 2. $100 Live Portfolio

- 残高: **$102.62** / 初期 $100.00 (+2.62%)
- 確定トレード: 53件 (TP 19 / SL 33 / EXP 1)
- 最新: GUA/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.62
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$284.67** / 初期 $100.00 (+184.67%)
- 確定: 2444件 (Win 754 / Loss 816 / Flat 874) / skip 2236件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $284.67

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.46** / 初期 $100.00 (+5.46%)
- 確定: 577件 (Win 140 / Loss 137 / Flat 300) / skip 953件
- 成長率目線: 平均log +0.000092 / 幾何平均 +0.009% per trade / maxDD +3.55%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BREV/USDT:USDT `LIMIT_FIB1272_LONG` SL_HIT account -0.35% 残高後 $105.46

## 5. Latest Market Context

- 更新: 2026-07-03T00:26:20.343699+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.31% price=61349.1
- Funnel: target 834 → liquid 172 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| THE/USDT:USDT | +29.63% | $1,823,095.03 |
| RPL/USDT:USDT | +19.59% | $1,289,467.69 |
| PIPPIN/USDT:USDT | +18.79% | $6,074,809.31 |
| MAGMA/USDT:USDT | +17.08% | $5,117,623.91 |
| GUA/USDT:USDT | +13.21% | $9,295,891.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GUA/USDT:USDT | below_1h_threshold | +4.00% | +4.31% |
| WLD/USDT:USDT | below_1h_threshold | +3.32% | +3.63% |
| ALLO/USDT:USDT | below_1h_threshold | +2.53% | +2.84% |
| INJ/USDT:USDT | below_1h_threshold | +2.16% | +2.47% |
| BASED/USDT:USDT | below_1h_threshold | +2.01% | +2.32% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
