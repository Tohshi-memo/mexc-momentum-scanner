# Decision Report

- generated_at: 2026-08-14T16:41:28.520382+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11576**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.31% / filled 20/20。**
- 全期間 MARKET基準: n=11576, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.31%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.31% | **+0.31%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 13/20 | 65.0% | +1.38% | **+0.90%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.96% | **+0.72%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.73% | **+0.62%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| MARKET | 20/20 | 100.0% | +0.31% | **+0.31%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.79% | **+1.26%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +3.43% | **+1.20%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.47% | **+0.99%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.98% | **+0.69%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$631.24** / 初期 $100.00 (+531.24%)
- 確定: 4044件 (Win 1270 / Loss 1331 / Flat 1443) / skip 4093件
- 成長率目線: 平均log +0.000456 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EDEN/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.44% 残高後 $631.24

## 4. Robust Adaptive DryRun ($100)

- 残高: **$149.41** / 初期 $100.00 (+49.41%)
- 確定: 1651件 (Win 471 / Loss 398 / Flat 782) / skip 3336件
- 成長率目線: 平均log +0.000243 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0314 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $149.41

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.64** / 初期 $100.00 (+17.64%)
- 確定: 1534件 (Win 467 / Loss 586 / Flat 481) / pending 5件 / skip 1511件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000218 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: EDEN/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $117.64

## 6. Latest Market Context

- 更新: 2026-08-14T16:41:17.902168+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.34% price=63172.1
- Funnel: target 985 → liquid 176 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +6.13% | $5,275,577.81 |
| ACE/USDT:USDT | +3.86% | $49,966,461.33 |
| MANA/USDT:USDT | +3.02% | $1,462,641.82 |
| GPS/USDT:USDT | +2.03% | $1,102,869.01 |
| NBISSTOCK/USDT:USDT | +1.77% | $9,887,070.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ACE/USDT:USDT | below_1h_threshold | +4.10% | +3.75% |
| MANA/USDT:USDT | below_1h_threshold | +3.02% | +2.68% |
| GPS/USDT:USDT | below_1h_threshold | +2.01% | +1.67% |
| RIVER/USDT:USDT | below_1h_threshold | +1.64% | +1.29% |
| EDEN/USDT:USDT | below_1h_threshold | +1.62% | +1.28% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
