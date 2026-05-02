# Decision Report

- generated_at: 2026-05-02T19:47:06.878397+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2975**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.15% / filled 20/20。**
- 全期間 MARKET基準: n=2975, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+1.15%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.15% | **+1.15%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.21% | **+1.21%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.34% | **+1.21%** |
| MARKET | 20/20 | 100.0% | +1.15% | **+1.15%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.71% | **+0.57%** |
| LIMIT_BB3S | 5/13 | 38.5% | +1.45% | **+0.56%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 6/20 | 30.0% | +5.04% | **+1.51%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +2.60% | **+0.91%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.65% | **+0.29%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.13% | **+0.12%** |

## 2. $100 Live Portfolio

- 残高: **$102.70** / 初期 $100.00 (+2.70%)
- 確定トレード: 9件 (TP 4 / SL 4 / EXP 1)
- 最新: RAVE/USDT:USDT EXPIRED PnL +5.55% 残高後 $102.70
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T19:47:04.370513+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=78460.9
- Funnel: target 755 → liquid 166 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.7 >= 65=1, 4h RSI 76.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LUNC/USDT:USDT | +9.12% | $25,350,105.97 |
| TAC/USDT:USDT | +8.76% | $2,620,860.26 |
| XNY/USDT:USDT | +8.29% | $1,359,611.39 |
| BSB/USDT:USDT | +7.40% | $10,692,400.64 |
| NAORIS/USDT:USDT | +6.73% | $3,702,277.41 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BIO/USDT:USDT | below_1h_threshold | +3.71% | +3.67% |
| SPACE/USDT:USDT | below_1h_threshold | +3.71% | +3.67% |
| CHILLGUY/USDT:USDT | below_1h_threshold | +3.07% | +3.03% |
| ALGO/USDT:USDT | below_1h_threshold | +1.92% | +1.89% |
| FET/USDT:USDT | below_1h_threshold | +1.57% | +1.53% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
