# Decision Report

- generated_at: 2026-04-30T17:55:54.123469+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2725**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2725, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=-2.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.80% | **-2.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 10/20 | 50.0% | +1.93% | **+0.97%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 4/20 | 20.0% | +3.29% | **+0.66%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.38% | **+0.19%** |
| LIMIT_7PCT | 6/20 | 30.0% | +0.54% | **+0.16%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +2.33% | **+2.33%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +6.55% | **+2.29%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +6.49% | **+1.95%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.16% | **+1.73%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +5.68% | **+1.71%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: GRIFFAIN/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-04-30T17:55:52.189269+00:00 / 保存件数 62/288
- BTC: STAGNANT 1h +0.02% price=76237.3
- Funnel: target 757 → liquid 232 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.7 >= 65=1, 4h RSI 81.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BR/USDT:USDT | +19.88% | $5,497,353.03 |
| AIOT/USDT:USDT | +19.09% | $13,003,018.86 |
| ASTEROID/USDT:USDT | +7.17% | $3,855,960.84 |
| BIO/USDT:USDT | +6.85% | $3,735,972.72 |
| ZEREBRO/USDT:USDT | +4.36% | $3,478,807.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLUAI/USDT:USDT | below_1h_threshold | +2.47% | +2.45% |
| APE/USDT:USDT | below_1h_threshold | +2.43% | +2.41% |
| BIO/USDT:USDT | below_1h_threshold | +2.18% | +2.16% |
| CHIP/USDT:USDT | below_1h_threshold | +2.02% | +2.00% |
| KLACSTOCK/USDT:USDT | below_1h_threshold | +1.91% | +1.88% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
