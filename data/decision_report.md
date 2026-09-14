# Decision Report

- generated_at: 2026-09-14T15:51:28.467515+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14524**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.92% / filled 20/20。**
- 全期間 MARKET基準: n=14524, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.92% | **+1.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +2.23% | **+2.01%** |
| MARKET | 20/20 | 100.0% | +1.92% | **+1.92%** |
| LIMIT_3PCT | 14/20 | 70.0% | +2.22% | **+1.56%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.89% | **+1.51%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.95% | **+1.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +1.69% | **+0.93%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -0.65% | **-0.07%** |
| LIMIT_5PCT_LONG | 14/20 | 70.0% | -0.15% | **-0.10%** |
| LIMIT_6PCT_LONG | 13/20 | 65.0% | -0.23% | **-0.15%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | -0.94% | **-0.24%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,052.44** / 初期 $100.00 (+952.44%)
- 確定: 5445件 (Win 1637 / Loss 1770 / Flat 2038) / skip 5640件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $1,052.44

## 4. Robust Adaptive DryRun ($100)

- 残高: **$227.62** / 初期 $100.00 (+127.62%)
- 確定: 2992件 (Win 830 / Loss 716 / Flat 1446) / skip 4943件
- 成長率目線: 平均log +0.000275 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0024 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AIN/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $227.62

## 5. Causal Adaptive DryRun ($100)

- 残高: **$125.54** / 初期 $100.00 (+25.54%)
- 確定: 2890件 (Win 859 / Loss 1120 / Flat 911) / pending 0件 / skip 3104件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000077 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PUNDIX/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $125.54

## 6. Latest Market Context

- 更新: 2026-09-14T15:51:18.026646+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=78502.6
- Funnel: target 1073 → liquid 162 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BR/USDT:USDT | +74.12% | $32,388,695.05 |
| AIN/USDT:USDT | +54.69% | $4,388,234.20 |
| CATE/USDT:USDT | +43.38% | $2,334,553.22 |
| CAP/USDT:USDT | +32.87% | $1,989,279.31 |
| KOMA/USDT:USDT | +21.69% | $1,145,290.37 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PONS/USDT:USDT | below_1h_threshold | +2.88% | +2.85% |
| XLM/USDT:USDT | below_1h_threshold | +2.06% | +2.03% |
| BTW/USDT:USDT | below_1h_threshold | +2.02% | +1.99% |
| POWER/USDT:USDT | below_1h_threshold | +1.97% | +1.94% |
| UB/USDT:USDT | below_1h_threshold | +1.83% | +1.80% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
