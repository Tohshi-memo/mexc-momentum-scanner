# Decision Report

- generated_at: 2026-05-05T16:13:05.822327+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3364**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.47% / filled 20/20。**
- 全期間 MARKET基準: n=3364, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+1.47%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.47% | **+1.47%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.49% | **+1.49%** |
| MARKET | 20/20 | 100.0% | +1.47% | **+1.47%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.61% | **+1.29%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.29% | **+1.23%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.33% | **+0.86%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.89% | **+0.39%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |
| MARKET_LONG | 20/20 | 100.0% | -0.09% | **-0.09%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -2.30% | **-0.35%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | -0.48% | **-0.38%** |

## 2. $100 Live Portfolio

- 残高: **$100.84** / 初期 $100.00 (+0.84%)
- 確定トレード: 17件 (TP 5 / SL 10 / EXP 2)
- 最新: M/USDT:USDT SL_HIT PnL -3.86% 残高後 $100.84
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T16:13:01.033419+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=81479.6
- Funnel: target 765 → liquid 188 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SWARMS/USDT:USDT | +9.83% | $1,283,638.80 |
| BSB/USDT:USDT | +4.34% | $38,816,010.80 |
| MYX/USDT:USDT | +2.77% | $3,290,970.06 |
| MERL/USDT:USDT | +2.56% | $3,647,876.83 |
| VIRTUAL/USDT:USDT | +2.39% | $4,596,587.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +4.41% | +4.42% |
| MYX/USDT:USDT | below_1h_threshold | +2.82% | +2.83% |
| MERL/USDT:USDT | below_1h_threshold | +2.56% | +2.57% |
| 4/USDT:USDT | below_1h_threshold | +2.43% | +2.44% |
| VIRTUAL/USDT:USDT | below_1h_threshold | +2.36% | +2.37% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
