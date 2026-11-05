# Decision Report

- generated_at: 2026-11-05T14:01:27.921553+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18180**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +4.26% / filled 20/20。**
- 全期間 MARKET基準: n=18180, expectancy=+0.03%
- 直近20件 MARKET基準: n=20, expectancy=+4.26%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +4.26% | **+4.26%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +4.26% | **+4.26%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_2PCT | 9/20 | 45.0% | +0.94% | **+0.42%** |
| LIMIT_3PCT | 8/20 | 40.0% | +0.93% | **+0.37%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 9/20 | 45.0% | +3.03% | **+1.36%** |
| LIMIT_10PCT_LONG | 7/20 | 35.0% | +3.75% | **+1.31%** |
| LIMIT_8PCT_LONG | 12/20 | 60.0% | +1.00% | **+0.60%** |
| LIMIT_BB3S_LONG | 5/5 | 100.0% | +0.34% | **+0.34%** |
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | -0.44% | **-0.13%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 262件 (TP 96 / SL 158 / EXP 8)
- 最新: SOXS/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,502.99** / 初期 $100.00 (+1402.99%)
- 確定: 6999件 (Win 2020 / Loss 2243 / Flat 2736) / skip 7742件
- 成長率目線: 平均log +0.000387 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ARIA/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $1,502.99

## 4. Robust Adaptive DryRun ($100)

- 残高: **$372.80** / 初期 $100.00 (+272.80%)
- 確定: 4572件 (Win 1226 / Loss 1030 / Flat 2316) / skip 7019件
- 成長率目線: 平均log +0.000288 / 幾何平均 +0.029% per trade / maxDD +4.25%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0064 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ARIA/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $372.80

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6338件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000494 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-05T14:01:14.536403+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=79649.6
- Funnel: target 1084 → liquid 182 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIO/USDT:USDT | +32.02% | $1,316,405.02 |
| APPSTOCK/USDT:USDT | +24.70% | $2,141,043.24 |
| ARIA/USDT:USDT | +19.47% | $2,232,560.88 |
| FLUID/USDT:USDT | +18.00% | $7,839,495.42 |
| LYN/USDT:USDT | +17.31% | $1,146,620.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| APPSTOCK/USDT:USDT | below_1h_threshold | +2.04% | +2.04% |
| SOXS/USDT:USDT | below_1h_threshold | +0.66% | +0.65% |
| ELSA/USDT:USDT | below_1h_threshold | +0.61% | +0.61% |
| LYN/USDT:USDT | below_1h_threshold | +0.57% | +0.56% |
| MRNASTOCK/USDT:USDT | below_1h_threshold | +0.51% | +0.51% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
