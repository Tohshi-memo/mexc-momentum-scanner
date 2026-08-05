# Decision Report

- generated_at: 2026-08-05T13:21:16.999918+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10410**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.32% / filled 20/20。**
- 全期間 MARKET基準: n=10410, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.32% | **+1.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 17/20 | 85.0% | +1.89% | **+1.60%** |
| MARKET | 20/20 | 100.0% | +1.32% | **+1.32%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.23% | **+1.17%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.55% | **+1.01%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +3.40% | **+0.85%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +4.53% | **+1.13%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +3.86% | **+0.96%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.03% | **+0.41%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.35% | **+0.24%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.49% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$605.31** / 初期 $100.00 (+505.31%)
- 確定: 3769件 (Win 1195 / Loss 1236 / Flat 1338) / skip 3202件
- 成長率目線: 平均log +0.000478 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $605.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$143.45** / 初期 $100.00 (+43.45%)
- 確定: 1318件 (Win 373 / Loss 310 / Flat 635) / skip 2503件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0573 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CYS/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $143.45

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.36** / 初期 $100.00 (+18.36%)
- 確定: 1139件 (Win 365 / Loss 441 / Flat 333) / pending 3件 / skip 739件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000134 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HEI/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $118.36

## 6. Latest Market Context

- 更新: 2026-08-05T13:21:09.541529+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.23% price=64149.1
- Funnel: target 945 → liquid 181 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +99.17% | $26,479,921.61 |
| HFT/USDT:USDT | +89.71% | $4,064,782.08 |
| BLESS/USDT:USDT | +88.61% | $59,210,017.11 |
| CYS/USDT:USDT | +36.67% | $33,624,550.99 |
| CASHCAT/USDT:USDT | +36.14% | $1,009,300.02 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAKE/USDT:USDT | below_1h_threshold | +4.82% | +5.05% |
| SYN/USDT:USDT | below_1h_threshold | +3.42% | +3.65% |
| UAI/USDT:USDT | below_1h_threshold | +3.21% | +3.44% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +2.42% | +2.65% |
| GRVT/USDT:USDT | below_1h_threshold | +1.93% | +2.16% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
