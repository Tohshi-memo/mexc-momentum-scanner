# Decision Report

- generated_at: 2026-09-04T16:41:49.333924+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13642**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.52% / filled 20/20。**
- 全期間 MARKET基準: n=13642, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.52%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.52% | **+0.52%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 16/20 | 80.0% | +0.66% | **+0.53%** |
| MARKET | 20/20 | 100.0% | +0.52% | **+0.52%** |
| LIMIT_5PCT | 2/20 | 10.0% | +4.48% | **+0.45%** |
| LIMIT_FIB1272 | 11/20 | 55.0% | +0.81% | **+0.45%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.63% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.88% | **+0.88%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +0.30% | **+0.21%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -2.18% | **-0.44%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 200件 (TP 75 / SL 120 / EXP 5)
- 最新: PLTRSTOCK/USDT:USDT TP_HIT PnL +3.01% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$859.66** / 初期 $100.00 (+759.66%)
- 確定: 5011件 (Win 1516 / Loss 1644 / Flat 1851) / skip 5192件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASECAT/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $859.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$185.38** / 初期 $100.00 (+85.38%)
- 確定: 2420件 (Win 682 / Loss 577 / Flat 1161) / skip 4633件
- 成長率目線: 平均log +0.000255 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: USELESS/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $185.38

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.57** / 初期 $100.00 (+16.57%)
- 確定: 2285件 (Win 674 / Loss 880 / Flat 731) / pending 6件 / skip 2829件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000170 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BONER/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $116.57

## 6. Latest Market Context

- 更新: 2026-09-04T16:41:32.285260+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.37% price=79678.7
- Funnel: target 1050 → liquid 168 → pre 50 → checked 50 → surge 4 → strict 2
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.8 >= 65=1, 4h RSI 77.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| 4/USDT:USDT | +13.78% | $1,006,957.08 |
| BONER/USDT:USDT | +8.99% | $1,922,653.31 |
| SKR/USDT:USDT | +6.05% | $6,390,333.62 |
| USELESS/USDT:USDT | +5.80% | $45,422,503.20 |
| ZEN/USDT:USDT | +4.89% | $3,592,332.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEN/USDT:USDT | below_1h_threshold | +4.89% | +4.52% |
| BLESS/USDT:USDT | below_1h_threshold | +4.59% | +4.22% |
| TUT/USDT:USDT | below_1h_threshold | +3.87% | +3.50% |
| ZEC/USDT:USDT | below_1h_threshold | +3.10% | +2.73% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +2.95% | +2.58% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
