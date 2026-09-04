# Decision Report

- generated_at: 2026-09-04T16:11:32.656939+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13636**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.16% / filled 20/20。**
- 全期間 MARKET基準: n=13636, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.16% | **+2.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.16% | **+2.16%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.67% | **+1.42%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.67% | **+1.17%** |
| LIMIT_ATR | 9/20 | 45.0% | +0.32% | **+0.14%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.16% | **+0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.00% | **+0.00%** |
| MARKET_LONG | 20/20 | 100.0% | -0.16% | **-0.16%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -2.31% | **-0.35%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 200件 (TP 75 / SL 120 / EXP 5)
- 最新: PLTRSTOCK/USDT:USDT TP_HIT PnL +3.01% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$859.66** / 初期 $100.00 (+759.66%)
- 確定: 5011件 (Win 1516 / Loss 1644 / Flat 1851) / skip 5186件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASECAT/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $859.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$185.38** / 初期 $100.00 (+85.38%)
- 確定: 2420件 (Win 682 / Loss 577 / Flat 1161) / skip 4627件
- 成長率目線: 平均log +0.000255 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: USELESS/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $185.38

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.58** / 初期 $100.00 (+16.58%)
- 確定: 2280件 (Win 672 / Loss 878 / Flat 730) / pending 6件 / skip 2825件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000132 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: UAI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $116.58

## 6. Latest Market Context

- 更新: 2026-09-04T16:11:22.694108+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=79443.7
- Funnel: target 1050 → liquid 165 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FLOCK/USDT:USDT | +5.72% | $1,016,482.13 |
| CP/USDT:USDT | +3.80% | $1,453,097.81 |
| CASHCAT/USDT:USDT | +3.16% | $1,052,732.61 |
| BLESS/USDT:USDT | +2.94% | $1,575,206.21 |
| DASH/USDT:USDT | +1.86% | $15,360,276.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CP/USDT:USDT | below_1h_threshold | +3.80% | +3.73% |
| CASHCAT/USDT:USDT | below_1h_threshold | +3.17% | +3.10% |
| BLESS/USDT:USDT | below_1h_threshold | +3.10% | +3.03% |
| KORU/USDT:USDT | below_1h_threshold | +2.17% | +2.10% |
| TUT/USDT:USDT | below_1h_threshold | +1.72% | +1.64% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
