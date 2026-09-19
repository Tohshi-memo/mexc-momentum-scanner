# Decision Report

- generated_at: 2026-09-19T04:51:30.755217+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14992**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=14992, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.78% | **+0.59%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.96% | **+0.29%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.60% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +4.60% | **+4.60%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.56% | **+0.70%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.52% | **+0.68%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.37% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,195.40** / 初期 $100.00 (+1095.40%)
- 確定: 5640件 (Win 1691 / Loss 1829 / Flat 2120) / skip 5913件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,195.40

## 4. Robust Adaptive DryRun ($100)

- 残高: **$239.14** / 初期 $100.00 (+139.14%)
- 確定: 3178件 (Win 878 / Loss 760 / Flat 1540) / skip 5225件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ONE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $239.14

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.09** / 初期 $100.00 (+23.09%)
- 確定: 2965件 (Win 879 / Loss 1169 / Flat 917) / pending 3件 / skip 3496件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000290 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: G/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $123.09

## 6. Latest Market Context

- 更新: 2026-09-19T04:51:17.127627+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.14% price=80982.7
- Funnel: target 1050 → liquid 170 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +79.66% | $41,428,140.30 |
| ONE/USDT:USDT | +37.04% | $26,721,831.14 |
| AR/USDT:USDT | +27.22% | $5,433,088.34 |
| SAGA/USDT:USDT | +23.54% | $4,249,712.08 |
| CATE/USDT:USDT | +22.79% | $1,460,605.97 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PIEVERSE/USDT:USDT | below_1h_threshold | +4.78% | +4.93% |
| VET/USDT:USDT | below_1h_threshold | +4.06% | +4.20% |
| MORPHO/USDT:USDT | below_1h_threshold | +1.78% | +1.92% |
| RAY/USDT:USDT | below_1h_threshold | +1.07% | +1.22% |
| 4/USDT:USDT | below_1h_threshold | +0.94% | +1.08% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
