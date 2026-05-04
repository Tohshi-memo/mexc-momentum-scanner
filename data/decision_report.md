# Decision Report

- generated_at: 2026-05-04T10:11:57.225058+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3185**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3185, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-0.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.39% | **-0.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/18 | 33.3% | +2.97% | **+0.99%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.62% | **+0.40%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.35% | **+0.25%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +2.03% | **+1.12%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +1.59% | **+1.03%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.05% | **+0.92%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.39% | **+0.63%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.60% | **+0.39%** |

## 2. $100 Live Portfolio

- 残高: **$103.40** / 初期 $100.00 (+3.40%)
- 確定トレード: 12件 (TP 5 / SL 5 / EXP 2)
- 最新: B2/USDT:USDT EXPIRED PnL +1.44% 残高後 $103.40
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T10:11:55.730828+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -1.39% price=78692.8
- Funnel: target 761 → liquid 183 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +64.48% | $8,098,160.55 |
| SKYAI/USDT:USDT | +60.92% | $52,144,947.63 |
| TAG/USDT:USDT | +53.79% | $14,096,515.27 |
| GIGA/USDT:USDT | +50.59% | $1,425,254.95 |
| BSB/USDT:USDT | +33.54% | $26,284,710.14 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UKOIL/USDT:USDT | below_1h_threshold | +3.34% | +4.73% |
| GIGA/USDT:USDT | below_1h_threshold | +3.23% | +4.62% |
| USOIL/USDT:USDT | below_1h_threshold | +3.18% | +4.57% |
| AIOT/USDT:USDT | below_1h_threshold | +2.18% | +3.56% |
| TST/USDT:USDT | below_1h_threshold | +2.07% | +3.46% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
