# Decision Report

- generated_at: 2026-05-03T01:17:07.315162+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3008**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.51% / filled 20/20。**
- 全期間 MARKET基準: n=3008, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+1.51%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.51% | **+1.51%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.51% | **+1.51%** |
| ASK | 20/20 | 100.0% | +0.94% | **+0.94%** |
| LIMIT_1PCT | 15/20 | 75.0% | +0.60% | **+0.45%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.51% | **+0.36%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.79% | **+0.16%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +6.41% | **+6.41%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +2.30% | **+1.03%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +2.04% | **+1.02%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.56% | **+0.71%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.84% | **+0.71%** |

## 2. $100 Live Portfolio

- 残高: **$103.73** / 初期 $100.00 (+3.73%)
- 確定トレード: 10件 (TP 5 / SL 4 / EXP 1)
- 最新: AIOT/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.73
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T01:17:05.515588+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.22% price=78325.3
- Funnel: target 755 → liquid 160 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LUNC/USDT:USDT | +19.55% | $33,611,805.76 |
| BABY/USDT:USDT | +19.28% | $1,719,214.25 |
| BIANRENSHENG/USDT:USDT | +15.41% | $1,842,711.36 |
| SPACE/USDT:USDT | +14.54% | $1,782,245.95 |
| TRADOOR/USDT:USDT | +14.22% | $1,327,550.06 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| USTC/USDT:USDT | below_1h_threshold | +2.14% | +2.37% |
| TRADOOR/USDT:USDT | below_1h_threshold | +2.10% | +2.32% |
| BABY/USDT:USDT | below_1h_threshold | +2.06% | +2.29% |
| SPACE/USDT:USDT | below_1h_threshold | +2.02% | +2.25% |
| ORCA/USDT:USDT | below_1h_threshold | +0.82% | +1.04% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
