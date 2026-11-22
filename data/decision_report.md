# Decision Report

- generated_at: 2026-11-22T10:56:17.102070+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19380**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19380, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.68%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.68% | **-0.68%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +3.70% | **+0.74%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.98% | **+0.49%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_BB3S | 9/18 | 50.0% | +0.71% | **+0.35%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +6.26% | **+6.26%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.56% | **+1.28%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.87% | **+1.03%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +2.02% | **+0.91%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.20% | **+0.88%** |

## 2. $100 Live Portfolio

- 残高: **$121.37** / 初期 $100.00 (+21.37%)
- 確定トレード: 284件 (TP 103 / SL 173 / EXP 8)
- 最新: MMT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.37
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,800.53** / 初期 $100.00 (+1700.53%)
- 確定: 7490件 (Win 2152 / Loss 2411 / Flat 2927) / skip 8451件
- 成長率目線: 平均log +0.000386 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DCTY/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $1,800.53

## 4. Robust Adaptive DryRun ($100)

- 残高: **$457.33** / 初期 $100.00 (+357.33%)
- 確定: 5144件 (Win 1370 / Loss 1107 / Flat 2667) / skip 7647件
- 成長率目線: 平均log +0.000296 / 幾何平均 +0.030% per trade / maxDD +4.29%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0613 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DCTY/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.52% 残高後 $457.33

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7539件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000350 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-22T10:56:04.046251+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=61057.2
- Funnel: target 1086 → liquid 107 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PIEVERSE/USDT:USDT | +54.69% | $18,189,948.57 |
| CLAUDIA/USDT:USDT | +44.71% | $2,603,564.09 |
| VELVET/USDT:USDT | +18.54% | $1,099,938.96 |
| DCTY/USDT:USDT | +13.78% | $1,724,667.79 |
| BLESS/USDT:USDT | +12.54% | $45,601,581.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VELVET/USDT:USDT | below_1h_threshold | +3.19% | +3.26% |
| ETHFI/USDT:USDT | below_1h_threshold | +3.12% | +3.19% |
| TIA/USDT:USDT | below_1h_threshold | +2.48% | +2.55% |
| JUP/USDT:USDT | below_1h_threshold | +2.46% | +2.53% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +2.29% | +2.36% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
