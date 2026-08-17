# Decision Report

- generated_at: 2026-08-17T08:36:33.038061+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11809**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.31% / filled 20/20。**
- 全期間 MARKET基準: n=11809, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.31%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.31% | **+0.31%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.96% | **+0.48%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.52% | **+0.47%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.36% | **+0.32%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 9/9 | 100.0% | +3.68% | **+3.68%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.67% | **+0.73%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +0.95% | **+0.43%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.61% | **+0.42%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 185件 (TP 71 / SL 109 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$620.90** / 初期 $100.00 (+520.90%)
- 確定: 4184件 (Win 1292 / Loss 1363 / Flat 1529) / skip 4186件
- 成長率目線: 平均log +0.000436 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ONG/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $620.90

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.44** / 初期 $100.00 (+55.44%)
- 確定: 1815件 (Win 502 / Loss 426 / Flat 887) / skip 3405件
- 成長率目線: 平均log +0.000243 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BSB/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.05% 残高後 $155.44

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.37** / 初期 $100.00 (+18.37%)
- 確定: 1672件 (Win 503 / Loss 635 / Flat 534) / pending 0件 / skip 1610件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000321 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: GPS/USDT:USDT `MARKET` EXPIRED account -0.07% 残高後 $118.37

## 6. Latest Market Context

- 更新: 2026-08-17T08:36:22.181392+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.17% price=63385.5
- Funnel: target 991 → liquid 159 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.8 >= 65=1, 4h RSI 70.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIULAI/USDT:USDT | +146.71% | $1,185,041.51 |
| GPS/USDT:USDT | +43.69% | $7,194,835.01 |
| PORTAL/USDT:USDT | +21.34% | $17,555,951.21 |
| TUT/USDT:USDT | +15.54% | $8,673,783.92 |
| AEON1/USDT:USDT | +13.52% | $1,029,661.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AEON1/USDT:USDT | below_1h_threshold | +4.26% | +4.43% |
| NIULAI/USDT:USDT | below_1h_threshold | +4.06% | +4.23% |
| US/USDT:USDT | below_1h_threshold | +3.40% | +3.57% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.02% | +2.20% |
| GPS/USDT:USDT | below_1h_threshold | +1.52% | +1.70% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
