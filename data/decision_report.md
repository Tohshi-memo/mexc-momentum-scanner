# Decision Report

- generated_at: 2026-09-17T01:36:30.122140+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14761**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.63% / filled 20/20。**
- 全期間 MARKET基準: n=14761, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.63%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.63% | **+0.63%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +3.70% | **+0.74%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.70% | **+0.63%** |
| MARKET | 20/20 | 100.0% | +0.63% | **+0.63%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.88% | **+0.61%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.60% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +2.07% | **+1.24%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.55% | **+1.16%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.23% | **+1.04%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +3.32% | **+0.83%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.95% | **+0.78%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,165.60** / 初期 $100.00 (+1065.60%)
- 確定: 5600件 (Win 1679 / Loss 1813 / Flat 2108) / skip 5722件
- 成長率目線: 平均log +0.000439 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BRETT/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $1,165.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$240.73** / 初期 $100.00 (+140.73%)
- 確定: 3129件 (Win 870 / Loss 746 / Flat 1513) / skip 5043件
- 成長率目線: 平均log +0.000281 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.1167 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $240.73

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.53** / 初期 $100.00 (+23.53%)
- 確定: 2956件 (Win 878 / Loss 1165 / Flat 913) / pending 0件 / skip 3275件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000279 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CNPY/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $123.53

## 6. Latest Market Context

- 更新: 2026-09-17T01:36:16.485118+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.36% price=76579.7
- Funnel: target 1059 → liquid 158 → pre 50 → checked 49 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=1
- Strict後reject: 4h RSI 65.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ONE/USDT:USDT | +55.11% | $2,385,360.89 |
| BATON/USDT:USDT | +49.02% | $2,308,067.73 |
| BULLA/USDT:USDT | +20.88% | $9,100,831.31 |
| MARSCOIN/USDT:USDT | +17.81% | $2,401,087.70 |
| HNT/USDT:USDT | +17.79% | $5,377,820.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VVV/USDT:USDT | below_1h_threshold | +2.94% | +2.58% |
| UNI/USDT:USDT | below_1h_threshold | +2.94% | +2.58% |
| ONE/USDT:USDT | below_1h_threshold | +2.89% | +2.53% |
| BR/USDT:USDT | below_1h_threshold | +2.68% | +2.32% |
| PONS/USDT:USDT | below_1h_threshold | +2.56% | +2.20% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
