# Decision Report

- generated_at: 2026-09-19T05:26:12.772287+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14996**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.09% / filled 20/20。**
- 全期間 MARKET基準: n=14996, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.09%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.09% | **+2.09%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.09% | **+2.09%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.96% | **+1.37%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.34% | **+1.14%** |
| LIMIT_3PCT | 11/20 | 55.0% | +1.05% | **+0.58%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.49% | **+0.45%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.94% | **+0.42%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.89% | **+0.40%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.60% | **+0.30%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | -0.15% | **-0.07%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,195.40** / 初期 $100.00 (+1095.40%)
- 確定: 5640件 (Win 1691 / Loss 1829 / Flat 2120) / skip 5917件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,195.40

## 4. Robust Adaptive DryRun ($100)

- 残高: **$239.14** / 初期 $100.00 (+139.14%)
- 確定: 3178件 (Win 878 / Loss 760 / Flat 1540) / skip 5229件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ONE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $239.14

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.30** / 初期 $100.00 (+23.30%)
- 確定: 2968件 (Win 880 / Loss 1170 / Flat 918) / pending 2件 / skip 3496件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000226 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: VET/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $123.30

## 6. Latest Market Context

- 更新: 2026-09-19T05:26:04.160015+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=81058.2
- Funnel: target 1050 → liquid 170 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +79.42% | $44,959,628.30 |
| ONE/USDT:USDT | +39.05% | $26,027,681.03 |
| AR/USDT:USDT | +30.36% | $5,832,954.51 |
| SAGA/USDT:USDT | +25.33% | $4,267,932.23 |
| CATE/USDT:USDT | +22.95% | $1,472,744.56 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SYN/USDT:USDT | below_1h_threshold | +3.54% | +3.47% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +3.12% | +3.04% |
| CATE/USDT:USDT | below_1h_threshold | +2.41% | +2.34% |
| XTZ/USDT:USDT | below_1h_threshold | +1.98% | +1.90% |
| MYX/USDT:USDT | below_1h_threshold | +1.85% | +1.78% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
