# Decision Report

- generated_at: 2026-06-15T20:29:21.209225+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6808**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.42% / filled 20/20。**
- 全期間 MARKET基準: n=6808, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+1.42%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.42% | **+1.42%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.42% | **+1.42%** |
| LIMIT_ATR | 14/20 | 70.0% | +1.82% | **+1.27%** |
| ASK | 20/20 | 100.0% | +0.96% | **+0.96%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.30% | **+0.69%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.73% | **+0.51%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.59% | **+0.50%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.58% | **+0.44%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.21% | **+0.14%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -0.01% | **-0.00%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | -0.48% | **-0.17%** |

## 2. $100 Live Portfolio

- 残高: **$104.05** / 初期 $100.00 (+4.05%)
- 確定トレード: 7件 (TP 5 / SL 2 / EXP 0)
- 最新: ASTEROID/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.05
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$176.50** / 初期 $100.00 (+76.50%)
- 確定: 1681件 (Win 438 / Loss 526 / Flat 717) / skip 1688件
- 成長率目線: 平均log +0.000338 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FARTCOIN/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $176.50

## 4. Robust Adaptive DryRun ($100)

- 残高: **$97.60** / 初期 $100.00 (-2.40%)
- 確定: 155件 (Win 28 / Loss 30 / Flat 97) / skip 64件
- 成長率目線: 平均log -0.000156 / 幾何平均 -0.016% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MEGA/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account -0.22% 残高後 $97.60

## 5. Latest Market Context

- 更新: 2026-06-15T20:29:11.663491+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=66546.8
- Funnel: target 772 → liquid 156 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROAM/USDT:USDT | +26.13% | $1,779,284.07 |
| EVAA/USDT:USDT | +16.00% | $43,349,632.42 |
| HOME/USDT:USDT | +13.76% | $1,009,235.51 |
| SPCXSTOCK/USDT:USDT | +10.50% | $224,100,320.00 |
| FOLKS/USDT:USDT | +9.35% | $2,175,799.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ROAM/USDT:USDT | below_1h_threshold | +2.57% | +2.60% |
| WLD/USDT:USDT | below_1h_threshold | +2.47% | +2.50% |
| VELVET/USDT:USDT | below_1h_threshold | +2.35% | +2.38% |
| HOME/USDT:USDT | below_1h_threshold | +1.96% | +2.00% |
| BABY/USDT:USDT | below_1h_threshold | +1.28% | +1.31% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
