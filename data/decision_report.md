# Decision Report

- generated_at: 2026-10-19T19:31:25.102893+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17024**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17024, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.19% | **-0.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 3/20 | 15.0% | +0.95% | **+0.14%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.02% | **+0.01%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | -0.14% | **-0.05%** |
| LIMIT_BB3S | 2/15 | 13.3% | -0.98% | **-0.13%** |
| MARKET | 20/20 | 100.0% | -0.19% | **-0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/5 | 100.0% | +2.30% | **+2.30%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.61% | **+1.36%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.77% | **+1.24%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.30% | **+0.84%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.30% | **+0.72%** |

## 2. $100 Live Portfolio

- 残高: **$121.48** / 初期 $100.00 (+21.48%)
- 確定トレード: 246件 (TP 91 / SL 148 / EXP 7)
- 最新: ZEREBRO/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.48
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,268.68** / 初期 $100.00 (+1168.68%)
- 確定: 6468件 (Win 1876 / Loss 2065 / Flat 2527) / skip 7117件
- 成長率目線: 平均log +0.000393 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CLAUDIA/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,268.68

## 4. Robust Adaptive DryRun ($100)

- 残高: **$277.45** / 初期 $100.00 (+177.45%)
- 確定: 3789件 (Win 1042 / Loss 886 / Flat 1861) / skip 6646件
- 成長率目線: 平均log +0.000269 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0000 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CLAUDIA/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $277.45

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5188件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000257 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-19T19:31:12.979414+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=81933.5
- Funnel: target 1090 → liquid 176 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PHA/USDT:USDT | +23.64% | $3,862,975.77 |
| Q/USDT:USDT | +13.70% | $13,311,046.71 |
| APR/USDT:USDT | +13.56% | $1,522,703.03 |
| BTW/USDT:USDT | +11.61% | $27,185,247.09 |
| BR/USDT:USDT | +8.99% | $30,724,907.93 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RLC/USDT:USDT | below_1h_threshold | +1.60% | +1.59% |
| AGT/USDT:USDT | below_1h_threshold | +1.29% | +1.28% |
| APR/USDT:USDT | below_1h_threshold | +1.26% | +1.25% |
| SPX/USDT:USDT | below_1h_threshold | +1.25% | +1.24% |
| LONGXIA/USDT:USDT | below_1h_threshold | +1.22% | +1.21% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
