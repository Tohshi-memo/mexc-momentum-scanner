# Decision Report

- generated_at: 2026-07-03T19:10:20.100710+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8185**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.95% / filled 20/20。**
- 全期間 MARKET基準: n=8185, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.95%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.95% | **+0.95%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.95% | **+0.95%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.68% | **+0.55%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.52% | **+0.26%** |
| LIMIT_8PCT | 3/20 | 15.0% | +1.14% | **+0.17%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |
| ASK_LONG | 20/20 | 100.0% | +0.57% | **+0.57%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +0.55% | **+0.33%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +0.98% | **+0.15%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.14% | **+0.07%** |

## 2. $100 Live Portfolio

- 残高: **$102.10** / 初期 $100.00 (+2.10%)
- 確定トレード: 57件 (TP 20 / SL 36 / EXP 1)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$289.07** / 初期 $100.00 (+189.07%)
- 確定: 2504件 (Win 769 / Loss 833 / Flat 902) / skip 2242件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TA/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $289.07

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.04** / 初期 $100.00 (+6.04%)
- 確定: 611件 (Win 147 / Loss 147 / Flat 317) / skip 985件
- 成長率目線: 平均log +0.000096 / 幾何平均 +0.010% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BAS/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $106.04

## 5. Latest Market Context

- 更新: 2026-07-03T19:10:15.091535+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=62164.5
- Funnel: target 834 → liquid 161 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MAGMA/USDT:USDT | +32.31% | $9,401,697.02 |
| ANSEM/USDT:USDT | +29.40% | $1,209,864.53 |
| TA/USDT:USDT | +20.26% | $1,933,328.79 |
| TLM/USDT:USDT | +13.19% | $15,442,330.75 |
| VELVET/USDT:USDT | +12.50% | $28,605,531.41 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MAGMA/USDT:USDT | below_1h_threshold | +2.44% | +2.47% |
| TA/USDT:USDT | below_1h_threshold | +2.39% | +2.42% |
| BASED/USDT:USDT | below_1h_threshold | +2.05% | +2.07% |
| ADA/USDT:USDT | below_1h_threshold | +1.46% | +1.48% |
| GPS/USDT:USDT | below_1h_threshold | +1.44% | +1.46% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
