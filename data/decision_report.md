# Decision Report

- generated_at: 2026-10-30T22:51:24.588111+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17868**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.31% / filled 20/20。**
- 全期間 MARKET基準: n=17868, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.31%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.31% | **+0.31%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +5.13% | **+1.54%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.85% | **+0.65%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.96% | **+0.59%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.81% | **+0.53%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 18/20 | 90.0% | +2.57% | **+2.31%** |
| LIMIT_5PCT_LONG | 14/20 | 70.0% | +2.18% | **+1.53%** |
| LIMIT_4PCT_LONG | 15/20 | 75.0% | +1.91% | **+1.43%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +2.00% | **+1.10%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +1.12% | **+0.90%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 256件 (TP 94 / SL 154 / EXP 8)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,515.94** / 初期 $100.00 (+1415.94%)
- 確定: 6807件 (Win 1975 / Loss 2182 / Flat 2650) / skip 7622件
- 成長率目線: 平均log +0.000399 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIN/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $1,515.94

## 4. Robust Adaptive DryRun ($100)

- 残高: **$363.50** / 初期 $100.00 (+263.50%)
- 確定: 4368件 (Win 1173 / Loss 983 / Flat 2212) / skip 6911件
- 成長率目線: 平均log +0.000295 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0311 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: IDOL/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $363.50

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6030件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000235 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-30T22:51:11.506100+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.37% price=76953.1
- Funnel: target 1090 → liquid 177 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SOPH/USDT:USDT | +27.92% | $1,265,262.18 |
| IDOL/USDT:USDT | +17.90% | $12,852,703.35 |
| OP/USDT:USDT | +8.23% | $11,763,157.70 |
| PYTH/USDT:USDT | +6.96% | $3,502,550.90 |
| AIN/USDT:USDT | +6.11% | $4,415,670.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| Q/USDT:USDT | below_1h_threshold | +4.73% | +4.36% |
| ETHFI/USDT:USDT | below_1h_threshold | +3.34% | +2.97% |
| TIA/USDT:USDT | below_1h_threshold | +2.35% | +1.99% |
| JTO/USDT:USDT | below_1h_threshold | +2.01% | +1.64% |
| PYTH/USDT:USDT | below_1h_threshold | +1.88% | +1.51% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
