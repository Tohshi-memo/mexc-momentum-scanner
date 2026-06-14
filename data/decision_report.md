# Decision Report

- generated_at: 2026-06-14T21:45:13.420083+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6703**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.45% / filled 20/20。**
- 全期間 MARKET基準: n=6703, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.45%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.45% | **+0.45%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 15/20 | 75.0% | +0.93% | **+0.70%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.95% | **+0.67%** |
| MARKET | 20/20 | 100.0% | +0.45% | **+0.45%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.95% | **+0.43%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.67% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +1.17% | **+0.59%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +0.46% | **+0.30%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.23% | **+0.15%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +0.37% | **+0.15%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +0.56% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$100.99** / 初期 $100.00 (+0.99%)
- 確定トレード: 4件 (TP 2 / SL 2 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.99
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$172.33** / 初期 $100.00 (+72.33%)
- 確定: 1576件 (Win 419 / Loss 498 / Flat 659) / skip 1688件
- 成長率目線: 平均log +0.000345 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EVAA/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.24% 残高後 $172.33

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.70** / 初期 $100.00 (-1.30%)
- 確定: 74件 (Win 20 / Loss 15 / Flat 39) / skip 40件
- 成長率目線: 平均log -0.000177 / 幾何平均 -0.018% per trade / maxDD +2.07%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLUAI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $98.70

## 5. Latest Market Context

- 更新: 2026-06-14T21:45:06.955199+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +1.98% price=65243.0
- Funnel: target 770 → liquid 134 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=40, below_relative_strength=7, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.3 >= 65=1, 4h RSI 92.0 >= 65=1, 4h RSI 70.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +51.65% | $11,523,426.26 |
| OPG/USDT:USDT | +27.03% | $2,500,514.15 |
| EDEN/USDT:USDT | +17.75% | $1,099,479.11 |
| RIF/USDT:USDT | +16.56% | $8,704,562.01 |
| BABY/USDT:USDT | +14.85% | $1,998,938.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EDEN/USDT:USDT | below_relative_strength | +6.67% | +4.69% |
| FARTCOIN/USDT:USDT | below_relative_strength | +6.45% | +4.47% |
| ZEC/USDT:USDT | below_relative_strength | +6.37% | +4.39% |
| BP/USDT:USDT | below_relative_strength | +6.31% | +4.34% |
| BANANAS31/USDT:USDT | below_relative_strength | +6.26% | +4.28% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
