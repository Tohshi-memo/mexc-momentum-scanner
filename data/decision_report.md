# Decision Report

- generated_at: 2026-08-24T06:56:33.821124+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12495**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.65% / filled 20/20。**
- 全期間 MARKET基準: n=12495, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.65%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.65% | **+1.65%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +2.20% | **+1.98%** |
| MARKET | 20/20 | 100.0% | +1.65% | **+1.65%** |
| LIMIT_ATR | 14/20 | 70.0% | +1.51% | **+1.06%** |
| LIMIT_2PCT | 12/20 | 60.0% | +0.24% | **+0.14%** |
| LIMIT_BB3S | 6/17 | 35.3% | +0.31% | **+0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | -0.28% | **-0.14%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | -0.57% | **-0.20%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -1.40% | **-0.28%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 191件 (TP 73 / SL 113 / EXP 5)
- 最新: ON/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$703.82** / 初期 $100.00 (+603.82%)
- 確定: 4509件 (Win 1375 / Loss 1477 / Flat 1657) / skip 4547件
- 成長率目線: 平均log +0.000433 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASECAT/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $703.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.71** / 初期 $100.00 (+56.71%)
- 確定: 1965件 (Win 536 / Loss 470 / Flat 959) / skip 3941件
- 成長率目線: 平均log +0.000229 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: GPS/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $156.71

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.37** / 初期 $100.00 (+16.37%)
- 確定: 1880件 (Win 553 / Loss 712 / Flat 615) / pending 6件 / skip 2084件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000028 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: UAI/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.04% 残高後 $116.37

## 6. Latest Market Context

- 更新: 2026-08-24T06:56:23.618856+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.40% price=77444.0
- Funnel: target 1017 → liquid 180 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.1 >= 65=1, 4h RSI 75.2 >= 65=1, 4h RSI 85.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PONS/USDT:USDT | +57.28% | $1,050,948.49 |
| TUT/USDT:USDT | +35.20% | $53,212,649.57 |
| PROM/USDT:USDT | +27.84% | $8,331,201.53 |
| CASHCAT/USDT:USDT | +17.98% | $1,190,086.43 |
| PORTAL/USDT:USDT | +16.21% | $2,810,945.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UAI/USDT:USDT | below_1h_threshold | +4.73% | +4.33% |
| 1000RATS/USDT:USDT | below_1h_threshold | +4.66% | +4.26% |
| FORM/USDT:USDT | below_1h_threshold | +3.14% | +2.74% |
| BTW/USDT:USDT | below_1h_threshold | +3.13% | +2.74% |
| STORJ/USDT:USDT | below_1h_threshold | +2.94% | +2.55% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
