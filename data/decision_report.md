# Decision Report

- generated_at: 2026-06-29T04:54:36.322248+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7789**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.63% / filled 20/20。**
- 全期間 MARKET基準: n=7789, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.63%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.63% | **+1.63%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.63% | **+1.63%** |
| ASK | 20/20 | 100.0% | +1.62% | **+1.62%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.06% | **+0.01%** |
| LIMIT_4PCT | 9/20 | 45.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.46% | **+0.39%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | -0.31% | **-0.28%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -2.07% | **-0.31%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$258.23** / 初期 $100.00 (+158.23%)
- 確定: 2293件 (Win 696 / Loss 764 / Flat 833) / skip 2057件
- 成長率目線: 平均log +0.000414 / 幾何平均 +0.041% per trade / maxDD +8.13%
- 次の候補: `LIMIT_8PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SLX/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.07% 残高後 $258.23

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.45** / 初期 $100.00 (+6.45%)
- 確定: 456件 (Win 120 / Loss 119 / Flat 217) / skip 744件
- 成長率目線: 平均log +0.000137 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SYN/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $106.45

## 5. Latest Market Context

- 更新: 2026-06-29T04:54:30.683151+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.26% price=59864.0
- Funnel: target 805 → liquid 130 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RAVE/USDT:USDT | +23.58% | $16,141,680.21 |
| SLX/USDT:USDT | +16.68% | $9,747,654.49 |
| POWR/USDT:USDT | +13.44% | $6,831,327.68 |
| HEI/USDT:USDT | +11.58% | $2,000,885.45 |
| BAS/USDT:USDT | +11.35% | $4,069,920.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HEI/USDT:USDT | below_1h_threshold | +3.27% | +3.53% |
| SYN/USDT:USDT | below_1h_threshold | +2.69% | +2.95% |
| RIF/USDT:USDT | below_1h_threshold | +2.07% | +2.33% |
| SLX/USDT:USDT | below_1h_threshold | +1.97% | +2.23% |
| HIGH/USDT:USDT | below_1h_threshold | +1.84% | +2.10% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
