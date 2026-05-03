# Decision Report

- generated_at: 2026-05-03T10:47:14.214602+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3062**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3062, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-1.83%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.83% | **-1.83%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +1.83% | **+0.73%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_4PCT | 16/20 | 80.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272 | 2/20 | 10.0% | -0.13% | **-0.01%** |
| LIMIT_ATR | 16/20 | 80.0% | -0.38% | **-0.31%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +4.39% | **+2.63%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +4.48% | **+2.24%** |
| LIMIT_BB3S_LONG | 5/6 | 83.3% | +2.21% | **+1.84%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +3.04% | **+1.82%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +3.39% | **+1.19%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T10:47:11.730020+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.16% price=78369.4
- Funnel: target 755 → liquid 166 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.8 >= 65=1, 4h RSI 86.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +51.74% | $1,811,329.02 |
| BABY/USDT:USDT | +36.32% | $17,458,000.92 |
| AIGENSYN/USDT:USDT | +30.22% | $3,956,785.01 |
| TAC/USDT:USDT | +20.25% | $2,643,605.42 |
| AKT/USDT:USDT | +19.03% | $1,756,028.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LYN/USDT:USDT | below_1h_threshold | +3.39% | +3.55% |
| TAC/USDT:USDT | below_1h_threshold | +3.38% | +3.54% |
| BIANRENSHENG/USDT:USDT | below_1h_threshold | +3.14% | +3.31% |
| GENIUS/USDT:USDT | below_1h_threshold | +2.75% | +2.91% |
| XNY/USDT:USDT | below_1h_threshold | +1.59% | +1.75% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
