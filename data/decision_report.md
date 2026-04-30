# Decision Report

- generated_at: 2026-04-30T18:56:04.204074+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2730**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2730, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 9/20 | 45.0% | +1.94% | **+0.87%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_8PCT | 4/20 | 20.0% | +2.85% | **+0.57%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.87% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +3.21% | **+2.73%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +2.33% | **+2.33%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +6.29% | **+2.20%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +6.49% | **+1.95%** |
| ASK_LONG | 20/20 | 100.0% | +1.65% | **+1.65%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: GRIFFAIN/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-04-30T18:56:02.735255+00:00 / 保存件数 75/288
- BTC: STAGNANT 1h +0.18% price=76348.3
- Funnel: target 757 → liquid 229 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=1, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BR/USDT:USDT | +24.87% | $7,261,671.18 |
| BIO/USDT:USDT | +9.69% | $3,807,505.32 |
| AIOT/USDT:USDT | +8.37% | $15,721,495.43 |
| ASTEROID/USDT:USDT | +5.58% | $3,930,657.23 |
| ZEREBRO/USDT:USDT | +5.46% | $3,431,951.31 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BR/USDT:USDT | below_relative_strength | +5.08% | +4.90% |
| BIO/USDT:USDT | below_1h_threshold | +2.88% | +2.70% |
| FLOW/USDT:USDT | below_1h_threshold | +2.66% | +2.48% |
| ORCA/USDT:USDT | below_1h_threshold | +2.28% | +2.09% |
| ZEC/USDT:USDT | below_1h_threshold | +2.25% | +2.06% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
