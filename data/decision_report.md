# Decision Report

- generated_at: 2026-11-22T11:41:34.537286+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19383**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19383, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.28% | **-1.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +3.70% | **+0.74%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.96% | **+0.59%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_9PCT | 2/20 | 10.0% | +0.29% | **+0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +2.84% | **+2.84%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.98% | **+1.39%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +2.45% | **+1.23%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +2.12% | **+0.95%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.96% | **+0.88%** |

## 2. $100 Live Portfolio

- 残高: **$121.37** / 初期 $100.00 (+21.37%)
- 確定トレード: 284件 (TP 103 / SL 173 / EXP 8)
- 最新: MMT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.37
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,782.57** / 初期 $100.00 (+1682.57%)
- 確定: 7493件 (Win 2152 / Loss 2413 / Flat 2928) / skip 8451件
- 成長率目線: 平均log +0.000384 / 幾何平均 +0.038% per trade / maxDD +9.04%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DCTY/USDT:USDT `LIMIT_BB3S` EXPIRED account +0.00% 残高後 $1,782.57

## 4. Robust Adaptive DryRun ($100)

- 残高: **$454.82** / 初期 $100.00 (+354.82%)
- 確定: 5147件 (Win 1371 / Loss 1109 / Flat 2667) / skip 7647件
- 成長率目線: 平均log +0.000294 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0613 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DCTY/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.15% 残高後 $454.82

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7542件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000315 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-22T11:41:14.138864+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.29% price=61018.7
- Funnel: target 1086 → liquid 107 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PIEVERSE/USDT:USDT | +55.63% | $20,154,883.33 |
| CLAUDIA/USDT:USDT | +43.30% | $2,631,977.27 |
| DCTY/USDT:USDT | +27.85% | $1,741,912.86 |
| BLESS/USDT:USDT | +18.82% | $40,191,182.26 |
| VELVET/USDT:USDT | +14.61% | $1,142,815.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIGHT/USDT:USDT | below_1h_threshold | +1.38% | +1.09% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +1.14% | +0.85% |
| INJ/USDT:USDT | below_1h_threshold | +0.55% | +0.26% |
| ZRO/USDT:USDT | below_1h_threshold | +0.54% | +0.25% |
| TESLA/USDT:USDT | below_1h_threshold | +0.51% | +0.22% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
