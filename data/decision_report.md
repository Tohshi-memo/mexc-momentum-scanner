# Decision Report

- generated_at: 2026-05-03T06:47:08.745357+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3043**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3043, expectancy=-0.14%
- 直近20件 MARKET基準: n=20, expectancy=+0.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.17% | **+0.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 8/12 | 66.7% | +1.80% | **+1.20%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.39% | **+0.33%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.68% | **+0.30%** |
| ASK | 20/20 | 100.0% | +0.28% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +2.63% | **+1.71%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +1.65% | **+0.83%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.71% | **+0.60%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.84% | **+0.46%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.51% | **+0.43%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T06:47:06.680498+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=78103.8
- Funnel: target 755 → liquid 168 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BABY/USDT:USDT | +45.86% | $4,967,916.00 |
| BR/USDT:USDT | +28.45% | $2,698,944.47 |
| AIGENSYN/USDT:USDT | +16.81% | $2,400,274.12 |
| BSB/USDT:USDT | +16.80% | $14,926,678.79 |
| AKT/USDT:USDT | +12.20% | $1,345,857.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +4.35% | +4.48% |
| BABY/USDT:USDT | below_1h_threshold | +3.87% | +4.00% |
| TAC/USDT:USDT | below_1h_threshold | +3.83% | +3.97% |
| ORCA/USDT:USDT | below_1h_threshold | +1.73% | +1.86% |
| BR/USDT:USDT | below_1h_threshold | +1.30% | +1.44% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
