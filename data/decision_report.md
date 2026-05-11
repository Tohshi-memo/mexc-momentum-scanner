# Decision Report

- generated_at: 2026-05-11T06:57:56.139979+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4015**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.70% / filled 20/20。**
- 全期間 MARKET基準: n=4015, expectancy=-0.12%
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
| LIMIT_1PCT | 15/20 | 75.0% | +0.96% | **+0.72%** |
| LIMIT_5PCT | 4/20 | 20.0% | +2.71% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +0.45% | **+0.32%** |
| LIMIT_FIB1272_LONG | 15/20 | 75.0% | +0.23% | **+0.17%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +0.25% | **+0.16%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +0.57% | **+0.11%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +0.03% | **+0.03%** |

## 2. $100 Live Portfolio

- 残高: **$98.70** / 初期 $100.00 (-1.30%)
- 確定トレード: 32件 (TP 8 / SL 21 / EXP 3)
- 最新: B/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.70
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.86** / 初期 $100.00 (+7.86%)
- 確定: 218件 (Win 54 / Loss 76 / Flat 88) / skip 358件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +4.09%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $107.86

## 4. Latest Market Context

- 更新: 2026-05-11T06:57:51.854891+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=80814.4
- Funnel: target 777 → liquid 180 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.8 >= 65=1, 4h RSI 74.9 >= 65=1, 4h RSI 73.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B/USDT:USDT | +36.38% | $5,558,575.38 |
| US/USDT:USDT | +33.69% | $10,887,296.54 |
| SAGA/USDT:USDT | +18.89% | $1,362,798.56 |
| TROLLSOL/USDT:USDT | +18.22% | $5,219,380.30 |
| ALCH/USDT:USDT | +17.48% | $4,532,310.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_1h_threshold | +3.04% | +3.02% |
| US/USDT:USDT | below_1h_threshold | +1.10% | +1.08% |
| JTO/USDT:USDT | below_1h_threshold | +0.96% | +0.95% |
| OG/USDT:USDT | below_1h_threshold | +0.95% | +0.93% |
| TRUTH/USDT:USDT | below_1h_threshold | +0.80% | +0.79% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
