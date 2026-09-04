# Decision Report

- generated_at: 2026-09-04T14:41:50.695233+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13630**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.31% / filled 20/20。**
- 全期間 MARKET基準: n=13630, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.31%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.31% | **+0.31%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 16/20 | 80.0% | +0.53% | **+0.42%** |
| MARKET | 20/20 | 100.0% | +0.31% | **+0.31%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.26% | **+0.16%** |
| LIMIT_5PCT | 3/20 | 15.0% | +0.95% | **+0.14%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.07% | **+0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.09% | **+1.09%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +0.53% | **+0.37%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | -1.01% | **-0.30%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 200件 (TP 75 / SL 120 / EXP 5)
- 最新: PLTRSTOCK/USDT:USDT TP_HIT PnL +3.01% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$859.66** / 初期 $100.00 (+759.66%)
- 確定: 5010件 (Win 1516 / Loss 1644 / Flat 1850) / skip 5181件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZEST/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $859.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$185.38** / 初期 $100.00 (+85.38%)
- 確定: 2420件 (Win 682 / Loss 577 / Flat 1161) / skip 4621件
- 成長率目線: 平均log +0.000255 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: USELESS/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $185.38

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.54** / 初期 $100.00 (+16.54%)
- 確定: 2275件 (Win 671 / Loss 878 / Flat 726) / pending 6件 / skip 2825件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000110 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $116.54

## 6. Latest Market Context

- 更新: 2026-09-04T14:41:34.474516+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=79188.6
- Funnel: target 1050 → liquid 172 → pre 50 → checked 50 → surge 5 → strict 1
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.1 >= 65=1, 4h RSI 66.4 >= 65=1, 4h RSI 72.2 >= 65=1, 4h RSI 78.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MARSCOIN/USDT:USDT | +55.58% | $7,555,311.29 |
| USELESS/USDT:USDT | +34.43% | $46,195,438.16 |
| PONS/USDT:USDT | +27.29% | $12,202,758.17 |
| TRIA/USDT:USDT | +26.20% | $10,832,673.92 |
| HNT/USDT:USDT | +20.66% | $14,320,751.24 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NBISSTOCK/USDT:USDT | below_1h_threshold | +3.66% | +3.86% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +3.62% | +3.82% |
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +3.53% | +3.72% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +3.51% | +3.70% |
| DRAM/USDT:USDT | below_1h_threshold | +3.44% | +3.64% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
