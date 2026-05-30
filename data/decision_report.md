# Decision Report

- generated_at: 2026-05-30T12:33:44.268860+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5124**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.35% / filled 20/20。**
- 全期間 MARKET基準: n=5124, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+2.35%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.35% | **+2.35%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.35% | **+2.35%** |
| LIMIT_1PCT | 17/20 | 85.0% | +2.29% | **+1.95%** |
| ASK | 20/20 | 100.0% | +1.78% | **+1.78%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.86% | **+1.30%** |
| LIMIT_ATR | 10/20 | 50.0% | +1.21% | **+0.61%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.89% | **+0.45%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -0.11% | **-0.02%** |

## 2. $100 Live Portfolio

- 残高: **$98.10** / 初期 $100.00 (-1.90%)
- 確定トレード: 75件 (TP 22 / SL 50 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$124.75** / 初期 $100.00 (+24.75%)
- 確定: 779件 (Win 182 / Loss 237 / Flat 360) / skip 906件
- 成長率目線: 平均log +0.000284 / 幾何平均 +0.028% per trade / maxDD +4.91%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UB/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $124.75

## 4. Latest Market Context

- 更新: 2026-05-30T12:33:42.319782+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=73663.4
- Funnel: target 773 → liquid 130 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +34.20% | $2,059,131.88 |
| STG/USDT:USDT | +33.51% | $1,138,430.33 |
| NFP/USDT:USDT | +30.99% | $3,336,790.67 |
| LAB/USDT:USDT | +30.21% | $123,970,870.42 |
| VTHO/USDT:USDT | +19.00% | $1,738,611.41 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FET/USDT:USDT | below_1h_threshold | +3.42% | +3.29% |
| QNTSTOCK/USDT:USDT | below_1h_threshold | +3.37% | +3.24% |
| PORTAL/USDT:USDT | below_1h_threshold | +3.09% | +2.96% |
| BEAT/USDT:USDT | below_1h_threshold | +2.04% | +1.91% |
| ID/USDT:USDT | below_1h_threshold | +2.03% | +1.91% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
