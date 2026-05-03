# Decision Report

- generated_at: 2026-05-03T05:12:11.330802+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3031**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.26% / filled 20/20。**
- 全期間 MARKET基準: n=3031, expectancy=-0.14%
- 直近20件 MARKET基準: n=20, expectancy=+2.26%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.26% | **+2.26%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.29% | **+2.29%** |
| MARKET | 20/20 | 100.0% | +2.26% | **+2.26%** |
| LIMIT_3PCT | 13/20 | 65.0% | +2.25% | **+1.46%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.48% | **+1.11%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.27% | **+1.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 9/20 | 45.0% | -0.00% | **-0.00%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | -0.37% | **-0.19%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | -1.93% | **-0.29%** |
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | -0.96% | **-0.29%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -1.45% | **-0.29%** |

## 2. $100 Live Portfolio

- 残高: **$103.73** / 初期 $100.00 (+3.73%)
- 確定トレード: 10件 (TP 5 / SL 4 / EXP 1)
- 最新: AIOT/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.73
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T05:12:09.070855+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=78200.0
- Funnel: target 755 → liquid 167 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.9 >= 65=1, 4h RSI 95.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BABY/USDT:USDT | +28.21% | $2,352,402.94 |
| BR/USDT:USDT | +22.04% | $2,197,507.30 |
| FHE/USDT:USDT | +16.26% | $2,493,065.00 |
| FIGHT/USDT:USDT | +14.94% | $1,007,616.29 |
| AKT/USDT:USDT | +12.24% | $1,180,401.61 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BR/USDT:USDT | below_1h_threshold | +2.96% | +2.87% |
| FIGHT/USDT:USDT | below_1h_threshold | +1.69% | +1.60% |
| XNY/USDT:USDT | below_1h_threshold | +1.37% | +1.28% |
| FHE/USDT:USDT | below_1h_threshold | +1.14% | +1.05% |
| ASTEROID/USDT:USDT | below_1h_threshold | +0.78% | +0.70% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
