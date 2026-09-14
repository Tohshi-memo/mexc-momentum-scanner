# Decision Report

- generated_at: 2026-09-14T13:46:27.998855+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14521**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.72% / filled 20/20。**
- 全期間 MARKET基準: n=14521, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+3.72%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.72% | **+3.72%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.72% | **+3.72%** |
| LIMIT_1PCT | 17/20 | 85.0% | +3.30% | **+2.81%** |
| LIMIT_2PCT | 14/20 | 70.0% | +2.73% | **+1.91%** |
| LIMIT_3PCT | 11/20 | 55.0% | +2.56% | **+1.41%** |
| LIMIT_ATR | 10/20 | 50.0% | +1.89% | **+0.95%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 13/20 | 65.0% | +1.27% | **+0.82%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +2.23% | **+0.33%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +0.55% | **+0.16%** |
| LIMIT_8PCT_LONG | 12/20 | 60.0% | -0.33% | **-0.20%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | -1.93% | **-0.29%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,052.44** / 初期 $100.00 (+952.44%)
- 確定: 5445件 (Win 1637 / Loss 1770 / Flat 2038) / skip 5637件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $1,052.44

## 4. Robust Adaptive DryRun ($100)

- 残高: **$227.62** / 初期 $100.00 (+127.62%)
- 確定: 2992件 (Win 830 / Loss 716 / Flat 1446) / skip 4940件
- 成長率目線: 平均log +0.000275 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0072 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AIN/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $227.62

## 5. Causal Adaptive DryRun ($100)

- 残高: **$125.54** / 初期 $100.00 (+25.54%)
- 確定: 2890件 (Win 859 / Loss 1120 / Flat 911) / pending 0件 / skip 3101件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000322 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PUNDIX/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $125.54

## 6. Latest Market Context

- 更新: 2026-09-14T13:46:15.209012+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.66% price=78176.3
- Funnel: target 1068 → liquid 160 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BR/USDT:USDT | +72.76% | $25,395,227.56 |
| AIN/USDT:USDT | +50.90% | $3,780,040.91 |
| CATE/USDT:USDT | +47.29% | $2,250,590.99 |
| CAP/USDT:USDT | +46.26% | $1,312,471.60 |
| KOMA/USDT:USDT | +21.24% | $1,099,726.14 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| T/USDT:USDT | below_1h_threshold | +3.05% | +2.39% |
| UNI/USDT:USDT | below_1h_threshold | +2.44% | +1.78% |
| CAP/USDT:USDT | below_1h_threshold | +2.34% | +1.68% |
| B/USDT:USDT | below_1h_threshold | +2.13% | +1.47% |
| ZEC/USDT:USDT | below_1h_threshold | +1.94% | +1.28% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
