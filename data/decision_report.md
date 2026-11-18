# Decision Report

- generated_at: 2026-11-18T01:41:34.775912+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19107**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19107, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.70%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.70% | **-0.70%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.93% | **+0.46%** |
| LIMIT_BB3S | 3/19 | 15.8% | +2.34% | **+0.37%** |
| LIMIT_5PCT | 5/20 | 25.0% | +1.37% | **+0.34%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.13% | **+0.11%** |
| LIMIT_1PCT | 20/20 | 100.0% | -0.19% | **-0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.03% | **+0.91%** |
| MARKET_LONG | 20/20 | 100.0% | +0.84% | **+0.84%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.22% | **+0.73%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +1.98% | **+0.69%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +1.64% | **+0.66%** |

## 2. $100 Live Portfolio

- 残高: **$120.76** / 初期 $100.00 (+20.76%)
- 確定トレード: 280件 (TP 100 / SL 172 / EXP 8)
- 最新: MVLL/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.76
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,677.36** / 初期 $100.00 (+1577.36%)
- 確定: 7352件 (Win 2109 / Loss 2358 / Flat 2885) / skip 8316件
- 成長率目線: 平均log +0.000384 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PENGU/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,677.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$431.95** / 初期 $100.00 (+331.95%)
- 確定: 4997件 (Win 1333 / Loss 1084 / Flat 2580) / skip 7521件
- 成長率目線: 平均log +0.000293 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BREV/USDT:USDT `LIMIT_FIB1272` TP_HIT account +0.69% 残高後 $431.95

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7271件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000028 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-18T01:41:20.792642+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.53% price=64424.0
- Funnel: target 1073 → liquid 143 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BREV/USDT:USDT | +28.96% | $9,874,806.72 |
| ICNT/USDT:USDT | +17.25% | $1,189,521.92 |
| MUU/USDT:USDT | +13.92% | $36,391,321.15 |
| SNXX/USDT:USDT | +13.34% | $48,181,725.44 |
| MMT/USDT:USDT | +12.81% | $2,088,060.17 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CSOPSKHYNIX2L/USDT:USDT | below_1h_threshold | +2.61% | +3.15% |
| LONGXIA/USDT:USDT | below_1h_threshold | +2.40% | +2.93% |
| MURATASTOCK/USDT:USDT | below_1h_threshold | +2.12% | +2.65% |
| ARIA/USDT:USDT | below_1h_threshold | +1.86% | +2.39% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +1.80% | +2.33% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
