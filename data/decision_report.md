# Decision Report

- generated_at: 2026-09-23T05:01:09.383888+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15390**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.11% / filled 20/20。**
- 全期間 MARKET基準: n=15390, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.11%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.11% | **+1.11%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.11% | **+1.11%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.42% | **+0.35%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.49% | **+0.34%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_BB3S | 4/14 | 28.6% | +0.69% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/6 | 83.3% | +1.34% | **+1.12%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.76% | **+0.57%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +2.72% | **+0.41%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +0.97% | **+0.29%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,158.22** / 初期 $100.00 (+1058.22%)
- 確定: 5866件 (Win 1732 / Loss 1883 / Flat 2251) / skip 6085件
- 成長率目線: 平均log +0.000418 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MUBARAK/USDT:USDT `LIMIT_7PCT_LONG` SL_HIT account -0.50% 残高後 $1,158.22

## 4. Robust Adaptive DryRun ($100)

- 残高: **$249.51** / 初期 $100.00 (+149.51%)
- 確定: 3353件 (Win 926 / Loss 781 / Flat 1646) / skip 5448件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KERNEL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $249.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.43** / 初期 $100.00 (+22.43%)
- 確定: 3125件 (Win 920 / Loss 1226 / Flat 979) / pending 4件 / skip 3739件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `見送り` (no_strategy_passed_causal_filters) / causal_score n/a / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: USELESS/USDT:USDT `MARKET_LONG` EXPIRED account +0.07% 残高後 $122.43

## 6. Latest Market Context

- 更新: 2026-09-23T05:01:01.779618+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=87050.9
- Funnel: target 1058 → liquid 191 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SHROOM/USDT:USDT | +60.13% | $1,192,289.47 |
| NIL/USDT:USDT | +18.09% | $6,514,934.17 |
| ALLO/USDT:USDT | +17.96% | $2,619,522.13 |
| USELESS/USDT:USDT | +17.15% | $11,004,002.57 |
| PENGU/USDT:USDT | +16.76% | $16,323,780.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIL/USDT:USDT | below_1h_threshold | +1.23% | +1.30% |
| SAGA/USDT:USDT | below_1h_threshold | +0.53% | +0.61% |
| UNI/USDT:USDT | below_1h_threshold | +0.35% | +0.43% |
| 4/USDT:USDT | below_1h_threshold | +0.24% | +0.32% |
| DRIFT/USDT:USDT | below_1h_threshold | +0.14% | +0.22% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
