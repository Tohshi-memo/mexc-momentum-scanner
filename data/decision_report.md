# Decision Report

- generated_at: 2026-06-23T18:02:12.544281+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7435**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.17% / filled 20/20。**
- 全期間 MARKET基準: n=7435, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.17% | **+1.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.17% | **+1.17%** |
| ASK | 20/20 | 100.0% | +1.13% | **+1.13%** |
| LIMIT_BB3S | 6/17 | 35.3% | +1.72% | **+0.61%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +3.82% | **+0.38%** |
| LIMIT_1PCT | 15/20 | 75.0% | +0.14% | **+0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +3.18% | **+0.80%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +0.45% | **+0.36%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.57% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$101.43** / 初期 $100.00 (+1.43%)
- 確定トレード: 30件 (TP 11 / SL 19 / EXP 0)
- 最新: HEI/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.43
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$228.71** / 初期 $100.00 (+128.71%)
- 確定: 2081件 (Win 617 / Loss 690 / Flat 774) / skip 1915件
- 成長率目線: 平均log +0.000398 / 幾何平均 +0.040% per trade / maxDD +7.25%
- 次の候補: `LIMIT_FIB1618_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $228.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.36** / 初期 $100.00 (+6.36%)
- 確定: 324件 (Win 92 / Loss 88 / Flat 144) / skip 522件
- 成長率目線: 平均log +0.000190 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SYN/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $106.36

## 5. Latest Market Context

- 更新: 2026-06-23T18:02:07.044083+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=62399.9
- Funnel: target 802 → liquid 168 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +29.55% | $1,473,463.95 |
| SYN/USDT:USDT | +16.20% | $16,673,723.17 |
| BASED/USDT:USDT | +5.62% | $2,583,758.91 |
| BEAT/USDT:USDT | +5.42% | $20,185,982.71 |
| RE/USDT:USDT | +3.98% | $22,249,971.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HEI/USDT:USDT | below_1h_threshold | +2.24% | +2.13% |
| MVLL/USDT:USDT | below_1h_threshold | +1.26% | +1.15% |
| BLESS/USDT:USDT | below_1h_threshold | +1.22% | +1.11% |
| BTW/USDT:USDT | below_1h_threshold | +0.96% | +0.84% |
| GRAM/USDT:USDT | below_1h_threshold | +0.57% | +0.46% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
