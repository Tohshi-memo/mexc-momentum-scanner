# Decision Report

- generated_at: 2026-05-03T02:32:04.629375+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3017**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.69% / filled 20/20。**
- 全期間 MARKET基準: n=3017, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+1.69%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.69% | **+1.69%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.71% | **+1.71%** |
| MARKET | 20/20 | 100.0% | +1.69% | **+1.69%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.94% | **+1.36%** |
| LIMIT_BB3S | 8/15 | 53.3% | +2.39% | **+1.28%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.87% | **+1.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +0.78% | **+0.62%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +0.73% | **+0.48%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +1.88% | **+0.47%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +1.75% | **+0.44%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +0.71% | **+0.43%** |

## 2. $100 Live Portfolio

- 残高: **$103.73** / 初期 $100.00 (+3.73%)
- 確定トレード: 10件 (TP 5 / SL 4 / EXP 1)
- 最新: AIOT/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.73
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T02:32:02.819962+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.14% price=78087.8
- Funnel: target 755 → liquid 160 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BABY/USDT:USDT | +14.68% | $1,871,409.54 |
| BIANRENSHENG/USDT:USDT | +14.35% | $2,078,844.32 |
| LUNC/USDT:USDT | +12.02% | $39,823,642.00 |
| TRADOOR/USDT:USDT | +10.65% | $1,555,405.77 |
| FHE/USDT:USDT | +9.93% | $2,373,021.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BR/USDT:USDT | below_1h_threshold | +4.76% | +4.90% |
| TRADOOR/USDT:USDT | below_1h_threshold | +3.56% | +3.70% |
| BABY/USDT:USDT | below_1h_threshold | +3.41% | +3.55% |
| ALCH/USDT:USDT | below_1h_threshold | +0.99% | +1.13% |
| BEAT/USDT:USDT | below_1h_threshold | +0.85% | +0.99% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
