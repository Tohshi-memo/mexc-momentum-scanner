# Decision Report

- generated_at: 2026-06-20T03:19:15.400147+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7203**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.79% / filled 20/20。**
- 全期間 MARKET基準: n=7203, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.79%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.79% | **+1.79%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.86% | **+1.86%** |
| MARKET | 20/20 | 100.0% | +1.79% | **+1.79%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.44% | **+1.30%** |
| LIMIT_ATR | 14/20 | 70.0% | +1.41% | **+0.99%** |
| LIMIT_BB3S | 3/17 | 17.6% | +4.59% | **+0.81%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.35% | **+0.17%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.00% | **+0.00%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | -0.03% | **-0.02%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | -0.03% | **-0.02%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | -0.48% | **-0.29%** |

## 2. $100 Live Portfolio

- 残高: **$101.96** / 初期 $100.00 (+1.96%)
- 確定トレード: 23件 (TP 9 / SL 14 / EXP 0)
- 最新: BLESS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.96
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$225.97** / 初期 $100.00 (+125.97%)
- 確定: 1969件 (Win 571 / Loss 640 / Flat 758) / skip 1795件
- 成長率目線: 平均log +0.000414 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BICO/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $225.97

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 310件 (Win 89 / Loss 87 / Flat 134) / skip 304件
- 成長率目線: 平均log +0.000189 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-20T03:19:11.034128+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=63375.8
- Funnel: target 795 → liquid 149 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +35.97% | $15,353,275.25 |
| BLESS/USDT:USDT | +25.42% | $5,497,843.13 |
| AXS/USDT:USDT | +22.32% | $1,499,738.65 |
| BICO/USDT:USDT | +18.45% | $18,537,795.78 |
| EIGEN/USDT:USDT | +18.32% | $6,337,267.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CLO/USDT:USDT | below_1h_threshold | +4.85% | +4.74% |
| EVAA/USDT:USDT | below_1h_threshold | +4.43% | +4.32% |
| AXS/USDT:USDT | below_1h_threshold | +3.49% | +3.38% |
| HIGH/USDT:USDT | below_1h_threshold | +2.74% | +2.63% |
| BTW/USDT:USDT | below_1h_threshold | +1.81% | +1.70% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
