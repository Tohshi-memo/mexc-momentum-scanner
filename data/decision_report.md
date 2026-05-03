# Decision Report

- generated_at: 2026-05-03T14:01:25.956257+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3076**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3076, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-1.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.32% | **-1.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 19/20 | 95.0% | +0.75% | **+0.71%** |
| LIMIT_BB3S | 9/15 | 60.0% | +0.91% | **+0.55%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_5PCT | 6/20 | 30.0% | +1.04% | **+0.31%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +4.39% | **+1.76%** |
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +2.91% | **+1.74%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +4.00% | **+1.60%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +3.32% | **+1.50%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +4.37% | **+1.09%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T14:01:24.141172+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=78657.4
- Funnel: target 755 → liquid 167 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAC/USDT:USDT | +45.04% | $3,009,386.96 |
| TST/USDT:USDT | +42.93% | $3,882,524.55 |
| NAORIS/USDT:USDT | +30.32% | $4,474,971.87 |
| FHE/USDT:USDT | +24.44% | $4,340,210.19 |
| AIGENSYN/USDT:USDT | +21.21% | $4,975,270.85 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAC/USDT:USDT | below_1h_threshold | +2.89% | +2.86% |
| FHE/USDT:USDT | below_1h_threshold | +1.10% | +1.07% |
| XNY/USDT:USDT | below_1h_threshold | +0.72% | +0.69% |
| BABY/USDT:USDT | below_1h_threshold | +0.70% | +0.67% |
| THETA/USDT:USDT | below_1h_threshold | +0.57% | +0.54% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
