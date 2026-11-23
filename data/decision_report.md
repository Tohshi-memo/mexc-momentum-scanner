# Decision Report

- generated_at: 2026-11-23T05:21:30.353464+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19420**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.95% / filled 20/20。**
- 全期間 MARKET基準: n=19420, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.95%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.95% | **+1.95%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.95% | **+1.95%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_5PCT | 4/20 | 20.0% | +2.71% | **+0.54%** |
| LIMIT_1PCT | 13/20 | 65.0% | +0.45% | **+0.29%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.11% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.40% | **+0.42%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.64% | **+0.35%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.51% | **+0.26%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.42% | **+0.25%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 285件 (TP 103 / SL 174 / EXP 8)
- 最新: BLESS/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,827.87** / 初期 $100.00 (+1727.87%)
- 確定: 7520件 (Win 2160 / Loss 2423 / Flat 2937) / skip 8461件
- 成長率目線: 平均log +0.000386 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_FIB1272_LONG` TP_HIT account +1.00% 残高後 $1,827.87

## 4. Robust Adaptive DryRun ($100)

- 残高: **$462.21** / 初期 $100.00 (+362.21%)
- 確定: 5182件 (Win 1381 / Loss 1117 / Flat 2684) / skip 7649件
- 成長率目線: 平均log +0.000295 / 幾何平均 +0.030% per trade / maxDD +4.29%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0091 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $462.21

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7581件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000225 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-23T05:21:17.028270+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=61317.6
- Funnel: target 1086 → liquid 116 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SI/USDT:USDT | +62.04% | $1,578,401.02 |
| ELSA/USDT:USDT | +22.27% | $1,804,205.47 |
| BULLA/USDT:USDT | +11.21% | $2,542,449.97 |
| ARIA/USDT:USDT | +9.55% | $1,619,207.87 |
| IDOL/USDT:USDT | +9.36% | $2,191,480.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PIEVERSE/USDT:USDT | below_1h_threshold | +3.24% | +3.08% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +2.31% | +2.15% |
| ELSA/USDT:USDT | below_1h_threshold | +1.57% | +1.40% |
| JUP/USDT:USDT | below_1h_threshold | +1.55% | +1.39% |
| MUU/USDT:USDT | below_1h_threshold | +1.51% | +1.35% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
