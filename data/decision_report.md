# Decision Report

- generated_at: 2026-09-09T16:51:57.709314+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14089**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14089, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.98%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.98% | **-0.98%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 11/20 | 55.0% | +1.14% | **+0.63%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.91% | **+0.27%** |
| LIMIT_BB3S | 2/18 | 11.1% | +2.27% | **+0.25%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +2.33% | **+2.33%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.01% | **+1.41%** |
| MARKET_LONG | 20/20 | 100.0% | +1.25% | **+1.25%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +2.40% | **+0.60%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.41% | **+0.41%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$991.95** / 初期 $100.00 (+891.95%)
- 確定: 5313件 (Win 1594 / Loss 1715 / Flat 2004) / skip 5337件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IOST/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $991.95

## 4. Robust Adaptive DryRun ($100)

- 残高: **$191.95** / 初期 $100.00 (+91.95%)
- 確定: 2683件 (Win 737 / Loss 628 / Flat 1318) / skip 4817件
- 成長率目線: 平均log +0.000243 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0499 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOCK/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $191.95

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.84** / 初期 $100.00 (+17.84%)
- 確定: 2620件 (Win 765 / Loss 1001 / Flat 854) / pending 0件 / skip 2951件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000225 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ZEC/USDT:USDT `MARKET` EXPIRED account -0.09% 残高後 $117.84

## 6. Latest Market Context

- 更新: 2026-09-09T16:51:39.456007+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.20% price=78723.4
- Funnel: target 1064 → liquid 165 → pre 50 → checked 50 → surge 8 → strict 1
- Surge前reject: below_1h_threshold=42, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1, 4h RSI 86.4 >= 65=1, 4h RSI 81.2 >= 65=1, 4h RSI 65.9 >= 65=1, 4h RSI 72.6 >= 65=1, 4h RSI 74.1 >= 65=1, 4h RSI 69.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SOCK/USDT:USDT | +17.60% | $1,509,061.80 |
| IOST/USDT:USDT | +8.99% | $17,468,895.33 |
| PHA/USDT:USDT | +7.94% | $1,296,269.22 |
| CATE/USDT:USDT | +6.72% | $1,997,873.96 |
| STRK/USDT:USDT | +6.50% | $2,029,896.74 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CASHCAT/USDT:USDT | below_1h_threshold | +3.54% | +3.35% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +3.31% | +3.11% |
| FARTCOIN/USDT:USDT | below_1h_threshold | +2.93% | +2.73% |
| 4/USDT:USDT | below_1h_threshold | +2.92% | +2.72% |
| BTR/USDT:USDT | below_1h_threshold | +2.91% | +2.71% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
