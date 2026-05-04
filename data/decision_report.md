# Decision Report

- generated_at: 2026-05-04T10:52:09.522863+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3193**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3193, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.02%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.02% | **+0.02%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 15/20 | 75.0% | +0.76% | **+0.57%** |
| LIMIT_BB3S | 4/19 | 21.1% | +2.14% | **+0.45%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.62% | **+0.40%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.20% | **+1.02%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.87% | **+0.65%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.09% | **+0.60%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.84% | **+0.55%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.74% | **+0.52%** |

## 2. $100 Live Portfolio

- 残高: **$103.40** / 初期 $100.00 (+3.40%)
- 確定トレード: 12件 (TP 5 / SL 5 / EXP 2)
- 最新: B2/USDT:USDT EXPIRED PnL +1.44% 残高後 $103.40
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T10:52:07.441420+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.96% price=79031.0
- Funnel: target 761 → liquid 188 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +81.03% | $9,088,574.32 |
| SKYAI/USDT:USDT | +68.82% | $56,873,669.17 |
| TAG/USDT:USDT | +51.45% | $14,844,307.45 |
| GIGA/USDT:USDT | +48.63% | $1,658,919.97 |
| 4/USDT:USDT | +37.68% | $1,435,089.76 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +3.78% | +4.74% |
| LUNC/USDT:USDT | below_1h_threshold | +3.59% | +4.56% |
| GIGA/USDT:USDT | below_1h_threshold | +2.29% | +3.25% |
| UKOIL/USDT:USDT | below_1h_threshold | +2.03% | +2.99% |
| USOIL/USDT:USDT | below_1h_threshold | +1.92% | +2.88% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
