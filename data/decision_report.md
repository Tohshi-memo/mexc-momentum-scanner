# Decision Report

- generated_at: 2026-05-04T12:42:19.287865+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3200**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.62% / filled 20/20。**
- 全期間 MARKET基準: n=3200, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.62%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.62% | **+0.62%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.62% | **+0.62%** |
| ASK | 20/20 | 100.0% | +0.58% | **+0.58%** |
| LIMIT_BB3S | 5/18 | 27.8% | +0.89% | **+0.25%** |
| LIMIT_7PCT | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.33% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.93% | **+0.93%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +1.02% | **+0.91%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.01% | **+0.56%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.77% | **+0.54%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.87% | **+0.48%** |

## 2. $100 Live Portfolio

- 残高: **$102.88** / 初期 $100.00 (+2.88%)
- 確定トレード: 13件 (TP 5 / SL 6 / EXP 2)
- 最新: LAB/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.88
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T12:42:14.707582+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.24% price=78939.9
- Funnel: target 761 → liquid 187 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +88.63% | $11,679,541.43 |
| SKYAI/USDT:USDT | +76.66% | $64,916,677.20 |
| GIGA/USDT:USDT | +54.51% | $2,058,730.54 |
| TAG/USDT:USDT | +32.32% | $15,960,064.41 |
| 4/USDT:USDT | +30.93% | $1,638,956.10 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GIGGLE/USDT:USDT | below_1h_threshold | +4.72% | +4.48% |
| ASTEROID/USDT:USDT | below_1h_threshold | +4.45% | +4.22% |
| ZBT/USDT:USDT | below_1h_threshold | +4.09% | +3.85% |
| AIOT/USDT:USDT | below_1h_threshold | +3.95% | +3.71% |
| SAPIEN/USDT:USDT | below_1h_threshold | +3.23% | +2.99% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
