# Decision Report

- generated_at: 2026-07-03T07:51:24.024935+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8143**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8143, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.76%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.76% | **-0.76%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +0.73% | **+0.07%** |
| LIMIT_9PCT | 2/20 | 10.0% | +0.29% | **+0.03%** |
| LIMIT_8PCT | 2/20 | 10.0% | -0.15% | **-0.01%** |
| LIMIT_6PCT | 6/20 | 30.0% | -0.08% | **-0.02%** |
| LIMIT_5PCT | 8/20 | 40.0% | -0.29% | **-0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.58% | **+1.58%** |
| MARKET_LONG | 20/20 | 100.0% | +1.35% | **+1.35%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +0.80% | **+0.56%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.71% | **+0.46%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.75% | **+0.26%** |

## 2. $100 Live Portfolio

- 残高: **$102.11** / 初期 $100.00 (+2.11%)
- 確定トレード: 54件 (TP 19 / SL 34 / EXP 1)
- 最新: SKHYNIXSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.11
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$284.03** / 初期 $100.00 (+184.03%)
- 確定: 2464件 (Win 758 / Loss 823 / Flat 883) / skip 2240件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `LIMIT_FIB1272_LONG` SL_HIT account -0.50% 残高後 $284.03

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.22** / 初期 $100.00 (+6.22%)
- 確定: 596件 (Win 143 / Loss 141 / Flat 312) / skip 958件
- 成長率目線: 平均log +0.000101 / 幾何平均 +0.010% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NOM/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.29% 残高後 $106.22

## 5. Latest Market Context

- 更新: 2026-07-03T07:51:16.667501+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.19% price=61799.0
- Funnel: target 834 → liquid 166 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NEX/USDT:USDT | +36.93% | $1,347,794.11 |
| RIF/USDT:USDT | +31.97% | $7,482,073.76 |
| ZKP/USDT:USDT | +25.93% | $3,404,235.49 |
| GUA/USDT:USDT | +20.23% | $9,216,647.87 |
| MAGMA/USDT:USDT | +20.17% | $6,618,678.19 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +4.01% | +3.82% |
| S/USDT:USDT | below_1h_threshold | +2.91% | +2.72% |
| XPL/USDT:USDT | below_1h_threshold | +1.94% | +1.75% |
| THE/USDT:USDT | below_1h_threshold | +1.77% | +1.58% |
| SEI/USDT:USDT | below_1h_threshold | +1.08% | +0.89% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
