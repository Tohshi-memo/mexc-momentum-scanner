# Decision Report

- generated_at: 2026-05-01T09:36:56.698681+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2781**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2781, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=-1.52%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.52% | **-1.52%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +2.94% | **+0.88%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.80% | **+0.60%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.25% | **+0.44%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +4.28% | **+0.43%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.87% | **+1.87%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +1.80% | **+1.80%** |
| LIMIT_BB3S_LONG | 2/4 | 50.0% | +3.39% | **+1.70%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +3.37% | **+1.69%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.37% | **+1.54%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: GRIFFAIN/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T09:36:54.262445+00:00 / 保存件数 256/288
- BTC: STAGNANT 1h -0.09% price=77267.6
- Funnel: target 760 → liquid 199 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.8 >= 65=1, 4h RSI 66.2 >= 65=1, 4h RSI 76.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B/USDT:USDT | +61.48% | $7,660,402.42 |
| BR/USDT:USDT | +40.73% | $22,862,889.73 |
| ZEREBRO/USDT:USDT | +34.49% | $6,771,149.07 |
| UB/USDT:USDT | +33.04% | $11,445,765.49 |
| ORCA/USDT:USDT | +28.18% | $10,346,846.30 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLAY/USDT:USDT | below_1h_threshold | +3.61% | +3.71% |
| TAC/USDT:USDT | below_1h_threshold | +1.60% | +1.69% |
| ZBT/USDT:USDT | below_1h_threshold | +1.23% | +1.33% |
| AIOT/USDT:USDT | below_1h_threshold | +0.92% | +1.02% |
| MYX/USDT:USDT | below_1h_threshold | +0.88% | +0.97% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
