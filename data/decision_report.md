# Decision Report

- generated_at: 2026-05-01T00:41:02.466080+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2747**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2747, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=-0.41%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.41% | **-0.41%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_BB3S | 4/13 | 30.8% | +0.86% | **+0.27%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |
| LIMIT_5PCT | 5/20 | 25.0% | -0.04% | **-0.01%** |
| LIMIT_4PCT | 13/20 | 65.0% | -0.24% | **-0.16%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +4.21% | **+1.89%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.86% | **+1.68%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.89% | **+1.23%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.53% | **+1.07%** |
| ASK_LONG | 20/20 | 100.0% | +0.97% | **+0.97%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: GRIFFAIN/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T00:41:00.643030+00:00 / 保存件数 147/288
- BTC: STAGNANT 1h +0.17% price=76430.0
- Funnel: target 758 → liquid 216 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ORCA/USDT:USDT | +34.18% | $7,242,680.91 |
| BR/USDT:USDT | +20.67% | $15,570,652.79 |
| GENIUS/USDT:USDT | +17.97% | $1,253,192.72 |
| AIOT/USDT:USDT | +14.21% | $18,822,620.82 |
| RDDTSTOCK/USDT:USDT | +13.71% | $4,069,583.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ASTEROID/USDT:USDT | below_1h_threshold | +3.91% | +3.74% |
| UB/USDT:USDT | below_1h_threshold | +3.88% | +3.71% |
| SKYAI/USDT:USDT | below_1h_threshold | +3.06% | +2.89% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +2.99% | +2.82% |
| GENIUS/USDT:USDT | below_1h_threshold | +2.81% | +2.64% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
