# Decision Report

- generated_at: 2026-11-26T10:56:34.246587+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19685**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.49% / filled 20/20。**
- 全期間 MARKET基準: n=19685, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.49%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.49% | **+2.49%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.49% | **+2.49%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.66% | **+1.33%** |
| LIMIT_ATR | 10/20 | 50.0% | +1.29% | **+0.65%** |
| LIMIT_3PCT | 10/20 | 50.0% | +0.82% | **+0.41%** |
| LIMIT_BB3S | 4/17 | 23.5% | +1.41% | **+0.33%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +0.67% | **+0.13%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +0.25% | **+0.07%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +0.05% | **+0.01%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | -0.11% | **-0.11%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | -0.40% | **-0.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.73** / 初期 $100.00 (+21.73%)
- 確定トレード: 290件 (TP 106 / SL 176 / EXP 8)
- 最新: MONAD/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.73
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,988.11** / 初期 $100.00 (+1888.11%)
- 確定: 7621件 (Win 2195 / Loss 2454 / Flat 2972) / skip 8625件
- 成長率目線: 平均log +0.000392 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EVAA/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $1,988.11

## 4. Robust Adaptive DryRun ($100)

- 残高: **$465.65** / 初期 $100.00 (+365.65%)
- 確定: 5221件 (Win 1389 / Loss 1125 / Flat 2707) / skip 7875件
- 成長率目線: 平均log +0.000295 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $465.65

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7849件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000194 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-26T10:56:19.848013+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.73% price=60464.2
- Funnel: target 1097 → liquid 152 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BULLA/USDT:USDT | +79.22% | $3,478,723.35 |
| SI/USDT:USDT | +57.62% | $1,488,004.57 |
| KOR/USDT:USDT | +44.08% | $1,963,580.10 |
| SOXL/USDT:USDT | +27.35% | $1,640,970,302.35 |
| SSV/USDT:USDT | +26.31% | $2,005,510.74 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SI/USDT:USDT | below_1h_threshold | +4.46% | +5.20% |
| INIT/USDT:USDT | below_1h_threshold | +3.81% | +4.54% |
| ELSA/USDT:USDT | below_1h_threshold | +3.38% | +4.11% |
| KOR/USDT:USDT | below_1h_threshold | +1.95% | +2.68% |
| ZRO/USDT:USDT | below_1h_threshold | +1.31% | +2.04% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
