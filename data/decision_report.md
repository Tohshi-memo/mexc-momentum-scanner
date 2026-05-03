# Decision Report

- generated_at: 2026-05-03T15:52:12.231496+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3082**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3082, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+0.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.05% | **+0.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 9/15 | 60.0% | +2.95% | **+1.77%** |
| LIMIT_ATR | 18/20 | 90.0% | +1.73% | **+1.56%** |
| LIMIT_3PCT | 15/20 | 75.0% | +1.65% | **+1.24%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.69% | **+0.59%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.51% | **+0.51%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +2.69% | **+1.35%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +2.68% | **+1.21%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +3.00% | **+1.05%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.97% | **+0.99%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.67% | **+0.92%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T15:52:10.211652+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=78597.5
- Funnel: target 755 → liquid 168 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NAORIS/USDT:USDT | +33.65% | $6,838,923.25 |
| TAC/USDT:USDT | +32.41% | $4,918,812.38 |
| TST/USDT:USDT | +28.89% | $4,841,119.66 |
| AIGENSYN/USDT:USDT | +19.20% | $5,301,678.11 |
| REZ/USDT:USDT | +17.19% | $1,423,386.94 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| WLFI/USDT:USDT | below_1h_threshold | +2.66% | +2.79% |
| REZ/USDT:USDT | below_1h_threshold | +2.50% | +2.63% |
| ZEC/USDT:USDT | below_1h_threshold | +2.49% | +2.62% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +2.48% | +2.61% |
| GUA/USDT:USDT | below_1h_threshold | +2.04% | +2.17% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
