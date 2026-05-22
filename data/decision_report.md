# Decision Report

- generated_at: 2026-05-22T03:14:00.114219+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4661**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.45% / filled 20/20。**
- 全期間 MARKET基準: n=4661, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+2.45%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.45% | **+2.45%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.45% | **+2.45%** |
| ASK | 20/20 | 100.0% | +2.00% | **+2.00%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.89% | **+1.51%** |
| LIMIT_2PCT | 13/20 | 65.0% | +2.24% | **+1.46%** |
| LIMIT_3PCT | 11/20 | 55.0% | +2.57% | **+1.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/5 | 40.0% | +1.63% | **+0.65%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -2.61% | **-0.52%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | -0.65% | **-0.58%** |

## 2. $100 Live Portfolio

- 残高: **$95.25** / 初期 $100.00 (-4.75%)
- 確定トレード: 60件 (TP 15 / SL 42 / EXP 3)
- 最新: STXSTOCK/USDT:USDT SL_HIT PnL -1.86% 残高後 $95.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定: 548件 (Win 138 / Loss 185 / Flat 225) / skip 674件
- 成長率目線: 平均log +0.000354 / 幾何平均 +0.035% per trade / maxDD +4.21%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $121.41

## 4. Latest Market Context

- 更新: 2026-05-22T03:13:57.748301+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=77680.1
- Funnel: target 766 → liquid 137 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NEAR/USDT:USDT | +15.94% | $53,792,534.35 |
| GRASS/USDT:USDT | +15.80% | $3,680,220.94 |
| PEAQ/USDT:USDT | +12.63% | $1,936,348.05 |
| PLUME/USDT:USDT | +10.93% | $1,717,753.76 |
| IBMSTOCK/USDT:USDT | +9.34% | $2,309,989.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLAY/USDT:USDT | below_1h_threshold | +2.46% | +2.40% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.18% | +2.13% |
| PEAQ/USDT:USDT | below_1h_threshold | +1.90% | +1.85% |
| NEAR/USDT:USDT | below_1h_threshold | +1.55% | +1.50% |
| BILL/USDT:USDT | below_1h_threshold | +1.51% | +1.46% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
