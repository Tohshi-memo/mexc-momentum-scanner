# Decision Report

- generated_at: 2026-06-15T16:04:42.108373+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6794**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.25% / filled 20/20。**
- 全期間 MARKET基準: n=6794, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.25%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.25% | **+0.25%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.30% | **+0.30%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| MARKET | 20/20 | 100.0% | +0.25% | **+0.25%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.16% | **+0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.04% | **+0.67%** |
| MARKET_LONG | 20/20 | 100.0% | +0.35% | **+0.35%** |
| ASK_LONG | 20/20 | 100.0% | +0.29% | **+0.29%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +0.76% | **+0.23%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | -0.20% | **-0.07%** |

## 2. $100 Live Portfolio

- 残高: **$104.05** / 初期 $100.00 (+4.05%)
- 確定トレード: 7件 (TP 5 / SL 2 / EXP 0)
- 最新: ASTEROID/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.05
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$178.16** / 初期 $100.00 (+78.16%)
- 確定: 1667件 (Win 435 / Loss 517 / Flat 715) / skip 1688件
- 成長率目線: 平均log +0.000346 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EVAA/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $178.16

## 4. Robust Adaptive DryRun ($100)

- 残高: **$97.82** / 初期 $100.00 (-2.18%)
- 確定: 154件 (Win 28 / Loss 29 / Flat 97) / skip 51件
- 成長率目線: 平均log -0.000143 / 幾何平均 -0.014% per trade / maxDD +2.82%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CLO/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.35% 残高後 $97.82

## 5. Latest Market Context

- 更新: 2026-06-15T16:04:37.091839+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=67120.9
- Funnel: target 772 → liquid 156 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +4.60% | $39,281,879.64 |
| CLO/USDT:USDT | +3.33% | $2,200,157.88 |
| BEAT/USDT:USDT | +3.30% | $97,943,883.56 |
| ALGO/USDT:USDT | +2.89% | $3,055,782.41 |
| ASTEROID/USDT:USDT | +2.31% | $5,937,348.21 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EVAA/USDT:USDT | below_1h_threshold | +4.93% | +5.12% |
| CLO/USDT:USDT | below_1h_threshold | +3.25% | +3.44% |
| BEAT/USDT:USDT | below_1h_threshold | +3.11% | +3.30% |
| ALGO/USDT:USDT | below_1h_threshold | +2.69% | +2.88% |
| ASTEROID/USDT:USDT | below_1h_threshold | +2.31% | +2.50% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
