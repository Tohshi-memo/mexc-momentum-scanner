# Decision Report

- generated_at: 2026-05-01T18:47:11.192678+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2824**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.08% / filled 20/20。**
- 全期間 MARKET基準: n=2824, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+1.08%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.08% | **+1.08%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.22% | **+1.22%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.32% | **+1.19%** |
| MARKET | 20/20 | 100.0% | +1.08% | **+1.08%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_BB3S | 2/15 | 13.3% | +3.33% | **+0.44%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.94% | **+0.42%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.42% | **+0.32%** |
| LIMIT_BB3S_LONG | 2/5 | 40.0% | +0.44% | **+0.18%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +0.38% | **+0.04%** |

## 2. $100 Live Portfolio

- 残高: **$103.54** / 初期 $100.00 (+3.54%)
- 確定トレード: 5件 (TP 4 / SL 1 / EXP 0)
- 最新: NAORIS/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.54
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T18:47:09.237657+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.16% price=78385.0
- Funnel: target 756 → liquid 193 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAG/USDT:USDT | +15.43% | $1,908,991.41 |
| MAGMA/USDT:USDT | +8.40% | $1,059,750.05 |
| ZEN/USDT:USDT | +7.86% | $4,503,882.15 |
| SQD/USDT:USDT | +7.07% | $2,007,951.92 |
| ZEC/USDT:USDT | +7.05% | $331,477,144.26 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +4.46% | +4.62% |
| TAG/USDT:USDT | below_1h_threshold | +3.45% | +3.61% |
| MAGMA/USDT:USDT | below_1h_threshold | +2.62% | +2.78% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +2.25% | +2.41% |
| RDDTSTOCK/USDT:USDT | below_1h_threshold | +2.25% | +2.41% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
