# Decision Report

- generated_at: 2026-08-07T02:31:40.851476+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10654**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.90% / filled 20/20。**
- 全期間 MARKET基準: n=10654, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.90%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.90% | **+0.90%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 15/20 | 75.0% | +1.59% | **+1.19%** |
| MARKET | 20/20 | 100.0% | +0.90% | **+0.90%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.18% | **+0.15%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.13% | **+0.10%** |
| LIMIT_5PCT | 4/20 | 20.0% | -0.15% | **-0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +4.90% | **+4.90%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.97% | **+0.53%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.55% | **+0.39%** |

## 2. $100 Live Portfolio

- 残高: **$121.05** / 初期 $100.00 (+21.05%)
- 確定トレード: 175件 (TP 67 / SL 103 / EXP 5)
- 最新: COTI/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.05
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$595.60** / 初期 $100.00 (+495.60%)
- 確定: 3797件 (Win 1203 / Loss 1250 / Flat 1344) / skip 3418件
- 成長率目線: 平均log +0.000470 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: KMNO/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $595.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$144.37** / 初期 $100.00 (+44.37%)
- 確定: 1454件 (Win 406 / Loss 342 / Flat 706) / skip 2611件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AXTISTOCK/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $144.37

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.56** / 初期 $100.00 (+16.56%)
- 確定: 1157件 (Win 369 / Loss 455 / Flat 333) / pending 2件 / skip 973件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000367 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: RIVER/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $116.56

## 6. Latest Market Context

- 更新: 2026-08-07T02:31:25.197215+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=64295.0
- Funnel: target 958 → liquid 189 → pre 50 → checked 50 → surge 5 → strict 2
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.2 >= 65=1, 4h RSI 76.9 >= 65=1, 4h RSI 92.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STG/USDT:USDT | +32.19% | $4,807,852.25 |
| CATE/USDT:USDT | +24.43% | $3,946,196.82 |
| RIVER/USDT:USDT | +18.38% | $7,135,175.19 |
| TWLOSTOCK/USDT:USDT | +17.69% | $1,388,842.78 |
| NETSTOCK/USDT:USDT | +15.29% | $1,328,505.27 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +3.71% | +3.86% |
| ACT/USDT:USDT | below_1h_threshold | +1.44% | +1.60% |
| SOXS/USDT:USDT | below_1h_threshold | +1.30% | +1.46% |
| NICKEL/USDT:USDT | below_1h_threshold | +1.08% | +1.23% |
| 1000BONK/USDT:USDT | below_1h_threshold | +0.82% | +0.97% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
