# Decision Report

- generated_at: 2026-05-04T05:07:14.367078+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3152**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3152, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-1.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.06% | **-1.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/14 | 35.7% | +1.78% | **+0.63%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.46% | **+0.44%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.12% | **+0.28%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/6 | 66.7% | +1.70% | **+1.13%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.03% | **+0.93%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +2.57% | **+0.90%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.73% | **+0.78%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.38% | **+0.76%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T05:07:12.456308+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=80312.5
- Funnel: target 758 → liquid 169 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +64.57% | $20,898,235.18 |
| SKYAI/USDT:USDT | +52.86% | $44,974,159.22 |
| LAB/USDT:USDT | +47.11% | $215,620,077.58 |
| TAG/USDT:USDT | +42.50% | $7,170,260.05 |
| TST/USDT:USDT | +35.93% | $6,318,497.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +4.63% | +4.61% |
| MEGA/USDT:USDT | below_1h_threshold | +2.94% | +2.92% |
| SAPIEN/USDT:USDT | below_1h_threshold | +2.48% | +2.47% |
| SIREN/USDT:USDT | below_1h_threshold | +1.40% | +1.39% |
| PARTI/USDT:USDT | below_1h_threshold | +1.08% | +1.06% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
