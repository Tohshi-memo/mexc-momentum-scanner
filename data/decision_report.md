# Decision Report

- generated_at: 2026-09-12T02:51:18.267180+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14272**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.39% / filled 20/20。**
- 全期間 MARKET基準: n=14272, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.39% | **+2.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.39% | **+2.39%** |
| LIMIT_1PCT | 18/20 | 90.0% | +2.51% | **+2.26%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.80% | **+0.56%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +2.09% | **+0.31%** |
| LIMIT_2PCT | 12/20 | 60.0% | +0.51% | **+0.31%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +3.38% | **+0.84%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +0.94% | **+0.42%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.40% | **+0.20%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | -0.55% | **-0.46%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,080.43** / 初期 $100.00 (+980.43%)
- 確定: 5427件 (Win 1635 / Loss 1760 / Flat 2032) / skip 5406件
- 成長率目線: 平均log +0.000439 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STORJ/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,080.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$209.84** / 初期 $100.00 (+109.84%)
- 確定: 2833件 (Win 780 / Loss 656 / Flat 1397) / skip 4850件
- 成長率目線: 平均log +0.000262 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $209.84

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.55** / 初期 $100.00 (+23.55%)
- 確定: 2763件 (Win 817 / Loss 1061 / Flat 885) / pending 4件 / skip 2977件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000192 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: STORJ/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $123.55

## 6. Latest Market Context

- 更新: 2026-09-12T02:51:07.311633+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=77240.5
- Funnel: target 1067 → liquid 156 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.7 >= 65=1, 4h RSI 75.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LONGXIA/USDT:USDT | +68.23% | $1,139,028.06 |
| LSK/USDT:USDT | +49.70% | $6,350,618.00 |
| LAB/USDT:USDT | +33.84% | $13,650,530.23 |
| STORJ/USDT:USDT | +26.59% | $17,388,194.11 |
| BEAT/USDT:USDT | +16.46% | $13,592,053.58 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| 4/USDT:USDT | below_1h_threshold | +4.29% | +4.29% |
| ETHFI/USDT:USDT | below_1h_threshold | +2.21% | +2.21% |
| KAS/USDT:USDT | below_1h_threshold | +2.15% | +2.14% |
| THETA/USDT:USDT | below_1h_threshold | +2.05% | +2.05% |
| VTHO/USDT:USDT | below_1h_threshold | +1.49% | +1.48% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
