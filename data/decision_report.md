# Decision Report

- generated_at: 2026-05-03T03:02:20.221725+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3018**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.69% / filled 20/20。**
- 全期間 MARKET基準: n=3018, expectancy=-0.15%
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
| LIMIT_BB3S | 8/15 | 53.3% | +2.39% | **+1.28%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.87% | **+1.21%** |
| LIMIT_2PCT | 13/20 | 65.0% | +1.48% | **+0.96%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | +2.79% | **+0.84%** |
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +0.78% | **+0.62%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +0.56% | **+0.34%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +0.43% | **+0.28%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +0.42% | **+0.28%** |

## 2. $100 Live Portfolio

- 残高: **$103.73** / 初期 $100.00 (+3.73%)
- 確定トレード: 10件 (TP 5 / SL 4 / EXP 1)
- 最新: AIOT/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.73
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T03:02:18.381543+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=78134.2
- Funnel: target 755 → liquid 163 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BIANRENSHENG/USDT:USDT | +15.67% | $2,120,691.03 |
| BABY/USDT:USDT | +11.50% | $1,852,143.61 |
| FHE/USDT:USDT | +11.44% | $2,391,769.74 |
| TRADOOR/USDT:USDT | +9.79% | $1,621,531.78 |
| LUNC/USDT:USDT | +7.51% | $40,875,209.29 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BABY/USDT:USDT | below_1h_threshold | +1.60% | +1.59% |
| ORCA/USDT:USDT | below_1h_threshold | +1.24% | +1.24% |
| ALCH/USDT:USDT | below_1h_threshold | +0.86% | +0.85% |
| ASTEROID/USDT:USDT | below_1h_threshold | +0.81% | +0.80% |
| BSB/USDT:USDT | below_1h_threshold | +0.56% | +0.56% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
