# Decision Report

- generated_at: 2026-05-11T07:08:20.929449+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4016**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.70% / filled 20/20。**
- 全期間 MARKET基準: n=4016, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+1.70%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.70% | **+1.70%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.70% | **+1.70%** |
| ASK | 20/20 | 100.0% | +1.11% | **+1.11%** |
| LIMIT_3PCT | 10/20 | 50.0% | +1.87% | **+0.94%** |
| LIMIT_1PCT | 15/20 | 75.0% | +1.03% | **+0.77%** |
| LIMIT_5PCT | 3/20 | 15.0% | +3.30% | **+0.50%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +0.57% | **+0.11%** |
| LIMIT_BB3S_LONG | 9/10 | 90.0% | +0.12% | **+0.11%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | -0.15% | **-0.07%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | -0.13% | **-0.08%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -0.89% | **-0.09%** |

## 2. $100 Live Portfolio

- 残高: **$98.70** / 初期 $100.00 (-1.30%)
- 確定トレード: 32件 (TP 8 / SL 21 / EXP 3)
- 最新: B/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.70
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.86** / 初期 $100.00 (+7.86%)
- 確定: 218件 (Win 54 / Loss 76 / Flat 88) / skip 359件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +4.09%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $107.86

## 4. Latest Market Context

- 更新: 2026-05-11T07:08:17.861413+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.14% price=80680.0
- Funnel: target 761 → liquid 176 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B/USDT:USDT | +35.63% | $5,973,571.64 |
| US/USDT:USDT | +34.32% | $10,924,351.14 |
| SAGA/USDT:USDT | +21.01% | $1,462,287.00 |
| TROLLSOL/USDT:USDT | +20.51% | $4,954,260.60 |
| ALCH/USDT:USDT | +17.84% | $4,546,666.37 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SAGA/USDT:USDT | below_1h_threshold | +2.15% | +2.29% |
| TROLLSOL/USDT:USDT | below_1h_threshold | +1.85% | +1.98% |
| TRUTH/USDT:USDT | below_1h_threshold | +0.96% | +1.10% |
| UB/USDT:USDT | below_1h_threshold | +0.90% | +1.03% |
| LUNC/USDT:USDT | below_1h_threshold | +0.73% | +0.87% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
