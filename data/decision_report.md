# Decision Report

- generated_at: 2026-10-30T21:46:13.910278+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17867**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.91% / filled 20/20。**
- 全期間 MARKET基準: n=17867, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.91%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.91% | **+0.91%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +5.13% | **+1.54%** |
| MARKET | 20/20 | 100.0% | +0.91% | **+0.91%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.82% | **+0.74%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.85% | **+0.65%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.96% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 19/20 | 95.0% | +2.23% | **+2.11%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +2.50% | **+1.50%** |
| LIMIT_5PCT_LONG | 15/20 | 75.0% | +1.83% | **+1.37%** |
| LIMIT_4PCT_LONG | 16/20 | 80.0% | +1.54% | **+1.23%** |
| LIMIT_ATR_LONG | 17/20 | 85.0% | +0.82% | **+0.70%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 256件 (TP 94 / SL 154 / EXP 8)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,515.94** / 初期 $100.00 (+1415.94%)
- 確定: 6807件 (Win 1975 / Loss 2182 / Flat 2650) / skip 7621件
- 成長率目線: 平均log +0.000399 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIN/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $1,515.94

## 4. Robust Adaptive DryRun ($100)

- 残高: **$363.50** / 初期 $100.00 (+263.50%)
- 確定: 4367件 (Win 1173 / Loss 983 / Flat 2211) / skip 6911件
- 成長率目線: 平均log +0.000296 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0311 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $363.50

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6028件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000235 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-30T21:46:04.017087+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=76816.2
- Funnel: target 1090 → liquid 178 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SOPH/USDT:USDT | +20.36% | $1,157,768.81 |
| IDOL/USDT:USDT | +9.51% | $12,330,641.48 |
| OP/USDT:USDT | +7.54% | $11,392,193.17 |
| AIN/USDT:USDT | +4.90% | $4,379,314.20 |
| PYTH/USDT:USDT | +4.89% | $3,619,897.84 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIN/USDT:USDT | below_1h_threshold | +3.87% | +3.96% |
| PYTH/USDT:USDT | below_1h_threshold | +3.05% | +3.15% |
| SOPH/USDT:USDT | below_1h_threshold | +1.96% | +2.05% |
| RSR/USDT:USDT | below_1h_threshold | +1.80% | +1.90% |
| ONDO/USDT:USDT | below_1h_threshold | +1.77% | +1.87% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
