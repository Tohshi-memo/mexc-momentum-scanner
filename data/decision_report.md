# Decision Report

- generated_at: 2026-07-20T23:06:17.652110+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9132**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9132, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.55%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.55% | **-0.55%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.03% | **+0.02%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.00% | **+0.00%** |
| LIMIT_BB3S | 2/15 | 13.3% | -0.79% | **-0.11%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | -0.75% | **-0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.81% | **+1.18%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.35% | **+0.95%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.93% | **+0.83%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.17% | **+0.70%** |
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +0.52% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$109.14** / 初期 $100.00 (+9.14%)
- 確定トレード: 123件 (TP 44 / SL 74 / EXP 5)
- 最新: US/USDT:USDT TP_HIT PnL +8.00% 残高後 $109.14
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$405.95** / 初期 $100.00 (+305.95%)
- 確定: 3194件 (Win 999 / Loss 1014 / Flat 1181) / skip 2499件
- 成長率目線: 平均log +0.000439 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MVLL/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $405.95

## 4. Robust Adaptive DryRun ($100)

- 残高: **$128.10** / 初期 $100.00 (+28.10%)
- 確定: 1093件 (Win 285 / Loss 222 / Flat 586) / skip 1450件
- 成長率目線: 平均log +0.000227 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1134 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MVLL/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $128.10

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.81** / 初期 $100.00 (+1.81%)
- 確定: 330件 (Win 117 / Loss 144 / Flat 69) / pending 4件 / skip 270件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000325 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MVLL/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $101.81

## 6. Latest Market Context

- 更新: 2026-07-20T23:06:11.088493+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=65147.5
- Funnel: target 885 → liquid 168 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +44.17% | $2,488,634.02 |
| HEMI/USDT:USDT | +23.51% | $2,625,221.13 |
| BLESS/USDT:USDT | +8.96% | $1,326,453.18 |
| BULLA/USDT:USDT | +8.27% | $1,018,677.58 |
| ON/USDT:USDT | +7.30% | $1,465,876.22 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXS/USDT:USDT | below_1h_threshold | +1.08% | +1.03% |
| ALLO/USDT:USDT | below_1h_threshold | +1.04% | +1.00% |
| HEMI/USDT:USDT | below_1h_threshold | +0.89% | +0.84% |
| 1000BONK/USDT:USDT | below_1h_threshold | +0.60% | +0.55% |
| WLD/USDT:USDT | below_1h_threshold | +0.56% | +0.52% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
