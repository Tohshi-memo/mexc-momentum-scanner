# Decision Report

- generated_at: 2026-05-02T15:57:07.872382+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2940**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2940, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-2.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.12% | **-2.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +6.70% | **+1.34%** |
| LIMIT_5PCT | 13/20 | 65.0% | +2.04% | **+1.32%** |
| LIMIT_6PCT | 6/20 | 30.0% | +3.92% | **+1.18%** |
| LIMIT_BB3S | 5/13 | 38.5% | +2.70% | **+1.04%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.77% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/7 | 57.1% | +6.78% | **+3.88%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +3.24% | **+2.43%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.89% | **+2.31%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +3.33% | **+2.16%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.62% | **+1.54%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 8件 (TP 4 / SL 4 / EXP 0)
- 最新: NAORIS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T15:57:04.810040+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=78442.5
- Funnel: target 755 → liquid 164 → pre 50 → checked 50 → surge 5 → strict 0
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.7 >= 65=2, 4h RSI 79.5 >= 65=1, 4h RSI 82.6 >= 65=1, 4h RSI 76.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +302.67% | $171,620,826.54 |
| TAG/USDT:USDT | +60.69% | $10,789,178.04 |
| SKYAI/USDT:USDT | +39.34% | $19,938,128.59 |
| BIO/USDT:USDT | +37.73% | $4,217,716.74 |
| KNC/USDT:USDT | +33.42% | $2,527,442.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BABY/USDT:USDT | below_1h_threshold | +3.15% | +3.08% |
| LAB/USDT:USDT | below_1h_threshold | +3.13% | +3.05% |
| XNY/USDT:USDT | below_1h_threshold | +2.86% | +2.78% |
| BEAT/USDT:USDT | below_1h_threshold | +2.47% | +2.39% |
| BSB/USDT:USDT | below_1h_threshold | +2.01% | +1.93% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
