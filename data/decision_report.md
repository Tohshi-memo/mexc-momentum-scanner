# Decision Report

- generated_at: 2026-09-22T16:21:23.383492+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15336**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.66% / filled 20/20。**
- 全期間 MARKET基準: n=15336, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.66%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.66% | **+2.66%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.66% | **+2.66%** |
| LIMIT_1PCT | 19/20 | 95.0% | +2.76% | **+2.62%** |
| LIMIT_2PCT | 14/20 | 70.0% | +2.25% | **+1.57%** |
| LIMIT_ATR | 13/20 | 65.0% | +2.08% | **+1.35%** |
| LIMIT_3PCT | 10/20 | 50.0% | +0.94% | **+0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 11/20 | 55.0% | +0.37% | **+0.20%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -0.89% | **-0.09%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -0.60% | **-0.09%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -2.49% | **-0.37%** |
| LIMIT_7PCT_LONG | 12/20 | 60.0% | -0.80% | **-0.48%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,167.92** / 初期 $100.00 (+1067.92%)
- 確定: 5823件 (Win 1727 / Loss 1874 / Flat 2222) / skip 6074件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FORM/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account -0.13% 残高後 $1,167.92

## 4. Robust Adaptive DryRun ($100)

- 残高: **$249.51** / 初期 $100.00 (+149.51%)
- 確定: 3353件 (Win 926 / Loss 781 / Flat 1646) / skip 5394件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KERNEL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $249.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.97** / 初期 $100.00 (+22.97%)
- 確定: 3106件 (Win 912 / Loss 1216 / Flat 978) / pending 6件 / skip 3705件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000158 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: FORM/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $122.97

## 6. Latest Market Context

- 更新: 2026-09-22T16:21:13.926469+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.33% price=86085.5
- Funnel: target 1058 → liquid 183 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.4 >= 65=1, 4h RSI 93.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CHR/USDT:USDT | +20.78% | $1,076,478.93 |
| MUBARAK/USDT:USDT | +8.13% | $8,891,516.48 |
| SAGA/USDT:USDT | +4.02% | $3,572,409.32 |
| ZRO/USDT:USDT | +3.69% | $2,525,396.18 |
| AIN/USDT:USDT | +2.44% | $1,000,402.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SAGA/USDT:USDT | below_1h_threshold | +4.50% | +4.82% |
| ZRO/USDT:USDT | below_1h_threshold | +3.62% | +3.95% |
| BR/USDT:USDT | below_1h_threshold | +2.20% | +2.53% |
| AIN/USDT:USDT | below_1h_threshold | +2.10% | +2.42% |
| 4/USDT:USDT | below_1h_threshold | +1.46% | +1.79% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
