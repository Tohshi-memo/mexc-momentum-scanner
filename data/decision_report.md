# Decision Report

- generated_at: 2026-05-22T06:23:52.247007+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4671**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.61% / filled 20/20。**
- 全期間 MARKET基準: n=4671, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+1.61%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.61% | **+1.61%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.61% | **+1.61%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.46% | **+1.31%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.62% | **+1.21%** |
| ASK | 20/20 | 100.0% | +1.11% | **+1.11%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.09% | **+0.71%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/8 | 50.0% | +3.16% | **+1.58%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.45% | **+0.45%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.46% | **+0.39%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.29% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$95.25** / 初期 $100.00 (-4.75%)
- 確定トレード: 60件 (TP 15 / SL 42 / EXP 3)
- 最新: STXSTOCK/USDT:USDT SL_HIT PnL -1.86% 残高後 $95.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定: 548件 (Win 138 / Loss 185 / Flat 225) / skip 684件
- 成長率目線: 平均log +0.000354 / 幾何平均 +0.035% per trade / maxDD +4.21%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $121.41

## 4. Latest Market Context

- 更新: 2026-05-22T06:23:49.501012+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=77421.3
- Funnel: target 766 → liquid 142 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BUILDONBOB/USDT:USDT | +66.30% | $2,532,345.75 |
| NEAR/USDT:USDT | +20.81% | $69,914,617.87 |
| GRASS/USDT:USDT | +19.43% | $4,260,465.30 |
| EDEN/USDT:USDT | +13.68% | $20,217,385.68 |
| PLUME/USDT:USDT | +10.46% | $1,795,761.47 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GRASS/USDT:USDT | below_1h_threshold | +2.30% | +2.33% |
| PEAQ/USDT:USDT | below_1h_threshold | +1.01% | +1.05% |
| LAB/USDT:USDT | below_1h_threshold | +0.97% | +1.01% |
| FET/USDT:USDT | below_1h_threshold | +0.96% | +1.00% |
| VIRTUAL/USDT:USDT | below_1h_threshold | +0.69% | +0.73% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
