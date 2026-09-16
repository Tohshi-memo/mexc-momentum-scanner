# Decision Report

- generated_at: 2026-09-16T09:41:19.648793+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14655**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.26% / filled 20/20。**
- 全期間 MARKET基準: n=14655, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.26%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.26% | **+0.26%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/12 | 50.0% | +1.77% | **+0.88%** |
| MARKET | 20/20 | 100.0% | +0.26% | **+0.26%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.17% | **+0.09%** |
| LIMIT_8PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |
| LIMIT_10PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/8 | 62.5% | +2.64% | **+1.65%** |
| MARKET_LONG | 20/20 | 100.0% | +1.34% | **+1.34%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.41% | **+1.20%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.84% | **+0.71%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +1.41% | **+0.21%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,044.14** / 初期 $100.00 (+944.14%)
- 確定: 5533件 (Win 1648 / Loss 1789 / Flat 2096) / skip 5683件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `LIMIT_FIB1272` SL_HIT account +0.03% 残高後 $1,044.14

## 4. Robust Adaptive DryRun ($100)

- 残高: **$228.53** / 初期 $100.00 (+128.53%)
- 確定: 3061件 (Win 840 / Loss 722 / Flat 1499) / skip 5005件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SKYAI/USDT:USDT `LIMIT_FIB1272` SL_HIT account +0.00% 残高後 $228.53

## 5. Causal Adaptive DryRun ($100)

- 残高: **$124.86** / 初期 $100.00 (+24.86%)
- 確定: 2944件 (Win 876 / Loss 1155 / Flat 913) / pending 3件 / skip 3179件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000368 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SKYAI/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $124.86

## 6. Latest Market Context

- 更新: 2026-09-16T09:41:10.995807+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.26% price=75893.5
- Funnel: target 1056 → liquid 154 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +108.45% | $14,649,454.62 |
| LSK/USDT:USDT | +33.76% | $20,424,704.71 |
| USELESS/USDT:USDT | +20.46% | $6,793,051.33 |
| LONGXIA/USDT:USDT | +15.20% | $2,616,393.32 |
| SKYAI/USDT:USDT | +11.47% | $1,421,277.06 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LSK/USDT:USDT | below_relative_strength | +5.11% | +4.85% |
| NEAR/USDT:USDT | below_1h_threshold | +2.85% | +2.59% |
| LONGXIA/USDT:USDT | below_1h_threshold | +2.85% | +2.59% |
| CNPY/USDT:USDT | below_1h_threshold | +2.54% | +2.28% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +2.45% | +2.19% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
