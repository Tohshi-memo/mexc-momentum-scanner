# Decision Report

- generated_at: 2026-08-15T18:01:27.092669+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11687**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11687, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.98%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.98% | **-0.98%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_BB3S | 5/16 | 31.2% | +0.91% | **+0.28%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.81% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.75% | **+0.88%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.64% | **+0.66%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.33% | **+0.60%** |
| MARKET_LONG | 20/20 | 100.0% | +0.58% | **+0.58%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +1.16% | **+0.52%** |

## 2. $100 Live Portfolio

- 残高: **$121.53** / 初期 $100.00 (+21.53%)
- 確定トレード: 183件 (TP 71 / SL 107 / EXP 5)
- 最新: MOVR/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.53
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$641.37** / 初期 $100.00 (+541.37%)
- 確定: 4155件 (Win 1290 / Loss 1355 / Flat 1510) / skip 4093件
- 成長率目線: 平均log +0.000447 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEMI/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $641.37

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.25** / 初期 $100.00 (+55.25%)
- 確定: 1750件 (Win 492 / Loss 413 / Flat 845) / skip 3348件
- 成長率目線: 平均log +0.000251 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0780 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HEMI/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $155.25

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.71** / 初期 $100.00 (+18.71%)
- 確定: 1620件 (Win 493 / Loss 616 / Flat 511) / pending 6件 / skip 1540件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000355 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: H/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $118.71

## 6. Latest Market Context

- 更新: 2026-08-15T18:01:18.698182+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=63040.8
- Funnel: target 985 → liquid 134 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEMI/USDT:USDT | +9.78% | $2,149,803.13 |
| AEON1/USDT:USDT | +9.18% | $2,302,043.09 |
| ROBO/USDT:USDT | +6.20% | $8,654,383.58 |
| AIO/USDT:USDT | +5.74% | $2,251,454.03 |
| H/USDT:USDT | +4.58% | $4,664,488.58 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| WAL/USDT:USDT | below_1h_threshold | +0.79% | +0.79% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +0.60% | +0.60% |
| ALLO/USDT:USDT | below_1h_threshold | +0.25% | +0.25% |
| LAB/USDT:USDT | below_1h_threshold | +0.23% | +0.23% |
| SOXL/USDT:USDT | below_1h_threshold | +0.22% | +0.22% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
