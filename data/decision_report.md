# Decision Report

- generated_at: 2026-06-28T18:29:19.131111+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7766**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7766, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.74%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.74% | **-0.74%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 7/20 | 35.0% | +4.82% | **+1.69%** |
| LIMIT_10PCT | 6/20 | 30.0% | +5.58% | **+1.67%** |
| LIMIT_BB3S | 10/13 | 76.9% | +1.67% | **+1.29%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +2.17% | **+1.09%** |
| LIMIT_8PCT | 7/20 | 35.0% | +2.73% | **+0.96%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +3.50% | **+1.57%** |
| MARKET_LONG | 20/20 | 100.0% | +1.54% | **+1.54%** |
| ASK_LONG | 20/20 | 100.0% | +1.49% | **+1.49%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.85% | **+1.28%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +2.46% | **+0.86%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$260.10** / 初期 $100.00 (+160.10%)
- 確定: 2273件 (Win 694 / Loss 761 / Flat 818) / skip 2054件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_8PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MANTA/USDT:USDT `LIMIT_9PCT` EXPIRED account +0.00% 残高後 $260.10

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.45** / 初期 $100.00 (+6.45%)
- 確定: 455件 (Win 120 / Loss 119 / Flat 216) / skip 722件
- 成長率目線: 平均log +0.000137 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MYX/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.45

## 5. Latest Market Context

- 更新: 2026-06-28T18:29:13.116272+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=59592.1
- Funnel: target 805 → liquid 124 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NES/USDT:USDT | +12.34% | $1,915,470.70 |
| MAGIC/USDT:USDT | +11.89% | $1,444,205.07 |
| RAVE/USDT:USDT | +8.49% | $10,836,377.59 |
| BAS/USDT:USDT | +5.21% | $5,741,872.33 |
| SLX/USDT:USDT | +4.83% | $17,506,817.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NES/USDT:USDT | below_1h_threshold | +2.95% | +2.89% |
| SLX/USDT:USDT | below_1h_threshold | +2.91% | +2.85% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +2.51% | +2.45% |
| BAS/USDT:USDT | below_1h_threshold | +1.65% | +1.59% |
| O/USDT:USDT | below_1h_threshold | +1.31% | +1.25% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
