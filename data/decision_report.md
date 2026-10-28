# Decision Report

- generated_at: 2026-10-28T00:26:31.423888+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17653**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17653, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.91%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.91% | **-0.91%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 17/20 | 85.0% | +1.84% | **+1.56%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +6.27% | **+1.25%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.86% | **+0.60%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.25% | **+0.44%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +2.34% | **+1.52%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +2.25% | **+1.35%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +3.13% | **+1.10%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.30% | **+0.91%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.07% | **+0.83%** |

## 2. $100 Live Portfolio

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定トレード: 255件 (TP 94 / SL 153 / EXP 8)
- 最新: BTW/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.62
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,532.91** / 初期 $100.00 (+1432.91%)
- 確定: 6760件 (Win 1968 / Loss 2170 / Flat 2622) / skip 7454件
- 成長率目線: 平均log +0.000404 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BULLA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,532.91

## 4. Robust Adaptive DryRun ($100)

- 残高: **$351.13** / 初期 $100.00 (+251.13%)
- 確定: 4182件 (Win 1141 / Loss 965 / Flat 2076) / skip 6882件
- 成長率目線: 平均log +0.000300 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.1305 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SI/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $351.13

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5816件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000432 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-28T00:26:13.872547+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.17% price=80728.5
- Funnel: target 1083 → liquid 160 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +55.46% | $3,644,613.00 |
| SI/USDT:USDT | +42.27% | $1,061,777.75 |
| BULLA/USDT:USDT | +30.19% | $10,145,990.59 |
| APR/USDT:USDT | +17.21% | $4,795,275.65 |
| BTW/USDT:USDT | +13.43% | $15,098,614.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SI/USDT:USDT | below_1h_threshold | +4.12% | +4.30% |
| MUU/USDT:USDT | below_1h_threshold | +3.33% | +3.50% |
| PONS/USDT:USDT | below_1h_threshold | +2.51% | +2.68% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +2.42% | +2.59% |
| BANK/USDT:USDT | below_1h_threshold | +2.06% | +2.24% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
