# Decision Report

- generated_at: 2026-09-22T10:31:27.962564+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15316**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15316, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 11/16 | 68.8% | +3.32% | **+2.28%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_5PCT | 6/20 | 30.0% | +2.13% | **+0.64%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.27% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +5.18% | **+3.88%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.46% | **+1.17%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.67% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,180.96** / 初期 $100.00 (+1080.96%)
- 確定: 5807件 (Win 1725 / Loss 1869 / Flat 2213) / skip 6070件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: 4STOCK/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $1,180.96

## 4. Robust Adaptive DryRun ($100)

- 残高: **$250.38** / 初期 $100.00 (+150.38%)
- 確定: 3352件 (Win 926 / Loss 780 / Flat 1646) / skip 5375件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $250.38

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.01** / 初期 $100.00 (+23.01%)
- 確定: 3087件 (Win 908 / Loss 1208 / Flat 971) / pending 5件 / skip 3696件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000061 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: 4STOCK/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.04% 残高後 $123.01

## 6. Latest Market Context

- 更新: 2026-09-22T10:31:16.691031+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.49% price=85786.7
- Funnel: target 1056 → liquid 176 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| 4STOCK/USDT:USDT | +62.98% | $2,589,843.72 |
| KERNEL/USDT:USDT | +34.07% | $4,388,885.05 |
| MUBARAK/USDT:USDT | +33.48% | $3,905,051.14 |
| NIL/USDT:USDT | +23.56% | $3,473,811.43 |
| GRASS/USDT:USDT | +21.11% | $3,586,587.73 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MARSCOIN/USDT:USDT | below_1h_threshold | +3.62% | +4.11% |
| SOXL/USDT:USDT | below_1h_threshold | +1.83% | +2.32% |
| QNT/USDT:USDT | below_1h_threshold | +1.66% | +2.15% |
| USELESS/USDT:USDT | below_1h_threshold | +1.64% | +2.13% |
| MVLL/USDT:USDT | below_1h_threshold | +1.40% | +1.90% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
