# Decision Report

- generated_at: 2026-11-16T09:11:24.517335+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19003**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.82% / filled 20/20。**
- 全期間 MARKET基準: n=19003, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.82%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.82% | **+0.82%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.82% | **+0.82%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.98% | **+0.69%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_3PCT | 12/20 | 60.0% | +0.69% | **+0.41%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.25% | **+0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +2.76% | **+2.07%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.36% | **+0.24%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.03% | **+0.01%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | -0.06% | **-0.02%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | -0.07% | **-0.05%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 276件 (TP 100 / SL 168 / EXP 8)
- 最新: IDOL/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,711.33** / 初期 $100.00 (+1611.33%)
- 確定: 7344件 (Win 2109 / Loss 2354 / Flat 2881) / skip 8220件
- 成長率目線: 平均log +0.000387 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EVAA/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,711.33

## 4. Robust Adaptive DryRun ($100)

- 残高: **$430.10** / 初期 $100.00 (+330.10%)
- 確定: 4984件 (Win 1332 / Loss 1081 / Flat 2571) / skip 7430件
- 成長率目線: 平均log +0.000293 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SHELL/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $430.10

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7162件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000083 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-16T09:11:09.353817+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=64311.1
- Funnel: target 1066 → liquid 119 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RARE/USDT:USDT | +65.61% | $9,624,278.12 |
| SKR/USDT:USDT | +28.21% | $3,994,607.42 |
| EVAA/USDT:USDT | +22.63% | $19,827,682.57 |
| BLESS/USDT:USDT | +12.03% | $1,149,454.43 |
| PIEVERSE/USDT:USDT | +6.41% | $1,739,836.49 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EVAA/USDT:USDT | below_1h_threshold | +2.64% | +2.83% |
| BARD/USDT:USDT | below_1h_threshold | +1.31% | +1.49% |
| SKR/USDT:USDT | below_1h_threshold | +1.24% | +1.42% |
| BLESS/USDT:USDT | below_1h_threshold | +1.19% | +1.37% |
| SHELL/USDT:USDT | below_1h_threshold | +1.14% | +1.33% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
