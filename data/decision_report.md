# Decision Report

- generated_at: 2026-06-20T12:45:43.395285+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7240**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7240, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.27%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.27% | **-0.27%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 20/20 | 100.0% | +2.40% | **+2.40%** |
| LIMIT_1PCT | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +3.55% | **+0.53%** |
| LIMIT_BB3S | 8/17 | 47.1% | +0.67% | **+0.31%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.40% | **+0.40%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +1.03% | **+0.36%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.67% | **+0.20%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.10% | **+0.04%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | -0.10% | **-0.05%** |

## 2. $100 Live Portfolio

- 残高: **$101.96** / 初期 $100.00 (+1.96%)
- 確定トレード: 23件 (TP 9 / SL 14 / EXP 0)
- 最新: BLESS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.96
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$225.97** / 初期 $100.00 (+125.97%)
- 確定: 1971件 (Win 572 / Loss 641 / Flat 758) / skip 1830件
- 成長率目線: 平均log +0.000414 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $225.97

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 310件 (Win 89 / Loss 87 / Flat 134) / skip 341件
- 成長率目線: 平均log +0.000189 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-20T12:45:36.685445+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=63591.0
- Funnel: target 795 → liquid 143 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.1 >= 65=1, 4h RSI 84.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +93.39% | $37,935,067.85 |
| BICO/USDT:USDT | +53.05% | $30,093,083.21 |
| BEL/USDT:USDT | +47.49% | $1,857,215.53 |
| SLX/USDT:USDT | +39.56% | $1,149,987.40 |
| RE/USDT:USDT | +32.00% | $91,892,135.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MET/USDT:USDT | below_1h_threshold | +4.08% | +4.17% |
| EDGE/USDT:USDT | below_1h_threshold | +3.49% | +3.59% |
| EVAA/USDT:USDT | below_1h_threshold | +2.17% | +2.26% |
| GRAM/USDT:USDT | below_1h_threshold | +1.06% | +1.16% |
| ZEC/USDT:USDT | below_1h_threshold | +0.61% | +0.71% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
