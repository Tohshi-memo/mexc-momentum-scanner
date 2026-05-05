# Decision Report

- generated_at: 2026-05-05T03:52:17.157892+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3303**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3303, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.24% | **-0.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +1.96% | **+0.69%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +1.29% | **+0.64%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_BB3S | 5/10 | 50.0% | +0.80% | **+0.40%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.67% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.35% | **+1.28%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.20% | **+0.90%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.95% | **+0.62%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.77% | **+0.54%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +0.48% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$101.85** / 初期 $100.00 (+1.85%)
- 確定トレード: 15件 (TP 5 / SL 8 / EXP 2)
- 最新: RAVE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.85
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T03:52:14.833795+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.37% price=80811.1
- Funnel: target 765 → liquid 206 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.5 >= 65=1, 4h RSI 89.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOGS/USDT:USDT | +72.89% | $5,166,929.69 |
| NOT/USDT:USDT | +28.84% | $1,944,364.53 |
| 4/USDT:USDT | +20.95% | $1,990,432.60 |
| TONCOIN/USDT:USDT | +20.67% | $62,269,464.36 |
| FHE/USDT:USDT | +19.05% | $3,407,452.10 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ONDO/USDT:USDT | below_1h_threshold | +2.33% | +1.96% |
| ZRO/USDT:USDT | below_1h_threshold | +1.79% | +1.42% |
| MONAD/USDT:USDT | below_1h_threshold | +1.74% | +1.37% |
| ALGO/USDT:USDT | below_1h_threshold | +1.48% | +1.11% |
| FHE/USDT:USDT | below_1h_threshold | +1.46% | +1.10% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
