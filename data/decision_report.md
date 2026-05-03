# Decision Report

- generated_at: 2026-05-03T13:52:23.808389+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3074**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3074, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-1.53%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.53% | **-1.53%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 19/20 | 95.0% | +0.87% | **+0.82%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.02% | **+0.41%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_BB3S | 10/16 | 62.5% | +0.25% | **+0.16%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +2.91% | **+2.18%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +3.87% | **+1.36%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +3.43% | **+1.20%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +2.74% | **+1.10%** |
| LIMIT_7PCT_LONG | 4/20 | 20.0% | +3.46% | **+0.69%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T13:52:20.997527+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=78619.9
- Funnel: target 755 → liquid 169 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.0 >= 65=1, 4h RSI 76.1 >= 65=1, 4h RSI 77.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAC/USDT:USDT | +42.52% | $2,895,736.17 |
| TST/USDT:USDT | +40.82% | $3,800,076.64 |
| NAORIS/USDT:USDT | +34.28% | $4,411,241.77 |
| AIGENSYN/USDT:USDT | +26.95% | $5,034,397.59 |
| FHE/USDT:USDT | +24.19% | $4,248,547.21 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XNY/USDT:USDT | below_1h_threshold | +2.81% | +2.93% |
| ALCH/USDT:USDT | below_1h_threshold | +2.03% | +2.15% |
| FIGHT/USDT:USDT | below_1h_threshold | +1.72% | +1.84% |
| AKT/USDT:USDT | below_1h_threshold | +1.63% | +1.75% |
| M/USDT:USDT | below_1h_threshold | +1.56% | +1.68% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
