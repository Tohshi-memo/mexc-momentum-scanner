# Decision Report

- generated_at: 2026-11-16T04:21:24.621191+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18994**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.75% / filled 20/20。**
- 全期間 MARKET基準: n=18994, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.75%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.75% | **+1.75%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.75% | **+1.75%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.61% | **+0.49%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +4.09% | **+0.41%** |
| LIMIT_2PCT | 13/20 | 65.0% | +0.52% | **+0.34%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.66% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 16/20 | 80.0% | +0.84% | **+0.67%** |
| LIMIT_BB3S_LONG | 4/9 | 44.4% | +1.07% | **+0.48%** |
| LIMIT_5PCT_LONG | 14/20 | 70.0% | +0.21% | **+0.15%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | -0.06% | **-0.02%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | -0.04% | **-0.03%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 276件 (TP 100 / SL 168 / EXP 8)
- 最新: IDOL/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,720.18** / 初期 $100.00 (+1620.18%)
- 確定: 7337件 (Win 2107 / Loss 2349 / Flat 2881) / skip 8218件
- 成長率目線: 平均log +0.000388 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BARD/USDT:USDT `MARKET` TP_HIT account +1.00% 残高後 $1,720.18

## 4. Robust Adaptive DryRun ($100)

- 残高: **$429.80** / 初期 $100.00 (+329.80%)
- 確定: 4982件 (Win 1331 / Loss 1081 / Flat 2570) / skip 7423件
- 成長率目線: 平均log +0.000293 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BARD/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $429.80

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7154件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000139 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-16T04:21:12.165022+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.22% price=64935.4
- Funnel: target 1066 → liquid 113 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RARE/USDT:USDT | +38.73% | $6,043,982.40 |
| SKR/USDT:USDT | +36.18% | $1,495,233.87 |
| SHELL/USDT:USDT | +12.81% | $1,539,584.07 |
| PIEVERSE/USDT:USDT | +8.12% | $1,981,448.86 |
| JCT/USDT:USDT | +5.51% | $9,203,649.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JCT/USDT:USDT | below_1h_threshold | +2.75% | +2.97% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +2.51% | +2.73% |
| SKR/USDT:USDT | below_1h_threshold | +0.38% | +0.60% |
| BLESS/USDT:USDT | below_1h_threshold | +0.36% | +0.58% |
| SYRUP/USDT:USDT | below_1h_threshold | +0.19% | +0.41% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
