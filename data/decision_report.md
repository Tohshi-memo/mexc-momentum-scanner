# Decision Report

- generated_at: 2026-05-17T04:18:23.001906+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4381**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.20% / filled 20/20。**
- 全期間 MARKET基準: n=4381, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 15/20 | 75.0% | +0.59% | **+0.44%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.50% | **+0.32%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.57% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.73% | **+0.47%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +2.27% | **+0.45%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.66% | **+0.30%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.22% | **+0.13%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.24% | **+0.12%** |

## 2. $100 Live Portfolio

- 残高: **$97.19** / 初期 $100.00 (-2.81%)
- 確定トレード: 50件 (TP 13 / SL 34 / EXP 3)
- 最新: VVV/USDT:USDT SL_HIT PnL -3.29% 残高後 $97.19
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$117.68** / 初期 $100.00 (+17.68%)
- 確定: 393件 (Win 97 / Loss 137 / Flat 159) / skip 549件
- 成長率目線: 平均log +0.000414 / 幾何平均 +0.041% per trade / maxDD +4.21%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CGPT/USDT:USDT `LIMIT_6PCT_LONG` EXPIRED account -0.27% 残高後 $117.68

## 4. Latest Market Context

- 更新: 2026-05-17T04:18:19.434634+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=78039.9
- Funnel: target 760 → liquid 125 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIA/USDT:USDT | +48.82% | $4,072,988.39 |
| CGPT/USDT:USDT | +22.09% | $1,467,223.59 |
| BSB/USDT:USDT | +17.70% | $4,261,912.27 |
| LYN/USDT:USDT | +8.37% | $4,449,388.52 |
| ASTEROID/USDT:USDT | +8.03% | $4,080,719.70 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIA/USDT:USDT | below_1h_threshold | +4.94% | +4.87% |
| RUNE/USDT:USDT | below_1h_threshold | +3.07% | +3.01% |
| ZEC/USDT:USDT | below_1h_threshold | +1.83% | +1.76% |
| MYX/USDT:USDT | below_1h_threshold | +1.82% | +1.76% |
| BSB/USDT:USDT | below_1h_threshold | +1.60% | +1.53% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
