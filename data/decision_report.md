# Decision Report

- generated_at: 2026-07-29T22:16:14.792996+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9840**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.86% / filled 20/20。**
- 全期間 MARKET基準: n=9840, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+3.86%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.86% | **+3.86%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.86% | **+3.86%** |
| LIMIT_1PCT | 14/20 | 70.0% | +3.24% | **+2.26%** |
| LIMIT_2PCT | 9/20 | 45.0% | +1.26% | **+0.57%** |
| LIMIT_3PCT | 7/20 | 35.0% | +0.05% | **+0.02%** |
| LIMIT_5PCT | 2/20 | 10.0% | -0.93% | **-0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 13/20 | 65.0% | +0.00% | **+0.00%** |
| LIMIT_7PCT_LONG | 14/20 | 70.0% | -0.43% | **-0.30%** |
| LIMIT_FIB1618_LONG | 8/20 | 40.0% | -2.24% | **-0.89%** |
| LIMIT_6PCT_LONG | 14/20 | 70.0% | -1.54% | **-1.08%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | -1.59% | **-1.51%** |

## 2. $100 Live Portfolio

- 残高: **$120.46** / 初期 $100.00 (+20.46%)
- 確定トレード: 166件 (TP 65 / SL 96 / EXP 5)
- 最新: MSFU/USDT:USDT SL_HIT PnL -3.27% 残高後 $120.46
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$494.05** / 初期 $100.00 (+394.05%)
- 確定: 3519件 (Win 1113 / Loss 1147 / Flat 1259) / skip 2882件
- 成長率目線: 平均log +0.000454 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $494.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$136.91** / 初期 $100.00 (+36.91%)
- 確定: 1242件 (Win 344 / Loss 283 / Flat 615) / skip 2009件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOXL/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $136.91

## 5. Causal Adaptive DryRun ($100)

- 残高: **$109.01** / 初期 $100.00 (+9.01%)
- 確定: 766件 (Win 246 / Loss 297 / Flat 223) / pending 0件 / skip 547件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000271 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: RIF/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $109.01

## 6. Latest Market Context

- 更新: 2026-07-29T22:16:08.466712+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.26% price=63998.6
- Funnel: target 911 → liquid 178 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MSFU/USDT:USDT | +13.92% | $7,002,808.81 |
| RE/USDT:USDT | +12.49% | $6,681,884.56 |
| LAB/USDT:USDT | +12.47% | $2,425,798.21 |
| AEON1/USDT:USDT | +9.86% | $2,627,474.45 |
| MSFTSTOCK/USDT:USDT | +6.93% | $2,429,576.07 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESP/USDT:USDT | below_1h_threshold | +4.43% | +4.17% |
| ANSEM/USDT:USDT | below_1h_threshold | +2.74% | +2.48% |
| AEON1/USDT:USDT | below_1h_threshold | +2.03% | +1.76% |
| SOXS/USDT:USDT | below_1h_threshold | +1.45% | +1.19% |
| UAI/USDT:USDT | below_1h_threshold | +1.26% | +0.99% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
