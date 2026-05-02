# Decision Report

- generated_at: 2026-05-02T15:47:07.647072+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2936**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2936, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-1.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.92% | **-1.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +6.70% | **+1.34%** |
| LIMIT_5PCT | 11/20 | 55.0% | +2.23% | **+1.23%** |
| LIMIT_6PCT | 6/20 | 30.0% | +3.92% | **+1.18%** |
| LIMIT_BB3S | 4/15 | 26.7% | +3.85% | **+1.03%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +6.62% | **+3.97%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.88% | **+1.79%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.28% | **+1.71%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.40% | **+1.56%** |
| MARKET_LONG | 20/20 | 100.0% | +1.14% | **+1.14%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 8件 (TP 4 / SL 4 / EXP 0)
- 最新: NAORIS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T15:47:04.623578+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=78388.8
- Funnel: target 755 → liquid 163 → pre 50 → checked 50 → surge 5 → strict 0
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.8 >= 65=1, 4h RSI 80.5 >= 65=1, 4h RSI 83.6 >= 65=1, 4h RSI 76.4 >= 65=1, 4h RSI 83.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +303.21% | $169,796,804.39 |
| TAG/USDT:USDT | +74.79% | $10,360,689.87 |
| BIO/USDT:USDT | +41.72% | $4,089,686.23 |
| SKYAI/USDT:USDT | +37.31% | $19,686,097.62 |
| KNC/USDT:USDT | +35.74% | $2,402,697.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| B/USDT:USDT | below_1h_threshold | +3.39% | +3.38% |
| LAB/USDT:USDT | below_1h_threshold | +2.95% | +2.94% |
| BABY/USDT:USDT | below_1h_threshold | +2.87% | +2.86% |
| XNY/USDT:USDT | below_1h_threshold | +2.51% | +2.50% |
| BEAT/USDT:USDT | below_1h_threshold | +2.39% | +2.37% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
