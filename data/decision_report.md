# Decision Report

- generated_at: 2026-05-08T04:02:48.991501+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3730**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.40% / filled 20/20。**
- 全期間 MARKET基準: n=3730, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+1.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.67% | **+1.51%** |
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +2.89% | **+1.30%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.26% | **+1.01%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.56% | **+1.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.63% | **+0.90%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +1.04% | **+0.52%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.78% | **+0.47%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +0.97% | **+0.19%** |

## 2. $100 Live Portfolio

- 残高: **$98.83** / 初期 $100.00 (-1.17%)
- 確定トレード: 24件 (TP 6 / SL 16 / EXP 2)
- 最新: PENGUIN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.83
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 190件 (Win 48 / Loss 64 / Flat 78) / skip 101件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.043% per trade / maxDD +3.48%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PENGUIN/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-08T04:02:46.200528+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=79572.1
- Funnel: target 770 → liquid 181 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +35.52% | $2,316,055.91 |
| LAB/USDT:USDT | +22.10% | $210,038,722.13 |
| NOT/USDT:USDT | +18.90% | $10,772,871.32 |
| TST/USDT:USDT | +17.06% | $6,317,009.77 |
| DYDX/USDT:USDT | +16.97% | $12,335,235.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLAY/USDT:USDT | below_1h_threshold | +2.30% | +2.26% |
| AGT/USDT:USDT | below_1h_threshold | +2.20% | +2.16% |
| B/USDT:USDT | below_1h_threshold | +1.43% | +1.39% |
| CHIP/USDT:USDT | below_1h_threshold | +0.87% | +0.83% |
| TONCOIN/USDT:USDT | below_1h_threshold | +0.84% | +0.80% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
