# Decision Report

- generated_at: 2026-09-16T00:06:16.241597+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14620**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.39% / filled 20/20。**
- 全期間 MARKET基準: n=14620, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.39% | **+2.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 17/20 | 85.0% | +3.31% | **+2.81%** |
| MARKET | 20/20 | 100.0% | +2.39% | **+2.39%** |
| LIMIT_2PCT | 14/20 | 70.0% | +2.04% | **+1.43%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +2.42% | **+0.97%** |
| LIMIT_ATR | 10/20 | 50.0% | +1.15% | **+0.58%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 12/20 | 60.0% | +0.41% | **+0.25%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | -1.45% | **-0.15%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | -0.44% | **-0.20%** |
| LIMIT_6PCT_LONG | 13/20 | 65.0% | -0.34% | **-0.22%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | -2.09% | **-0.52%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,044.12** / 初期 $100.00 (+944.12%)
- 確定: 5517件 (Win 1645 / Loss 1786 / Flat 2086) / skip 5664件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIN/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $1,044.12

## 4. Robust Adaptive DryRun ($100)

- 残高: **$230.42** / 初期 $100.00 (+130.42%)
- 確定: 3054件 (Win 839 / Loss 719 / Flat 1496) / skip 4977件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0382 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $230.42

## 5. Causal Adaptive DryRun ($100)

- 残高: **$124.74** / 初期 $100.00 (+24.74%)
- 確定: 2912件 (Win 865 / Loss 1134 / Flat 913) / pending 1件 / skip 3176件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000448 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CNPY/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $124.74

## 6. Latest Market Context

- 更新: 2026-09-16T00:06:06.263716+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=75714.3
- Funnel: target 1060 → liquid 154 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=1, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ON/USDT:USDT | +19.19% | $1,756,036.89 |
| CNPY/USDT:USDT | +16.43% | $1,782,497.11 |
| SAGA/USDT:USDT | +15.55% | $7,437,783.89 |
| SYN/USDT:USDT | +14.82% | $1,393,621.28 |
| 4/USDT:USDT | +7.42% | $1,351,239.17 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CNPY/USDT:USDT | below_relative_strength | +5.04% | +4.88% |
| USELESS/USDT:USDT | below_1h_threshold | +1.49% | +1.33% |
| 4/USDT:USDT | below_1h_threshold | +1.20% | +1.04% |
| ON/USDT:USDT | below_1h_threshold | +0.92% | +0.77% |
| ARB/USDT:USDT | below_1h_threshold | +0.62% | +0.47% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
