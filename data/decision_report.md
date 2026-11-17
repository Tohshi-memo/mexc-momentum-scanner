# Decision Report

- generated_at: 2026-11-17T15:51:26.504853+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19083**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.91% / filled 20/20。**
- 全期間 MARKET基準: n=19083, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.91%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.91% | **+0.91%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.07% | **+1.01%** |
| MARKET | 20/20 | 100.0% | +0.91% | **+0.91%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.92% | **+0.67%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.64% | **+0.45%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +0.44% | **+0.13%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.05% | **+0.03%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | -0.37% | **-0.16%** |

## 2. $100 Live Portfolio

- 残高: **$121.13** / 初期 $100.00 (+21.13%)
- 確定トレード: 277件 (TP 100 / SL 169 / EXP 8)
- 最新: BTW/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.13
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,677.36** / 初期 $100.00 (+1577.36%)
- 確定: 7351件 (Win 2109 / Loss 2358 / Flat 2884) / skip 8293件
- 成長率目線: 平均log +0.000384 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $1,677.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$430.10** / 初期 $100.00 (+330.10%)
- 確定: 4992件 (Win 1332 / Loss 1081 / Flat 2579) / skip 7502件
- 成長率目線: 平均log +0.000292 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $430.10

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7242件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000149 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-17T15:51:10.402236+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -1.90% price=63744.3
- Funnel: target 1073 → liquid 142 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BREV/USDT:USDT | +76.62% | $4,732,316.33 |
| CLAUDIA/USDT:USDT | +32.86% | $1,463,260.70 |
| UVXY/USDT:USDT | +15.22% | $1,444,000.97 |
| AGT/USDT:USDT | +12.30% | $1,695,952.11 |
| SOXS/USDT:USDT | +10.96% | $36,539,269.20 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BREV/USDT:USDT | below_1h_threshold | +4.22% | +6.12% |
| CBRSSTOCK/USDT:USDT | below_1h_threshold | +3.69% | +5.60% |
| EVAA/USDT:USDT | below_1h_threshold | +3.42% | +5.33% |
| SOXS/USDT:USDT | below_1h_threshold | +3.19% | +5.09% |
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +2.04% | +3.94% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
