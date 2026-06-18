# Decision Report

- generated_at: 2026-06-18T20:13:06.441658+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7074**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.65% / filled 20/20。**
- 全期間 MARKET基準: n=7074, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.65%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.65% | **+0.65%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.73% | **+0.73%** |
| MARKET | 20/20 | 100.0% | +0.65% | **+0.65%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.73% | **+0.62%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.59% | **+0.56%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.05% | **+0.90%** |
| MARKET_LONG | 20/20 | 100.0% | +0.48% | **+0.48%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.58% | **+0.41%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.57% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$101.47** / 初期 $100.00 (+1.47%)
- 確定トレード: 15件 (TP 6 / SL 9 / EXP 0)
- 最新: BEAT/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.47
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$222.23** / 初期 $100.00 (+122.23%)
- 確定: 1894件 (Win 538 / Loss 605 / Flat 751) / skip 1741件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EDEN/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $222.23

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.40** / 初期 $100.00 (+6.40%)
- 確定: 308件 (Win 89 / Loss 86 / Flat 133) / skip 177件
- 成長率目線: 平均log +0.000202 / 幾何平均 +0.020% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MITO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.40

## 5. Latest Market Context

- 更新: 2026-06-18T20:13:01.886210+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.28% price=63100.1
- Funnel: target 795 → liquid 168 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +15.29% | $31,259,594.30 |
| PLAY/USDT:USDT | +14.00% | $1,815,128.57 |
| ZEREBRO/USDT:USDT | +13.81% | $1,925,743.11 |
| BASED/USDT:USDT | +10.70% | $1,223,614.62 |
| EDEN/USDT:USDT | +10.46% | $1,271,431.86 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ENJ/USDT:USDT | below_1h_threshold | +3.77% | +3.49% |
| ZRO/USDT:USDT | below_1h_threshold | +2.38% | +2.10% |
| INJ/USDT:USDT | below_1h_threshold | +2.20% | +1.93% |
| BR/USDT:USDT | below_1h_threshold | +2.09% | +1.82% |
| EIGEN/USDT:USDT | below_1h_threshold | +2.07% | +1.79% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
