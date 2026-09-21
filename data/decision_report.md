# Decision Report

- generated_at: 2026-09-21T10:06:18.776935+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15245**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15245, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.15%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.15% | **+0.15%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_5PCT | 6/20 | 30.0% | +2.13% | **+0.64%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.36% | **+0.20%** |
| LIMIT_BB3S | 5/13 | 38.5% | +0.50% | **+0.19%** |
| LIMIT_3PCT | 12/20 | 60.0% | +0.27% | **+0.16%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/6 | 83.3% | +1.39% | **+1.15%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.48% | **+0.26%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.40% | **+0.26%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.23% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,173.55** / 初期 $100.00 (+1073.55%)
- 確定: 5736件 (Win 1709 / Loss 1846 / Flat 2181) / skip 6070件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PHA/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.12% 残高後 $1,173.55

## 4. Robust Adaptive DryRun ($100)

- 残高: **$247.33** / 初期 $100.00 (+147.33%)
- 確定: 3307件 (Win 914 / Loss 765 / Flat 1628) / skip 5349件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0177 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PHA/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $247.33

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.65** / 初期 $100.00 (+22.65%)
- 確定: 3023件 (Win 891 / Loss 1186 / Flat 946) / pending 6件 / skip 3689件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000136 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PHA/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $122.65

## 6. Latest Market Context

- 更新: 2026-09-21T10:06:08.990973+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=84546.4
- Funnel: target 1050 → liquid 156 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 95.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ZETA/USDT:USDT | +72.15% | $6,050,245.29 |
| PHA/USDT:USDT | +54.07% | $1,442,041.16 |
| NIL/USDT:USDT | +35.22% | $7,309,568.53 |
| PTB/USDT:USDT | +27.44% | $1,151,056.46 |
| UAI/USDT:USDT | +24.58% | $1,579,230.27 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PIEVERSE/USDT:USDT | below_1h_threshold | +2.86% | +2.96% |
| ENA/USDT:USDT | below_1h_threshold | +1.73% | +1.83% |
| FARTCOIN/USDT:USDT | below_1h_threshold | +1.32% | +1.41% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +1.24% | +1.33% |
| VVV/USDT:USDT | below_1h_threshold | +1.00% | +1.09% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
