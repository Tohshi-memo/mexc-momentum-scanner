# Decision Report

- generated_at: 2026-05-02T13:48:16.804527+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2908**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2908, expectancy=-0.14%
- 直近20件 MARKET基準: n=20, expectancy=-2.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.19% | **-2.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +3.92% | **+1.18%** |
| LIMIT_5PCT | 11/20 | 55.0% | +1.14% | **+0.63%** |
| LIMIT_BB3S | 9/16 | 56.2% | -0.05% | **-0.03%** |
| LIMIT_4PCT | 16/20 | 80.0% | -0.25% | **-0.20%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | -0.76% | **-0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +4.24% | **+2.12%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +3.50% | **+1.40%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +3.22% | **+1.13%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +2.03% | **+1.12%** |
| MARKET_LONG | 20/20 | 100.0% | +0.99% | **+0.99%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 8件 (TP 4 / SL 4 / EXP 0)
- 最新: NAORIS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T13:48:14.124819+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.17% price=78304.9
- Funnel: target 755 → liquid 166 → pre 50 → checked 50 → surge 4 → strict 0
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.2 >= 65=1, 4h RSI 94.5 >= 65=1, 4h RSI 73.8 >= 65=1, 4h RSI 78.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +226.32% | $135,659,876.01 |
| BIO/USDT:USDT | +44.35% | $2,813,036.79 |
| TAG/USDT:USDT | +43.89% | $6,843,787.22 |
| SPACE/USDT:USDT | +29.12% | $1,366,716.28 |
| SKYAI/USDT:USDT | +23.49% | $21,553,800.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| B/USDT:USDT | below_1h_threshold | +4.86% | +4.69% |
| SPACE/USDT:USDT | below_1h_threshold | +4.06% | +3.89% |
| UB/USDT:USDT | below_1h_threshold | +3.92% | +3.75% |
| ORDI/USDT:USDT | below_1h_threshold | +3.33% | +3.16% |
| LUNC/USDT:USDT | below_1h_threshold | +2.06% | +1.89% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
