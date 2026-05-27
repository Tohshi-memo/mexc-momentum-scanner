# Decision Report

- generated_at: 2026-05-27T17:54:31.363406+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4938**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.20% / filled 20/20。**
- 全期間 MARKET基準: n=4938, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+1.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.20% | **+1.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 13/20 | 65.0% | +3.01% | **+1.96%** |
| LIMIT_2PCT | 16/20 | 80.0% | +2.33% | **+1.87%** |
| LIMIT_1PCT | 17/20 | 85.0% | +2.13% | **+1.81%** |
| MARKET | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_4PCT | 9/20 | 45.0% | +2.22% | **+1.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 11/20 | 55.0% | +2.18% | **+1.20%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +1.69% | **+0.93%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +3.29% | **+0.82%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +1.14% | **+0.74%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.70% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$96.19** / 初期 $100.00 (-3.81%)
- 確定トレード: 67件 (TP 18 / SL 46 / EXP 3)
- 最新: GUA/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.19
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$126.79** / 初期 $100.00 (+26.79%)
- 確定: 684件 (Win 172 / Loss 220 / Flat 292) / skip 815件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +4.72%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $126.79

## 4. Latest Market Context

- 更新: 2026-05-27T17:54:29.178427+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.51% price=74890.9
- Funnel: target 771 → liquid 149 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| GENIUS/USDT:USDT | +5.38% | $1,148,121.59 |
| BILL/USDT:USDT | +2.98% | $9,535,975.42 |
| PIPPIN/USDT:USDT | +2.57% | $1,544,225.53 |
| RKLBSTOCK/USDT:USDT | +2.54% | $1,253,199.26 |
| ASTEROID/USDT:USDT | +2.44% | $1,022,002.49 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GENIUS/USDT:USDT | below_1h_threshold | +4.65% | +5.16% |
| BILL/USDT:USDT | below_1h_threshold | +3.97% | +4.48% |
| H/USDT:USDT | below_1h_threshold | +3.13% | +3.63% |
| ON/USDT:USDT | below_1h_threshold | +2.79% | +3.29% |
| RIF/USDT:USDT | below_1h_threshold | +1.14% | +1.65% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
