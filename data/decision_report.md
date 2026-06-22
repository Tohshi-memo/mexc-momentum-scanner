# Decision Report

- generated_at: 2026-06-22T14:52:38.619565+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7376**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.16% / filled 20/20。**
- 全期間 MARKET基準: n=7376, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+2.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.16% | **+2.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.20% | **+2.20%** |
| MARKET | 20/20 | 100.0% | +2.16% | **+2.16%** |
| LIMIT_BB3S | 5/17 | 29.4% | +2.80% | **+0.82%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.47% | **+0.62%** |
| LIMIT_1PCT | 14/20 | 70.0% | +0.65% | **+0.46%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +0.42% | **+0.28%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -2.83% | **-0.28%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | -0.97% | **-0.48%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | -1.44% | **-0.58%** |

## 2. $100 Live Portfolio

- 残高: **$102.45** / 初期 $100.00 (+2.45%)
- 確定トレード: 28件 (TP 11 / SL 17 / EXP 0)
- 最新: BTW/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.45
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$229.44** / 初期 $100.00 (+129.44%)
- 確定: 2035件 (Win 600 / Loss 670 / Flat 765) / skip 1902件
- 成長率目線: 平均log +0.000408 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $229.44

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 312件 (Win 89 / Loss 87 / Flat 136) / skip 475件
- 成長率目線: 平均log +0.000188 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-22T14:52:34.089174+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.89% price=64967.6
- Funnel: target 808 → liquid 158 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +47.97% | $21,843,224.93 |
| BEL/USDT:USDT | +38.59% | $2,683,565.96 |
| BTW/USDT:USDT | +33.37% | $37,027,895.66 |
| CLO/USDT:USDT | +24.79% | $3,360,904.04 |
| MMT/USDT:USDT | +20.50% | $1,008,534.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MMT/USDT:USDT | below_1h_threshold | +4.64% | +5.53% |
| CLO/USDT:USDT | below_1h_threshold | +2.48% | +3.36% |
| BTW/USDT:USDT | below_1h_threshold | +2.43% | +3.31% |
| AERO/USDT:USDT | below_1h_threshold | +2.10% | +2.98% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +1.86% | +2.75% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
