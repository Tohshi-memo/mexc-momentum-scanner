# Decision Report

- generated_at: 2026-11-21T13:41:48.024246+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19308**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19308, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 11/20 | 55.0% | +1.97% | **+1.08%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.69% | **+0.66%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.39% | **+0.63%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.21% | **+0.49%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.42% | **+0.31%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +5.93% | **+5.93%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +4.19% | **+1.88%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +1.94% | **+1.74%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.80% | **+1.68%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +1.42% | **+1.42%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 283件 (TP 103 / SL 172 / EXP 8)
- 最新: INTCSTOCK/USDT:USDT TP_HIT PnL +5.26% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,659.36** / 初期 $100.00 (+1559.36%)
- 確定: 7451件 (Win 2137 / Loss 2400 / Flat 2914) / skip 8418件
- 成長率目線: 平均log +0.000377 / 幾何平均 +0.038% per trade / maxDD +9.04%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IDOL/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $1,659.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$453.01** / 初期 $100.00 (+353.01%)
- 確定: 5113件 (Win 1361 / Loss 1094 / Flat 2658) / skip 7606件
- 成長率目線: 平均log +0.000295 / 幾何平均 +0.030% per trade / maxDD +4.29%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score +0.0330 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: IDOL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $453.01

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7469件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000279 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-21T13:41:27.234527+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +2.55% price=60334.1
- Funnel: target 1086 → liquid 155 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=1, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLAUDIA/USDT:USDT | +56.89% | $1,129,493.23 |
| IDOL/USDT:USDT | +25.21% | $1,346,532.96 |
| DODO/USDT:USDT | +19.83% | $1,226,288.03 |
| RARE/USDT:USDT | +17.43% | $7,861,386.90 |
| VVV/USDT:USDT | +16.64% | $4,581,359.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UNI/USDT:USDT | below_relative_strength | +5.75% | +3.20% |
| ETHFI/USDT:USDT | below_1h_threshold | +4.22% | +1.67% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +3.77% | +1.22% |
| ZEC/USDT:USDT | below_1h_threshold | +3.38% | +0.82% |
| VET/USDT:USDT | below_1h_threshold | +3.35% | +0.80% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
