# Decision Report

- generated_at: 2026-09-20T17:26:30.038868+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15197**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.63% / filled 20/20。**
- 全期間 MARKET基準: n=15197, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.63%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.63% | **+0.63%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 17/20 | 85.0% | +1.11% | **+0.94%** |
| MARKET | 20/20 | 100.0% | +0.63% | **+0.63%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.89% | **+0.62%** |
| LIMIT_BB3S | 8/16 | 50.0% | +1.14% | **+0.57%** |
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +6.37% | **+1.27%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.71% | **+0.60%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.63% | **+0.41%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,173.63** / 初期 $100.00 (+1073.63%)
- 確定: 5717件 (Win 1705 / Loss 1845 / Flat 2167) / skip 6041件
- 成長率目線: 平均log +0.000431 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: OFC/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $1,173.63

## 4. Robust Adaptive DryRun ($100)

- 残高: **$247.68** / 初期 $100.00 (+147.68%)
- 確定: 3290件 (Win 911 / Loss 764 / Flat 1615) / skip 5318件
- 成長率目線: 平均log +0.000276 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $247.68

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.84** / 初期 $100.00 (+21.84%)
- 確定: 2986件 (Win 882 / Loss 1179 / Flat 925) / pending 6件 / skip 3683件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000144 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AR/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $121.84

## 6. Latest Market Context

- 更新: 2026-09-20T17:26:18.233499+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=81247.7
- Funnel: target 1050 → liquid 144 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.5 >= 65=1, 4h RSI 79.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LUNANEW/USDT:USDT | +16.01% | $1,600,354.75 |
| AR/USDT:USDT | +13.23% | $5,999,980.93 |
| SAGA/USDT:USDT | +11.37% | $3,530,222.50 |
| ENA/USDT:USDT | +9.06% | $70,605,527.12 |
| AKE/USDT:USDT | +7.76% | $86,201,438.73 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZAMA/USDT:USDT | below_1h_threshold | +3.53% | +3.59% |
| AKE/USDT:USDT | below_1h_threshold | +3.05% | +3.10% |
| STRK/USDT:USDT | below_1h_threshold | +1.57% | +1.63% |
| ZRO/USDT:USDT | below_1h_threshold | +1.08% | +1.14% |
| ARB/USDT:USDT | below_1h_threshold | +0.87% | +0.93% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
