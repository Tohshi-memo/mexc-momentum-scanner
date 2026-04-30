# Decision Report

- generated_at: 2026-04-30T18:51:03.111683+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2729**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2729, expectancy=-0.10%
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
| LIMIT_8PCT | 5/20 | 25.0% | +3.02% | **+0.76%** |
| LIMIT_9PCT | 4/20 | 20.0% | +3.29% | **+0.66%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.44% | **+0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +6.70% | **+2.35%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +6.29% | **+2.20%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +2.51% | **+2.13%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +1.87% | **+1.87%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +5.11% | **+1.79%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: GRIFFAIN/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-04-30T18:51:01.610178+00:00 / 保存件数 74/288
- BTC: BULLISH 1h +0.23% price=76385.0
- Funnel: target 757 → liquid 229 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BR/USDT:USDT | +20.88% | $6,923,008.23 |
| BIO/USDT:USDT | +10.81% | $3,794,259.74 |
| AIOT/USDT:USDT | +5.97% | $15,585,579.29 |
| ZEREBRO/USDT:USDT | +5.54% | $3,430,778.41 |
| CVNASTOCK/USDT:USDT | +4.91% | $3,577,903.61 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BIO/USDT:USDT | below_1h_threshold | +3.93% | +3.70% |
| PLAY/USDT:USDT | below_1h_threshold | +2.35% | +2.11% |
| LUNANEW/USDT:USDT | below_1h_threshold | +2.30% | +2.07% |
| BR/USDT:USDT | below_1h_threshold | +2.18% | +1.95% |
| ORCA/USDT:USDT | below_1h_threshold | +2.14% | +1.91% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
