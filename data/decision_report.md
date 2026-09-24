# Decision Report

- generated_at: 2026-09-24T21:26:34.358035+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15491**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.26% / filled 20/20。**
- 全期間 MARKET基準: n=15491, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.26%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.26% | **+0.26%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 16/20 | 80.0% | +0.49% | **+0.39%** |
| MARKET | 20/20 | 100.0% | +0.26% | **+0.26%** |
| LIMIT_9PCT | 2/20 | 10.0% | +0.29% | **+0.03%** |
| LIMIT_6PCT | 3/20 | 15.0% | -0.01% | **-0.00%** |
| LIMIT_8PCT | 2/20 | 10.0% | -0.15% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 8/12 | 66.7% | +2.92% | **+1.95%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.11% | **+0.83%** |
| MARKET_LONG | 20/20 | 100.0% | +0.82% | **+0.82%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.88% | **+0.71%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.98% | **+0.64%** |

## 2. $100 Live Portfolio

- 残高: **$120.08** / 初期 $100.00 (+20.08%)
- 確定トレード: 219件 (TP 79 / SL 135 / EXP 5)
- 最新: XPL/USDT:USDT SL_HIT PnL -3.85% 残高後 $120.08
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,197.79** / 初期 $100.00 (+1097.79%)
- 確定: 5899件 (Win 1739 / Loss 1890 / Flat 2270) / skip 6153件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ONDO/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $1,197.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$253.55** / 初期 $100.00 (+153.55%)
- 確定: 3437件 (Win 949 / Loss 792 / Flat 1696) / skip 5465件
- 成長率目線: 平均log +0.000271 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ETC/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $253.55

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.05** / 初期 $100.00 (+21.05%)
- 確定: 3160件 (Win 932 / Loss 1247 / Flat 981) / pending 3件 / skip 3803件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000057 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SAGA/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $121.05

## 6. Latest Market Context

- 更新: 2026-09-24T21:26:20.745760+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=84378.6
- Funnel: target 1069 → liquid 174 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| XAI/USDT:USDT | +23.91% | $9,700,356.92 |
| SAGA/USDT:USDT | +23.12% | $2,294,264.47 |
| LSK/USDT:USDT | +14.39% | $18,664,134.89 |
| CHIP/USDT:USDT | +8.81% | $1,206,503.24 |
| XPL/USDT:USDT | +7.73% | $11,073,579.47 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XAI/USDT:USDT | below_1h_threshold | +3.07% | +3.00% |
| XPL/USDT:USDT | below_1h_threshold | +1.65% | +1.58% |
| ONDO/USDT:USDT | below_1h_threshold | +1.62% | +1.56% |
| TIA/USDT:USDT | below_1h_threshold | +1.32% | +1.25% |
| NEAR/USDT:USDT | below_1h_threshold | +1.22% | +1.15% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
