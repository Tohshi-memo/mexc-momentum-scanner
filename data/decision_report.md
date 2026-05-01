# Decision Report

- generated_at: 2026-05-01T21:11:46.650125+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2832**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.33% / filled 20/20。**
- 全期間 MARKET基準: n=2832, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+1.33%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.33% | **+1.33%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.79% | **+1.79%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.67% | **+1.59%** |
| MARKET | 20/20 | 100.0% | +1.33% | **+1.33%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.45% | **+0.34%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.94% | **+0.70%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +0.85% | **+0.38%** |
| LIMIT_BB3S_LONG | 5/10 | 50.0% | +0.57% | **+0.28%** |

## 2. $100 Live Portfolio

- 残高: **$103.54** / 初期 $100.00 (+3.54%)
- 確定トレード: 5件 (TP 4 / SL 1 / EXP 0)
- 最新: NAORIS/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.54
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T21:11:45.251758+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=77918.0
- Funnel: target 755 → liquid 187 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +27.07% | $6,476,845.59 |
| ZEN/USDT:USDT | +10.55% | $7,894,832.01 |
| TAG/USDT:USDT | +10.42% | $3,459,301.43 |
| FIGHT/USDT:USDT | +9.78% | $1,212,531.40 |
| SNDKSTOCK/USDT:USDT | +7.68% | $6,573,688.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BR/USDT:USDT | below_1h_threshold | +2.44% | +2.34% |
| RIF/USDT:USDT | below_1h_threshold | +1.26% | +1.16% |
| FIGHT/USDT:USDT | below_1h_threshold | +0.97% | +0.87% |
| PLAY/USDT:USDT | below_1h_threshold | +0.89% | +0.79% |
| TAG/USDT:USDT | below_1h_threshold | +0.87% | +0.76% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
