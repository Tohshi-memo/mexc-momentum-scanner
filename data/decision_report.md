# Decision Report

- generated_at: 2026-05-01T07:41:07.290665+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2763**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.58% / filled 20/20。**
- 全期間 MARKET基準: n=2763, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=+1.58%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.58% | **+1.58%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.63% | **+1.63%** |
| MARKET | 20/20 | 100.0% | +1.58% | **+1.58%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.35% | **+1.22%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.08% | **+0.70%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +4.00% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.33% | **+0.25%** |
| LIMIT_BB3S_LONG | 4/7 | 57.1% | +0.40% | **+0.23%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.07% | **+0.06%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.03% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: GRIFFAIN/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T07:41:02.760596+00:00 / 保存件数 232/288
- BTC: STAGNANT 1h +0.04% price=76981.5
- Funnel: target 760 → liquid 205 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.1 >= 65=1, 4h RSI 88.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B/USDT:USDT | +56.04% | $1,963,190.38 |
| ZEREBRO/USDT:USDT | +50.70% | $4,150,769.95 |
| ORCA/USDT:USDT | +28.92% | $10,134,266.39 |
| BR/USDT:USDT | +21.40% | $20,030,605.97 |
| GENIUS/USDT:USDT | +18.86% | $1,580,247.41 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLAY/USDT:USDT | below_1h_threshold | +4.75% | +4.71% |
| EDU/USDT:USDT | below_1h_threshold | +3.43% | +3.39% |
| MYX/USDT:USDT | below_1h_threshold | +2.93% | +2.90% |
| DRIFT/USDT:USDT | below_1h_threshold | +1.69% | +1.66% |
| COAI/USDT:USDT | below_1h_threshold | +1.68% | +1.65% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
