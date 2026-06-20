# Decision Report

- generated_at: 2026-06-20T05:05:44.957353+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7204**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.92% / filled 20/20。**
- 全期間 MARKET基準: n=7204, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.92% | **+1.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.97% | **+1.97%** |
| MARKET | 20/20 | 100.0% | +1.92% | **+1.92%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.59% | **+1.43%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.62% | **+1.05%** |
| LIMIT_BB3S | 3/17 | 17.6% | +4.59% | **+0.81%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +0.35% | **+0.21%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.35% | **+0.17%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.00% | **+0.00%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | -0.03% | **-0.02%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | -0.32% | **-0.22%** |

## 2. $100 Live Portfolio

- 残高: **$101.96** / 初期 $100.00 (+1.96%)
- 確定トレード: 23件 (TP 9 / SL 14 / EXP 0)
- 最新: BLESS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.96
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$225.97** / 初期 $100.00 (+125.97%)
- 確定: 1969件 (Win 571 / Loss 640 / Flat 758) / skip 1796件
- 成長率目線: 平均log +0.000414 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BICO/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $225.97

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 310件 (Win 89 / Loss 87 / Flat 134) / skip 305件
- 成長率目線: 平均log +0.000189 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-20T05:05:40.594710+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=63539.2
- Funnel: target 795 → liquid 145 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +42.31% | $17,388,788.28 |
| BICO/USDT:USDT | +27.68% | $19,681,019.25 |
| BLESS/USDT:USDT | +25.30% | $5,881,735.92 |
| AXS/USDT:USDT | +23.49% | $3,375,774.92 |
| EIGEN/USDT:USDT | +19.80% | $6,566,985.17 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RIVER/USDT:USDT | below_1h_threshold | +2.35% | +2.37% |
| BICO/USDT:USDT | below_1h_threshold | +2.11% | +2.14% |
| CLO/USDT:USDT | below_1h_threshold | +0.64% | +0.67% |
| VVV/USDT:USDT | below_1h_threshold | +0.41% | +0.43% |
| JUP/USDT:USDT | below_1h_threshold | +0.41% | +0.43% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
