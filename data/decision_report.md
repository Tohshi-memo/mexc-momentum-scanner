# Decision Report

- generated_at: 2026-05-01T20:52:01.715175+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2831**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.33% / filled 20/20。**
- 全期間 MARKET基準: n=2831, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+1.33%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.33% | **+1.33%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.79% | **+1.79%** |
| MARKET | 20/20 | 100.0% | +1.33% | **+1.33%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.32% | **+1.19%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.45% | **+0.34%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.94% | **+0.70%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.49% | **+0.29%** |
| LIMIT_BB3S_LONG | 5/10 | 50.0% | +0.57% | **+0.28%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.50% | **+0.25%** |

## 2. $100 Live Portfolio

- 残高: **$103.54** / 初期 $100.00 (+3.54%)
- 確定トレード: 5件 (TP 4 / SL 1 / EXP 0)
- 最新: NAORIS/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.54
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T20:51:59.803604+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.49% price=77933.8
- Funnel: target 755 → liquid 190 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +32.63% | $4,999,568.95 |
| ZEN/USDT:USDT | +10.33% | $7,396,157.53 |
| SQD/USDT:USDT | +9.57% | $2,126,297.87 |
| FIGHT/USDT:USDT | +7.96% | $1,258,420.55 |
| SNDKSTOCK/USDT:USDT | +7.49% | $9,768,773.81 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| B/USDT:USDT | below_1h_threshold | +3.93% | +4.42% |
| SQD/USDT:USDT | below_1h_threshold | +1.87% | +2.36% |
| ORCA/USDT:USDT | below_1h_threshold | +1.84% | +2.33% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +1.76% | +2.25% |
| PROM/USDT:USDT | below_1h_threshold | +1.66% | +2.15% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
