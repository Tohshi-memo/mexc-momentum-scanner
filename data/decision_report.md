# Decision Report

- generated_at: 2026-09-15T23:16:41.363114+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14617**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.78% / filled 20/20。**
- 全期間 MARKET基準: n=14617, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.78%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.78% | **+2.78%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.78% | **+2.78%** |
| LIMIT_1PCT | 16/20 | 80.0% | +3.11% | **+2.49%** |
| LIMIT_2PCT | 13/20 | 65.0% | +1.78% | **+1.16%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +2.82% | **+1.13%** |
| LIMIT_ATR | 10/20 | 50.0% | +1.32% | **+0.66%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +1.54% | **+1.54%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -0.60% | **-0.09%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | -0.28% | **-0.15%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | -0.44% | **-0.20%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | -1.88% | **-0.47%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,044.12** / 初期 $100.00 (+944.12%)
- 確定: 5517件 (Win 1645 / Loss 1786 / Flat 2086) / skip 5661件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIN/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $1,044.12

## 4. Robust Adaptive DryRun ($100)

- 残高: **$230.42** / 初期 $100.00 (+130.42%)
- 確定: 3054件 (Win 839 / Loss 719 / Flat 1496) / skip 4974件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $230.42

## 5. Causal Adaptive DryRun ($100)

- 残高: **$124.53** / 初期 $100.00 (+24.53%)
- 確定: 2910件 (Win 864 / Loss 1133 / Flat 913) / pending 3件 / skip 3176件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000393 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: POWER/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $124.53

## 6. Latest Market Context

- 更新: 2026-09-15T23:16:31.013338+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.30% price=75859.9
- Funnel: target 1060 → liquid 155 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +20.58% | $1,055,738.00 |
| ON/USDT:USDT | +18.37% | $1,455,394.59 |
| SAGA/USDT:USDT | +18.15% | $7,156,697.68 |
| POWER/USDT:USDT | +9.61% | $14,755,359.34 |
| CNPY/USDT:USDT | +8.96% | $1,742,007.88 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| 4/USDT:USDT | below_1h_threshold | +2.32% | +2.02% |
| CVC/USDT:USDT | below_1h_threshold | +2.07% | +1.77% |
| NIULAI/USDT:USDT | below_1h_threshold | +1.91% | +1.61% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +1.19% | +0.89% |
| XPL/USDT:USDT | below_1h_threshold | +1.13% | +0.83% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
