# Decision Report

- generated_at: 2026-07-23T02:26:22.417922+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9342**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9342, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.14%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.14% | **+0.14%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +6.57% | **+0.99%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.15% | **+0.79%** |
| LIMIT_7PCT | 4/20 | 20.0% | +3.70% | **+0.74%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.16% | **+0.65%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +1.99% | **+1.40%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.10% | **+0.55%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.72% | **+0.51%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.01% | **+0.46%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.54% | **+0.41%** |

## 2. $100 Live Portfolio

- 残高: **$103.79** / 初期 $100.00 (+3.79%)
- 確定トレード: 136件 (TP 45 / SL 86 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -2.63% 残高後 $103.79
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$426.05** / 初期 $100.00 (+326.05%)
- 確定: 3320件 (Win 1048 / Loss 1075 / Flat 1197) / skip 2583件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BANK/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $426.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.36** / 初期 $100.00 (+30.36%)
- 確定: 1161件 (Win 312 / Loss 254 / Flat 595) / skip 1592件
- 成長率目線: 平均log +0.000228 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0524 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $130.36

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.27** / 初期 $100.00 (+1.27%)
- 確定: 428件 (Win 143 / Loss 178 / Flat 107) / pending 0件 / skip 385件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000297 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CBRSSTOCK/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $101.27

## 6. Latest Market Context

- 更新: 2026-07-23T02:26:13.817325+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.18% price=65674.9
- Funnel: target 890 → liquid 179 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.6 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +56.00% | $5,886,455.34 |
| RIF/USDT:USDT | +40.97% | $4,861,423.74 |
| O/USDT:USDT | +29.39% | $4,472,322.35 |
| BANK/USDT:USDT | +28.21% | $108,803,119.61 |
| ZAMA/USDT:USDT | +20.89% | $3,745,314.02 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZAMA/USDT:USDT | below_1h_threshold | +3.51% | +3.69% |
| JIMOTHY/USDT:USDT | below_1h_threshold | +2.11% | +2.29% |
| BANK/USDT:USDT | below_1h_threshold | +2.10% | +2.28% |
| TRIA/USDT:USDT | below_1h_threshold | +1.92% | +2.10% |
| MORPHO/USDT:USDT | below_1h_threshold | +1.84% | +2.02% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
