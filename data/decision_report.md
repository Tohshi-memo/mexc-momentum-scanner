# Decision Report

- generated_at: 2026-05-04T19:57:12.332063+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3254**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.66% / filled 20/20。**
- 全期間 MARKET基準: n=3254, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=+0.66%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.66% | **+0.66%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.11% | **+1.06%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.14% | **+0.92%** |
| MARKET | 20/20 | 100.0% | +0.66% | **+0.66%** |
| ASK | 20/20 | 100.0% | +0.62% | **+0.62%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.83% | **+0.57%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 15/20 | 75.0% | +2.47% | **+1.85%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +1.76% | **+1.14%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +1.93% | **+0.68%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.29% | **+0.58%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |

## 2. $100 Live Portfolio

- 残高: **$101.85** / 初期 $100.00 (+1.85%)
- 確定トレード: 15件 (TP 5 / SL 8 / EXP 2)
- 最新: RAVE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.85
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T19:57:10.231400+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=79963.9
- Funnel: target 760 → liquid 203 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RAVE/USDT:USDT | +39.89% | $23,622,998.92 |
| TST/USDT:USDT | +10.84% | $22,365,530.04 |
| SKYAI/USDT:USDT | +7.10% | $97,715,193.88 |
| FHE/USDT:USDT | +6.87% | $2,672,928.55 |
| LUNC/USDT:USDT | +6.86% | $70,581,133.17 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GIGGLE/USDT:USDT | below_1h_threshold | +3.44% | +3.58% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +2.86% | +3.01% |
| TST/USDT:USDT | below_1h_threshold | +2.64% | +2.78% |
| ONDO/USDT:USDT | below_1h_threshold | +1.86% | +2.00% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.78% | +1.92% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
