# Decision Report

- generated_at: 2026-09-15T02:01:21.162238+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14547**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.84% / filled 20/20。**
- 全期間 MARKET基準: n=14547, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.84%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.84% | **+1.84%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.84% | **+1.84%** |
| LIMIT_8PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +2.30% | **+0.92%** |
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.73% | **+0.55%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +1.10% | **+0.73%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.44% | **+0.20%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +0.75% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 213件 (TP 79 / SL 129 / EXP 5)
- 最新: STORJ/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,062.96** / 初期 $100.00 (+962.96%)
- 確定: 5449件 (Win 1638 / Loss 1770 / Flat 2041) / skip 5659件
- 成長率目線: 平均log +0.000434 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIN/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,062.96

## 4. Robust Adaptive DryRun ($100)

- 残高: **$227.62** / 初期 $100.00 (+127.62%)
- 確定: 2992件 (Win 830 / Loss 716 / Flat 1446) / skip 4966件
- 成長率目線: 平均log +0.000275 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score +0.0090 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AIN/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $227.62

## 5. Causal Adaptive DryRun ($100)

- 残高: **$125.53** / 初期 $100.00 (+25.53%)
- 確定: 2893件 (Win 860 / Loss 1122 / Flat 911) / pending 5件 / skip 3121件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000526 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AIN/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $125.53

## 6. Latest Market Context

- 更新: 2026-09-15T02:01:10.296650+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=77899.2
- Funnel: target 1073 → liquid 159 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIN/USDT:USDT | +35.47% | $7,155,392.49 |
| SHROOM/USDT:USDT | +21.02% | $1,259,367.38 |
| POWER/USDT:USDT | +20.04% | $6,015,767.00 |
| CNPY/USDT:USDT | +17.85% | $1,770,634.38 |
| CAP/USDT:USDT | +14.83% | $2,535,799.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SHROOM/USDT:USDT | below_1h_threshold | +0.95% | +0.93% |
| CAP/USDT:USDT | below_1h_threshold | +0.58% | +0.56% |
| POWER/USDT:USDT | below_1h_threshold | +0.53% | +0.52% |
| AIN/USDT:USDT | below_1h_threshold | +0.52% | +0.50% |
| USELESS/USDT:USDT | below_1h_threshold | +0.46% | +0.45% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
