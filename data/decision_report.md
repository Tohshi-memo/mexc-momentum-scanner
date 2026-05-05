# Decision Report

- generated_at: 2026-05-05T00:26:54.434330+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3280**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.70% / filled 20/20。**
- 全期間 MARKET基準: n=3280, expectancy=-0.16%
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
| ASK | 20/20 | 100.0% | +1.64% | **+1.64%** |
| LIMIT_1PCT | 15/20 | 75.0% | +1.37% | **+1.03%** |
| LIMIT_BB3S | 3/10 | 30.0% | +2.22% | **+0.67%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.38% | **+0.25%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +4.22% | **+1.05%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.76% | **+0.34%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.34% | **+0.33%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.57% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$101.85** / 初期 $100.00 (+1.85%)
- 確定トレード: 15件 (TP 5 / SL 8 / EXP 2)
- 最新: RAVE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.85
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T00:26:52.695200+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=79855.2
- Funnel: target 760 → liquid 203 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RAVE/USDT:USDT | +34.50% | $57,314,348.17 |
| FHE/USDT:USDT | +19.51% | $2,617,616.76 |
| TONCOIN/USDT:USDT | +11.96% | $41,638,594.15 |
| PLAY/USDT:USDT | +11.58% | $2,641,099.23 |
| B3/USDT:USDT | +9.75% | $1,143,306.25 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ENSO/USDT:USDT | below_1h_threshold | +4.87% | +4.83% |
| TST/USDT:USDT | below_1h_threshold | +4.77% | +4.74% |
| FHE/USDT:USDT | below_1h_threshold | +4.17% | +4.14% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.66% | +1.62% |
| ALBSTOCK/USDT:USDT | below_1h_threshold | +1.14% | +1.10% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
