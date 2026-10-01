# Decision Report

- generated_at: 2026-10-01T20:16:31.964645+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15943**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.19% / filled 20/20。**
- 全期間 MARKET基準: n=15943, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.19% | **+1.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +5.92% | **+1.48%** |
| LIMIT_8PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| MARKET | 20/20 | 100.0% | +1.19% | **+1.19%** |
| LIMIT_6PCT | 5/20 | 25.0% | +4.33% | **+1.08%** |
| LIMIT_ATR | 9/20 | 45.0% | +1.93% | **+0.87%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/6 | 100.0% | +1.86% | **+1.86%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.29% | **+1.10%** |
| LIMIT_4PCT_LONG | 15/20 | 75.0% | +1.07% | **+0.80%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.86% | **+0.64%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$120.51** / 初期 $100.00 (+20.51%)
- 確定トレード: 227件 (TP 82 / SL 138 / EXP 7)
- 最新: BATON/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.51
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,297.43** / 初期 $100.00 (+1197.43%)
- 確定: 6051件 (Win 1794 / Loss 1954 / Flat 2303) / skip 6453件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LONGXIA/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,297.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$277.90** / 初期 $100.00 (+177.90%)
- 確定: 3596件 (Win 1003 / Loss 838 / Flat 1755) / skip 5758件
- 成長率目線: 平均log +0.000284 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0879 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ALICE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $277.90

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4108件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000330 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-01T20:16:20.275956+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=84749.6
- Funnel: target 1097 → liquid 174 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BATON/USDT:USDT | +96.44% | $1,990,156.62 |
| MAGMA/USDT:USDT | +23.33% | $1,224,393.60 |
| LONGXIA/USDT:USDT | +14.24% | $11,300,108.15 |
| ALICE/USDT:USDT | +14.05% | $2,063,450.78 |
| VELO/USDT:USDT | +9.78% | $1,103,141.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BATON/USDT:USDT | below_1h_threshold | +1.66% | +1.52% |
| MAGMA/USDT:USDT | below_1h_threshold | +1.29% | +1.14% |
| MUU/USDT:USDT | below_1h_threshold | +1.25% | +1.11% |
| LONGXIA/USDT:USDT | below_1h_threshold | +1.22% | +1.07% |
| GRASS/USDT:USDT | below_1h_threshold | +0.99% | +0.85% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
