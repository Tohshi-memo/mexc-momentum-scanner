# Decision Report

- generated_at: 2026-07-27T18:16:17.157516+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9643**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9643, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.43%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.43% | **-0.43%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 18/20 | 90.0% | +0.34% | **+0.31%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.16% | **+0.12%** |
| LIMIT_1PCT | 20/20 | 100.0% | -0.02% | **-0.02%** |
| LIMIT_5PCT | 4/20 | 20.0% | -0.29% | **-0.06%** |
| LIMIT_4PCT | 13/20 | 65.0% | -0.15% | **-0.10%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/6 | 33.3% | +6.85% | **+2.28%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.99% | **+1.19%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +2.15% | **+1.08%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +2.11% | **+0.84%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.24% | **+0.62%** |

## 2. $100 Live Portfolio

- 残高: **$106.92** / 初期 $100.00 (+6.92%)
- 確定トレード: 145件 (TP 50 / SL 90 / EXP 5)
- 最新: ON/USDT:USDT SL_HIT PnL -4.00% 残高後 $106.92
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$454.09** / 初期 $100.00 (+354.09%)
- 確定: 3430件 (Win 1085 / Loss 1117 / Flat 1228) / skip 2774件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $454.09

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1224件 (Win 338 / Loss 275 / Flat 611) / skip 1830件
- 成長率目線: 平均log +0.000259 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0008 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOXS/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$108.87** / 初期 $100.00 (+8.87%)
- 確定: 663件 (Win 219 / Loss 251 / Flat 193) / pending 4件 / skip 447件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000422 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $108.87

## 6. Latest Market Context

- 更新: 2026-07-27T18:16:10.365373+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.24% price=64839.3
- Funnel: target 902 → liquid 174 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LA/USDT:USDT | +34.31% | $2,554,457.76 |
| JIMOTHY/USDT:USDT | +17.22% | $1,953,312.08 |
| RIF/USDT:USDT | +10.61% | $4,966,306.49 |
| AEON1/USDT:USDT | +9.13% | $1,022,377.50 |
| ALLO/USDT:USDT | +6.60% | $4,228,962.41 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MUU/USDT:USDT | below_1h_threshold | +3.21% | +3.45% |
| ALLO/USDT:USDT | below_1h_threshold | +2.45% | +2.69% |
| AEON1/USDT:USDT | below_1h_threshold | +1.79% | +2.02% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +1.54% | +1.78% |
| SOXL/USDT:USDT | below_1h_threshold | +1.06% | +1.30% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
