# Decision Report

- generated_at: 2026-07-21T02:51:34.619863+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9143**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.51% / filled 20/20。**
- 全期間 MARKET基準: n=9143, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.51%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.51% | **+1.51%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.51% | **+1.51%** |
| LIMIT_7PCT | 3/20 | 15.0% | +6.27% | **+0.94%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.02% | **+0.86%** |
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.94% | **+0.70%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +4.18% | **+1.04%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +5.11% | **+1.02%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +1.09% | **+0.98%** |
| LIMIT_3PCT_LONG | 17/20 | 85.0% | +1.13% | **+0.96%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.90% | **+0.85%** |

## 2. $100 Live Portfolio

- 残高: **$108.59** / 初期 $100.00 (+8.59%)
- 確定トレード: 124件 (TP 44 / SL 75 / EXP 5)
- 最新: ZHIPUSTOCK/USDT:USDT SL_HIT PnL -3.93% 残高後 $108.59
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$411.00** / 初期 $100.00 (+311.00%)
- 確定: 3205件 (Win 1004 / Loss 1020 / Flat 1181) / skip 2499件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ERA/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $411.00

## 4. Robust Adaptive DryRun ($100)

- 残高: **$129.13** / 初期 $100.00 (+29.13%)
- 確定: 1104件 (Win 290 / Loss 228 / Flat 586) / skip 1450件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1087 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ERA/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $129.13

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.09** / 初期 $100.00 (+1.09%)
- 確定: 338件 (Win 119 / Loss 150 / Flat 69) / pending 3件 / skip 276件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000223 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ERA/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $101.09

## 6. Latest Market Context

- 更新: 2026-07-21T02:51:23.703174+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.18% price=65324.1
- Funnel: target 885 → liquid 173 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.4 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ERA/USDT:USDT | +59.51% | $1,842,351.71 |
| JIMOTHY/USDT:USDT | +23.45% | $2,821,448.57 |
| AKE/USDT:USDT | +14.09% | $20,046,388.90 |
| BLESS/USDT:USDT | +13.75% | $1,998,548.51 |
| ZHIPUSTOCK/USDT:USDT | +12.61% | $1,138,020.76 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KORU/USDT:USDT | below_1h_threshold | +4.99% | +4.81% |
| BLESS/USDT:USDT | below_1h_threshold | +2.55% | +2.37% |
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +2.41% | +2.23% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +2.01% | +1.83% |
| EWY/USDT:USDT | below_1h_threshold | +1.68% | +1.50% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
