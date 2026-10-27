# Decision Report

- generated_at: 2026-10-27T23:11:23.208561+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17645**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17645, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.64%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.64% | **-0.64%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 17/20 | 85.0% | +1.31% | **+1.11%** |
| LIMIT_5PCT | 9/20 | 45.0% | +2.20% | **+0.99%** |
| LIMIT_4PCT | 14/20 | 70.0% | +1.14% | **+0.80%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.47% | **+0.69%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 9/20 | 45.0% | +3.17% | **+1.43%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.66% | **+0.53%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.70% | **+0.52%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.54% | **+0.24%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.50% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定トレード: 255件 (TP 94 / SL 153 / EXP 8)
- 最新: BTW/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.62
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,571.82** / 初期 $100.00 (+1471.82%)
- 確定: 6753件 (Win 1968 / Loss 2165 / Flat 2620) / skip 7453件
- 成長率目線: 平均log +0.000408 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BULLA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,571.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$347.57** / 初期 $100.00 (+247.57%)
- 確定: 4174件 (Win 1139 / Loss 964 / Flat 2071) / skip 6882件
- 成長率目線: 平均log +0.000298 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1216 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $347.57

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5807件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000414 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-27T23:11:10.617321+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=80854.4
- Funnel: target 1083 → liquid 159 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +31.75% | $2,708,789.14 |
| APR/USDT:USDT | +14.29% | $4,695,505.67 |
| BULLA/USDT:USDT | +13.19% | $9,937,018.04 |
| BTW/USDT:USDT | +12.92% | $14,577,393.29 |
| HAEDAL/USDT:USDT | +9.78% | $1,101,508.12 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JCT/USDT:USDT | below_1h_threshold | +3.41% | +3.43% |
| IRYS/USDT:USDT | below_1h_threshold | +2.14% | +2.16% |
| US/USDT:USDT | below_1h_threshold | +1.37% | +1.40% |
| GRASS/USDT:USDT | below_1h_threshold | +0.78% | +0.80% |
| ZEC/USDT:USDT | below_1h_threshold | +0.55% | +0.58% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
