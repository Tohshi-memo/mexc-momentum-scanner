# Decision Report

- generated_at: 2026-09-14T12:51:33.184013+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14519**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +4.92% / filled 20/20。**
- 全期間 MARKET基準: n=14519, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+4.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +4.92% | **+4.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +4.92% | **+4.92%** |
| LIMIT_1PCT | 17/20 | 85.0% | +4.65% | **+3.95%** |
| LIMIT_2PCT | 13/20 | 65.0% | +4.01% | **+2.61%** |
| LIMIT_3PCT | 10/20 | 50.0% | +4.11% | **+2.05%** |
| LIMIT_ATR | 9/20 | 45.0% | +3.52% | **+1.58%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 15/20 | 75.0% | +0.95% | **+0.72%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.67% | **+0.33%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +0.55% | **+0.16%** |
| LIMIT_8PCT_LONG | 14/20 | 70.0% | -0.29% | **-0.20%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | -1.93% | **-0.29%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,052.44** / 初期 $100.00 (+952.44%)
- 確定: 5445件 (Win 1637 / Loss 1770 / Flat 2038) / skip 5635件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $1,052.44

## 4. Robust Adaptive DryRun ($100)

- 残高: **$227.62** / 初期 $100.00 (+127.62%)
- 確定: 2991件 (Win 830 / Loss 716 / Flat 1445) / skip 4939件
- 成長率目線: 平均log +0.000275 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $227.62

## 5. Causal Adaptive DryRun ($100)

- 残高: **$125.54** / 初期 $100.00 (+25.54%)
- 確定: 2890件 (Win 859 / Loss 1120 / Flat 911) / pending 0件 / skip 3099件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000388 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PUNDIX/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $125.54

## 6. Latest Market Context

- 更新: 2026-09-14T12:51:20.059080+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=77725.1
- Funnel: target 1068 → liquid 157 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.2 >= 65=1, 4h RSI 89.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BR/USDT:USDT | +72.96% | $20,944,701.73 |
| CATE/USDT:USDT | +46.71% | $2,173,114.69 |
| CAP/USDT:USDT | +44.70% | $1,086,680.96 |
| AIN/USDT:USDT | +37.48% | $3,600,206.23 |
| KOMA/USDT:USDT | +30.86% | $1,051,026.32 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +4.18% | +4.21% |
| LONGXIA/USDT:USDT | below_1h_threshold | +3.75% | +3.78% |
| KOMA/USDT:USDT | below_1h_threshold | +2.71% | +2.73% |
| METASTOCK/USDT:USDT | below_1h_threshold | +1.86% | +1.88% |
| SOXS/USDT:USDT | below_1h_threshold | +1.65% | +1.68% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
