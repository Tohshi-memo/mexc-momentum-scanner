# Decision Report

- generated_at: 2026-05-22T06:34:00.496856+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4672**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.01% / filled 20/20。**
- 全期間 MARKET基準: n=4672, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+1.01%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.01% | **+1.01%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.11% | **+1.11%** |
| MARKET | 20/20 | 100.0% | +1.01% | **+1.01%** |
| LIMIT_7PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.79% | **+0.71%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.47% | **+0.69%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/9 | 55.6% | +4.13% | **+2.29%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +1.05% | **+1.05%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.16% | **+0.99%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.77% | **+0.54%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |

## 2. $100 Live Portfolio

- 残高: **$95.25** / 初期 $100.00 (-4.75%)
- 確定トレード: 60件 (TP 15 / SL 42 / EXP 3)
- 最新: STXSTOCK/USDT:USDT SL_HIT PnL -1.86% 残高後 $95.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定: 548件 (Win 138 / Loss 185 / Flat 225) / skip 685件
- 成長率目線: 平均log +0.000354 / 幾何平均 +0.035% per trade / maxDD +4.21%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $121.41

## 4. Latest Market Context

- 更新: 2026-05-22T06:33:58.248264+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=77380.1
- Funnel: target 766 → liquid 142 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BUILDONBOB/USDT:USDT | +71.23% | $2,581,127.11 |
| NEAR/USDT:USDT | +21.59% | $70,584,789.66 |
| GRASS/USDT:USDT | +18.62% | $4,341,845.74 |
| PLUME/USDT:USDT | +12.24% | $1,811,254.45 |
| EDEN/USDT:USDT | +11.44% | $20,711,216.51 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GRASS/USDT:USDT | below_1h_threshold | +1.60% | +1.69% |
| FET/USDT:USDT | below_1h_threshold | +1.44% | +1.53% |
| PLUME/USDT:USDT | below_1h_threshold | +1.40% | +1.49% |
| VIRTUAL/USDT:USDT | below_1h_threshold | +0.83% | +0.92% |
| LAB/USDT:USDT | below_1h_threshold | +0.82% | +0.91% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
