# Decision Report

- generated_at: 2026-05-03T15:04:27.404841+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3080**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3080, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-0.18%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.18% | **-0.18%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 10/15 | 66.7% | +2.62% | **+1.75%** |
| LIMIT_ATR | 18/20 | 90.0% | +1.89% | **+1.70%** |
| LIMIT_3PCT | 15/20 | 75.0% | +1.65% | **+1.24%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.69% | **+0.59%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +3.34% | **+1.51%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +3.28% | **+1.31%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +3.68% | **+1.10%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.77% | **+0.80%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.50% | **+0.75%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T15:04:25.594795+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=78737.2
- Funnel: target 755 → liquid 165 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAC/USDT:USDT | +46.66% | $4,071,291.39 |
| TST/USDT:USDT | +46.42% | $4,306,746.73 |
| NAORIS/USDT:USDT | +32.67% | $5,874,124.47 |
| FHE/USDT:USDT | +22.89% | $4,604,045.32 |
| BABY/USDT:USDT | +20.49% | $21,389,564.16 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GUA/USDT:USDT | below_1h_threshold | +2.58% | +2.53% |
| LUNC/USDT:USDT | below_1h_threshold | +1.80% | +1.76% |
| B/USDT:USDT | below_1h_threshold | +1.18% | +1.13% |
| BABY/USDT:USDT | below_1h_threshold | +1.15% | +1.10% |
| JTO/USDT:USDT | below_1h_threshold | +0.85% | +0.80% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
