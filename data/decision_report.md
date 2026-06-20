# Decision Report

- generated_at: 2026-06-20T18:47:37.214751+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7263**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7263, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.72%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.72% | **-0.72%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +5.72% | **+0.86%** |
| LIMIT_8PCT | 4/20 | 20.0% | +3.93% | **+0.79%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +4.10% | **+0.41%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.05% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.86% | **+1.86%** |
| ASK_LONG | 20/20 | 100.0% | +1.47% | **+1.47%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +0.44% | **+0.13%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$101.45** / 初期 $100.00 (+1.45%)
- 確定トレード: 24件 (TP 9 / SL 15 / EXP 0)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.45
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$237.46** / 初期 $100.00 (+137.46%)
- 確定: 1992件 (Win 586 / Loss 648 / Flat 758) / skip 1832件
- 成長率目線: 平均log +0.000434 / 幾何平均 +0.043% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BICO/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $237.46

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 310件 (Win 89 / Loss 87 / Flat 134) / skip 364件
- 成長率目線: 平均log +0.000189 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-20T18:47:30.143676+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=63800.9
- Funnel: target 796 → liquid 138 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.3 >= 65=1, 4h RSI 89.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BICO/USDT:USDT | +46.48% | $40,188,850.30 |
| BTW/USDT:USDT | +19.14% | $62,777,894.84 |
| VELVET/USDT:USDT | +12.20% | $16,525,986.89 |
| LAB/USDT:USDT | +6.36% | $28,418,375.19 |
| AGT/USDT:USDT | +6.32% | $2,548,736.08 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ALICE/USDT:USDT | below_1h_threshold | +4.02% | +4.04% |
| ENJ/USDT:USDT | below_1h_threshold | +3.61% | +3.62% |
| BEL/USDT:USDT | below_1h_threshold | +3.26% | +3.28% |
| CHIP/USDT:USDT | below_1h_threshold | +2.82% | +2.84% |
| ASTEROID/USDT:USDT | below_1h_threshold | +2.74% | +2.76% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
