# Decision Report

- generated_at: 2026-05-06T00:52:22.835641+00:00
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

- 更新: 2026-05-06T00:52:20.661786+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=80900.7
- Funnel: target 761 → liquid 191 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B3/USDT:USDT | +31.75% | $1,068,548.02 |
| FHE/USDT:USDT | +28.36% | $27,385,683.85 |
| MAVIA/USDT:USDT | +27.25% | $1,599,510.25 |
| SWARMS/USDT:USDT | +20.30% | $2,389,617.33 |
| ZEC/USDT:USDT | +19.63% | $604,257,713.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MERL/USDT:USDT | below_1h_threshold | +3.31% | +3.27% |
| FHE/USDT:USDT | below_1h_threshold | +2.80% | +2.75% |
| DUSK/USDT:USDT | below_1h_threshold | +2.58% | +2.54% |
| DASH/USDT:USDT | below_1h_threshold | +2.18% | +2.13% |
| GIGGLE/USDT:USDT | below_1h_threshold | +2.13% | +2.09% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
