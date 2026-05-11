# Decision Report

- generated_at: 2026-05-11T04:12:44.229837+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4006**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.10% / filled 20/20。**
- 全期間 MARKET基準: n=4006, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+2.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.10% | **+2.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.10% | **+2.10%** |
| ASK | 20/20 | 100.0% | +2.06% | **+2.06%** |
| LIMIT_1PCT | 17/20 | 85.0% | +2.19% | **+1.86%** |
| LIMIT_BB3S | 5/12 | 41.7% | +2.89% | **+1.20%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.53% | **+1.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 16/20 | 80.0% | +1.58% | **+1.26%** |
| LIMIT_3PCT_LONG | 19/20 | 95.0% | +0.69% | **+0.66%** |
| LIMIT_ATR_LONG | 18/20 | 90.0% | +0.61% | **+0.55%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +0.61% | **+0.40%** |
| LIMIT_FIB1272_LONG | 15/20 | 75.0% | +0.43% | **+0.32%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$109.49** / 初期 $100.00 (+9.49%)
- 確定: 212件 (Win 54 / Loss 73 / Flat 85) / skip 355件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +4.09%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAYER/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.85% 残高後 $109.49

## 4. Latest Market Context

- 更新: 2026-05-11T04:12:41.191452+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=80644.5
- Funnel: target 775 → liquid 175 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +32.94% | $10,194,967.63 |
| ALCH/USDT:USDT | +22.04% | $4,061,797.35 |
| TROLLSOL/USDT:USDT | +16.45% | $5,259,465.14 |
| OPG/USDT:USDT | +14.32% | $1,620,715.47 |
| FOLKS/USDT:USDT | +12.88% | $1,460,423.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GIGA/USDT:USDT | below_1h_threshold | +3.37% | +3.43% |
| TROLLSOL/USDT:USDT | below_1h_threshold | +2.47% | +2.53% |
| LAYER/USDT:USDT | below_1h_threshold | +1.51% | +1.58% |
| ALCH/USDT:USDT | below_1h_threshold | +0.93% | +0.99% |
| FOLKS/USDT:USDT | below_1h_threshold | +0.91% | +0.97% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
