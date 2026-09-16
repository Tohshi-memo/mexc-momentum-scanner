# Decision Report

- generated_at: 2026-09-16T09:46:32.358782+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14656**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14656, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.34% | **-0.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/13 | 46.2% | +1.77% | **+0.82%** |
| LIMIT_5PCT | 11/20 | 55.0% | +0.24% | **+0.13%** |
| LIMIT_8PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |
| LIMIT_10PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |
| LIMIT_9PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/7 | 57.1% | +4.30% | **+2.46%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.94% | **+1.65%** |
| MARKET_LONG | 20/20 | 100.0% | +1.34% | **+1.34%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +0.53% | **+0.32%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,044.14** / 初期 $100.00 (+944.14%)
- 確定: 5534件 (Win 1648 / Loss 1789 / Flat 2097) / skip 5683件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LSK/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,044.14

## 4. Robust Adaptive DryRun ($100)

- 残高: **$228.53** / 初期 $100.00 (+128.53%)
- 確定: 3062件 (Win 840 / Loss 722 / Flat 1500) / skip 5005件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $228.53

## 5. Causal Adaptive DryRun ($100)

- 残高: **$124.64** / 初期 $100.00 (+24.64%)
- 確定: 2945件 (Win 876 / Loss 1156 / Flat 913) / pending 3件 / skip 3179件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000360 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LSK/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $124.64

## 6. Latest Market Context

- 更新: 2026-09-16T09:46:16.997890+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.24% price=75875.4
- Funnel: target 1057 → liquid 154 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +107.59% | $14,825,300.95 |
| LSK/USDT:USDT | +35.84% | $20,669,779.21 |
| USELESS/USDT:USDT | +17.88% | $6,871,515.24 |
| LONGXIA/USDT:USDT | +13.21% | $2,622,047.67 |
| SKYAI/USDT:USDT | +13.20% | $1,509,294.06 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NEAR/USDT:USDT | below_1h_threshold | +2.64% | +2.40% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +2.56% | +2.33% |
| ARB/USDT:USDT | below_1h_threshold | +2.47% | +2.24% |
| CNPY/USDT:USDT | below_1h_threshold | +2.28% | +2.04% |
| RAY/USDT:USDT | below_1h_threshold | +1.86% | +1.63% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
