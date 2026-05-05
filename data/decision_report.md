# Decision Report

- generated_at: 2026-05-05T16:16:24.942741+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3365**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.07% / filled 20/20。**
- 全期間 MARKET基準: n=3365, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+2.07%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.07% | **+2.07%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.09% | **+2.09%** |
| MARKET | 20/20 | 100.0% | +2.07% | **+2.07%** |
| LIMIT_2PCT | 16/20 | 80.0% | +2.36% | **+1.89%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.92% | **+1.83%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.77% | **+1.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +2.59% | **+0.39%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -2.30% | **-0.35%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | -0.89% | **-0.40%** |
| MARKET_LONG | 20/20 | 100.0% | -0.49% | **-0.49%** |

## 2. $100 Live Portfolio

- 残高: **$100.84** / 初期 $100.00 (+0.84%)
- 確定トレード: 17件 (TP 5 / SL 10 / EXP 2)
- 最新: M/USDT:USDT SL_HIT PnL -3.86% 残高後 $100.84
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T16:16:18.636307+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=81393.9
- Funnel: target 765 → liquid 188 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SWARMS/USDT:USDT | +11.08% | $1,332,322.55 |
| BSB/USDT:USDT | +5.71% | $38,887,663.83 |
| MERL/USDT:USDT | +5.33% | $3,666,007.86 |
| MYX/USDT:USDT | +2.57% | $3,312,661.51 |
| FHE/USDT:USDT | +2.56% | $7,189,981.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| M/USDT:USDT | below_1h_threshold | +2.82% | +2.94% |
| FHE/USDT:USDT | below_1h_threshold | +2.34% | +2.46% |
| MYX/USDT:USDT | below_1h_threshold | +2.29% | +2.41% |
| VIRTUAL/USDT:USDT | below_1h_threshold | +2.16% | +2.27% |
| 4/USDT:USDT | below_1h_threshold | +2.01% | +2.13% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
