# Decision Report

- generated_at: 2026-08-24T05:51:28.494317+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12493**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.57% / filled 20/20。**
- 全期間 MARKET基準: n=12493, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.57%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.57% | **+2.57%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.57% | **+2.57%** |
| LIMIT_1PCT | 17/20 | 85.0% | +2.93% | **+2.49%** |
| LIMIT_ATR | 13/20 | 65.0% | +2.26% | **+1.47%** |
| LIMIT_BB3S | 5/17 | 29.4% | +2.30% | **+0.68%** |
| LIMIT_2PCT | 11/20 | 55.0% | +0.99% | **+0.55%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | -0.35% | **-0.19%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | -0.50% | **-0.20%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -1.40% | **-0.28%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 191件 (TP 73 / SL 113 / EXP 5)
- 最新: ON/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$703.82** / 初期 $100.00 (+603.82%)
- 確定: 4509件 (Win 1375 / Loss 1477 / Flat 1657) / skip 4545件
- 成長率目線: 平均log +0.000433 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASECAT/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $703.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.71** / 初期 $100.00 (+56.71%)
- 確定: 1965件 (Win 536 / Loss 470 / Flat 959) / skip 3939件
- 成長率目線: 平均log +0.000229 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: GPS/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $156.71

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.33** / 初期 $100.00 (+16.33%)
- 確定: 1879件 (Win 552 / Loss 712 / Flat 615) / pending 4件 / skip 2083件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000167 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $116.33

## 6. Latest Market Context

- 更新: 2026-08-24T05:51:19.265600+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.19% price=77037.6
- Funnel: target 1017 → liquid 176 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TUT/USDT:USDT | +27.15% | $52,193,693.94 |
| CASHCAT/USDT:USDT | +21.09% | $1,148,254.36 |
| PROM/USDT:USDT | +18.99% | $7,439,971.15 |
| LIT/USDT:USDT | +13.54% | $18,169,647.80 |
| PORTAL/USDT:USDT | +13.13% | $2,635,653.54 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UAI/USDT:USDT | below_1h_threshold | +4.52% | +4.32% |
| STX/USDT:USDT | below_1h_threshold | +3.94% | +3.74% |
| CHIP/USDT:USDT | below_1h_threshold | +3.89% | +3.70% |
| GRASS/USDT:USDT | below_1h_threshold | +2.99% | +2.80% |
| ON/USDT:USDT | below_1h_threshold | +2.71% | +2.52% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
