# Decision Report

- generated_at: 2026-11-23T15:37:23.919113+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19506**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19506, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.24% | **-0.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 17/20 | 85.0% | +0.85% | **+0.72%** |
| LIMIT_ATR | 18/20 | 90.0% | +0.35% | **+0.32%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.31% | **+0.30%** |
| LIMIT_5PCT | 2/20 | 10.0% | +0.95% | **+0.10%** |
| LIMIT_4PCT | 10/20 | 50.0% | +0.04% | **+0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.59% | **+1.03%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +1.23% | **+0.74%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.76% | **+0.53%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +0.83% | **+0.33%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.28% | **+0.26%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 285件 (TP 103 / SL 174 / EXP 8)
- 最新: BLESS/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$2,020.57** / 初期 $100.00 (+1920.57%)
- 確定: 7587件 (Win 2185 / Loss 2434 / Flat 2968) / skip 8480件
- 成長率目線: 平均log +0.000396 / 幾何平均 +0.040% per trade / maxDD +9.04%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ELSA/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $2,020.57

## 4. Robust Adaptive DryRun ($100)

- 残高: **$467.69** / 初期 $100.00 (+367.69%)
- 確定: 5219件 (Win 1389 / Loss 1123 / Flat 2707) / skip 7698件
- 成長率目線: 平均log +0.000296 / 幾何平均 +0.030% per trade / maxDD +4.29%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0789 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SKHYSTOCK/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.10% 残高後 $467.69

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7685件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000517 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-23T15:36:56.369739+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.39% price=63109.3
- Funnel: target 1088 → liquid 143 → pre 50 → checked 50 → surge 13 → strict 1
- Surge前reject: below_1h_threshold=37, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.2 >= 65=1, 4h RSI 77.8 >= 65=1, 4h RSI 68.4 >= 65=1, 4h RSI 76.2 >= 65=1, 4h RSI 69.6 >= 65=1, 4h RSI 71.7 >= 65=1, 4h RSI 73.1 >= 65=1, 4h RSI 75.4 >= 65=1, 4h RSI 71.0 >= 65=1, 4h RSI 68.7 >= 65=1, 4h RSI 67.8 >= 65=1, 4h RSI 80.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SI/USDT:USDT | +87.70% | $2,800,134.82 |
| NVDL/USDT:USDT | +51.66% | $6,324,432.38 |
| PROM/USDT:USDT | +45.40% | $1,946,203.61 |
| MVLL/USDT:USDT | +31.59% | $1,766,525.99 |
| ELSA/USDT:USDT | +31.57% | $2,839,579.43 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TSMSTOCK/USDT:USDT | below_1h_threshold | +4.99% | +4.60% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +4.89% | +4.50% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +4.63% | +4.24% |
| KORU/USDT:USDT | below_1h_threshold | +4.45% | +4.06% |
| MUBARAK/USDT:USDT | below_1h_threshold | +4.16% | +3.77% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
