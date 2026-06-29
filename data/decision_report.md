# Decision Report

- generated_at: 2026-06-29T00:24:24.915517+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7778**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.09% / filled 20/20。**
- 全期間 MARKET基準: n=7778, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+3.09%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.09% | **+3.09%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.09% | **+3.09%** |
| ASK | 20/20 | 100.0% | +3.07% | **+3.07%** |
| LIMIT_BB3S | 6/14 | 42.9% | +3.80% | **+1.63%** |
| LIMIT_1PCT | 14/20 | 70.0% | +1.71% | **+1.19%** |
| LIMIT_2PCT | 11/20 | 55.0% | +2.07% | **+1.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.89% | **+0.40%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +0.46% | **+0.26%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | -0.28% | **-0.17%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$260.10** / 初期 $100.00 (+160.10%)
- 確定: 2282件 (Win 694 / Loss 761 / Flat 827) / skip 2057件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: POWR/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $260.10

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.45** / 初期 $100.00 (+6.45%)
- 確定: 455件 (Win 120 / Loss 119 / Flat 216) / skip 734件
- 成長率目線: 平均log +0.000137 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MYX/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.45

## 5. Latest Market Context

- 更新: 2026-06-29T00:24:20.038008+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.53% price=59234.8
- Funnel: target 805 → liquid 124 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NES/USDT:USDT | +15.16% | $2,874,854.73 |
| BAS/USDT:USDT | +10.09% | $5,062,177.09 |
| G/USDT:USDT | +9.28% | $1,131,479.54 |
| RAVE/USDT:USDT | +9.13% | $12,679,035.53 |
| POWR/USDT:USDT | +8.69% | $6,467,207.25 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SYN/USDT:USDT | below_1h_threshold | +2.88% | +3.41% |
| HEI/USDT:USDT | below_1h_threshold | +2.00% | +2.53% |
| APDSTOCK/USDT:USDT | below_1h_threshold | +1.36% | +1.89% |
| BAS/USDT:USDT | below_1h_threshold | +1.29% | +1.82% |
| BIANRENSHENG/USDT:USDT | below_1h_threshold | +1.22% | +1.75% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
