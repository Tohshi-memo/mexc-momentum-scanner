# Decision Report

- generated_at: 2026-06-19T11:54:57.178130+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7137**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7137, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-2.22%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.22% | **-2.22%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 11/20 | 55.0% | +0.69% | **+0.38%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.08% | **+0.38%** |
| LIMIT_7PCT | 4/20 | 20.0% | +0.70% | **+0.14%** |
| LIMIT_4PCT | 17/20 | 85.0% | -0.00% | **-0.00%** |
| LIMIT_8PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.41% | **+2.41%** |
| ASK_LONG | 20/20 | 100.0% | +2.36% | **+2.36%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +2.61% | **+2.08%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +1.88% | **+1.04%** |
| LIMIT_ATR_LONG | 7/20 | 35.0% | +1.03% | **+0.36%** |

## 2. $100 Live Portfolio

- 残高: **$102.98** / 初期 $100.00 (+2.98%)
- 確定トレード: 21件 (TP 9 / SL 12 / EXP 0)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.98
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$232.89** / 初期 $100.00 (+132.89%)
- 確定: 1957件 (Win 568 / Loss 631 / Flat 758) / skip 1741件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BEAT/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $232.89

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 309件 (Win 89 / Loss 87 / Flat 133) / skip 239件
- 成長率目線: 平均log +0.000190 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-19T11:54:50.005733+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=62592.1
- Funnel: target 795 → liquid 164 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.4 >= 65=2, 4h RSI n/a=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +87.71% | $8,451,927.40 |
| RE/USDT:USDT | +57.46% | $30,362,611.68 |
| HEI/USDT:USDT | +45.62% | $8,909,011.69 |
| BICO/USDT:USDT | +38.31% | $1,039,596.37 |
| BTW/USDT:USDT | +36.87% | $3,678,180.61 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEREBRO/USDT:USDT | below_1h_threshold | +3.29% | +3.16% |
| BTW/USDT:USDT | below_1h_threshold | +3.13% | +2.99% |
| CLO/USDT:USDT | below_1h_threshold | +1.86% | +1.73% |
| PI/USDT:USDT | below_1h_threshold | +1.45% | +1.32% |
| COAI/USDT:USDT | below_1h_threshold | +1.21% | +1.07% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
