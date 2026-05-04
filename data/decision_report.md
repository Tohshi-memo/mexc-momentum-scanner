# Decision Report

- generated_at: 2026-05-04T14:07:11.923918+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3211**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3211, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.86%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.86% | **-0.86%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_8PCT | 4/20 | 20.0% | +1.78% | **+0.36%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.94% | **+0.28%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.80% | **+0.24%** |
| LIMIT_9PCT | 2/20 | 10.0% | +0.29% | **+0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +3.34% | **+3.34%** |
| ASK_LONG | 20/20 | 100.0% | +1.89% | **+1.89%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.62% | **+1.70%** |
| MARKET_LONG | 20/20 | 100.0% | +1.51% | **+1.51%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +1.76% | **+1.14%** |

## 2. $100 Live Portfolio

- 残高: **$102.88** / 初期 $100.00 (+2.88%)
- 確定トレード: 13件 (TP 5 / SL 6 / EXP 2)
- 最新: LAB/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.88
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T14:07:09.976288+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.25% price=78547.0
- Funnel: target 761 → liquid 191 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +113.42% | $15,383,091.37 |
| SKYAI/USDT:USDT | +91.52% | $76,933,814.47 |
| GIGA/USDT:USDT | +46.73% | $2,191,981.52 |
| 4/USDT:USDT | +36.80% | $1,775,976.61 |
| TAG/USDT:USDT | +26.80% | $16,585,856.84 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +1.24% | +1.49% |
| UB/USDT:USDT | below_1h_threshold | +1.14% | +1.40% |
| LUNC/USDT:USDT | below_1h_threshold | +0.91% | +1.16% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +0.88% | +1.14% |
| ONDO/USDT:USDT | below_1h_threshold | +0.72% | +0.97% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
