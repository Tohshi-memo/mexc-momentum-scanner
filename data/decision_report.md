# Decision Report

- generated_at: 2026-09-04T17:01:22.357943+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13645**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13645, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.08%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.08% | **-0.08%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.43% | **+0.64%** |
| LIMIT_5PCT | 4/20 | 20.0% | +2.71% | **+0.54%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.04% | **+0.03%** |
| LIMIT_4PCT | 10/20 | 50.0% | +0.00% | **+0.00%** |
| MARKET | 20/20 | 100.0% | -0.08% | **-0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.22% | **+0.91%** |
| MARKET_LONG | 20/20 | 100.0% | +0.88% | **+0.88%** |
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +1.10% | **+0.83%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +0.30% | **+0.15%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 201件 (TP 75 / SL 121 / EXP 5)
- 最新: UAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$859.66** / 初期 $100.00 (+759.66%)
- 確定: 5011件 (Win 1516 / Loss 1644 / Flat 1851) / skip 5195件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASECAT/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $859.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$185.38** / 初期 $100.00 (+85.38%)
- 確定: 2420件 (Win 682 / Loss 577 / Flat 1161) / skip 4636件
- 成長率目線: 平均log +0.000255 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: USELESS/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $185.38

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.96** / 初期 $100.00 (+16.96%)
- 確定: 2287件 (Win 676 / Loss 880 / Flat 731) / pending 6件 / skip 2831件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000162 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: 4/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $116.96

## 6. Latest Market Context

- 更新: 2026-09-04T17:01:15.477301+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=79687.4
- Funnel: target 1050 → liquid 164 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| 4/USDT:USDT | +18.40% | $1,240,880.97 |
| UAI/USDT:USDT | +12.19% | $5,612,196.85 |
| BONER/USDT:USDT | +8.83% | $1,951,555.24 |
| SKR/USDT:USDT | +8.62% | $6,473,695.28 |
| TUT/USDT:USDT | +5.54% | $1,331,967.45 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +2.10% | +2.12% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +1.28% | +1.31% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +1.28% | +1.31% |
| MVLL/USDT:USDT | below_1h_threshold | +1.24% | +1.27% |
| MUU/USDT:USDT | below_1h_threshold | +1.23% | +1.26% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
