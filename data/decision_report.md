# Decision Report

- generated_at: 2026-11-23T15:22:17.359521+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19500**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19500, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.27%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.27% | **-0.27%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 18/20 | 90.0% | +0.91% | **+0.82%** |
| LIMIT_ATR | 19/20 | 95.0% | +0.50% | **+0.48%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.13% | **+0.08%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | -0.06% | **-0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.48% | **+0.44%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +0.93% | **+0.37%** |
| MARKET_LONG | 20/20 | 100.0% | +0.36% | **+0.36%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.35% | **+0.20%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +0.36% | **+0.18%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 285件 (TP 103 / SL 174 / EXP 8)
- 最新: BLESS/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$2,020.57** / 初期 $100.00 (+1920.57%)
- 確定: 7587件 (Win 2185 / Loss 2434 / Flat 2968) / skip 8474件
- 成長率目線: 平均log +0.000396 / 幾何平均 +0.040% per trade / maxDD +9.04%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ELSA/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $2,020.57

## 4. Robust Adaptive DryRun ($100)

- 残高: **$467.69** / 初期 $100.00 (+367.69%)
- 確定: 5219件 (Win 1389 / Loss 1123 / Flat 2707) / skip 7692件
- 成長率目線: 平均log +0.000296 / 幾何平均 +0.030% per trade / maxDD +4.29%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0901 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SKHYSTOCK/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.10% 残高後 $467.69

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7681件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000624 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-23T15:21:58.907347+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.56% price=63214.0
- Funnel: target 1088 → liquid 141 → pre 50 → checked 50 → surge 11 → strict 1
- Surge前reject: below_1h_threshold=37, below_relative_strength=2, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.1 >= 65=1, 4h RSI 78.5 >= 65=1, 4h RSI 69.9 >= 65=1, 4h RSI 76.8 >= 65=1, 4h RSI 69.0 >= 65=1, 4h RSI 72.2 >= 65=1, 4h RSI 75.6 >= 65=1, 4h RSI 71.6 >= 65=1, 4h RSI 68.1 >= 65=1, 4h RSI 67.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SI/USDT:USDT | +96.28% | $2,768,460.42 |
| NVDL/USDT:USDT | +53.33% | $6,180,554.76 |
| PROM/USDT:USDT | +48.15% | $1,846,624.61 |
| ELSA/USDT:USDT | +33.46% | $2,804,430.46 |
| MVLL/USDT:USDT | +32.07% | $1,640,311.40 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NVIDIA/USDT:USDT | below_relative_strength | +5.50% | +4.94% |
| ELSA/USDT:USDT | below_relative_strength | +5.43% | +4.87% |
| TSMSTOCK/USDT:USDT | below_1h_threshold | +4.99% | +4.43% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +4.89% | +4.34% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +4.63% | +4.08% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
