# Decision Report

- generated_at: 2026-10-13T09:51:20.465837+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16635**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.64% / filled 20/20。**
- 全期間 MARKET基準: n=16635, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.64%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.64% | **+1.64%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.64% | **+1.64%** |
| LIMIT_BB3S | 3/14 | 21.4% | +3.86% | **+0.83%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.76% | **+0.64%** |
| LIMIT_10PCT | 3/20 | 15.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | -0.11% | **-0.05%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +1.20% | **+0.60%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_BB3S_LONG | 4/6 | 66.7% | +0.76% | **+0.51%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.32% | **+0.27%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | -0.02% | **-0.02%** |

## 2. $100 Live Portfolio

- 残高: **$121.72** / 初期 $100.00 (+21.72%)
- 確定トレード: 238件 (TP 89 / SL 142 / EXP 7)
- 最新: BATON/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.72
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,285.29** / 初期 $100.00 (+1185.29%)
- 確定: 6294件 (Win 1845 / Loss 2017 / Flat 2432) / skip 6902件
- 成長率目線: 平均log +0.000406 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MAGIC/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,285.29

## 4. Robust Adaptive DryRun ($100)

- 残高: **$271.50** / 初期 $100.00 (+171.50%)
- 確定: 3651件 (Win 1014 / Loss 862 / Flat 1775) / skip 6395件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KAIA/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $271.50

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4795件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000124 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-13T09:51:08.659413+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=83582.2
- Funnel: target 1089 → liquid 194 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| OGN/USDT:USDT | +19.98% | $6,481,499.35 |
| BAT/USDT:USDT | +16.31% | $13,765,172.77 |
| SYN/USDT:USDT | +8.83% | $1,937,192.49 |
| CT/USDT:USDT | +8.42% | $5,327,031.12 |
| STX/USDT:USDT | +7.67% | $17,329,365.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| OGN/USDT:USDT | below_1h_threshold | +3.91% | +3.88% |
| BTW/USDT:USDT | below_1h_threshold | +1.75% | +1.72% |
| SAFE/USDT:USDT | below_1h_threshold | +1.71% | +1.68% |
| STX/USDT:USDT | below_1h_threshold | +0.64% | +0.60% |
| TIA/USDT:USDT | below_1h_threshold | +0.45% | +0.41% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
