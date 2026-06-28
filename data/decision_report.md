# Decision Report

- generated_at: 2026-06-28T10:19:29.696999+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7739**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.11% / filled 20/20。**
- 全期間 MARKET基準: n=7739, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.11%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.11% | **+1.11%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.14% | **+1.14%** |
| MARKET | 20/20 | 100.0% | +1.11% | **+1.11%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.33% | **+0.13%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.60% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |
| ASK_LONG | 20/20 | 100.0% | +0.44% | **+0.44%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.10% | **+0.33%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +0.32% | **+0.05%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$243.09** / 初期 $100.00 (+143.09%)
- 確定: 2247件 (Win 680 / Loss 752 / Flat 815) / skip 2053件
- 成長率目線: 平均log +0.000395 / 幾何平均 +0.040% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: O/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $243.09

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.45** / 初期 $100.00 (+6.45%)
- 確定: 455件 (Win 120 / Loss 119 / Flat 216) / skip 695件
- 成長率目線: 平均log +0.000137 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MYX/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.45

## 5. Latest Market Context

- 更新: 2026-06-28T10:19:22.999516+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=60222.7
- Funnel: target 805 → liquid 120 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| O/USDT:USDT | +28.36% | $10,556,737.34 |
| S/USDT:USDT | +22.34% | $7,078,949.54 |
| SIREN/USDT:USDT | +20.85% | $1,610,156.14 |
| BASED/USDT:USDT | +16.99% | $1,799,815.47 |
| ACT/USDT:USDT | +16.85% | $1,698,278.23 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ACT/USDT:USDT | below_1h_threshold | +4.22% | +4.23% |
| RAVE/USDT:USDT | below_1h_threshold | +1.76% | +1.78% |
| ALLO/USDT:USDT | below_1h_threshold | +1.28% | +1.29% |
| RE/USDT:USDT | below_1h_threshold | +1.12% | +1.13% |
| POWR/USDT:USDT | below_1h_threshold | +0.71% | +0.72% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
