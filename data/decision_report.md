# Decision Report

- generated_at: 2026-11-10T08:11:25.069819+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18587**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18587, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.60% | **-0.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.76% | **+0.79%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.01% | **+0.40%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.29% | **+1.29%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.77% | **+0.88%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.03% | **+0.82%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +1.17% | **+0.65%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.08% | **+0.54%** |

## 2. $100 Live Portfolio

- 残高: **$121.13** / 初期 $100.00 (+21.13%)
- 確定トレード: 268件 (TP 97 / SL 163 / EXP 8)
- 最新: CRWVSTOCK/USDT:USDT SL_HIT PnL -2.78% 残高後 $121.13
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,673.83** / 初期 $100.00 (+1573.83%)
- 確定: 7184件 (Win 2066 / Loss 2292 / Flat 2826) / skip 7964件
- 成長率目線: 平均log +0.000392 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ONE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $1,673.83

## 4. Robust Adaptive DryRun ($100)

- 残高: **$387.85** / 初期 $100.00 (+287.85%)
- 確定: 4758件 (Win 1277 / Loss 1048 / Flat 2433) / skip 7240件
- 成長率目線: 平均log +0.000285 / 幾何平均 +0.028% per trade / maxDD +4.29%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1015 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: INIT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $387.85

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6747件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000402 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-10T08:11:11.931871+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=74800.0
- Funnel: target 1094 → liquid 146 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| INIT/USDT:USDT | +66.83% | $11,575,964.31 |
| ON/USDT:USDT | +25.00% | $5,781,438.52 |
| NIUBI/USDT:USDT | +18.88% | $2,265,194.84 |
| ARIA/USDT:USDT | +11.33% | $1,142,276.57 |
| ZHIPUSTOCK/USDT:USDT | +9.61% | $1,534,545.35 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXL/USDT:USDT | below_1h_threshold | +0.68% | +0.68% |
| NVIDIA/USDT:USDT | below_1h_threshold | +0.60% | +0.61% |
| BR/USDT:USDT | below_1h_threshold | +0.45% | +0.45% |
| KORU/USDT:USDT | below_1h_threshold | +0.39% | +0.40% |
| XPT/USDT:USDT | below_1h_threshold | +0.36% | +0.36% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
