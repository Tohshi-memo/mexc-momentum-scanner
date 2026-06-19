# Decision Report

- generated_at: 2026-06-19T11:12:25.678386+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7130**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7130, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-2.22%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.22% | **-2.22%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 12/20 | 60.0% | +1.13% | **+0.68%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.92% | **+0.58%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_4PCT | 17/20 | 85.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.81% | **+1.81%** |
| ASK_LONG | 20/20 | 100.0% | +1.66% | **+1.66%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +2.47% | **+1.24%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.64% | **+1.23%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +1.93% | **+0.77%** |

## 2. $100 Live Portfolio

- 残高: **$102.98** / 初期 $100.00 (+2.98%)
- 確定トレード: 21件 (TP 9 / SL 12 / EXP 0)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.98
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$230.60** / 初期 $100.00 (+130.60%)
- 確定: 1950件 (Win 564 / Loss 628 / Flat 758) / skip 1741件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RE/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $230.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 309件 (Win 89 / Loss 87 / Flat 133) / skip 232件
- 成長率目線: 平均log +0.000190 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-19T11:12:17.241457+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=62470.7
- Funnel: target 795 → liquid 161 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1, 4h RSI 82.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +75.19% | $8,287,682.62 |
| HEI/USDT:USDT | +56.10% | $7,917,937.93 |
| RE/USDT:USDT | +37.31% | $25,037,811.56 |
| BTW/USDT:USDT | +30.69% | $3,442,109.82 |
| ZEREBRO/USDT:USDT | +30.05% | $4,271,184.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEREBRO/USDT:USDT | below_1h_threshold | +3.39% | +3.44% |
| EDEN/USDT:USDT | below_1h_threshold | +2.41% | +2.47% |
| BEAT/USDT:USDT | below_1h_threshold | +1.48% | +1.54% |
| BASED/USDT:USDT | below_1h_threshold | +1.19% | +1.25% |
| COAI/USDT:USDT | below_1h_threshold | +1.09% | +1.14% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
