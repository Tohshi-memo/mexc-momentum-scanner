# Decision Report

- generated_at: 2026-10-29T20:31:26.440711+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17806**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.72% / filled 20/20。**
- 全期間 MARKET基準: n=17806, expectancy=+0.02%
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
| LIMIT_1PCT | 17/20 | 85.0% | +2.67% | **+2.27%** |
| LIMIT_BB3S | 6/14 | 42.9% | +4.90% | **+2.10%** |
| LIMIT_2PCT | 14/20 | 70.0% | +2.87% | **+2.01%** |
| LIMIT_3PCT | 11/20 | 55.0% | +2.83% | **+1.56%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/6 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +2.34% | **+0.82%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.56% | **+0.71%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +2.52% | **+0.38%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 256件 (TP 94 / SL 154 / EXP 8)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,531.22** / 初期 $100.00 (+1431.22%)
- 確定: 6804件 (Win 1975 / Loss 2180 / Flat 2649) / skip 7563件
- 成長率目線: 平均log +0.000401 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,531.22

## 4. Robust Adaptive DryRun ($100)

- 残高: **$362.93** / 初期 $100.00 (+262.93%)
- 確定: 4327件 (Win 1165 / Loss 980 / Flat 2182) / skip 6890件
- 成長率目線: 平均log +0.000298 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PARTI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $362.93

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5965件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000452 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-29T20:31:13.764637+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.52% price=80390.3
- Funnel: target 1086 → liquid 179 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PARTI/USDT:USDT | +70.50% | $4,802,330.81 |
| BLESS/USDT:USDT | +14.66% | $13,304,971.19 |
| SOXS/USDT:USDT | +11.58% | $76,307,551.57 |
| BULLA/USDT:USDT | +8.95% | $1,610,324.79 |
| USOIL/USDT:USDT | +2.16% | $117,124,554.58 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +3.29% | +3.81% |
| MRNASTOCK/USDT:USDT | below_1h_threshold | +2.30% | +2.82% |
| FTNTSTOCK/USDT:USDT | below_1h_threshold | +1.66% | +2.18% |
| PLTRSTOCK/USDT:USDT | below_1h_threshold | +1.28% | +1.80% |
| SNXX/USDT:USDT | below_1h_threshold | +0.87% | +1.39% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
