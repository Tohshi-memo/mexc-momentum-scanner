# Decision Report

- generated_at: 2026-07-21T21:21:42.178484+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9209**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.99% / filled 20/20。**
- 全期間 MARKET基準: n=9209, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.99%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.99% | **+1.99%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.99% | **+1.99%** |
| LIMIT_1PCT | 15/20 | 75.0% | +0.38% | **+0.29%** |
| LIMIT_6PCT | 6/20 | 30.0% | -0.92% | **-0.27%** |
| LIMIT_7PCT | 5/20 | 25.0% | -1.11% | **-0.28%** |
| LIMIT_5PCT | 7/20 | 35.0% | -0.92% | **-0.32%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.10% | **+0.27%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.00% | **+0.00%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | -0.15% | **-0.14%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | -0.29% | **-0.14%** |
| MARKET_LONG | 20/20 | 100.0% | -0.45% | **-0.45%** |

## 2. $100 Live Portfolio

- 残高: **$105.38** / 初期 $100.00 (+5.38%)
- 確定トレード: 130件 (TP 44 / SL 81 / EXP 5)
- 最新: QNTSTOCK/USDT:USDT SL_HIT PnL -3.23% 残高後 $105.38
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$419.29** / 初期 $100.00 (+319.29%)
- 確定: 3249件 (Win 1021 / Loss 1039 / Flat 1189) / skip 2521件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.12% 残高後 $419.29

## 4. Robust Adaptive DryRun ($100)

- 残高: **$131.28** / 初期 $100.00 (+31.28%)
- 確定: 1159件 (Win 312 / Loss 252 / Flat 595) / skip 1461件
- 成長率目線: 平均log +0.000235 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RIF/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $131.28

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.03** / 初期 $100.00 (+1.03%)
- 確定: 360件 (Win 123 / Loss 155 / Flat 82) / pending 6件 / skip 320件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000109 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BOTSTOCK/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $101.03

## 6. Latest Market Context

- 更新: 2026-07-21T21:21:29.973624+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=66312.8
- Funnel: target 885 → liquid 177 → pre 50 → checked 50 → surge 6 → strict 1
- Surge前reject: below_1h_threshold=44, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.8 >= 65=1, 4h RSI 75.1 >= 65=1, 4h RSI 72.5 >= 65=1, 4h RSI 70.0 >= 65=1, 4h RSI 66.2 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SMCISTOCK/USDT:USDT | +17.64% | $2,261,675.87 |
| FWDISTOCK/USDT:USDT | +16.53% | $3,303,081.90 |
| SNXX/USDT:USDT | +11.92% | $1,313,524.87 |
| BEAT/USDT:USDT | +11.62% | $10,681,460.89 |
| BOTSTOCK/USDT:USDT | +8.73% | $2,527,211.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SNXX/USDT:USDT | below_1h_threshold | +4.48% | +4.57% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.81% | +2.90% |
| HEMI/USDT:USDT | below_1h_threshold | +2.52% | +2.61% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +2.13% | +2.22% |
| KORU/USDT:USDT | below_1h_threshold | +2.07% | +2.16% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
