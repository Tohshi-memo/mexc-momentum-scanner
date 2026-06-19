# Decision Report

- generated_at: 2026-06-19T13:19:06.344929+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7142**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7142, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.62%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.62% | **-1.62%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 10/20 | 50.0% | +0.67% | **+0.33%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.94% | **+0.28%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.12% | **+0.28%** |
| LIMIT_4PCT | 16/20 | 80.0% | -0.00% | **-0.00%** |
| LIMIT_8PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +2.06% | **+1.65%** |
| MARKET_LONG | 20/20 | 100.0% | +1.61% | **+1.61%** |
| ASK_LONG | 20/20 | 100.0% | +1.54% | **+1.54%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.47% | **+1.18%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +1.25% | **+0.56%** |

## 2. $100 Live Portfolio

- 残高: **$102.98** / 初期 $100.00 (+2.98%)
- 確定トレード: 21件 (TP 9 / SL 12 / EXP 0)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.98
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$234.04** / 初期 $100.00 (+134.04%)
- 確定: 1962件 (Win 571 / Loss 633 / Flat 758) / skip 1741件
- 成長率目線: 平均log +0.000433 / 幾何平均 +0.043% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEI/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $234.04

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 309件 (Win 89 / Loss 87 / Flat 133) / skip 244件
- 成長率目線: 平均log +0.000190 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-19T13:19:01.753112+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.24% price=62647.2
- Funnel: target 795 → liquid 160 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +80.88% | $8,821,525.90 |
| HEI/USDT:USDT | +71.88% | $10,621,761.53 |
| RE/USDT:USDT | +56.42% | $41,413,000.52 |
| ZEREBRO/USDT:USDT | +37.15% | $4,825,928.94 |
| BTW/USDT:USDT | +35.90% | $3,965,046.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| OPG/USDT:USDT | below_1h_threshold | +4.05% | +4.29% |
| BEAT/USDT:USDT | below_1h_threshold | +3.37% | +3.62% |
| BLESS/USDT:USDT | below_1h_threshold | +2.69% | +2.93% |
| O/USDT:USDT | below_1h_threshold | +2.65% | +2.89% |
| ENJ/USDT:USDT | below_1h_threshold | +1.47% | +1.72% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
