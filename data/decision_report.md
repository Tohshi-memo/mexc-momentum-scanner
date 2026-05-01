# Decision Report

- generated_at: 2026-05-01T09:14:15.004104+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2779**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2779, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-2.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.12% | **-2.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +3.15% | **+0.79%** |
| LIMIT_4PCT | 16/20 | 80.0% | +0.75% | **+0.60%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.25% | **+0.44%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +4.28% | **+0.43%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +3.80% | **+2.47%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +2.10% | **+2.10%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +3.20% | **+2.08%** |
| LIMIT_BB3S_LONG | 3/6 | 50.0% | +3.77% | **+1.89%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +4.19% | **+1.89%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: GRIFFAIN/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T09:14:12.792097+00:00 / 保存件数 251/288
- BTC: STAGNANT 1h -0.05% price=77299.3
- Funnel: target 760 → liquid 198 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.7 >= 65=1, 4h RSI 75.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B/USDT:USDT | +65.93% | $6,773,128.63 |
| ZEREBRO/USDT:USDT | +40.42% | $6,372,431.76 |
| BR/USDT:USDT | +38.16% | $22,397,852.58 |
| UB/USDT:USDT | +29.03% | $10,709,179.83 |
| ORCA/USDT:USDT | +28.59% | $10,275,515.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DRIFT/USDT:USDT | below_1h_threshold | +4.42% | +4.47% |
| TAC/USDT:USDT | below_1h_threshold | +2.96% | +3.01% |
| AIOT/USDT:USDT | below_1h_threshold | +2.52% | +2.57% |
| PLAY/USDT:USDT | below_1h_threshold | +1.75% | +1.80% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.34% | +1.39% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
