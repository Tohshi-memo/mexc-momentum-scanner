# Decision Report

- generated_at: 2026-05-03T21:37:02.695535+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3108**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3108, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-2.53%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.53% | **-2.53%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +3.15% | **+0.79%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.48% | **+0.59%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_4PCT | 17/20 | 85.0% | +0.07% | **+0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +3.70% | **+3.33%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +4.91% | **+3.19%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.59% | **+2.46%** |
| LIMIT_5PCT_LONG | 6/20 | 30.0% | +6.00% | **+1.80%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +3.95% | **+1.78%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T21:37:00.677782+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=78859.3
- Funnel: target 755 → liquid 159 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +59.96% | $287,900,031.52 |
| SKYAI/USDT:USDT | +21.69% | $26,967,877.73 |
| BSB/USDT:USDT | +17.50% | $15,406,149.88 |
| TAG/USDT:USDT | +12.46% | $4,082,296.91 |
| TRADOOR/USDT:USDT | +9.30% | $3,221,783.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TRADOOR/USDT:USDT | below_1h_threshold | +2.91% | +2.95% |
| PARTI/USDT:USDT | below_1h_threshold | +1.31% | +1.35% |
| EDU/USDT:USDT | below_1h_threshold | +1.10% | +1.14% |
| RENDER/USDT:USDT | below_1h_threshold | +1.09% | +1.13% |
| BR/USDT:USDT | below_1h_threshold | +1.03% | +1.06% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
