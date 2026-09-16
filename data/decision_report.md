# Decision Report

- generated_at: 2026-09-16T23:51:34.436735+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14751**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.70% / filled 20/20。**
- 全期間 MARKET基準: n=14751, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.70%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.70% | **+0.70%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +4.56% | **+1.14%** |
| MARKET | 20/20 | 100.0% | +0.70% | **+0.70%** |
| LIMIT_ATR | 9/20 | 45.0% | +0.81% | **+0.37%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.41% | **+0.31%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.25% | **+0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/7 | 71.4% | +3.23% | **+2.31%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.46% | **+1.09%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +2.47% | **+0.99%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.88% | **+0.94%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.96% | **+0.91%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,165.60** / 初期 $100.00 (+1065.60%)
- 確定: 5600件 (Win 1679 / Loss 1813 / Flat 2108) / skip 5712件
- 成長率目線: 平均log +0.000439 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BRETT/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $1,165.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$240.73** / 初期 $100.00 (+140.73%)
- 確定: 3129件 (Win 870 / Loss 746 / Flat 1513) / skip 5033件
- 成長率目線: 平均log +0.000281 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.1258 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $240.73

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.53** / 初期 $100.00 (+23.53%)
- 確定: 2956件 (Win 878 / Loss 1165 / Flat 913) / pending 0件 / skip 3268件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000320 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CNPY/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $123.53

## 6. Latest Market Context

- 更新: 2026-09-16T23:51:19.031229+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.75% price=76212.8
- Funnel: target 1059 → liquid 155 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ONE/USDT:USDT | +53.58% | $1,152,195.07 |
| BATON/USDT:USDT | +42.82% | $2,293,173.40 |
| HNT/USDT:USDT | +21.75% | $4,762,927.18 |
| BULLA/USDT:USDT | +17.82% | $8,625,000.97 |
| POWER/USDT:USDT | +11.69% | $4,963,955.16 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UNI/USDT:USDT | below_relative_strength | +5.36% | +4.61% |
| ZEC/USDT:USDT | below_1h_threshold | +3.83% | +3.08% |
| CRV/USDT:USDT | below_1h_threshold | +3.71% | +2.97% |
| VVV/USDT:USDT | below_1h_threshold | +3.65% | +2.90% |
| APT/USDT:USDT | below_1h_threshold | +3.65% | +2.90% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
