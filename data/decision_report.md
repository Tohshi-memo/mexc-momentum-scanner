# Decision Report

- generated_at: 2026-05-25T05:59:36.388188+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4844**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.43% / filled 20/20。**
- 全期間 MARKET基準: n=4844, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+0.43%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.43% | **+0.43%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.49% | **+0.49%** |
| MARKET | 20/20 | 100.0% | +0.43% | **+0.43%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | -0.06% | **-0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +1.01% | **+1.01%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.38% | **+0.29%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.31% | **+0.20%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.54% | **+0.19%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$96.68** / 初期 $100.00 (-3.32%)
- 確定トレード: 63件 (TP 17 / SL 43 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$124.23** / 初期 $100.00 (+24.23%)
- 確定: 650件 (Win 162 / Loss 206 / Flat 282) / skip 755件
- 成長率目線: 平均log +0.000334 / 幾何平均 +0.033% per trade / maxDD +4.72%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UB/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $124.23

## 4. Latest Market Context

- 更新: 2026-05-25T05:59:34.366970+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=77363.4
- Funnel: target 764 → liquid 118 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| XAN/USDT:USDT | +38.57% | $3,297,469.90 |
| SPORTFUN/USDT:USDT | +14.38% | $1,255,921.54 |
| NIL/USDT:USDT | +9.12% | $14,452,558.38 |
| H/USDT:USDT | +8.14% | $1,187,953.78 |
| SAGA/USDT:USDT | +5.77% | $1,310,064.56 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIL/USDT:USDT | below_1h_threshold | +4.63% | +4.62% |
| XAN/USDT:USDT | below_1h_threshold | +2.96% | +2.95% |
| UB/USDT:USDT | below_1h_threshold | +2.96% | +2.95% |
| TIA/USDT:USDT | below_1h_threshold | +2.62% | +2.61% |
| ATOM/USDT:USDT | below_1h_threshold | +2.44% | +2.43% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
