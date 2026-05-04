# Decision Report

- generated_at: 2026-05-04T05:32:18.944175+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3160**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.79% / filled 20/20。**
- 全期間 MARKET基準: n=3160, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=+0.79%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.79% | **+0.79%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.06% | **+0.95%** |
| LIMIT_BB3S | 4/11 | 36.4% | +2.37% | **+0.86%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.16% | **+0.81%** |
| MARKET | 20/20 | 100.0% | +0.79% | **+0.79%** |
| ASK | 20/20 | 100.0% | +0.63% | **+0.63%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.64% | **+0.74%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.48% | **+0.74%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.50% | **+0.60%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.65% | **+0.49%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T05:32:16.867001+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.38% price=79993.0
- Funnel: target 758 → liquid 172 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +55.29% | $22,727,571.78 |
| SKYAI/USDT:USDT | +46.74% | $46,028,956.87 |
| TAG/USDT:USDT | +45.41% | $7,315,930.29 |
| LAB/USDT:USDT | +44.20% | $217,155,620.38 |
| TST/USDT:USDT | +39.77% | $6,438,407.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ORDI/USDT:USDT | below_1h_threshold | +2.71% | +3.09% |
| TST/USDT:USDT | below_1h_threshold | +2.61% | +2.99% |
| USTC/USDT:USDT | below_1h_threshold | +2.50% | +2.89% |
| GIGGLE/USDT:USDT | below_1h_threshold | +2.41% | +2.80% |
| TAG/USDT:USDT | below_1h_threshold | +2.11% | +2.50% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
