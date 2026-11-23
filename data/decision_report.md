# Decision Report

- generated_at: 2026-11-23T14:47:41.509645+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19487**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19487, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-2.71%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.71% | **-2.71%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.22% | **+0.13%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.27% | **+0.11%** |
| LIMIT_3PCT | 15/20 | 75.0% | -0.07% | **-0.05%** |
| LIMIT_2PCT | 20/20 | 100.0% | -0.79% | **-0.79%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.91% | **+2.91%** |
| LIMIT_1PCT_LONG | 11/20 | 55.0% | +3.89% | **+2.14%** |
| LIMIT_BB3S_LONG | 9/14 | 64.3% | +2.45% | **+1.58%** |
| LIMIT_ATR_LONG | 7/20 | 35.0% | +3.48% | **+1.22%** |
| LIMIT_2PCT_LONG | 5/20 | 25.0% | +4.58% | **+1.14%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 285件 (TP 103 / SL 174 / EXP 8)
- 最新: BLESS/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$2,061.50** / 初期 $100.00 (+1961.50%)
- 確定: 7583件 (Win 2185 / Loss 2430 / Flat 2968) / skip 8465件
- 成長率目線: 平均log +0.000399 / 幾何平均 +0.040% per trade / maxDD +9.04%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NVDL/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $2,061.50

## 4. Robust Adaptive DryRun ($100)

- 残高: **$467.69** / 初期 $100.00 (+367.69%)
- 確定: 5219件 (Win 1389 / Loss 1123 / Flat 2707) / skip 7679件
- 成長率目線: 平均log +0.000296 / 幾何平均 +0.030% per trade / maxDD +4.29%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1203 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SKHYSTOCK/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.10% 残高後 $467.69

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7666件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000744 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-23T14:47:02.458551+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.92% price=63263.2
- Funnel: target 1088 → liquid 136 → pre 50 → checked 50 → surge 18 → strict 9
- Surge前reject: below_1h_threshold=32, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.1 >= 65=2, 4h RSI 74.5 >= 65=1, 4h RSI 69.1 >= 65=1, 4h RSI 77.5 >= 65=1, 4h RSI 73.0 >= 65=1, 4h RSI 67.7 >= 65=1, 4h RSI 70.0 >= 65=1, 4h RSI 65.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SI/USDT:USDT | +105.34% | $2,713,619.95 |
| PROM/USDT:USDT | +47.63% | $1,439,518.86 |
| NVDL/USDT:USDT | +42.89% | $5,734,410.33 |
| ELSA/USDT:USDT | +28.93% | $2,763,554.86 |
| EVAA/USDT:USDT | +25.55% | $38,677,251.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +4.74% | +5.66% |
| LIT/USDT:USDT | below_1h_threshold | +4.66% | +5.57% |
| UNI/USDT:USDT | below_1h_threshold | +4.11% | +5.03% |
| TSMSTOCK/USDT:USDT | below_1h_threshold | +3.99% | +4.90% |
| INJ/USDT:USDT | below_1h_threshold | +3.78% | +4.69% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
