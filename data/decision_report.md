# Decision Report

- generated_at: 2026-11-23T15:17:20.022094+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19499**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19499, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.34% | **-0.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 18/20 | 90.0% | +0.83% | **+0.75%** |
| LIMIT_ATR | 19/20 | 95.0% | +0.38% | **+0.36%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.12% | **+0.08%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | -0.14% | **-0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.91% | **+0.81%** |
| MARKET_LONG | 20/20 | 100.0% | +0.69% | **+0.69%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +0.93% | **+0.37%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +0.42% | **+0.25%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.35% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 285件 (TP 103 / SL 174 / EXP 8)
- 最新: BLESS/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$2,020.57** / 初期 $100.00 (+1920.57%)
- 確定: 7587件 (Win 2185 / Loss 2434 / Flat 2968) / skip 8473件
- 成長率目線: 平均log +0.000396 / 幾何平均 +0.040% per trade / maxDD +9.04%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ELSA/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $2,020.57

## 4. Robust Adaptive DryRun ($100)

- 残高: **$467.69** / 初期 $100.00 (+367.69%)
- 確定: 5219件 (Win 1389 / Loss 1123 / Flat 2707) / skip 7691件
- 成長率目線: 平均log +0.000296 / 幾何平均 +0.030% per trade / maxDD +4.29%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0932 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SKHYSTOCK/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.10% 残高後 $467.69

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7681件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000663 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-23T15:16:59.668501+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.20% price=62989.6
- Funnel: target 1088 → liquid 140 → pre 50 → checked 50 → surge 11 → strict 1
- Surge前reject: below_1h_threshold=39, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.8 >= 65=2, 4h RSI 76.9 >= 65=1, 4h RSI 68.7 >= 65=1, 4h RSI 75.5 >= 65=1, 4h RSI 69.9 >= 65=1, 4h RSI 70.4 >= 65=1, 4h RSI 66.6 >= 65=1, 4h RSI 65.9 >= 65=1, 4h RSI 79.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SI/USDT:USDT | +97.42% | $2,763,706.63 |
| NVDL/USDT:USDT | +48.94% | $6,142,093.33 |
| PROM/USDT:USDT | +46.35% | $1,763,148.09 |
| MVLL/USDT:USDT | +30.38% | $1,605,933.55 |
| ELSA/USDT:USDT | +29.81% | $2,775,439.98 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TSMSTOCK/USDT:USDT | below_1h_threshold | +4.99% | +4.79% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +4.89% | +4.69% |
| ARIA/USDT:USDT | below_1h_threshold | +4.77% | +4.57% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +4.63% | +4.43% |
| KORU/USDT:USDT | below_1h_threshold | +4.45% | +4.25% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
