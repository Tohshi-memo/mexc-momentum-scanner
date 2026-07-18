# Decision Report

- generated_at: 2026-07-18T10:21:18.227400+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8933**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.30% / filled 20/20。**
- 全期間 MARKET基準: n=8933, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.30%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.30% | **+0.30%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/17 | 23.5% | +2.52% | **+0.59%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.98% | **+0.50%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.02% | **+0.46%** |
| MARKET | 20/20 | 100.0% | +0.30% | **+0.30%** |
| LIMIT_FIB1272 | 11/20 | 55.0% | +0.53% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.02% | **+0.61%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.76% | **+0.50%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +2.12% | **+0.42%** |
| MARKET_LONG | 20/20 | 100.0% | +0.32% | **+0.32%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.70% | **+0.25%** |

## 2. $100 Live Portfolio

- 残高: **$110.69** / 初期 $100.00 (+10.69%)
- 確定トレード: 116件 (TP 43 / SL 69 / EXP 4)
- 最新: B/USDT:USDT SL_HIT PnL -3.30% 残高後 $110.69
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$360.57** / 初期 $100.00 (+260.57%)
- 確定: 3048件 (Win 946 / Loss 972 / Flat 1130) / skip 2446件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $360.57

## 4. Robust Adaptive DryRun ($100)

- 残高: **$110.81** / 初期 $100.00 (+10.81%)
- 確定: 894件 (Win 213 / Loss 181 / Flat 500) / skip 1450件
- 成長率目線: 平均log +0.000115 / 幾何平均 +0.011% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0390 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $110.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.59** / 初期 $100.00 (-0.41%)
- 確定: 188件 (Win 60 / Loss 101 / Flat 27) / pending 5件 / skip 212件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000310 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $99.59

## 6. Latest Market Context

- 更新: 2026-07-18T10:21:12.516140+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=63967.4
- Funnel: target 885 → liquid 164 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.8 >= 65=1, 4h RSI 79.9 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +36.88% | $68,056,674.36 |
| TRADOOR/USDT:USDT | +28.89% | $4,269,726.24 |
| B/USDT:USDT | +27.59% | $3,026,457.81 |
| ROAM/USDT:USDT | +15.06% | $1,021,782.06 |
| ESPORTS/USDT:USDT | +13.06% | $14,867,428.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TRADOOR/USDT:USDT | below_1h_threshold | +2.59% | +2.58% |
| BANK/USDT:USDT | below_1h_threshold | +2.52% | +2.52% |
| ROAM/USDT:USDT | below_1h_threshold | +2.07% | +2.06% |
| TRUMPOFFICIAL/USDT:USDT | below_1h_threshold | +1.57% | +1.56% |
| PENGU/USDT:USDT | below_1h_threshold | +1.35% | +1.35% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
