# Decision Report

- generated_at: 2026-05-05T10:52:31.578899+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3346**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3346, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.43%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.43% | **-0.43%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.46% | **+0.23%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.02% | **+0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.62% | **+1.62%** |
| ASK_LONG | 20/20 | 100.0% | +1.14% | **+1.14%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.24% | **+0.93%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.40% | **+0.84%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$100.84** / 初期 $100.00 (+0.84%)
- 確定トレード: 17件 (TP 5 / SL 10 / EXP 2)
- 最新: M/USDT:USDT SL_HIT PnL -3.86% 残高後 $100.84
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T10:52:26.899751+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.24% price=80746.9
- Funnel: target 765 → liquid 200 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOGS/USDT:USDT | +100.11% | $18,588,197.09 |
| HIVE/USDT:USDT | +43.83% | $5,884,102.77 |
| FHE/USDT:USDT | +35.50% | $4,820,951.00 |
| LAB/USDT:USDT | +30.00% | $98,979,355.26 |
| TONCOIN/USDT:USDT | +27.75% | $92,977,579.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NOT/USDT:USDT | below_1h_threshold | +2.34% | +2.09% |
| BLEND/USDT:USDT | below_1h_threshold | +2.34% | +2.09% |
| M/USDT:USDT | below_1h_threshold | +2.10% | +1.86% |
| DOGS/USDT:USDT | below_1h_threshold | +1.56% | +1.32% |
| ICP/USDT:USDT | below_1h_threshold | +1.52% | +1.28% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
