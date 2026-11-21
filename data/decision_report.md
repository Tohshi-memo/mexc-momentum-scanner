# Decision Report

- generated_at: 2026-11-21T08:01:27.091213+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19288**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.68% / filled 20/20。**
- 全期間 MARKET基準: n=19288, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.68%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.68% | **+0.68%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 16/20 | 80.0% | +2.36% | **+1.89%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +3.77% | **+1.51%** |
| LIMIT_10PCT | 3/20 | 15.0% | +6.45% | **+0.97%** |
| LIMIT_9PCT | 3/20 | 15.0% | +6.45% | **+0.97%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.81% | **+0.69%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +6.56% | **+1.31%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +3.86% | **+0.96%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +1.33% | **+0.93%** |
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +1.16% | **+0.93%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.56% | **+0.86%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 283件 (TP 103 / SL 172 / EXP 8)
- 最新: INTCSTOCK/USDT:USDT TP_HIT PnL +5.26% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,660.88** / 初期 $100.00 (+1560.88%)
- 確定: 7431件 (Win 2135 / Loss 2397 / Flat 2899) / skip 8418件
- 成長率目線: 平均log +0.000378 / 幾何平均 +0.038% per trade / maxDD +9.04%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DCTY/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $1,660.88

## 4. Robust Adaptive DryRun ($100)

- 残高: **$447.64** / 初期 $100.00 (+347.64%)
- 確定: 5093件 (Win 1357 / Loss 1088 / Flat 2648) / skip 7606件
- 成長率目線: 平均log +0.000294 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DCTY/USDT:USDT `LIMIT_FIB1272` TP_HIT account +0.69% 残高後 $447.64

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7447件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000166 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-21T08:01:11.012030+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=57854.8
- Funnel: target 1086 → liquid 158 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLESS/USDT:USDT | +34.18% | $23,747,728.61 |
| DCTY/USDT:USDT | +19.95% | $1,240,378.76 |
| PIEVERSE/USDT:USDT | +17.44% | $4,104,776.60 |
| BTW/USDT:USDT | +14.97% | $4,109,225.98 |
| UVXY/USDT:USDT | +10.25% | $6,109,622.22 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DCTY/USDT:USDT | below_1h_threshold | +1.88% | +2.07% |
| SOXS/USDT:USDT | below_1h_threshold | +1.81% | +2.00% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +0.75% | +0.94% |
| UVXY/USDT:USDT | below_1h_threshold | +0.47% | +0.66% |
| BLESS/USDT:USDT | below_1h_threshold | +0.44% | +0.63% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
