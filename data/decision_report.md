# Decision Report

- generated_at: 2026-11-13T07:06:32.145288+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18797**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.32% / filled 20/20。**
- 全期間 MARKET基準: n=18797, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.32% | **+0.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.47% | **+1.40%** |
| LIMIT_8PCT | 5/20 | 25.0% | +3.88% | **+0.97%** |
| LIMIT_7PCT | 5/20 | 25.0% | +3.52% | **+0.88%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +2.01% | **+1.21%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +1.33% | **+1.19%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.24% | **+1.18%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +2.35% | **+1.06%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.23% | **+0.78%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 273件 (TP 99 / SL 166 / EXP 8)
- 最新: IDOL/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,776.71** / 初期 $100.00 (+1676.71%)
- 確定: 7267件 (Win 2095 / Loss 2327 / Flat 2845) / skip 8091件
- 成長率目線: 平均log +0.000396 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_8PCT_LONG` TP_HIT account +1.00% 残高後 $1,776.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$402.74** / 初期 $100.00 (+302.74%)
- 確定: 4816件 (Win 1299 / Loss 1071 / Flat 2446) / skip 7392件
- 成長率目線: 平均log +0.000289 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0626 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $402.74

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6956件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000185 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-13T07:06:11.468199+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=69147.1
- Funnel: target 1086 → liquid 152 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +60.19% | $10,657,102.99 |
| BARD/USDT:USDT | +52.35% | $11,185,996.13 |
| ARIA/USDT:USDT | +40.90% | $9,484,196.08 |
| KOR/USDT:USDT | +37.57% | $1,735,168.01 |
| GANG/USDT:USDT | +18.49% | $1,195,478.56 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +4.68% | +4.52% |
| KGEN/USDT:USDT | below_1h_threshold | +3.73% | +3.57% |
| USELESS/USDT:USDT | below_1h_threshold | +1.77% | +1.62% |
| PONS/USDT:USDT | below_1h_threshold | +1.49% | +1.34% |
| H/USDT:USDT | below_1h_threshold | +1.48% | +1.32% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
