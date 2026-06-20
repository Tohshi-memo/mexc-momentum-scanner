# Decision Report

- generated_at: 2026-06-20T00:03:09.327816+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7179**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7179, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.03% | **-0.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.59% | **+0.59%** |
| LIMIT_BB3S | 3/17 | 17.6% | +1.30% | **+0.23%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.22% | **+0.16%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.48% | **+0.14%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.47% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.61% | **+1.45%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.19% | **+0.83%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.89% | **+0.58%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.07% | **+0.43%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.38% | **+0.23%** |

## 2. $100 Live Portfolio

- 残高: **$101.96** / 初期 $100.00 (+1.96%)
- 確定トレード: 23件 (TP 9 / SL 14 / EXP 0)
- 最新: BLESS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.96
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$225.97** / 初期 $100.00 (+125.97%)
- 確定: 1969件 (Win 571 / Loss 640 / Flat 758) / skip 1771件
- 成長率目線: 平均log +0.000414 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BICO/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $225.97

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 310件 (Win 89 / Loss 87 / Flat 134) / skip 280件
- 成長率目線: 平均log +0.000189 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-20T00:03:04.842633+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=63539.7
- Funnel: target 795 → liquid 146 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +33.55% | $9,646,169.59 |
| BICO/USDT:USDT | +31.87% | $12,110,271.75 |
| BLESS/USDT:USDT | +21.24% | $4,771,489.46 |
| RE/USDT:USDT | +20.04% | $72,514,965.85 |
| RIF/USDT:USDT | +12.50% | $1,760,569.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +2.82% | +2.78% |
| BLESS/USDT:USDT | below_1h_threshold | +2.04% | +2.00% |
| BICO/USDT:USDT | below_1h_threshold | +1.85% | +1.80% |
| RE/USDT:USDT | below_1h_threshold | +1.35% | +1.31% |
| AGT/USDT:USDT | below_1h_threshold | +1.31% | +1.27% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
