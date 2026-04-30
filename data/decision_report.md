# Decision Report

- generated_at: 2026-04-30T14:21:09.974713+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2709**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.16% / filled 20/20。**
- 全期間 MARKET基準: n=2709, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+1.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.16% | **+1.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.27% | **+1.21%** |
| MARKET | 20/20 | 100.0% | +1.16% | **+1.16%** |
| ASK | 20/20 | 100.0% | +1.14% | **+1.14%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_BB3S | 6/19 | 31.6% | +1.68% | **+0.53%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +1.15% | **+0.92%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +6.07% | **+0.91%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.50% | **+0.60%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.30% | **+0.58%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +1.04% | **+0.57%** |

## 2. $100 Live Portfolio

- 残高: **$100.50** / 初期 $100.00 (+0.50%)
- 確定トレード: 2件 (TP 1 / SL 1 / EXP 0)
- 最新: UB/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.50
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-04-30T14:21:08.219456+00:00 / 保存件数 17/288
- BTC: STAGNANT 1h -0.18% price=76229.3
- Funnel: target 760 → liquid 223 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROLL/USDT:USDT | +39.00% | $2,872,252.28 |
| BR/USDT:USDT | +33.43% | $1,413,781.04 |
| BSB/USDT:USDT | +32.97% | $43,547,459.78 |
| SKYAI/USDT:USDT | +28.71% | $23,166,416.29 |
| RIVER/USDT:USDT | +20.21% | $18,448,330.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RIVER/USDT:USDT | below_1h_threshold | +2.86% | +3.04% |
| QCOMSTOCK/USDT:USDT | below_1h_threshold | +2.67% | +2.85% |
| NAORIS/USDT:USDT | below_1h_threshold | +2.51% | +2.69% |
| SOLV/USDT:USDT | below_1h_threshold | +1.82% | +2.01% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.76% | +1.94% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
