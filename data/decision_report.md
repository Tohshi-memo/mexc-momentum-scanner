# Decision Report

- generated_at: 2026-06-28T19:49:04.907312+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7768**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7768, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.14%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.14% | **-0.14%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 9/13 | 69.2% | +3.40% | **+2.35%** |
| LIMIT_10PCT | 6/20 | 30.0% | +5.58% | **+1.67%** |
| LIMIT_9PCT | 6/20 | 30.0% | +4.86% | **+1.46%** |
| LIMIT_8PCT | 6/20 | 30.0% | +2.57% | **+0.77%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +1.34% | **+0.67%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +2.94% | **+1.47%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +2.25% | **+1.13%** |
| MARKET_LONG | 20/20 | 100.0% | +0.94% | **+0.94%** |
| ASK_LONG | 20/20 | 100.0% | +0.86% | **+0.86%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.66% | **+0.66%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$260.10** / 初期 $100.00 (+160.10%)
- 確定: 2275件 (Win 694 / Loss 761 / Flat 820) / skip 2054件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RAVE/USDT:USDT `LIMIT_8PCT` EXPIRED account +0.00% 残高後 $260.10

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.45** / 初期 $100.00 (+6.45%)
- 確定: 455件 (Win 120 / Loss 119 / Flat 216) / skip 724件
- 成長率目線: 平均log +0.000137 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MYX/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.45

## 5. Latest Market Context

- 更新: 2026-06-28T19:48:59.969772+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.55% price=59251.9
- Funnel: target 805 → liquid 124 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MAGIC/USDT:USDT | +18.70% | $2,159,436.79 |
| RAVE/USDT:USDT | +9.06% | $12,337,924.05 |
| NES/USDT:USDT | +7.98% | $2,247,418.64 |
| ZEREBRO/USDT:USDT | +6.77% | $1,385,322.01 |
| SLX/USDT:USDT | +5.16% | $12,621,144.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEREBRO/USDT:USDT | below_1h_threshold | +1.57% | +2.12% |
| BAS/USDT:USDT | below_1h_threshold | +1.00% | +1.56% |
| ALLO/USDT:USDT | below_1h_threshold | +0.91% | +1.46% |
| VELVET/USDT:USDT | below_1h_threshold | +0.81% | +1.37% |
| GRAM/USDT:USDT | below_1h_threshold | +0.69% | +1.24% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
