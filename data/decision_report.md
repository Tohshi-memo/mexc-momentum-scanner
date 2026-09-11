# Decision Report

- generated_at: 2026-09-11T15:56:31.114502+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14231**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14231, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.36%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.36% | **-0.36%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_5PCT | 6/20 | 30.0% | +1.02% | **+0.31%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.85% | **+0.26%** |
| LIMIT_BB3S | 4/14 | 28.6% | +0.88% | **+0.25%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.26% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/6 | 83.3% | +1.62% | **+1.35%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +3.16% | **+1.26%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.25% | **+0.69%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.80% | **+0.63%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.71% | **+0.57%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 209件 (TP 78 / SL 126 / EXP 5)
- 最新: RIVER/USDT:USDT SL_HIT PnL -3.59% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,078.25** / 初期 $100.00 (+978.25%)
- 確定: 5390件 (Win 1623 / Loss 1743 / Flat 2024) / skip 5402件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RIVER/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $1,078.25

## 4. Robust Adaptive DryRun ($100)

- 残高: **$207.79** / 初期 $100.00 (+107.79%)
- 確定: 2808件 (Win 770 / Loss 651 / Flat 1387) / skip 4834件
- 成長率目線: 平均log +0.000260 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0039 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RIVER/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $207.79

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.49** / 初期 $100.00 (+23.49%)
- 確定: 2729件 (Win 807 / Loss 1045 / Flat 877) / pending 6件 / skip 2975件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000289 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: 4STOCK/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $123.49

## 6. Latest Market Context

- 更新: 2026-09-11T15:56:18.028054+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -1.71% price=77411.6
- Funnel: target 1067 → liquid 164 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STONK/USDT:USDT | +75.55% | $1,311,081.78 |
| NIULAI/USDT:USDT | +62.04% | $23,379,525.92 |
| STORJ/USDT:USDT | +56.87% | $5,541,715.69 |
| LAB/USDT:USDT | +28.62% | $3,410,614.41 |
| RAY/USDT:USDT | +23.08% | $26,306,789.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| 4STOCK/USDT:USDT | below_1h_threshold | +3.14% | +4.85% |
| HPQSTOCK/USDT:USDT | below_1h_threshold | +1.63% | +3.34% |
| DELLSTOCK/USDT:USDT | below_1h_threshold | +1.33% | +3.04% |
| FARTCOIN/USDT:USDT | below_1h_threshold | +1.01% | +2.72% |
| STONK/USDT:USDT | below_1h_threshold | +0.93% | +2.64% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
