# Decision Report

- generated_at: 2026-05-05T20:37:28.553467+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3382**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3382, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-0.22%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.22% | **-0.22%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +2.98% | **+1.04%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.59% | **+0.72%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.97% | **+0.63%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | -0.11% | **-0.05%** |
| MARKET | 20/20 | 100.0% | -0.22% | **-0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/7 | 71.4% | +1.96% | **+1.40%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.30% | **+1.17%** |
| ASK_LONG | 20/20 | 100.0% | +1.09% | **+1.09%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.14% | **+0.74%** |
| MARKET_LONG | 20/20 | 100.0% | +0.59% | **+0.59%** |

## 2. $100 Live Portfolio

- 残高: **$100.33** / 初期 $100.00 (+0.33%)
- 確定トレード: 18件 (TP 5 / SL 11 / EXP 2)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.33
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T20:37:25.499888+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=81628.2
- Funnel: target 760 → liquid 187 → pre 50 → checked 50 → surge 4 → strict 0
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.7 >= 65=1, 4h RSI 83.9 >= 65=1, 4h RSI 84.5 >= 65=1, 4h RSI 69.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FHE/USDT:USDT | +40.27% | $15,933,186.01 |
| SWARMS/USDT:USDT | +18.33% | $2,208,668.36 |
| SMCISTOCK/USDT:USDT | +18.07% | $3,436,436.47 |
| ZEC/USDT:USDT | +12.27% | $469,617,687.51 |
| STX/USDT:USDT | +9.80% | $15,289,373.34 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +4.75% | +4.66% |
| ICP/USDT:USDT | below_1h_threshold | +4.74% | +4.65% |
| SWARMS/USDT:USDT | below_1h_threshold | +3.36% | +3.27% |
| 4/USDT:USDT | below_1h_threshold | +3.22% | +3.13% |
| GALA/USDT:USDT | below_1h_threshold | +3.16% | +3.07% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
