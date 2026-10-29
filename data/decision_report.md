# Decision Report

- generated_at: 2026-10-29T20:56:40.910789+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17809**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.12% / filled 20/20。**
- 全期間 MARKET基準: n=17809, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.12% | **+2.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.12% | **+2.12%** |
| LIMIT_BB3S | 4/14 | 28.6% | +5.35% | **+1.53%** |
| LIMIT_2PCT | 14/20 | 70.0% | +2.02% | **+1.41%** |
| LIMIT_3PCT | 12/20 | 60.0% | +2.26% | **+1.36%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.66% | **+1.32%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/6 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +2.34% | **+0.82%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.56% | **+0.71%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +2.04% | **+0.41%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +0.13% | **+0.09%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 256件 (TP 94 / SL 154 / EXP 8)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,531.22** / 初期 $100.00 (+1431.22%)
- 確定: 6804件 (Win 1975 / Loss 2180 / Flat 2649) / skip 7566件
- 成長率目線: 平均log +0.000401 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,531.22

## 4. Robust Adaptive DryRun ($100)

- 残高: **$362.93** / 初期 $100.00 (+262.93%)
- 確定: 4330件 (Win 1165 / Loss 980 / Flat 2185) / skip 6890件
- 成長率目線: 平均log +0.000298 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: Q/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $362.93

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5970件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000458 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-29T20:56:21.278326+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -2.18% price=79049.9
- Funnel: target 1086 → liquid 187 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PARTI/USDT:USDT | +67.76% | $5,015,806.29 |
| Q/USDT:USDT | +13.74% | $24,537,411.81 |
| SOXS/USDT:USDT | +12.71% | $77,309,979.50 |
| BLESS/USDT:USDT | +11.86% | $13,814,522.28 |
| BULLA/USDT:USDT | +4.41% | $1,660,092.04 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XMR/USDT:USDT | below_1h_threshold | +4.60% | +6.78% |
| AKE/USDT:USDT | below_1h_threshold | +4.41% | +6.59% |
| JCT/USDT:USDT | below_1h_threshold | +4.20% | +6.38% |
| MRNASTOCK/USDT:USDT | below_1h_threshold | +2.30% | +4.48% |
| FTNTSTOCK/USDT:USDT | below_1h_threshold | +1.66% | +3.83% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
