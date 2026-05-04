# Decision Report

- generated_at: 2026-05-04T16:17:25.389085+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3231**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3231, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-2.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.10% | **-2.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT | 16/20 | 80.0% | +1.75% | **+1.40%** |
| LIMIT_6PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.75% | **+1.14%** |
| LIMIT_5PCT | 8/20 | 40.0% | +2.10% | **+0.84%** |
| LIMIT_7PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/4 | 50.0% | +5.07% | **+2.53%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +3.32% | **+2.16%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.92% | **+1.82%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +5.60% | **+1.40%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.77% | **+1.33%** |

## 2. $100 Live Portfolio

- 残高: **$102.36** / 初期 $100.00 (+2.36%)
- 確定トレード: 14件 (TP 5 / SL 7 / EXP 2)
- 最新: B/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.36
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T16:17:20.775928+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.37% price=79683.6
- Funnel: target 761 → liquid 199 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +13.17% | $19,405,525.12 |
| BSB/USDT:USDT | +8.11% | $33,156,568.00 |
| ASTEROID/USDT:USDT | +4.04% | $5,034,404.57 |
| SKYAI/USDT:USDT | +3.77% | $93,557,067.66 |
| UB/USDT:USDT | +3.61% | $8,638,589.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ASTEROID/USDT:USDT | below_1h_threshold | +4.33% | +4.70% |
| SKYAI/USDT:USDT | below_1h_threshold | +3.78% | +4.14% |
| UB/USDT:USDT | below_1h_threshold | +3.49% | +3.85% |
| BABY/USDT:USDT | below_1h_threshold | +2.54% | +2.90% |
| GIGGLE/USDT:USDT | below_1h_threshold | +2.43% | +2.80% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
