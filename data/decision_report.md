# Decision Report

- generated_at: 2026-05-04T09:42:19.631838+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3178**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3178, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-0.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.32% | **-0.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 14/20 | 70.0% | +0.95% | **+0.67%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.61% | **+0.43%** |
| LIMIT_BB3S | 4/18 | 22.2% | +1.93% | **+0.43%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.36% | **+0.54%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.80% | **+0.40%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +0.64% | **+0.32%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.37% | **+0.17%** |

## 2. $100 Live Portfolio

- 残高: **$103.40** / 初期 $100.00 (+3.40%)
- 確定トレード: 12件 (TP 5 / SL 5 / EXP 2)
- 最新: B2/USDT:USDT EXPIRED PnL +1.44% 残高後 $103.40
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T09:42:17.233833+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=79777.7
- Funnel: target 761 → liquid 181 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.8 >= 65=1, 4h RSI 71.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +70.95% | $8,182,489.12 |
| SKYAI/USDT:USDT | +63.22% | $50,868,845.29 |
| TAG/USDT:USDT | +48.80% | $13,729,440.25 |
| GIGA/USDT:USDT | +38.00% | $1,332,438.70 |
| 4/USDT:USDT | +36.88% | $1,259,188.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GIGGLE/USDT:USDT | below_relative_strength | +5.02% | +4.88% |
| ZBT/USDT:USDT | below_1h_threshold | +4.21% | +4.07% |
| DASH/USDT:USDT | below_1h_threshold | +4.10% | +3.96% |
| MERL/USDT:USDT | below_1h_threshold | +3.59% | +3.45% |
| GIGA/USDT:USDT | below_1h_threshold | +3.38% | +3.24% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
