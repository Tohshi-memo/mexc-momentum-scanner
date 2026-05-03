# Decision Report

- generated_at: 2026-05-03T13:47:08.646353+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3072**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3072, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-1.55%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.55% | **-1.55%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 19/20 | 95.0% | +1.07% | **+1.02%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.02% | **+0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +2.35% | **+1.57%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +3.32% | **+1.50%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +3.87% | **+1.36%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +3.43% | **+1.20%** |
| LIMIT_7PCT_LONG | 4/20 | 20.0% | +3.46% | **+0.69%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T13:47:06.046946+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=78620.8
- Funnel: target 755 → liquid 169 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.6 >= 65=1, 4h RSI 76.4 >= 65=1, 4h RSI 77.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAC/USDT:USDT | +42.18% | $2,791,411.74 |
| TST/USDT:USDT | +41.37% | $3,760,154.13 |
| NAORIS/USDT:USDT | +32.63% | $4,331,950.06 |
| AIGENSYN/USDT:USDT | +24.97% | $4,987,275.29 |
| FHE/USDT:USDT | +24.64% | $4,224,216.03 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XNY/USDT:USDT | below_1h_threshold | +3.55% | +3.67% |
| FIGHT/USDT:USDT | below_1h_threshold | +2.19% | +2.31% |
| AKT/USDT:USDT | below_1h_threshold | +2.08% | +2.20% |
| ALCH/USDT:USDT | below_1h_threshold | +1.84% | +1.96% |
| BR/USDT:USDT | below_1h_threshold | +1.44% | +1.56% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
