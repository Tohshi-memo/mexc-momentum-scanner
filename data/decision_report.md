# Decision Report

- generated_at: 2026-08-09T04:16:13.324441+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10933**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.00% / filled 20/20。**
- 全期間 MARKET基準: n=10933, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.00% | **+1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 12/20 | 60.0% | +2.54% | **+1.53%** |
| MARKET | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.01% | **+0.96%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.75% | **+0.64%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.87% | **+0.56%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +5.61% | **+0.84%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.16% | **+0.46%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.44% | **+0.20%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +0.33% | **+0.08%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | -0.25% | **-0.10%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$631.27** / 初期 $100.00 (+531.27%)
- 確定: 3930件 (Win 1230 / Loss 1280 / Flat 1420) / skip 3564件
- 成長率目線: 平均log +0.000469 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TST/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $631.27

## 4. Robust Adaptive DryRun ($100)

- 残高: **$142.00** / 初期 $100.00 (+42.00%)
- 確定: 1511件 (Win 424 / Loss 360 / Flat 727) / skip 2833件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score -0.0030 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CAT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $142.00

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.44** / 初期 $100.00 (+17.44%)
- 確定: 1248件 (Win 390 / Loss 480 / Flat 378) / pending 0件 / skip 1159件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `見送り` (no_strategy_passed_causal_filters) / causal_score n/a / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CAP/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account -0.10% 残高後 $117.44

## 6. Latest Market Context

- 更新: 2026-08-09T04:16:07.197609+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=64799.0
- Funnel: target 961 → liquid 152 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TUT/USDT:USDT | +97.68% | $30,822,230.44 |
| IOTX/USDT:USDT | +36.44% | $2,888,857.62 |
| BLUAI/USDT:USDT | +31.02% | $7,950,322.61 |
| SAGA/USDT:USDT | +30.80% | $1,636,159.95 |
| COOKIE/USDT:USDT | +24.74% | $4,133,584.70 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SAGA/USDT:USDT | below_1h_threshold | +4.56% | +4.50% |
| BEAT/USDT:USDT | below_1h_threshold | +3.87% | +3.80% |
| COOKIE/USDT:USDT | below_1h_threshold | +2.45% | +2.38% |
| MMT/USDT:USDT | below_1h_threshold | +2.31% | +2.25% |
| UB/USDT:USDT | below_1h_threshold | +2.10% | +2.04% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
