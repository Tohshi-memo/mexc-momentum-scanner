# Decision Report

- generated_at: 2026-08-16T04:16:31.394479+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11714**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.63% / filled 20/20。**
- 全期間 MARKET基準: n=11714, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.63%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.63% | **+0.63%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 18/20 | 90.0% | +1.96% | **+1.76%** |
| LIMIT_ATR | 14/20 | 70.0% | +2.01% | **+1.41%** |
| LIMIT_3PCT | 14/20 | 70.0% | +1.65% | **+1.16%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.08% | **+1.03%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.57% | **+0.71%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.28% | **+0.58%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.31% | **+0.52%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.44% | **+0.37%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.65% | **+0.36%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.68% | **+0.24%** |

## 2. $100 Live Portfolio

- 残高: **$121.53** / 初期 $100.00 (+21.53%)
- 確定トレード: 183件 (TP 71 / SL 107 / EXP 5)
- 最新: MOVR/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.53
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$630.31** / 初期 $100.00 (+530.31%)
- 確定: 4180件 (Win 1292 / Loss 1360 / Flat 1528) / skip 4095件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CROSS/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.02% 残高後 $630.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.79** / 初期 $100.00 (+54.79%)
- 確定: 1768件 (Win 493 / Loss 416 / Flat 859) / skip 3357件
- 成長率目線: 平均log +0.000247 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CROSS/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.03% 残高後 $154.79

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.28** / 初期 $100.00 (+19.28%)
- 確定: 1626件 (Win 495 / Loss 618 / Flat 513) / pending 0件 / skip 1559件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000087 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: H/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $119.28

## 6. Latest Market Context

- 更新: 2026-08-16T04:16:20.320867+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=63099.9
- Funnel: target 986 → liquid 135 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEMI/USDT:USDT | +21.06% | $5,490,534.74 |
| SPORTFUN/USDT:USDT | +18.07% | $4,291,224.23 |
| CROSS/USDT:USDT | +17.17% | $1,209,856.86 |
| H/USDT:USDT | +14.81% | $6,694,465.72 |
| BASED/USDT:USDT | +11.65% | $2,074,498.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BICO/USDT:USDT | below_1h_threshold | +2.38% | +2.37% |
| AIO/USDT:USDT | below_1h_threshold | +2.20% | +2.20% |
| HEMI/USDT:USDT | below_1h_threshold | +1.23% | +1.22% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.04% | +1.03% |
| H/USDT:USDT | below_1h_threshold | +1.04% | +1.03% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
