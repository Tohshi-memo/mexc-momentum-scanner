# Decision Report

- generated_at: 2026-08-12T02:06:18.196269+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11317**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.88% / filled 20/20。**
- 全期間 MARKET基準: n=11317, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.88%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.88% | **+0.88%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 17/20 | 85.0% | +1.45% | **+1.23%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.14% | **+1.02%** |
| MARKET | 20/20 | 100.0% | +0.88% | **+0.88%** |
| LIMIT_BB3S | 7/16 | 43.8% | +1.57% | **+0.69%** |
| LIMIT_ATR | 11/20 | 55.0% | +0.95% | **+0.52%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.09% | **+0.63%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.83% | **+0.58%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.72% | **+0.50%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +4.64% | **+0.46%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 180件 (TP 69 / SL 106 / EXP 5)
- 最新: JIMOTHY/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$616.77** / 初期 $100.00 (+516.77%)
- 確定: 3939件 (Win 1230 / Loss 1285 / Flat 1424) / skip 3939件
- 成長率目線: 平均log +0.000462 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BEAT/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $616.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$143.44** / 初期 $100.00 (+43.44%)
- 確定: 1568件 (Win 437 / Loss 364 / Flat 767) / skip 3160件
- 成長率目線: 平均log +0.000230 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SQD/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $143.44

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.83** / 初期 $100.00 (+14.83%)
- 確定: 1336件 (Win 408 / Loss 526 / Flat 402) / pending 4件 / skip 1452件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000113 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PROM/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $114.83

## 6. Latest Market Context

- 更新: 2026-08-12T02:06:11.709270+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=63805.0
- Funnel: target 967 → liquid 188 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HOLO/USDT:USDT | +29.39% | $5,385,913.76 |
| JIMOTHY/USDT:USDT | +28.85% | $1,823,062.66 |
| PROM/USDT:USDT | +21.55% | $6,095,311.71 |
| LSK/USDT:USDT | +17.46% | $3,315,527.98 |
| CRWVSTOCK/USDT:USDT | +17.19% | $3,866,632.97 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KORU/USDT:USDT | below_1h_threshold | +3.11% | +3.09% |
| JIMOTHY/USDT:USDT | below_1h_threshold | +2.94% | +2.92% |
| SNXX/USDT:USDT | below_1h_threshold | +2.70% | +2.69% |
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +2.59% | +2.58% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +2.30% | +2.29% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
