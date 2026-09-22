# Decision Report

- generated_at: 2026-09-22T14:36:46.174809+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15334**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.06% / filled 20/20。**
- 全期間 MARKET基準: n=15334, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.06% | **+2.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.06% | **+2.06%** |
| LIMIT_1PCT | 19/20 | 95.0% | +2.12% | **+2.02%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.39% | **+0.97%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.43% | **+0.93%** |
| LIMIT_4PCT | 10/20 | 50.0% | +0.91% | **+0.46%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.41% | **+0.20%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -0.89% | **-0.09%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -0.60% | **-0.09%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -1.32% | **-0.20%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | -0.78% | **-0.43%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,169.49** / 初期 $100.00 (+1069.49%)
- 確定: 5821件 (Win 1727 / Loss 1873 / Flat 2221) / skip 6074件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,169.49

## 4. Robust Adaptive DryRun ($100)

- 残高: **$249.51** / 初期 $100.00 (+149.51%)
- 確定: 3353件 (Win 926 / Loss 781 / Flat 1646) / skip 5392件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KERNEL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $249.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.55** / 初期 $100.00 (+22.55%)
- 確定: 3104件 (Win 911 / Loss 1216 / Flat 977) / pending 5件 / skip 3703件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000137 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: UNI/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $122.55

## 6. Latest Market Context

- 更新: 2026-09-22T14:36:29.853603+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.84% price=85577.0
- Funnel: target 1058 → liquid 181 → pre 50 → checked 50 → surge 7 → strict 0
- Surge前reject: below_1h_threshold=43, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.4 >= 65=1, 4h RSI 74.8 >= 65=1, 4h RSI 79.1 >= 65=1, 4h RSI 74.2 >= 65=1, 4h RSI 78.4 >= 65=1, 4h RSI 71.5 >= 65=1, 4h RSI 72.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| 4STOCK/USDT:USDT | +65.72% | $3,787,858.37 |
| MUBARAK/USDT:USDT | +36.91% | $7,480,428.12 |
| NIL/USDT:USDT | +32.31% | $4,305,807.90 |
| AGT/USDT:USDT | +24.55% | $1,968,185.31 |
| KERNEL/USDT:USDT | +24.15% | $5,836,431.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| 4STOCK/USDT:USDT | below_1h_threshold | +4.81% | +5.65% |
| NIL/USDT:USDT | below_1h_threshold | +4.25% | +5.09% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +3.90% | +4.74% |
| DRAM/USDT:USDT | below_1h_threshold | +3.86% | +4.70% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +3.72% | +4.56% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
