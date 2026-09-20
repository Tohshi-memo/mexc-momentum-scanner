# Decision Report

- generated_at: 2026-09-20T11:21:18.994405+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15178**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15178, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-2.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.16% | **-2.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 9/20 | 45.0% | +1.31% | **+0.59%** |
| LIMIT_7PCT | 6/20 | 30.0% | -0.00% | **-0.00%** |
| LIMIT_8PCT | 6/20 | 30.0% | -0.00% | **-0.00%** |
| LIMIT_ATR | 17/20 | 85.0% | -0.12% | **-0.10%** |
| LIMIT_FIB1618 | 5/20 | 25.0% | -0.60% | **-0.15%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.87% | **+2.29%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +3.15% | **+2.05%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +3.32% | **+1.99%** |
| MARKET_LONG | 20/20 | 100.0% | +1.36% | **+1.36%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.48% | **+1.33%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,203.42** / 初期 $100.00 (+1103.42%)
- 確定: 5704件 (Win 1705 / Loss 1840 / Flat 2159) / skip 6035件
- 成長率目線: 平均log +0.000436 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ONE/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $1,203.42

## 4. Robust Adaptive DryRun ($100)

- 残高: **$247.51** / 初期 $100.00 (+147.51%)
- 確定: 3282件 (Win 910 / Loss 764 / Flat 1608) / skip 5307件
- 成長率目線: 平均log +0.000276 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0344 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CELR/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $247.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.37** / 初期 $100.00 (+21.37%)
- 確定: 2978件 (Win 880 / Loss 1179 / Flat 919) / pending 0件 / skip 3674件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000174 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $121.37

## 6. Latest Market Context

- 更新: 2026-09-20T11:21:10.029931+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=80351.8
- Funnel: target 1050 → liquid 146 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CELR/USDT:USDT | +64.20% | $7,193,929.81 |
| ONE/USDT:USDT | +40.44% | $53,087,178.66 |
| OFC/USDT:USDT | +24.44% | $2,479,596.97 |
| BTW/USDT:USDT | +20.98% | $2,210,131.13 |
| PIEVERSE/USDT:USDT | +15.47% | $1,172,127.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| S/USDT:USDT | below_1h_threshold | +2.92% | +2.85% |
| SAGA/USDT:USDT | below_1h_threshold | +1.89% | +1.81% |
| CATE/USDT:USDT | below_1h_threshold | +1.54% | +1.46% |
| VVV/USDT:USDT | below_1h_threshold | +1.15% | +1.07% |
| AVAX/USDT:USDT | below_1h_threshold | +1.11% | +1.03% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
