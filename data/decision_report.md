# Decision Report

- generated_at: 2026-06-29T04:46:00.906542+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7788**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.23% / filled 20/20。**
- 全期間 MARKET基準: n=7788, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+2.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.23% | **+2.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.23% | **+2.23%** |
| ASK | 20/20 | 100.0% | +2.21% | **+2.21%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_1PCT | 13/20 | 65.0% | +0.06% | **+0.04%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.06% | **+0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.00% | **+0.40%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +0.22% | **+0.19%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -2.07% | **-0.31%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | -1.08% | **-0.43%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$258.42** / 初期 $100.00 (+158.42%)
- 確定: 2292件 (Win 696 / Loss 763 / Flat 833) / skip 2057件
- 成長率目線: 平均log +0.000414 / 幾何平均 +0.041% per trade / maxDD +8.13%
- 次の候補: `LIMIT_8PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RAVE/USDT:USDT `LIMIT_8PCT` EXPIRED account +0.00% 残高後 $258.42

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.45** / 初期 $100.00 (+6.45%)
- 確定: 456件 (Win 120 / Loss 119 / Flat 217) / skip 743件
- 成長率目線: 平均log +0.000137 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SYN/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $106.45

## 5. Latest Market Context

- 更新: 2026-06-29T04:45:56.229197+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.39% price=59788.0
- Funnel: target 805 → liquid 130 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RAVE/USDT:USDT | +27.94% | $15,894,684.80 |
| SLX/USDT:USDT | +15.37% | $9,640,134.60 |
| BAS/USDT:USDT | +13.90% | $4,052,766.37 |
| POWR/USDT:USDT | +13.75% | $6,814,686.17 |
| G/USDT:USDT | +11.34% | $1,464,562.83 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HIGH/USDT:USDT | below_1h_threshold | +3.01% | +3.39% |
| RIF/USDT:USDT | below_1h_threshold | +2.14% | +2.53% |
| H/USDT:USDT | below_1h_threshold | +1.89% | +2.28% |
| HEI/USDT:USDT | below_1h_threshold | +1.78% | +2.16% |
| BASED/USDT:USDT | below_1h_threshold | +1.29% | +1.68% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
