# Decision Report

- generated_at: 2026-11-04T01:06:15.989991+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18099**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.86% / filled 20/20。**
- 全期間 MARKET基準: n=18099, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.86%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.86% | **+0.86%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.86% | **+0.86%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.85% | **+0.81%** |
| LIMIT_ATR | 14/20 | 70.0% | +1.13% | **+0.79%** |
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +1.47% | **+1.47%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +1.17% | **+1.17%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.84% | **+0.71%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.71% | **+0.60%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.56% | **+0.45%** |

## 2. $100 Live Portfolio

- 残高: **$121.61** / 初期 $100.00 (+21.61%)
- 確定トレード: 261件 (TP 96 / SL 157 / EXP 8)
- 最新: IDOL/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,500.44** / 初期 $100.00 (+1400.44%)
- 確定: 6921件 (Win 2001 / Loss 2219 / Flat 2701) / skip 7739件
- 成長率目線: 平均log +0.000391 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ICNT/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $1,500.44

## 4. Robust Adaptive DryRun ($100)

- 残高: **$378.70** / 初期 $100.00 (+278.70%)
- 確定: 4513件 (Win 1208 / Loss 1005 / Flat 2300) / skip 6997件
- 成長率目線: 平均log +0.000295 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0602 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOXL/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $378.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6259件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000121 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-04T01:06:04.115476+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.43% price=76897.6
- Funnel: target 1084 → liquid 162 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLANKER/USDT:USDT | +31.55% | $1,136,991.11 |
| SOXS/USDT:USDT | +9.76% | $27,804,065.27 |
| BEAT/USDT:USDT | +5.90% | $11,463,518.00 |
| IDOL/USDT:USDT | +5.42% | $10,283,648.41 |
| SQQQ/USDT:USDT | +4.82% | $1,185,264.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXS/USDT:USDT | below_1h_threshold | +3.91% | +4.33% |
| SQQQ/USDT:USDT | below_1h_threshold | +1.80% | +2.23% |
| UAI/USDT:USDT | below_1h_threshold | +1.50% | +1.93% |
| ALUMINUM/USDT:USDT | below_1h_threshold | +0.50% | +0.92% |
| NICKEL/USDT:USDT | below_1h_threshold | +0.42% | +0.84% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
