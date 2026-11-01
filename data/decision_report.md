# Decision Report

- generated_at: 2026-11-01T01:46:18.449633+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17919**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.98% / filled 20/20。**
- 全期間 MARKET基準: n=17919, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.98%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.98% | **+2.98%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.98% | **+2.98%** |
| LIMIT_2PCT | 13/20 | 65.0% | +2.89% | **+1.88%** |
| LIMIT_1PCT | 16/20 | 80.0% | +2.17% | **+1.74%** |
| LIMIT_ATR | 11/20 | 55.0% | +2.38% | **+1.31%** |
| LIMIT_BB3S | 6/16 | 37.5% | +2.79% | **+1.05%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.00% | **+0.40%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | -1.65% | **-0.41%** |

## 2. $100 Live Portfolio

- 残高: **$121.74** / 初期 $100.00 (+21.74%)
- 確定トレード: 257件 (TP 95 / SL 154 / EXP 8)
- 最新: JCT/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.74
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,485.74** / 初期 $100.00 (+1385.74%)
- 確定: 6821件 (Win 1976 / Loss 2188 / Flat 2657) / skip 7659件
- 成長率目線: 平均log +0.000396 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `MARKET` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GANG/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $1,485.74

## 4. Robust Adaptive DryRun ($100)

- 残高: **$370.19** / 初期 $100.00 (+270.19%)
- 確定: 4418件 (Win 1185 / Loss 983 / Flat 2250) / skip 6912件
- 成長率目線: 平均log +0.000296 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: Q/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $370.19

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6078件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000494 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-01T01:46:05.414158+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=77706.8
- Funnel: target 1089 → liquid 118 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| GANG/USDT:USDT | +21.18% | $1,109,882.15 |
| POWR/USDT:USDT | +20.26% | $1,076,664.41 |
| LIT/USDT:USDT | +8.36% | $15,462,696.95 |
| AIN/USDT:USDT | +6.60% | $23,692,015.14 |
| MAGMA/USDT:USDT | +5.34% | $1,390,437.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIN/USDT:USDT | below_1h_threshold | +3.74% | +3.66% |
| POWR/USDT:USDT | below_1h_threshold | +3.41% | +3.33% |
| EVAA/USDT:USDT | below_1h_threshold | +2.28% | +2.20% |
| PONS/USDT:USDT | below_1h_threshold | +1.59% | +1.51% |
| VVV/USDT:USDT | below_1h_threshold | +1.56% | +1.48% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
