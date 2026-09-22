# Decision Report

- generated_at: 2026-09-22T16:31:30.008703+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15337**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.05% / filled 20/20。**
- 全期間 MARKET基準: n=15337, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+3.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.05% | **+3.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.05% | **+3.05%** |
| LIMIT_1PCT | 18/20 | 90.0% | +3.07% | **+2.77%** |
| LIMIT_2PCT | 13/20 | 65.0% | +1.80% | **+1.17%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.59% | **+0.95%** |
| LIMIT_BB3S | 5/17 | 29.4% | +1.43% | **+0.42%** |

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
- 確定: 5823件 (Win 1727 / Loss 1874 / Flat 2222) / skip 6075件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FORM/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account -0.13% 残高後 $1,167.92

## 4. Robust Adaptive DryRun ($100)

- 残高: **$249.51** / 初期 $100.00 (+149.51%)
- 確定: 3353件 (Win 926 / Loss 781 / Flat 1646) / skip 5395件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KERNEL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $249.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.97** / 初期 $100.00 (+22.97%)
- 確定: 3106件 (Win 912 / Loss 1216 / Flat 978) / pending 6件 / skip 3706件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000166 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: FORM/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $122.97

## 6. Latest Market Context

- 更新: 2026-09-22T16:31:18.172814+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.28% price=86123.2
- Funnel: target 1058 → liquid 183 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.7 >= 65=1, 4h RSI 93.7 >= 65=1, 4h RSI 80.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CHR/USDT:USDT | +21.31% | $1,420,657.00 |
| MUBARAK/USDT:USDT | +11.24% | $9,050,773.38 |
| ZRO/USDT:USDT | +8.83% | $2,708,965.44 |
| SAGA/USDT:USDT | +4.76% | $3,684,819.72 |
| BR/USDT:USDT | +3.40% | $4,795,465.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SAGA/USDT:USDT | below_1h_threshold | +4.76% | +5.04% |
| BR/USDT:USDT | below_1h_threshold | +3.41% | +3.69% |
| AKE/USDT:USDT | below_1h_threshold | +3.11% | +3.40% |
| GIGGLE/USDT:USDT | below_1h_threshold | +2.34% | +2.62% |
| AIN/USDT:USDT | below_1h_threshold | +2.14% | +2.42% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
