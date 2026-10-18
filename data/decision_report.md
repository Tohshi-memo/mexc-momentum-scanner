# Decision Report

- generated_at: 2026-10-18T02:06:30.479975+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16933**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.15% / filled 20/20。**
- 全期間 MARKET基準: n=16933, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.15%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.15% | **+1.15%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.15% | **+1.15%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.97% | **+1.04%** |
| LIMIT_3PCT | 15/20 | 75.0% | +1.06% | **+0.80%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.72% | **+0.65%** |
| LIMIT_BB3S | 8/18 | 44.4% | +1.32% | **+0.58%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.40% | **+0.98%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.02% | **+0.81%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +1.00% | **+0.65%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.69% | **+0.38%** |

## 2. $100 Live Portfolio

- 残高: **$121.72** / 初期 $100.00 (+21.72%)
- 確定トレード: 244件 (TP 91 / SL 146 / EXP 7)
- 最新: CLAUDIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.72
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,285.81** / 初期 $100.00 (+1185.81%)
- 確定: 6399件 (Win 1864 / Loss 2047 / Flat 2488) / skip 7095件
- 成長率目線: 平均log +0.000399 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AGT/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.50% 残高後 $1,285.81

## 4. Robust Adaptive DryRun ($100)

- 残高: **$275.45** / 初期 $100.00 (+175.45%)
- 確定: 3698件 (Win 1029 / Loss 879 / Flat 1790) / skip 6646件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0383 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AGT/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $275.45

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5092件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000142 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-18T02:06:15.791285+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=81633.3
- Funnel: target 1084 → liquid 138 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 98.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +37.50% | $15,037,094.23 |
| CLAUDIA/USDT:USDT | +34.32% | $2,061,925.42 |
| BR/USDT:USDT | +27.73% | $10,424,632.12 |
| Q/USDT:USDT | +25.54% | $7,747,790.18 |
| AVA/USDT:USDT | +11.77% | $2,225,390.57 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +2.81% | +2.79% |
| SIREN/USDT:USDT | below_1h_threshold | +0.77% | +0.75% |
| BR/USDT:USDT | below_1h_threshold | +0.63% | +0.61% |
| SOXS/USDT:USDT | below_1h_threshold | +0.59% | +0.58% |
| BAT/USDT:USDT | below_1h_threshold | +0.45% | +0.43% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
