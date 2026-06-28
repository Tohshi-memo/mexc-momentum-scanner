# Decision Report

- generated_at: 2026-06-28T23:43:04.538336+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7777**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.73% / filled 20/20。**
- 全期間 MARKET基準: n=7777, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+2.73%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.73% | **+2.73%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.73% | **+2.73%** |
| ASK | 20/20 | 100.0% | +2.69% | **+2.69%** |
| LIMIT_BB3S | 6/13 | 46.2% | +3.80% | **+1.76%** |
| LIMIT_2PCT | 12/20 | 60.0% | +1.56% | **+0.94%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.51% | **+0.88%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.89% | **+0.40%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +0.46% | **+0.26%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | -0.28% | **-0.17%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$260.10** / 初期 $100.00 (+160.10%)
- 確定: 2281件 (Win 694 / Loss 761 / Flat 826) / skip 2057件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $260.10

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.45** / 初期 $100.00 (+6.45%)
- 確定: 455件 (Win 120 / Loss 119 / Flat 216) / skip 733件
- 成長率目線: 平均log +0.000137 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MYX/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.45

## 5. Latest Market Context

- 更新: 2026-06-28T23:42:59.866627+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +1.16% price=59732.6
- Funnel: target 805 → liquid 121 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NES/USDT:USDT | +13.78% | $2,677,466.35 |
| RAVE/USDT:USDT | +11.32% | $12,360,633.06 |
| G/USDT:USDT | +9.94% | $1,021,816.77 |
| BAS/USDT:USDT | +7.79% | $5,248,688.36 |
| SLX/USDT:USDT | +7.57% | $9,745,482.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EIGEN/USDT:USDT | below_1h_threshold | +3.24% | +2.07% |
| FARTCOIN/USDT:USDT | below_1h_threshold | +2.99% | +1.83% |
| RAVE/USDT:USDT | below_1h_threshold | +2.73% | +1.57% |
| FET/USDT:USDT | below_1h_threshold | +2.52% | +1.35% |
| ENA/USDT:USDT | below_1h_threshold | +2.35% | +1.18% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
