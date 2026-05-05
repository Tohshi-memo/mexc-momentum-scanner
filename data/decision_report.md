# Decision Report

- generated_at: 2026-05-05T10:27:29.109157+00:00
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

- 更新: 2026-05-05T10:27:27.007563+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.20% price=80710.1
- Funnel: target 765 → liquid 198 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOGS/USDT:USDT | +98.71% | $17,735,005.27 |
| LAB/USDT:USDT | +48.96% | $94,451,811.89 |
| HIVE/USDT:USDT | +43.49% | $5,508,277.68 |
| FHE/USDT:USDT | +37.22% | $4,699,878.47 |
| TONCOIN/USDT:USDT | +27.69% | $90,300,098.90 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MERL/USDT:USDT | below_1h_threshold | +2.78% | +2.58% |
| M/USDT:USDT | below_1h_threshold | +2.70% | +2.50% |
| TONCOIN/USDT:USDT | below_1h_threshold | +1.47% | +1.27% |
| INJ/USDT:USDT | below_1h_threshold | +1.23% | +1.03% |
| NAORIS/USDT:USDT | below_1h_threshold | +1.17% | +0.97% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
