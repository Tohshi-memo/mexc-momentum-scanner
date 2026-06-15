# Decision Report

- generated_at: 2026-06-15T10:10:07.418853+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6771**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6771, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.70% | **+0.21%** |
| LIMIT_10PCT | 2/20 | 10.0% | +0.73% | **+0.07%** |
| LIMIT_4PCT | 16/20 | 80.0% | -0.00% | **-0.00%** |
| LIMIT_BB3S | 6/17 | 35.3% | -0.03% | **-0.01%** |
| LIMIT_5PCT | 9/20 | 45.0% | -0.15% | **-0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.20% | **+1.65%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.84% | **+1.47%** |
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.84% | **+0.92%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$103.02** / 初期 $100.00 (+3.02%)
- 確定トレード: 6件 (TP 4 / SL 2 / EXP 0)
- 最新: RIF/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.02
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$176.27** / 初期 $100.00 (+76.27%)
- 確定: 1644件 (Win 429 / Loss 508 / Flat 707) / skip 1688件
- 成長率目線: 平均log +0.000345 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SIREN/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $176.27

## 4. Robust Adaptive DryRun ($100)

- 残高: **$99.15** / 初期 $100.00 (-0.85%)
- 確定: 138件 (Win 27 / Loss 23 / Flat 88) / skip 44件
- 成長率目線: 平均log -0.000062 / 幾何平均 -0.006% per trade / maxDD +2.07%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_robust_growth_score) / robust_score -0.0080 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SIREN/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account -0.13% 残高後 $99.15

## 5. Latest Market Context

- 更新: 2026-06-15T10:10:04.103843+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.17% price=65668.9
- Funnel: target 770 → liquid 143 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +91.50% | $26,975,353.51 |
| ASTEROID/USDT:USDT | +78.32% | $4,543,909.32 |
| CLO/USDT:USDT | +44.15% | $2,235,322.86 |
| H/USDT:USDT | +41.81% | $140,143,883.99 |
| PUFFER/USDT:USDT | +32.89% | $1,440,989.97 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIL/USDT:USDT | below_1h_threshold | +2.72% | +2.56% |
| BABY/USDT:USDT | below_1h_threshold | +2.63% | +2.46% |
| EIGEN/USDT:USDT | below_1h_threshold | +2.29% | +2.12% |
| AAVE/USDT:USDT | below_1h_threshold | +0.97% | +0.80% |
| FHE/USDT:USDT | below_1h_threshold | +0.77% | +0.61% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
