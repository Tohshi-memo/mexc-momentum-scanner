# Decision Report

- generated_at: 2026-11-10T15:46:59.305605+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18610**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.36% / filled 20/20。**
- 全期間 MARKET基準: n=18610, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.36%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.36% | **+0.36%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 8/20 | 40.0% | +2.27% | **+0.91%** |
| LIMIT_5PCT | 11/20 | 55.0% | +1.14% | **+0.63%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.67% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.86% | **+1.00%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +2.40% | **+0.84%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.89% | **+0.67%** |
| MARKET_LONG | 20/20 | 100.0% | +0.57% | **+0.57%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.66% | **+0.56%** |

## 2. $100 Live Portfolio

- 残高: **$121.13** / 初期 $100.00 (+21.13%)
- 確定トレード: 268件 (TP 97 / SL 163 / EXP 8)
- 最新: CRWVSTOCK/USDT:USDT SL_HIT PnL -2.78% 残高後 $121.13
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,674.39** / 初期 $100.00 (+1574.39%)
- 確定: 7207件 (Win 2073 / Loss 2303 / Flat 2831) / skip 7964件
- 成長率目線: 平均log +0.000391 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SNXX/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $1,674.39

## 4. Robust Adaptive DryRun ($100)

- 残高: **$393.03** / 初期 $100.00 (+293.03%)
- 確定: 4776件 (Win 1283 / Loss 1055 / Flat 2438) / skip 7245件
- 成長率目線: 平均log +0.000287 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0353 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SNXX/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $393.03

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6783件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000215 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-10T15:46:37.541722+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -1.74% price=73081.7
- Funnel: target 1099 → liquid 156 → pre 50 → checked 50 → surge 7 → strict 5
- Surge前reject: below_1h_threshold=43, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.9 >= 65=1, 4h RSI 68.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| INIT/USDT:USDT | +96.57% | $28,662,204.50 |
| ARIA/USDT:USDT | +18.57% | $2,780,005.03 |
| ONE/USDT:USDT | +16.75% | $9,896,491.28 |
| BR/USDT:USDT | +10.79% | $3,915,622.42 |
| ZHIPUSTOCK/USDT:USDT | +10.43% | $1,640,962.73 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +4.86% | +6.60% |
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +4.68% | +6.42% |
| SNOWSTOCK/USDT:USDT | below_1h_threshold | +3.76% | +5.50% |
| TSMSTOCK/USDT:USDT | below_1h_threshold | +3.36% | +5.09% |
| EWY/USDT:USDT | below_1h_threshold | +2.14% | +3.88% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
