# Decision Report

- generated_at: 2026-05-06T07:07:27.303981+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3424**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.19% / filled 20/20。**
- 全期間 MARKET基準: n=3424, expectancy=-0.14%
- 直近20件 MARKET基準: n=20, expectancy=+1.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.19% | **+1.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/12 | 33.3% | +6.00% | **+2.00%** |
| ASK | 20/20 | 100.0% | +1.24% | **+1.24%** |
| MARKET | 20/20 | 100.0% | +1.19% | **+1.19%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.09% | **+0.73%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 7/8 | 87.5% | +1.45% | **+1.27%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.41% | **+0.37%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.41% | **+0.33%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +0.17% | **+0.13%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-06T07:07:25.260730+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=81447.6
- Funnel: target 765 → liquid 191 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IO/USDT:USDT | +58.67% | $2,646,208.26 |
| ZEC/USDT:USDT | +33.25% | $653,818,778.79 |
| STORJ/USDT:USDT | +31.41% | $2,279,435.89 |
| B3/USDT:USDT | +27.23% | $1,425,816.35 |
| MAVIA/USDT:USDT | +23.08% | $1,882,800.40 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEC/USDT:USDT | below_1h_threshold | +4.29% | +4.27% |
| DASH/USDT:USDT | below_1h_threshold | +4.17% | +4.15% |
| DUSK/USDT:USDT | below_1h_threshold | +2.98% | +2.96% |
| ZEN/USDT:USDT | below_1h_threshold | +2.03% | +2.01% |
| IO/USDT:USDT | below_1h_threshold | +1.52% | +1.50% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
