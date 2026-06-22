# Decision Report

- generated_at: 2026-06-22T17:49:42.240685+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7386**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.07% / filled 20/20。**
- 全期間 MARKET基準: n=7386, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.07%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.07% | **+1.07%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.20% | **+1.20%** |
| MARKET | 20/20 | 100.0% | +1.07% | **+1.07%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.00% | **+0.60%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.24% | **+0.43%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.56% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +0.80% | **+0.16%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -0.89% | **-0.09%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | -1.45% | **-0.15%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | -0.57% | **-0.20%** |
| MARKET_LONG | 20/20 | 100.0% | -0.26% | **-0.26%** |

## 2. $100 Live Portfolio

- 残高: **$102.45** / 初期 $100.00 (+2.45%)
- 確定トレード: 28件 (TP 11 / SL 17 / EXP 0)
- 最新: BTW/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.45
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$232.89** / 初期 $100.00 (+132.89%)
- 確定: 2042件 (Win 605 / Loss 672 / Flat 765) / skip 1905件
- 成長率目線: 平均log +0.000414 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RE/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $232.89

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 312件 (Win 89 / Loss 87 / Flat 136) / skip 485件
- 成長率目線: 平均log +0.000188 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-22T17:49:34.711718+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.37% price=64455.6
- Funnel: target 808 → liquid 159 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RE/USDT:USDT | +11.01% | $23,607,386.47 |
| BLESS/USDT:USDT | +9.93% | $4,302,968.55 |
| SYN/USDT:USDT | +8.31% | $26,115,418.38 |
| NAORIS/USDT:USDT | +7.45% | $5,986,188.04 |
| AAOISTOCK/USDT:USDT | +6.93% | $1,653,014.79 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NAORIS/USDT:USDT | below_1h_threshold | +3.48% | +3.85% |
| MMT/USDT:USDT | below_1h_threshold | +3.35% | +3.72% |
| BASED/USDT:USDT | below_1h_threshold | +3.24% | +3.61% |
| MYX/USDT:USDT | below_1h_threshold | +3.18% | +3.55% |
| AAOISTOCK/USDT:USDT | below_1h_threshold | +3.09% | +3.46% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
