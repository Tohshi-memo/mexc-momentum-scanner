# Decision Report

- generated_at: 2026-05-05T05:37:15.794568+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3315**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.30% / filled 20/20。**
- 全期間 MARKET基準: n=3315, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+1.30%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.30% | **+1.30%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.38% | **+1.38%** |
| MARKET | 20/20 | 100.0% | +1.30% | **+1.30%** |
| LIMIT_BB3S | 5/13 | 38.5% | +1.72% | **+0.66%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.84% | **+0.38%** |
| LIMIT_5PCT | 5/20 | 25.0% | +1.07% | **+0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/7 | 28.6% | +6.30% | **+1.80%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.27% | **+0.23%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.06% | **+0.02%** |
| ASK_LONG | 20/20 | 100.0% | -0.06% | **-0.06%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 16件 (TP 5 / SL 9 / EXP 2)
- 最新: NAORIS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.34
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T05:37:11.151856+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.29% price=81083.9
- Funnel: target 765 → liquid 206 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 92.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOGS/USDT:USDT | +72.35% | $7,651,212.94 |
| HIVE/USDT:USDT | +40.69% | $1,569,410.04 |
| FHE/USDT:USDT | +28.39% | $3,726,567.87 |
| TONCOIN/USDT:USDT | +18.87% | $65,682,299.42 |
| M/USDT:USDT | +17.17% | $1,926,122.70 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEREBRO/USDT:USDT | below_1h_threshold | +2.24% | +1.96% |
| ALGO/USDT:USDT | below_1h_threshold | +2.13% | +1.84% |
| MORPHO/USDT:USDT | below_1h_threshold | +2.08% | +1.80% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +1.64% | +1.35% |
| JUP/USDT:USDT | below_1h_threshold | +1.54% | +1.25% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
