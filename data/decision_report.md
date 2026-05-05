# Decision Report

- generated_at: 2026-05-05T05:32:40.614779+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3313**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.03% / filled 20/20。**
- 全期間 MARKET基準: n=3313, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+1.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.03% | **+1.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.09% | **+1.09%** |
| MARKET | 20/20 | 100.0% | +1.03% | **+1.03%** |
| LIMIT_5PCT | 6/20 | 30.0% | +2.22% | **+0.67%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.01% | **+0.65%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +1.22% | **+0.61%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/7 | 42.9% | +2.87% | **+1.23%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.19% | **+0.48%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +0.17% | **+0.07%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +0.19% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 16件 (TP 5 / SL 9 / EXP 2)
- 最新: NAORIS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.34
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T05:32:35.682627+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.17% price=80985.0
- Funnel: target 765 → liquid 206 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 92.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOGS/USDT:USDT | +71.23% | $7,586,086.07 |
| HIVE/USDT:USDT | +38.36% | $1,408,067.81 |
| FHE/USDT:USDT | +28.06% | $3,699,458.72 |
| TONCOIN/USDT:USDT | +19.10% | $65,462,703.62 |
| 4/USDT:USDT | +15.44% | $2,289,090.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIGENSYN/USDT:USDT | below_1h_threshold | +2.07% | +1.90% |
| ALGO/USDT:USDT | below_1h_threshold | +1.88% | +1.71% |
| PLAY/USDT:USDT | below_1h_threshold | +1.80% | +1.63% |
| MORPHO/USDT:USDT | below_1h_threshold | +1.68% | +1.51% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.40% | +1.23% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
