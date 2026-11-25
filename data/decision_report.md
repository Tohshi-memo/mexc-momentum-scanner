# Decision Report

- generated_at: 2026-11-25T15:31:17.437386+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19611**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.88% / filled 20/20。**
- 全期間 MARKET基準: n=19611, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.88%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.88% | **+2.88%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.88% | **+2.88%** |
| LIMIT_1PCT | 16/20 | 80.0% | +2.32% | **+1.86%** |
| LIMIT_3PCT | 11/20 | 55.0% | +1.48% | **+0.81%** |
| LIMIT_ATR | 9/20 | 45.0% | +1.62% | **+0.73%** |
| LIMIT_2PCT | 11/20 | 55.0% | +0.76% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | +1.71% | **+0.51%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.11% | **+0.42%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.40% | **+0.42%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | +0.36% | **+0.20%** |
| LIMIT_6PCT_LONG | 13/20 | 65.0% | -0.63% | **-0.41%** |

## 2. $100 Live Portfolio

- 残高: **$121.61** / 初期 $100.00 (+21.61%)
- 確定トレード: 288件 (TP 105 / SL 175 / EXP 8)
- 最新: SOXS/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,988.31** / 初期 $100.00 (+1888.31%)
- 確定: 7611件 (Win 2191 / Loss 2450 / Flat 2970) / skip 8561件
- 成長率目線: 平均log +0.000393 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BIGTIME/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,988.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$467.28** / 初期 $100.00 (+367.28%)
- 確定: 5220件 (Win 1389 / Loss 1124 / Flat 2707) / skip 7802件
- 成長率目線: 平均log +0.000295 / 幾何平均 +0.030% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KIMCHI/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.09% 残高後 $467.28

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7773件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000132 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-25T15:31:06.201280+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.38% price=57990.3
- Funnel: target 1097 → liquid 149 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KOR/USDT:USDT | +83.91% | $1,428,095.34 |
| BIGTIME/USDT:USDT | +52.87% | $7,880,738.08 |
| MANTRA/USDT:USDT | +42.11% | $1,318,326.47 |
| BTW/USDT:USDT | +24.90% | $7,562,489.34 |
| MMT/USDT:USDT | +24.64% | $3,125,602.82 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MMT/USDT:USDT | below_1h_threshold | +3.20% | +3.58% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +2.18% | +2.56% |
| UVXY/USDT:USDT | below_1h_threshold | +1.96% | +2.33% |
| METASTOCK/USDT:USDT | below_1h_threshold | +1.27% | +1.65% |
| ANTHROPIC/USDT:USDT | below_1h_threshold | +1.23% | +1.60% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
