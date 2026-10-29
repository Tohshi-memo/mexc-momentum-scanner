# Decision Report

- generated_at: 2026-10-29T20:01:22.032470+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17803**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.72% / filled 20/20。**
- 全期間 MARKET基準: n=17803, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.72%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.72% | **+2.72%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.72% | **+2.72%** |
| LIMIT_1PCT | 16/20 | 80.0% | +2.34% | **+1.87%** |
| LIMIT_BB3S | 5/12 | 41.7% | +4.28% | **+1.78%** |
| LIMIT_2PCT | 13/20 | 65.0% | +2.48% | **+1.61%** |
| LIMIT_3PCT | 10/20 | 50.0% | +2.31% | **+1.16%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +3.70% | **+1.11%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.56% | **+0.71%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | +0.73% | **+0.40%** |
| LIMIT_7PCT_LONG | 12/20 | 60.0% | +0.46% | **+0.28%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | -0.07% | **-0.04%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 256件 (TP 94 / SL 154 / EXP 8)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,531.22** / 初期 $100.00 (+1431.22%)
- 確定: 6804件 (Win 1975 / Loss 2180 / Flat 2649) / skip 7560件
- 成長率目線: 平均log +0.000401 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,531.22

## 4. Robust Adaptive DryRun ($100)

- 残高: **$362.93** / 初期 $100.00 (+262.93%)
- 確定: 4324件 (Win 1165 / Loss 980 / Flat 2179) / skip 6890件
- 成長率目線: 平均log +0.000298 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PARTI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $362.93

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5965件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000263 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-29T20:01:09.079363+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=80796.6
- Funnel: target 1086 → liquid 175 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PARTI/USDT:USDT | +73.74% | $4,423,403.73 |
| BLESS/USDT:USDT | +15.31% | $12,409,794.81 |
| BULLA/USDT:USDT | +8.99% | $1,586,533.36 |
| AIN/USDT:USDT | +2.94% | $3,584,310.69 |
| UAI/USDT:USDT | +2.64% | $2,786,868.82 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MRNASTOCK/USDT:USDT | below_1h_threshold | +2.30% | +2.31% |
| FTNTSTOCK/USDT:USDT | below_1h_threshold | +1.66% | +1.67% |
| PLTRSTOCK/USDT:USDT | below_1h_threshold | +1.28% | +1.30% |
| EWY/USDT:USDT | below_1h_threshold | +1.10% | +1.12% |
| ORCLSTOCK/USDT:USDT | below_1h_threshold | +1.10% | +1.11% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
