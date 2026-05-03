# Decision Report

- generated_at: 2026-05-03T00:57:08.354264+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3005**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.94% / filled 20/20。**
- 全期間 MARKET基準: n=3005, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.94%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.94% | **+0.94%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.94% | **+0.94%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.76% | **+0.65%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.69% | **+0.55%** |
| LIMIT_BB3S | 7/18 | 38.9% | +1.21% | **+0.47%** |
| ASK | 20/20 | 100.0% | +0.37% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +6.41% | **+6.41%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +2.31% | **+1.04%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.50% | **+1.00%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.56% | **+0.71%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.84% | **+0.71%** |

## 2. $100 Live Portfolio

- 残高: **$103.73** / 初期 $100.00 (+3.73%)
- 確定トレード: 10件 (TP 5 / SL 4 / EXP 1)
- 最新: AIOT/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.73
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T00:57:05.773483+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.22% price=78479.2
- Funnel: target 755 → liquid 163 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.7 >= 65=1, 4h RSI 67.5 >= 65=1, 4h RSI 93.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FHE/USDT:USDT | +24.19% | $2,014,834.87 |
| LUNC/USDT:USDT | +17.57% | $32,715,111.10 |
| BABY/USDT:USDT | +16.05% | $1,569,070.20 |
| BIANRENSHENG/USDT:USDT | +15.76% | $1,824,067.51 |
| TRADOOR/USDT:USDT | +14.73% | $1,219,749.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FHE/USDT:USDT | below_1h_threshold | +3.87% | +4.09% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +3.76% | +3.98% |
| EDGE/USDT:USDT | below_1h_threshold | +2.62% | +2.84% |
| APE/USDT:USDT | below_1h_threshold | +1.93% | +2.15% |
| SPACE/USDT:USDT | below_1h_threshold | +1.72% | +1.94% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
