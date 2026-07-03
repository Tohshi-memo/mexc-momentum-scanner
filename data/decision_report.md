# Decision Report

- generated_at: 2026-07-03T16:26:29.440016+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8172**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.25% / filled 20/20。**
- 全期間 MARKET基準: n=8172, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.25%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.25% | **+2.25%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.25% | **+2.25%** |
| ASK | 20/20 | 100.0% | +1.57% | **+1.57%** |
| LIMIT_1PCT | 15/20 | 75.0% | +1.16% | **+0.87%** |
| LIMIT_3PCT | 12/20 | 60.0% | +0.78% | **+0.47%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.15% | **+0.08%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.13% | **+0.08%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +0.05% | **+0.03%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -1.79% | **-0.36%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | -4.00% | **-0.40%** |

## 2. $100 Live Portfolio

- 残高: **$102.61** / 初期 $100.00 (+2.61%)
- 確定トレード: 56件 (TP 20 / SL 35 / EXP 1)
- 最新: RIF/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$283.87** / 初期 $100.00 (+183.87%)
- 確定: 2492件 (Win 765 / Loss 833 / Flat 894) / skip 2241件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GUA/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.50% 残高後 $283.87

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.04** / 初期 $100.00 (+6.04%)
- 確定: 611件 (Win 147 / Loss 147 / Flat 317) / skip 972件
- 成長率目線: 平均log +0.000096 / 幾何平均 +0.010% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BAS/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $106.04

## 5. Latest Market Context

- 更新: 2026-07-03T16:26:24.139047+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.22% price=62032.1
- Funnel: target 834 → liquid 161 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.7 >= 65=1, 4h RSI 70.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| GUA/USDT:USDT | +14.14% | $5,588,112.41 |
| MAGMA/USDT:USDT | +6.17% | $7,964,652.53 |
| ARPA/USDT:USDT | +5.94% | $6,927,815.82 |
| XPL/USDT:USDT | +3.59% | $20,079,600.18 |
| BASED/USDT:USDT | +3.38% | $8,966,540.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XPL/USDT:USDT | below_1h_threshold | +3.59% | +3.37% |
| BASED/USDT:USDT | below_1h_threshold | +3.39% | +3.17% |
| POPCAT/USDT:USDT | below_1h_threshold | +2.05% | +1.83% |
| SYN/USDT:USDT | below_1h_threshold | +1.60% | +1.38% |
| LIT/USDT:USDT | below_1h_threshold | +1.56% | +1.34% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
