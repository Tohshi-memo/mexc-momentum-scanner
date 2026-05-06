# Decision Report

- generated_at: 2026-05-06T08:02:37.479027+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3431**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.12% / filled 20/20。**
- 全期間 MARKET基準: n=3431, expectancy=-0.14%
- 直近20件 MARKET基準: n=20, expectancy=+1.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.12% | **+1.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.17% | **+1.17%** |
| MARKET | 20/20 | 100.0% | +1.12% | **+1.12%** |
| LIMIT_BB3S | 4/9 | 44.4% | +2.40% | **+1.07%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.62% | **+0.43%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.91% | **+0.91%** |
| LIMIT_8PCT_LONG | 3/20 | 15.0% | +0.00% | **+0.00%** |
| MARKET_LONG | 20/20 | 100.0% | -0.01% | **-0.01%** |
| ASK_LONG | 20/20 | 100.0% | -0.06% | **-0.06%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | -0.15% | **-0.06%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-06T08:02:35.487742+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=81395.0
- Funnel: target 765 → liquid 196 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IO/USDT:USDT | +73.89% | $6,997,707.27 |
| ZEC/USDT:USDT | +37.56% | $690,439,033.63 |
| B3/USDT:USDT | +30.42% | $1,442,134.69 |
| STORJ/USDT:USDT | +28.13% | $2,484,149.74 |
| MAVIA/USDT:USDT | +22.96% | $1,898,264.54 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ARKM/USDT:USDT | below_1h_threshold | +1.63% | +1.55% |
| EIGEN/USDT:USDT | below_1h_threshold | +0.86% | +0.78% |
| TRIA/USDT:USDT | below_1h_threshold | +0.84% | +0.76% |
| LAB/USDT:USDT | below_1h_threshold | +0.76% | +0.69% |
| NAORIS/USDT:USDT | below_1h_threshold | +0.74% | +0.66% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
