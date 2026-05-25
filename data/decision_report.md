# Decision Report

- generated_at: 2026-05-25T05:39:08.316779+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4843**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.43% / filled 20/20。**
- 全期間 MARKET基準: n=4843, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+0.43%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.43% | **+0.43%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.50% | **+0.50%** |
| MARKET | 20/20 | 100.0% | +0.43% | **+0.43%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.19% | **+0.09%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +1.01% | **+1.01%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.31% | **+0.20%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.54% | **+0.19%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +0.05% | **+0.03%** |

## 2. $100 Live Portfolio

- 残高: **$96.68** / 初期 $100.00 (-3.32%)
- 確定トレード: 63件 (TP 17 / SL 43 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$124.23** / 初期 $100.00 (+24.23%)
- 確定: 649件 (Win 162 / Loss 206 / Flat 281) / skip 755件
- 成長率目線: 平均log +0.000334 / 幾何平均 +0.033% per trade / maxDD +4.72%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GENIUS/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.06% 残高後 $124.23

## 4. Latest Market Context

- 更新: 2026-05-25T05:39:06.058993+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=77432.8
- Funnel: target 764 → liquid 117 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| XAN/USDT:USDT | +38.79% | $3,023,281.30 |
| SPORTFUN/USDT:USDT | +15.02% | $1,243,370.61 |
| H/USDT:USDT | +8.58% | $1,150,543.49 |
| SUPER/USDT:USDT | +5.08% | $2,881,998.53 |
| SAGA/USDT:USDT | +4.93% | $1,300,753.02 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XAN/USDT:USDT | below_1h_threshold | +3.12% | +3.02% |
| ATOM/USDT:USDT | below_1h_threshold | +1.96% | +1.86% |
| UB/USDT:USDT | below_1h_threshold | +1.78% | +1.68% |
| TIA/USDT:USDT | below_1h_threshold | +1.59% | +1.49% |
| MYX/USDT:USDT | below_1h_threshold | +1.51% | +1.41% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
