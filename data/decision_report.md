# Decision Report

- generated_at: 2026-09-14T09:41:18.998983+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14507**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.60% / filled 20/20。**
- 全期間 MARKET基準: n=14507, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.60% | **+2.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.60% | **+2.60%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.95% | **+1.66%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.89% | **+1.42%** |
| LIMIT_3PCT | 12/20 | 60.0% | +1.02% | **+0.61%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.49% | **+0.45%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 12/20 | 60.0% | +0.95% | **+0.57%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +0.96% | **+0.43%** |
| LIMIT_4PCT_LONG | 16/20 | 80.0% | +0.50% | **+0.40%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +2.54% | **+0.38%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,072.50** / 初期 $100.00 (+972.50%)
- 確定: 5440件 (Win 1637 / Loss 1766 / Flat 2037) / skip 5628件
- 成長率目線: 平均log +0.000436 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ARK/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $1,072.50

## 4. Robust Adaptive DryRun ($100)

- 残高: **$227.62** / 初期 $100.00 (+127.62%)
- 確定: 2991件 (Win 830 / Loss 716 / Flat 1445) / skip 4927件
- 成長率目線: 平均log +0.000275 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $227.62

## 5. Causal Adaptive DryRun ($100)

- 残高: **$125.76** / 初期 $100.00 (+25.76%)
- 確定: 2887件 (Win 859 / Loss 1119 / Flat 909) / pending 3件 / skip 3089件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000064 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ARK/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $125.76

## 6. Latest Market Context

- 更新: 2026-09-14T09:41:10.587233+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=77783.6
- Funnel: target 1068 → liquid 151 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIN/USDT:USDT | +52.17% | $2,586,157.20 |
| CATE/USDT:USDT | +49.86% | $1,950,690.34 |
| BR/USDT:USDT | +49.27% | $7,584,998.78 |
| KOMA/USDT:USDT | +28.02% | $1,003,172.65 |
| MTL/USDT:USDT | +22.83% | $1,325,970.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CATE/USDT:USDT | below_1h_threshold | +3.32% | +3.22% |
| AKE/USDT:USDT | below_1h_threshold | +3.28% | +3.17% |
| SOXS/USDT:USDT | below_1h_threshold | +2.26% | +2.15% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.64% | +1.53% |
| PONS/USDT:USDT | below_1h_threshold | +1.22% | +1.11% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
