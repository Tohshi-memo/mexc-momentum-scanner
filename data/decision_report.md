# Decision Report

- generated_at: 2026-05-06T03:17:28.215679+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3411**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.83% / filled 20/20。**
- 全期間 MARKET基準: n=3411, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+0.83%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.83% | **+0.83%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/11 | 45.5% | +2.39% | **+1.08%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +2.16% | **+0.97%** |
| ASK | 20/20 | 100.0% | +0.95% | **+0.95%** |
| MARKET | 20/20 | 100.0% | +0.83% | **+0.83%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.62% | **+0.53%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 7/8 | 87.5% | +1.10% | **+0.97%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.26% | **+0.64%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.90% | **+0.58%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +2.55% | **+0.51%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.31% | **+0.23%** |

## 2. $100 Live Portfolio

- 残高: **$100.33** / 初期 $100.00 (+0.33%)
- 確定トレード: 18件 (TP 5 / SL 11 / EXP 2)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.33
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-06T03:17:26.247093+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=81339.1
- Funnel: target 765 → liquid 187 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B3/USDT:USDT | +29.88% | $1,345,629.02 |
| MAVIA/USDT:USDT | +27.84% | $1,739,922.50 |
| NOT/USDT:USDT | +26.85% | $6,333,667.36 |
| ZEC/USDT:USDT | +22.45% | $598,568,682.73 |
| SMCISTOCK/USDT:USDT | +20.08% | $5,232,999.61 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +3.32% | +3.30% |
| FILECOIN/USDT:USDT | below_1h_threshold | +1.84% | +1.81% |
| NAORIS/USDT:USDT | below_1h_threshold | +1.15% | +1.13% |
| VVV/USDT:USDT | below_1h_threshold | +1.15% | +1.13% |
| APT/USDT:USDT | below_1h_threshold | +0.92% | +0.89% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
