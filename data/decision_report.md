# Decision Report

- generated_at: 2026-06-24T21:43:07.092124+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7501**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.86% / filled 20/20。**
- 全期間 MARKET基準: n=7501, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.86%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.86% | **+0.86%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.88% | **+0.88%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.92% | **+0.87%** |
| MARKET | 20/20 | 100.0% | +0.86% | **+0.86%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.80% | **+0.68%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.70% | **+0.53%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.00% | **+0.40%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.33% | **+0.21%** |
| MARKET_LONG | 20/20 | 100.0% | +0.14% | **+0.14%** |
| ASK_LONG | 20/20 | 100.0% | +0.11% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$102.95** / 初期 $100.00 (+2.95%)
- 確定トレード: 36件 (TP 14 / SL 22 / EXP 0)
- 最新: SNDKSTOCK/USDT:USDT SL_HIT PnL -3.46% 残高後 $102.95
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$223.69** / 初期 $100.00 (+123.69%)
- 確定: 2121件 (Win 627 / Loss 709 / Flat 785) / skip 1941件
- 成長率目線: 平均log +0.000380 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $223.69

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.76** / 初期 $100.00 (+6.76%)
- 確定: 349件 (Win 98 / Loss 95 / Flat 156) / skip 563件
- 成長率目線: 平均log +0.000187 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: H/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $106.76

## 5. Latest Market Context

- 更新: 2026-06-24T21:43:02.406750+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.23% price=61068.2
- Funnel: target 808 → liquid 161 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KORU/USDT:USDT | +21.51% | $4,228,386.73 |
| MUSTOCK/USDT:USDT | +13.12% | $89,690,917.18 |
| SOXL/USDT:USDT | +12.42% | $6,030,845.85 |
| DRAM/USDT:USDT | +12.23% | $7,713,226.84 |
| MVLL/USDT:USDT | +11.36% | $2,390,970.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SLX/USDT:USDT | below_1h_threshold | +4.99% | +4.76% |
| O/USDT:USDT | below_1h_threshold | +4.96% | +4.73% |
| UB/USDT:USDT | below_1h_threshold | +2.97% | +2.74% |
| AERO/USDT:USDT | below_1h_threshold | +2.65% | +2.41% |
| LIT/USDT:USDT | below_1h_threshold | +2.39% | +2.16% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
