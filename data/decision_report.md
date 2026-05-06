# Decision Report

- generated_at: 2026-05-06T00:17:13.389882+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3401**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.54% / filled 20/20。**
- 全期間 MARKET基準: n=3401, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+0.54%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.54% | **+0.54%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 14/20 | 70.0% | +1.35% | **+0.95%** |
| ASK | 20/20 | 100.0% | +0.64% | **+0.64%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.39% | **+0.56%** |
| MARKET | 20/20 | 100.0% | +0.54% | **+0.54%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.84% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 18/20 | 90.0% | +1.62% | **+1.46%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.94% | **+0.56%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +2.62% | **+0.39%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.78% | **+0.35%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.39% | **+0.24%** |

## 2. $100 Live Portfolio

- 残高: **$100.33** / 初期 $100.00 (+0.33%)
- 確定トレード: 18件 (TP 5 / SL 11 / EXP 2)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.33
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-06T00:17:11.496147+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.34% price=81133.6
- Funnel: target 760 → liquid 189 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FHE/USDT:USDT | +28.24% | $26,659,602.14 |
| MAVIA/USDT:USDT | +24.22% | $1,544,757.15 |
| SWARMS/USDT:USDT | +20.91% | $2,356,738.20 |
| ZEC/USDT:USDT | +20.46% | $589,955,486.90 |
| SMCISTOCK/USDT:USDT | +19.69% | $5,168,658.98 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKT/USDT:USDT | below_1h_threshold | +4.14% | +3.80% |
| DASH/USDT:USDT | below_1h_threshold | +4.04% | +3.70% |
| TST/USDT:USDT | below_1h_threshold | +3.63% | +3.29% |
| 4/USDT:USDT | below_1h_threshold | +3.38% | +3.05% |
| FHE/USDT:USDT | below_1h_threshold | +2.62% | +2.29% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
