# Decision Report

- generated_at: 2026-09-14T12:31:19.687491+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14517**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +4.92% / filled 20/20。**
- 全期間 MARKET基準: n=14517, expectancy=-0.00%
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
| LIMIT_ATR | 9/20 | 45.0% | +3.73% | **+1.68%** |

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
- 確定: 5445件 (Win 1637 / Loss 1770 / Flat 2038) / skip 5633件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $1,052.44

## 4. Robust Adaptive DryRun ($100)

- 残高: **$227.62** / 初期 $100.00 (+127.62%)
- 確定: 2991件 (Win 830 / Loss 716 / Flat 1445) / skip 4937件
- 成長率目線: 平均log +0.000275 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $227.62

## 5. Causal Adaptive DryRun ($100)

- 残高: **$125.76** / 初期 $100.00 (+25.76%)
- 確定: 2889件 (Win 859 / Loss 1119 / Flat 911) / pending 1件 / skip 3095件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000437 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: B/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $125.76

## 6. Latest Market Context

- 更新: 2026-09-14T12:31:08.938272+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.27% price=77957.8
- Funnel: target 1068 → liquid 154 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BR/USDT:USDT | +68.24% | $19,156,492.23 |
| CATE/USDT:USDT | +46.78% | $2,152,102.54 |
| AIN/USDT:USDT | +32.56% | $3,424,697.84 |
| KOMA/USDT:USDT | +29.10% | $1,038,285.15 |
| MTL/USDT:USDT | +13.81% | $1,240,074.17 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +4.12% | +3.85% |
| TRUMPOFFICIAL/USDT:USDT | below_1h_threshold | +2.76% | +2.49% |
| BR/USDT:USDT | below_1h_threshold | +2.55% | +2.28% |
| METASTOCK/USDT:USDT | below_1h_threshold | +1.86% | +1.58% |
| SOXS/USDT:USDT | below_1h_threshold | +1.65% | +1.38% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
