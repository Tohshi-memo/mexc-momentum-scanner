# Decision Report

- generated_at: 2026-09-27T12:51:12.672275+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15644**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.46% / filled 20/20。**
- 全期間 MARKET基準: n=15644, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.46%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.46% | **+2.46%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.46% | **+2.46%** |
| LIMIT_1PCT | 16/20 | 80.0% | +2.77% | **+2.22%** |
| LIMIT_2PCT | 10/20 | 50.0% | +1.48% | **+0.74%** |
| LIMIT_BB3S | 5/17 | 29.4% | +2.15% | **+0.63%** |
| LIMIT_ATR | 10/20 | 50.0% | +0.99% | **+0.50%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +2.41% | **+1.21%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.50% | **+0.60%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | -0.12% | **-0.07%** |

## 2. $100 Live Portfolio

- 残高: **$120.87** / 初期 $100.00 (+20.87%)
- 確定トレード: 224件 (TP 82 / SL 135 / EXP 7)
- 最新: UNI/USDT:USDT EXPIRED PnL +1.69% 残高後 $120.87
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,239.61** / 初期 $100.00 (+1139.61%)
- 確定: 5979件 (Win 1766 / Loss 1923 / Flat 2290) / skip 6226件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: QNT/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,239.61

## 4. Robust Adaptive DryRun ($100)

- 残高: **$263.08** / 初期 $100.00 (+163.08%)
- 確定: 3534件 (Win 974 / Loss 812 / Flat 1748) / skip 5521件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0560 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: QNT/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $263.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.97** / 初期 $100.00 (+18.97%)
- 確定: 3226件 (Win 946 / Loss 1276 / Flat 1004) / pending 5件 / skip 3885件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000087 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: QNT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $118.97

## 6. Latest Market Context

- 更新: 2026-09-27T12:51:03.668068+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=84920.0
- Funnel: target 1070 → liquid 144 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=1, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| QNT/USDT:USDT | +37.47% | $134,318,345.31 |
| SOONNETWORK/USDT:USDT | +31.97% | $2,668,695.51 |
| Q/USDT:USDT | +20.71% | $1,019,688.14 |
| GRASS/USDT:USDT | +17.95% | $6,444,494.06 |
| US/USDT:USDT | +16.88% | $1,171,541.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JASMY/USDT:USDT | below_relative_strength | +5.06% | +4.99% |
| US/USDT:USDT | below_1h_threshold | +4.13% | +4.05% |
| PENGU/USDT:USDT | below_1h_threshold | +3.40% | +3.33% |
| SOONNETWORK/USDT:USDT | below_1h_threshold | +2.47% | +2.40% |
| SUI/USDT:USDT | below_1h_threshold | +1.69% | +1.62% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
