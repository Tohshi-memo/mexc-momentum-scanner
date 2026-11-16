# Decision Report

- generated_at: 2026-11-16T02:06:21.981492+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18991**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.03% / filled 20/20。**
- 全期間 MARKET基準: n=18991, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.03% | **+1.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 3/11 | 27.3% | +4.68% | **+1.28%** |
| MARKET | 20/20 | 100.0% | +1.03% | **+1.03%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.72% | **+0.54%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.40% | **+0.34%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.12% | **+0.34%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 15/20 | 75.0% | +1.32% | **+0.99%** |
| LIMIT_BB3S_LONG | 4/9 | 44.4% | +1.07% | **+0.48%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +0.73% | **+0.48%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.67% | **+0.33%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.24% | **+0.17%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 276件 (TP 100 / SL 168 / EXP 8)
- 最新: IDOL/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,711.71** / 初期 $100.00 (+1611.71%)
- 確定: 7335件 (Win 2106 / Loss 2348 / Flat 2881) / skip 8217件
- 成長率目線: 平均log +0.000387 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SOPH/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,711.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$429.80** / 初期 $100.00 (+329.80%)
- 確定: 4981件 (Win 1331 / Loss 1081 / Flat 2569) / skip 7421件
- 成長率目線: 平均log +0.000293 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BARD/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $429.80

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7151件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000095 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-16T02:06:08.429802+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.35% price=64761.6
- Funnel: target 1066 → liquid 110 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RARE/USDT:USDT | +51.64% | $5,533,053.45 |
| SHELL/USDT:USDT | +7.68% | $1,600,847.10 |
| PIEVERSE/USDT:USDT | +5.44% | $2,083,002.92 |
| EVAA/USDT:USDT | +4.49% | $17,491,904.79 |
| AKE/USDT:USDT | +4.18% | $24,887,867.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JCT/USDT:USDT | below_1h_threshold | +2.20% | +1.85% |
| AGT/USDT:USDT | below_1h_threshold | +1.22% | +0.87% |
| RARE/USDT:USDT | below_1h_threshold | +1.18% | +0.83% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +1.17% | +0.82% |
| VVV/USDT:USDT | below_1h_threshold | +1.17% | +0.82% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
