# Decision Report

- generated_at: 2026-09-21T18:06:26.303643+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15276**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15276, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.98%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.98% | **-0.98%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT | 15/20 | 75.0% | +0.86% | **+0.65%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.88% | **+0.22%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.27% | **+0.08%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | -0.16% | **-0.06%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.60% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.47% | **+1.85%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +2.16% | **+1.51%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.51% | **+1.28%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.82% | **+1.09%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +3.02% | **+1.06%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,189.67** / 初期 $100.00 (+1089.67%)
- 確定: 5767件 (Win 1716 / Loss 1852 / Flat 2199) / skip 6070件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SAGA/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $1,189.67

## 4. Robust Adaptive DryRun ($100)

- 残高: **$247.93** / 初期 $100.00 (+147.93%)
- 確定: 3318件 (Win 916 / Loss 766 / Flat 1636) / skip 5369件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0540 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SAGA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.52% 残高後 $247.93

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.78** / 初期 $100.00 (+22.78%)
- 確定: 3049件 (Win 896 / Loss 1192 / Flat 961) / pending 5件 / skip 3695件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000281 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SAGA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $122.78

## 6. Latest Market Context

- 更新: 2026-09-21T18:06:15.772210+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=85936.0
- Funnel: target 1055 → liquid 170 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FORM/USDT:USDT | +27.65% | $5,453,554.69 |
| SYN/USDT:USDT | +9.04% | $4,218,854.06 |
| EVAA/USDT:USDT | +6.80% | $1,001,665.09 |
| SAGA/USDT:USDT | +6.55% | $8,337,568.08 |
| PTB/USDT:USDT | +3.73% | $1,178,418.19 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SAGA/USDT:USDT | below_1h_threshold | +2.88% | +2.78% |
| PTB/USDT:USDT | below_1h_threshold | +2.61% | +2.51% |
| METASTOCK/USDT:USDT | below_1h_threshold | +2.10% | +2.01% |
| ZETA/USDT:USDT | below_1h_threshold | +1.67% | +1.58% |
| LAB/USDT:USDT | below_1h_threshold | +1.61% | +1.52% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
