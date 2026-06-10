# Decision Report

- generated_at: 2026-06-10T06:11:23.819158+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6187**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.54% / filled 20/20。**
- 全期間 MARKET基準: n=6187, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.54%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.54% | **+0.54%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +5.92% | **+1.48%** |
| LIMIT_8PCT | 3/20 | 15.0% | +6.57% | **+0.99%** |
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.76% | **+0.65%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.72% | **+0.65%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +3.00% | **+1.20%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.29% | **+1.03%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +2.33% | **+0.93%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.43% | **+0.37%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$148.52** / 初期 $100.00 (+48.52%)
- 確定: 1203件 (Win 299 / Loss 376 / Flat 528) / skip 1545件
- 成長率目線: 平均log +0.000329 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STG/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $148.52

## 4. Latest Market Context

- 更新: 2026-06-10T06:11:20.680268+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=61318.3
- Funnel: target 779 → liquid 145 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STG/USDT:USDT | +32.63% | $5,458,816.25 |
| BTW/USDT:USDT | +23.52% | $28,702,412.43 |
| UB/USDT:USDT | +9.33% | $1,732,035.66 |
| BABY/USDT:USDT | +8.92% | $1,019,115.61 |
| HOME/USDT:USDT | +8.81% | $4,122,179.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EWY/USDT:USDT | below_1h_threshold | +0.76% | +0.76% |
| UB/USDT:USDT | below_1h_threshold | +0.73% | +0.73% |
| DRAM/USDT:USDT | below_1h_threshold | +0.72% | +0.73% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +0.70% | +0.70% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +0.70% | +0.70% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
