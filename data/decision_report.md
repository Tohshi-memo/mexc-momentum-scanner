# Decision Report

- generated_at: 2026-05-01T14:14:14.694099+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2808**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2808, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-1.78%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.78% | **-1.78%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +3.92% | **+1.18%** |
| LIMIT_7PCT | 4/20 | 20.0% | +5.40% | **+1.08%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.46% | **+0.23%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.25% | **+0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.86% | **+1.48%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.65% | **+1.48%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +2.02% | **+0.81%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.17% | **+0.70%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +1.72% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$102.51** / 初期 $100.00 (+2.51%)
- 確定トレード: 4件 (TP 3 / SL 1 / EXP 0)
- 最新: PLAY/USDT:USDT TP_HIT PnL +7.74% 残高後 $102.51
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T14:14:12.684332+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=78780.1
- Funnel: target 760 → liquid 200 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B/USDT:USDT | +104.22% | $22,174,436.85 |
| UB/USDT:USDT | +75.28% | $20,622,462.42 |
| NFP/USDT:USDT | +56.39% | $1,807,944.41 |
| BR/USDT:USDT | +45.38% | $26,023,868.20 |
| ZEREBRO/USDT:USDT | +35.14% | $12,089,656.22 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_1h_threshold | +4.62% | +4.50% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +4.18% | +4.07% |
| ST/USDT:USDT | below_1h_threshold | +2.01% | +1.90% |
| RDDTSTOCK/USDT:USDT | below_1h_threshold | +1.78% | +1.67% |
| BR/USDT:USDT | below_1h_threshold | +1.50% | +1.39% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
