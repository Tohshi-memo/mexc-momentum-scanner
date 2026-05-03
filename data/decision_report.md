# Decision Report

- generated_at: 2026-05-03T14:17:09.107436+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3078**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3078, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-0.72%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.72% | **-0.72%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 11/16 | 68.8% | +2.20% | **+1.51%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.88% | **+0.75%** |
| LIMIT_ATR | 18/20 | 90.0% | +0.77% | **+0.70%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +2.91% | **+2.18%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +4.79% | **+2.16%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +4.45% | **+2.00%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +4.97% | **+1.49%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.89% | **+1.30%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T14:17:07.279779+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=78708.9
- Funnel: target 755 → liquid 167 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +41.83% | $3,951,107.37 |
| TAC/USDT:USDT | +37.66% | $3,412,955.49 |
| NAORIS/USDT:USDT | +30.77% | $4,802,247.46 |
| FHE/USDT:USDT | +25.00% | $4,406,943.11 |
| AKT/USDT:USDT | +22.09% | $2,445,223.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BABY/USDT:USDT | below_1h_threshold | +3.16% | +3.07% |
| BSB/USDT:USDT | below_1h_threshold | +3.06% | +2.96% |
| TRADOOR/USDT:USDT | below_1h_threshold | +2.15% | +2.05% |
| AKT/USDT:USDT | below_1h_threshold | +2.12% | +2.03% |
| FHE/USDT:USDT | below_1h_threshold | +1.71% | +1.62% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
