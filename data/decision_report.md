# Decision Report

- generated_at: 2026-06-07T11:42:56.970707+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5954**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5954, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=-1.02%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.02% | **-1.02%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 10/14 | 71.4% | +0.91% | **+0.65%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.60% | **+0.24%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.79% | **+1.79%** |
| ASK_LONG | 20/20 | 100.0% | +1.14% | **+1.14%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +2.17% | **+0.76%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +0.75% | **+0.49%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +0.94% | **+0.28%** |

## 2. $100 Live Portfolio

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定トレード: 5件 (TP 1 / SL 4 / EXP 0)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.00
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$143.85** / 初期 $100.00 (+43.85%)
- 確定: 1071件 (Win 260 / Loss 326 / Flat 485) / skip 1444件
- 成長率目線: 平均log +0.000339 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SIREN/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $143.85

## 4. Latest Market Context

- 更新: 2026-06-07T11:42:53.367395+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.46% price=62629.4
- Funnel: target 768 → liquid 123 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FIDA/USDT:USDT | +56.57% | $7,562,690.63 |
| SIREN/USDT:USDT | +42.91% | $10,325,286.52 |
| LAB/USDT:USDT | +41.47% | $63,187,399.65 |
| EDEN/USDT:USDT | +38.19% | $4,732,037.58 |
| BSB/USDT:USDT | +35.38% | $6,941,756.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_relative_strength | +5.20% | +4.74% |
| BSB/USDT:USDT | below_1h_threshold | +4.97% | +4.51% |
| BEAT/USDT:USDT | below_1h_threshold | +3.28% | +2.82% |
| VELVET/USDT:USDT | below_1h_threshold | +3.26% | +2.80% |
| DRAM/USDT:USDT | below_1h_threshold | +2.99% | +2.53% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
