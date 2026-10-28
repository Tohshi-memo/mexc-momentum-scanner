# Decision Report

- generated_at: 2026-10-28T00:31:37.785354+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17654**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17654, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.31%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.31% | **-0.31%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 16/20 | 80.0% | +1.45% | **+1.16%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.25% | **+0.44%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +2.34% | **+1.52%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +2.25% | **+1.35%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +3.55% | **+1.24%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.30% | **+0.91%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.07% | **+0.83%** |

## 2. $100 Live Portfolio

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定トレード: 255件 (TP 94 / SL 153 / EXP 8)
- 最新: BTW/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.62
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,532.91** / 初期 $100.00 (+1432.91%)
- 確定: 6760件 (Win 1968 / Loss 2170 / Flat 2622) / skip 7455件
- 成長率目線: 平均log +0.000404 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BULLA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,532.91

## 4. Robust Adaptive DryRun ($100)

- 残高: **$351.13** / 初期 $100.00 (+251.13%)
- 確定: 4183件 (Win 1141 / Loss 965 / Flat 2077) / skip 6882件
- 成長率目線: 平均log +0.000300 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.1249 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DOOD/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $351.13

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5817件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000424 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-28T00:31:17.831983+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=80746.0
- Funnel: target 1083 → liquid 160 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +57.54% | $3,684,258.11 |
| SI/USDT:USDT | +40.22% | $1,065,317.36 |
| BULLA/USDT:USDT | +29.41% | $10,159,549.24 |
| APR/USDT:USDT | +17.83% | $4,808,037.42 |
| BTW/USDT:USDT | +13.28% | $15,127,053.32 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MUU/USDT:USDT | below_1h_threshold | +3.33% | +3.48% |
| PONS/USDT:USDT | below_1h_threshold | +3.18% | +3.33% |
| SI/USDT:USDT | below_1h_threshold | +2.70% | +2.85% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +2.42% | +2.57% |
| BANK/USDT:USDT | below_1h_threshold | +1.52% | +1.68% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
