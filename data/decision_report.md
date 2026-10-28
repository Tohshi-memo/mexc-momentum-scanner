# Decision Report

- generated_at: 2026-10-28T00:16:19.873697+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17651**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17651, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.91%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.91% | **-0.91%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 17/20 | 85.0% | +1.66% | **+1.41%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +3.45% | **+1.03%** |
| LIMIT_7PCT | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.96% | **+0.59%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.57% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +1.41% | **+0.92%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +2.24% | **+0.90%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +1.25% | **+0.75%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.40% | **+0.63%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.11% | **+0.61%** |

## 2. $100 Live Portfolio

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定トレード: 255件 (TP 94 / SL 153 / EXP 8)
- 最新: BTW/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.62
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,540.62** / 初期 $100.00 (+1440.62%)
- 確定: 6759件 (Win 1968 / Loss 2169 / Flat 2622) / skip 7453件
- 成長率目線: 平均log +0.000405 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EVAA/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $1,540.62

## 4. Robust Adaptive DryRun ($100)

- 残高: **$351.13** / 初期 $100.00 (+251.13%)
- 確定: 4180件 (Win 1141 / Loss 965 / Flat 2074) / skip 6882件
- 成長率目線: 平均log +0.000300 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.1252 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $351.13

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5813件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000403 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-28T00:16:07.045999+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=80750.3
- Funnel: target 1083 → liquid 160 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +57.44% | $3,530,159.08 |
| SI/USDT:USDT | +40.02% | $1,052,460.56 |
| BULLA/USDT:USDT | +25.97% | $10,101,096.95 |
| APR/USDT:USDT | +15.93% | $4,761,356.84 |
| BTW/USDT:USDT | +14.31% | $15,016,749.27 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DOOD/USDT:USDT | below_1h_threshold | +4.72% | +4.87% |
| BULLA/USDT:USDT | below_1h_threshold | +3.59% | +3.74% |
| MUU/USDT:USDT | below_1h_threshold | +3.33% | +3.47% |
| SI/USDT:USDT | below_1h_threshold | +2.55% | +2.69% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +2.42% | +2.56% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
