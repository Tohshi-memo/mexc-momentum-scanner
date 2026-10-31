# Decision Report

- generated_at: 2026-10-31T21:36:15.174702+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17912**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.05% / filled 20/20。**
- 全期間 MARKET基準: n=17912, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.05% | **+2.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.05% | **+2.05%** |
| LIMIT_2PCT | 13/20 | 65.0% | +1.11% | **+0.72%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +0.00% | **+0.00%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -0.44% | **-0.09%** |

## 2. $100 Live Portfolio

- 残高: **$121.74** / 初期 $100.00 (+21.74%)
- 確定トレード: 257件 (TP 95 / SL 154 / EXP 8)
- 最新: JCT/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.74
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,485.74** / 初期 $100.00 (+1385.74%)
- 確定: 6820件 (Win 1976 / Loss 2188 / Flat 2656) / skip 7653件
- 成長率目線: 平均log +0.000396 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `MARKET` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BEAMX/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $1,485.74

## 4. Robust Adaptive DryRun ($100)

- 残高: **$370.19** / 初期 $100.00 (+270.19%)
- 確定: 4412件 (Win 1185 / Loss 983 / Flat 2244) / skip 6911件
- 成長率目線: 平均log +0.000297 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0534 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: IDOL/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $370.19

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6075件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000430 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-31T21:36:04.690749+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=77460.8
- Funnel: target 1089 → liquid 121 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +11.33% | $1,017,458.25 |
| EVAA/USDT:USDT | +6.60% | $3,820,396.51 |
| LIT/USDT:USDT | +6.53% | $7,472,264.75 |
| MORPHO/USDT:USDT | +3.76% | $2,483,217.72 |
| MAGMA/USDT:USDT | +2.77% | $1,061,966.19 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZRO/USDT:USDT | below_1h_threshold | +2.49% | +2.57% |
| STX/USDT:USDT | below_1h_threshold | +1.28% | +1.36% |
| MAGMA/USDT:USDT | below_1h_threshold | +0.77% | +0.85% |
| AKE/USDT:USDT | below_1h_threshold | +0.64% | +0.73% |
| AIN/USDT:USDT | below_1h_threshold | +0.56% | +0.64% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
