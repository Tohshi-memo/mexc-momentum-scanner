# Decision Report

- generated_at: 2026-05-17T05:13:25.463554+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4384**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.29% / filled 20/20。**
- 全期間 MARKET基準: n=4384, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.29%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.29% | **+0.29%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| MARKET | 20/20 | 100.0% | +0.29% | **+0.29%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +0.77% | **+0.12%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.01% | **+0.01%** |
| LIMIT_4PCT | 10/20 | 50.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.98% | **+0.98%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.13% | **+0.79%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +3.13% | **+0.47%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.42% | **+0.29%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.31% | **+0.14%** |

## 2. $100 Live Portfolio

- 残高: **$97.19** / 初期 $100.00 (-2.81%)
- 確定トレード: 50件 (TP 13 / SL 34 / EXP 3)
- 最新: VVV/USDT:USDT SL_HIT PnL -3.29% 残高後 $97.19
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$117.68** / 初期 $100.00 (+17.68%)
- 確定: 393件 (Win 97 / Loss 137 / Flat 159) / skip 552件
- 成長率目線: 平均log +0.000414 / 幾何平均 +0.041% per trade / maxDD +4.21%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CGPT/USDT:USDT `LIMIT_6PCT_LONG` EXPIRED account -0.27% 残高後 $117.68

## 4. Latest Market Context

- 更新: 2026-05-17T05:13:21.961365+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=78235.2
- Funnel: target 760 → liquid 126 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIA/USDT:USDT | +35.53% | $5,933,251.29 |
| CGPT/USDT:USDT | +32.20% | $1,634,945.50 |
| BSB/USDT:USDT | +15.24% | $4,363,750.89 |
| ASTEROID/USDT:USDT | +12.45% | $3,986,366.56 |
| AIGENSYN/USDT:USDT | +7.48% | $2,734,278.99 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CGPT/USDT:USDT | below_1h_threshold | +3.25% | +3.10% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +2.46% | +2.31% |
| INJ/USDT:USDT | below_1h_threshold | +1.55% | +1.39% |
| ONDO/USDT:USDT | below_1h_threshold | +1.50% | +1.34% |
| ASTEROID/USDT:USDT | below_1h_threshold | +1.44% | +1.29% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
