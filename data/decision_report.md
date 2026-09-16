# Decision Report

- generated_at: 2026-09-16T13:16:18.289260+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14692**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14692, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.20% | **-1.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 4/20 | 20.0% | +8.00% | **+1.60%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.17% | **+0.65%** |
| LIMIT_8PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_9PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.30% | **+0.30%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +2.81% | **+2.53%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.49% | **+2.37%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +2.35% | **+1.76%** |
| LIMIT_BB3S_LONG | 5/9 | 55.6% | +2.63% | **+1.46%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +3.86% | **+1.16%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,145.12** / 初期 $100.00 (+1045.12%)
- 確定: 5569件 (Win 1667 / Loss 1800 / Flat 2102) / skip 5684件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IOST/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $1,145.12

## 4. Robust Adaptive DryRun ($100)

- 残高: **$237.38** / 初期 $100.00 (+137.38%)
- 確定: 3096件 (Win 856 / Loss 731 / Flat 1509) / skip 5007件
- 成長率目線: 平均log +0.000279 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1732 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: IOST/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $237.38

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.75** / 初期 $100.00 (+23.75%)
- 確定: 2955件 (Win 878 / Loss 1164 / Flat 913) / pending 1件 / skip 3208件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000370 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BTW/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $123.75

## 6. Latest Market Context

- 更新: 2026-09-16T13:16:07.588498+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.25% price=75747.2
- Funnel: target 1058 → liquid 150 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +115.07% | $23,655,391.13 |
| BR/USDT:USDT | +112.82% | $28,438,114.97 |
| LSK/USDT:USDT | +37.68% | $27,695,904.34 |
| USELESS/USDT:USDT | +17.24% | $7,993,744.79 |
| ARB/USDT:USDT | +15.44% | $86,831,136.83 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ARB/USDT:USDT | below_1h_threshold | +1.76% | +2.01% |
| ZIL/USDT:USDT | below_1h_threshold | +1.07% | +1.32% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +0.70% | +0.94% |
| BTW/USDT:USDT | below_1h_threshold | +0.53% | +0.78% |
| KORU/USDT:USDT | below_1h_threshold | +0.31% | +0.55% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
