# Decision Report

- generated_at: 2026-11-08T04:51:18.119741+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18404**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.65% / filled 20/20。**
- 全期間 MARKET基準: n=18404, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.65%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.65% | **+0.65%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.26% | **+0.68%** |
| MARKET | 20/20 | 100.0% | +0.65% | **+0.65%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.51% | **+0.41%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.42% | **+0.40%** |
| LIMIT_6PCT | 10/20 | 50.0% | +0.78% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 16/20 | 80.0% | +2.18% | **+1.75%** |
| LIMIT_5PCT_LONG | 14/20 | 70.0% | +2.34% | **+1.64%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +1.23% | **+1.11%** |
| LIMIT_3PCT_LONG | 17/20 | 85.0% | +1.01% | **+0.86%** |
| LIMIT_BB3S_LONG | 5/7 | 71.4% | +0.80% | **+0.57%** |

## 2. $100 Live Portfolio

- 残高: **$121.61** / 初期 $100.00 (+21.61%)
- 確定トレード: 264件 (TP 97 / SL 159 / EXP 8)
- 最新: CSOPSKHYNIX2L/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,523.60** / 初期 $100.00 (+1423.60%)
- 確定: 7100件 (Win 2041 / Loss 2269 / Flat 2790) / skip 7865件
- 成長率目線: 平均log +0.000384 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LYN/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $1,523.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$389.21** / 初期 $100.00 (+289.21%)
- 確定: 4754件 (Win 1277 / Loss 1047 / Flat 2430) / skip 7061件
- 成長率目線: 平均log +0.000286 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0873 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: IDOL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $389.21

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6563件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000382 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-08T04:51:07.513999+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=75815.2
- Funnel: target 1089 → liquid 111 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLAUDIA/USDT:USDT | +138.34% | $7,656,151.70 |
| BTW/USDT:USDT | +5.00% | $6,681,205.58 |
| MET/USDT:USDT | +3.63% | $1,580,547.82 |
| DASH/USDT:USDT | +3.17% | $7,006,215.96 |
| ARIA/USDT:USDT | +2.84% | $1,782,770.83 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIOT/USDT:USDT | below_1h_threshold | +2.82% | +2.92% |
| SOXL/USDT:USDT | below_1h_threshold | +0.53% | +0.62% |
| BLESS/USDT:USDT | below_1h_threshold | +0.29% | +0.38% |
| MUU/USDT:USDT | below_1h_threshold | +0.29% | +0.38% |
| DASH/USDT:USDT | below_1h_threshold | +0.21% | +0.30% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
