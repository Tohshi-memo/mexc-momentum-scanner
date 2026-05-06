# Decision Report

- generated_at: 2026-05-06T03:27:18.064272+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3412**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.36% / filled 20/20。**
- 全期間 MARKET基準: n=3412, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+1.36%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.36% | **+1.36%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.48% | **+1.48%** |
| MARKET | 20/20 | 100.0% | +1.36% | **+1.36%** |
| LIMIT_BB3S | 5/12 | 41.7% | +2.39% | **+0.99%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +2.47% | **+0.99%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.77% | **+0.61%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.26% | **+0.64%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.54% | **+0.64%** |
| LIMIT_BB3S_LONG | 6/7 | 85.7% | +0.62% | **+0.53%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +2.55% | **+0.51%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | -0.20% | **-0.15%** |

## 2. $100 Live Portfolio

- 残高: **$100.33** / 初期 $100.00 (+0.33%)
- 確定トレード: 18件 (TP 5 / SL 11 / EXP 2)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.33
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-06T03:27:16.143092+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.39% price=81635.9
- Funnel: target 765 → liquid 188 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B3/USDT:USDT | +28.42% | $1,371,138.05 |
| MAVIA/USDT:USDT | +25.81% | $1,758,129.51 |
| NOT/USDT:USDT | +24.82% | $6,591,886.49 |
| ZEC/USDT:USDT | +22.38% | $601,713,300.47 |
| SMCISTOCK/USDT:USDT | +20.44% | $5,239,455.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FILECOIN/USDT:USDT | below_1h_threshold | +3.29% | +2.90% |
| LAB/USDT:USDT | below_1h_threshold | +3.21% | +2.82% |
| VVV/USDT:USDT | below_1h_threshold | +1.63% | +1.24% |
| TIA/USDT:USDT | below_1h_threshold | +1.59% | +1.20% |
| NAORIS/USDT:USDT | below_1h_threshold | +1.38% | +0.99% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
