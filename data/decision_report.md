# Decision Report

- generated_at: 2026-05-11T08:02:43.098275+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4018**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.77% / filled 20/20。**
- 全期間 MARKET基準: n=4018, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.77%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.77% | **+0.77%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 12/20 | 60.0% | +1.41% | **+0.84%** |
| MARKET | 20/20 | 100.0% | +0.77% | **+0.77%** |
| LIMIT_5PCT | 4/20 | 20.0% | +2.71% | **+0.54%** |
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |
| LIMIT_4PCT | 9/20 | 45.0% | +0.92% | **+0.41%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 10/11 | 90.9% | +0.64% | **+0.58%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.14% | **+0.10%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.09% | **+0.05%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.04% | **+0.03%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -0.04% | **-0.01%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 33件 (TP 8 / SL 22 / EXP 3)
- 最新: SIREN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.86** / 初期 $100.00 (+7.86%)
- 確定: 218件 (Win 54 / Loss 76 / Flat 88) / skip 361件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +4.09%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $107.86

## 4. Latest Market Context

- 更新: 2026-05-11T08:02:40.164012+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=80713.8
- Funnel: target 761 → liquid 177 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +39.22% | $11,301,518.09 |
| B/USDT:USDT | +24.52% | $7,237,422.80 |
| SAGA/USDT:USDT | +19.95% | $1,758,599.49 |
| VVV/USDT:USDT | +18.62% | $8,336,230.04 |
| ALCH/USDT:USDT | +17.48% | $4,604,066.87 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| US/USDT:USDT | below_1h_threshold | +1.81% | +1.81% |
| SAGA/USDT:USDT | below_1h_threshold | +1.43% | +1.43% |
| BILL/USDT:USDT | below_1h_threshold | +0.87% | +0.86% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +0.69% | +0.68% |
| UB/USDT:USDT | below_1h_threshold | +0.62% | +0.62% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
