# Decision Report

- generated_at: 2026-05-05T10:37:12.966608+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3345**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3345, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.46% | **+0.23%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |
| LIMIT_ATR | 13/20 | 65.0% | -0.55% | **-0.35%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.00% | **+2.00%** |
| ASK_LONG | 20/20 | 100.0% | +1.53% | **+1.53%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.82% | **+1.37%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +1.86% | **+1.02%** |
| LIMIT_BB3S_LONG | 5/10 | 50.0% | +1.88% | **+0.94%** |

## 2. $100 Live Portfolio

- 残高: **$100.84** / 初期 $100.00 (+0.84%)
- 確定トレード: 17件 (TP 5 / SL 10 / EXP 2)
- 最新: M/USDT:USDT SL_HIT PnL -3.86% 残高後 $100.84
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T10:37:10.790751+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.27% price=80770.0
- Funnel: target 765 → liquid 199 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOGS/USDT:USDT | +105.74% | $18,200,343.32 |
| HIVE/USDT:USDT | +42.04% | $5,689,853.13 |
| LAB/USDT:USDT | +38.12% | $96,167,101.94 |
| FHE/USDT:USDT | +35.45% | $4,732,328.40 |
| TONCOIN/USDT:USDT | +29.56% | $91,317,993.70 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DOGS/USDT:USDT | below_1h_threshold | +4.42% | +4.15% |
| BLEND/USDT:USDT | below_1h_threshold | +3.14% | +2.87% |
| TONCOIN/USDT:USDT | below_1h_threshold | +2.81% | +2.54% |
| NOT/USDT:USDT | below_1h_threshold | +1.98% | +1.71% |
| MERL/USDT:USDT | below_1h_threshold | +1.69% | +1.42% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
