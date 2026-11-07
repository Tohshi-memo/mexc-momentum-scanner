# Decision Report

- generated_at: 2026-11-07T09:36:07.038785+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18364**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18364, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.29%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.29% | **-0.29%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 5/20 | 25.0% | +4.07% | **+1.02%** |
| LIMIT_8PCT | 3/20 | 15.0% | +6.57% | **+0.99%** |
| LIMIT_7PCT | 3/20 | 15.0% | +6.27% | **+0.94%** |
| LIMIT_6PCT | 6/20 | 30.0% | +2.94% | **+0.88%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +2.57% | **+2.32%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.59% | **+1.11%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +1.41% | **+0.91%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.25% | **+0.56%** |

## 2. $100 Live Portfolio

- 残高: **$121.61** / 初期 $100.00 (+21.61%)
- 確定トレード: 264件 (TP 97 / SL 159 / EXP 8)
- 最新: CSOPSKHYNIX2L/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,476.64** / 初期 $100.00 (+1376.64%)
- 確定: 7060件 (Win 2030 / Loss 2255 / Flat 2775) / skip 7865件
- 成長率目線: 平均log +0.000381 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $1,476.64

## 4. Robust Adaptive DryRun ($100)

- 残高: **$393.70** / 初期 $100.00 (+293.70%)
- 確定: 4730件 (Win 1273 / Loss 1042 / Flat 2415) / skip 7045件
- 成長率目線: 平均log +0.000290 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0811 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_6PCT` TP_HIT account +0.69% 残高後 $393.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6522件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000208 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-07T09:35:58.971221+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=76064.8
- Funnel: target 1089 → liquid 149 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +54.98% | $62,830,390.05 |
| AIN/USDT:USDT | +43.48% | $8,471,389.01 |
| ONE/USDT:USDT | +18.63% | $17,819,056.42 |
| LYN/USDT:USDT | +9.00% | $1,812,622.62 |
| ARIA/USDT:USDT | +8.33% | $1,327,715.04 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MUU/USDT:USDT | below_1h_threshold | +3.35% | +3.47% |
| SOXL/USDT:USDT | below_1h_threshold | +3.13% | +3.26% |
| MVLL/USDT:USDT | below_1h_threshold | +2.18% | +2.30% |
| INTW/USDT:USDT | below_1h_threshold | +1.69% | +1.81% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +1.57% | +1.70% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
