# Decision Report

- generated_at: 2026-05-11T07:32:56.132487+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4017**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.11% / filled 20/20。**
- 全期間 MARKET基準: n=4017, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+1.11%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.11% | **+1.11%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.11% | **+1.11%** |
| LIMIT_3PCT | 11/20 | 55.0% | +1.62% | **+0.89%** |
| ASK | 20/20 | 100.0% | +0.52% | **+0.52%** |
| LIMIT_5PCT | 3/20 | 15.0% | +3.30% | **+0.50%** |
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 10/11 | 90.9% | +0.64% | **+0.58%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.33% | **+0.13%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.20% | **+0.12%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +0.57% | **+0.11%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | -0.02% | **-0.01%** |

## 2. $100 Live Portfolio

- 残高: **$98.70** / 初期 $100.00 (-1.30%)
- 確定トレード: 32件 (TP 8 / SL 21 / EXP 3)
- 最新: B/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.70
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.86** / 初期 $100.00 (+7.86%)
- 確定: 218件 (Win 54 / Loss 76 / Flat 88) / skip 360件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +4.09%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $107.86

## 4. Latest Market Context

- 更新: 2026-05-11T07:32:50.339111+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=80717.6
- Funnel: target 761 → liquid 177 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +34.45% | $11,085,481.03 |
| B/USDT:USDT | +32.40% | $6,594,834.84 |
| TROLLSOL/USDT:USDT | +21.16% | $4,992,395.27 |
| VVV/USDT:USDT | +18.61% | $7,343,894.02 |
| SAGA/USDT:USDT | +17.14% | $1,677,117.37 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TROLLSOL/USDT:USDT | below_1h_threshold | +2.21% | +2.30% |
| BABY/USDT:USDT | below_1h_threshold | +2.19% | +2.29% |
| LUNC/USDT:USDT | below_1h_threshold | +2.12% | +2.21% |
| BILL/USDT:USDT | below_1h_threshold | +2.11% | +2.20% |
| BAS/USDT:USDT | below_1h_threshold | +1.35% | +1.44% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
