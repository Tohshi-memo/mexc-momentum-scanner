# Decision Report

- generated_at: 2026-06-22T17:01:39.250094+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7382**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.77% / filled 20/20。**
- 全期間 MARKET基準: n=7382, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.77%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.77% | **+1.77%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.84% | **+1.84%** |
| MARKET | 20/20 | 100.0% | +1.77% | **+1.77%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.60% | **+0.40%** |
| LIMIT_ATR | 9/20 | 45.0% | +0.83% | **+0.38%** |
| LIMIT_2PCT | 13/20 | 65.0% | +0.58% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +0.90% | **+0.14%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -0.89% | **-0.09%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | -0.18% | **-0.10%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | -1.45% | **-0.15%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | -0.57% | **-0.20%** |

## 2. $100 Live Portfolio

- 残高: **$102.45** / 初期 $100.00 (+2.45%)
- 確定トレード: 28件 (TP 11 / SL 17 / EXP 0)
- 最新: BTW/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.45
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$232.90** / 初期 $100.00 (+132.90%)
- 確定: 2038件 (Win 603 / Loss 670 / Flat 765) / skip 1905件
- 成長率目線: 平均log +0.000415 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $232.90

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 312件 (Win 89 / Loss 87 / Flat 136) / skip 481件
- 成長率目線: 平均log +0.000188 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-22T17:01:33.804090+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=64672.9
- Funnel: target 808 → liquid 157 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +8.89% | $25,147,046.12 |
| MYX/USDT:USDT | +4.69% | $3,293,499.73 |
| NAORIS/USDT:USDT | +4.11% | $5,906,997.43 |
| RE/USDT:USDT | +4.05% | $21,167,453.52 |
| BLESS/USDT:USDT | +3.98% | $3,295,051.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +1.57% | +1.61% |
| MYX/USDT:USDT | below_1h_threshold | +1.55% | +1.58% |
| BEAT/USDT:USDT | below_1h_threshold | +0.47% | +0.50% |
| UB/USDT:USDT | below_1h_threshold | +0.37% | +0.41% |
| BASED/USDT:USDT | below_1h_threshold | +0.33% | +0.37% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
