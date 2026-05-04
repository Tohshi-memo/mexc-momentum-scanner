# Decision Report

- generated_at: 2026-05-04T20:36:58.817337+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3257**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3257, expectancy=-0.18%
- 直近20件 MARKET基準: n=20, expectancy=-0.54%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.54% | **-0.54%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 12/20 | 60.0% | +1.55% | **+0.93%** |
| LIMIT_6PCT | 6/20 | 30.0% | +2.92% | **+0.88%** |
| LIMIT_7PCT | 4/20 | 20.0% | +4.13% | **+0.83%** |
| LIMIT_BB3S | 2/13 | 15.4% | +2.06% | **+0.32%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.26% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 14/20 | 70.0% | +2.80% | **+1.96%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.72% | **+0.94%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +2.48% | **+0.75%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.22% | **+0.49%** |

## 2. $100 Live Portfolio

- 残高: **$101.85** / 初期 $100.00 (+1.85%)
- 確定トレード: 15件 (TP 5 / SL 8 / EXP 2)
- 最新: RAVE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.85
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T20:36:56.742083+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=79926.7
- Funnel: target 760 → liquid 200 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RAVE/USDT:USDT | +46.70% | $37,623,349.93 |
| TST/USDT:USDT | +12.32% | $22,608,687.22 |
| SKYAI/USDT:USDT | +11.62% | $101,952,616.84 |
| FHE/USDT:USDT | +9.20% | $2,627,274.49 |
| LUNC/USDT:USDT | +6.24% | $71,351,886.91 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +3.58% | +3.69% |
| AIOZ/USDT:USDT | below_1h_threshold | +2.12% | +2.24% |
| FHE/USDT:USDT | below_1h_threshold | +2.04% | +2.16% |
| TONCOIN/USDT:USDT | below_1h_threshold | +1.89% | +2.00% |
| TST/USDT:USDT | below_1h_threshold | +1.78% | +1.90% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
