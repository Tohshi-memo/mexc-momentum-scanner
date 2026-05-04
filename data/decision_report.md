# Decision Report

- generated_at: 2026-05-04T15:17:17.187443+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3221**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3221, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-1.36%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.36% | **-1.36%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +1.25% | **+0.44%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.96% | **+0.29%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +0.49% | **+0.10%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.07% | **+0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +2.07% | **+2.07%** |
| ASK_LONG | 20/20 | 100.0% | +1.75% | **+1.75%** |
| MARKET_LONG | 20/20 | 100.0% | +1.41% | **+1.41%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.64% | **+1.14%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +3.78% | **+0.95%** |

## 2. $100 Live Portfolio

- 残高: **$102.36** / 初期 $100.00 (+2.36%)
- 確定トレード: 14件 (TP 5 / SL 7 / EXP 2)
- 最新: B/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.36
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T15:17:15.271716+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=80144.5
- Funnel: target 761 → liquid 198 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ELIZAOS/USDT:USDT | +130.30% | $1,440,651.80 |
| SKYAI/USDT:USDT | +85.54% | $88,757,430.79 |
| TST/USDT:USDT | +74.14% | $18,483,880.18 |
| GIGA/USDT:USDT | +41.15% | $2,283,962.82 |
| ASTEROID/USDT:USDT | +33.92% | $4,627,299.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAG/USDT:USDT | below_1h_threshold | +3.70% | +3.73% |
| ELIZAOS/USDT:USDT | below_1h_threshold | +2.74% | +2.77% |
| B/USDT:USDT | below_1h_threshold | +2.58% | +2.62% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +1.81% | +1.84% |
| LAB/USDT:USDT | below_1h_threshold | +1.81% | +1.84% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
