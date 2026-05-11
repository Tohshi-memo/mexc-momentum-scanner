# Decision Report

- generated_at: 2026-05-11T04:07:38.974976+00:00
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

- 更新: 2026-05-11T04:07:35.881574+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=80689.2
- Funnel: target 775 → liquid 175 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +36.38% | $10,158,795.91 |
| ALCH/USDT:USDT | +21.83% | $4,053,202.09 |
| TROLLSOL/USDT:USDT | +15.74% | $5,253,396.75 |
| FOLKS/USDT:USDT | +13.32% | $1,434,536.59 |
| OPG/USDT:USDT | +12.98% | $1,600,022.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAYER/USDT:USDT | below_1h_threshold | +2.19% | +2.20% |
| TROLLSOL/USDT:USDT | below_1h_threshold | +1.85% | +1.86% |
| FOLKS/USDT:USDT | below_1h_threshold | +1.62% | +1.63% |
| US/USDT:USDT | below_1h_threshold | +1.20% | +1.21% |
| ALCH/USDT:USDT | below_1h_threshold | +0.75% | +0.76% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
