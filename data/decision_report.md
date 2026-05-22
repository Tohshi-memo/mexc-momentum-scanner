# Decision Report

- generated_at: 2026-05-22T06:13:54.483292+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4669**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.69% / filled 20/20。**
- 全期間 MARKET基準: n=4669, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+1.69%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.69% | **+1.69%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.69% | **+1.69%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.61% | **+1.45%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.86% | **+1.40%** |
| ASK | 20/20 | 100.0% | +1.21% | **+1.21%** |
| LIMIT_3PCT | 12/20 | 60.0% | +1.51% | **+0.91%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/7 | 57.1% | +4.81% | **+2.75%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +0.67% | **+0.61%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +0.47% | **+0.37%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.22% | **+0.22%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$95.25** / 初期 $100.00 (-4.75%)
- 確定トレード: 60件 (TP 15 / SL 42 / EXP 3)
- 最新: STXSTOCK/USDT:USDT SL_HIT PnL -1.86% 残高後 $95.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定: 548件 (Win 138 / Loss 185 / Flat 225) / skip 682件
- 成長率目線: 平均log +0.000354 / 幾何平均 +0.035% per trade / maxDD +4.21%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $121.41

## 4. Latest Market Context

- 更新: 2026-05-22T06:13:51.913251+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=77459.0
- Funnel: target 766 → liquid 141 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BUILDONBOB/USDT:USDT | +71.38% | $2,481,862.31 |
| NEAR/USDT:USDT | +21.09% | $69,152,215.89 |
| EDEN/USDT:USDT | +16.92% | $19,272,444.29 |
| GRASS/USDT:USDT | +16.21% | $4,178,149.12 |
| PLUME/USDT:USDT | +9.84% | $1,791,502.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JUP/USDT:USDT | below_1h_threshold | +0.83% | +0.82% |
| FET/USDT:USDT | below_1h_threshold | +0.58% | +0.57% |
| LAB/USDT:USDT | below_1h_threshold | +0.50% | +0.49% |
| ATOM/USDT:USDT | below_1h_threshold | +0.47% | +0.45% |
| VIRTUAL/USDT:USDT | below_1h_threshold | +0.43% | +0.42% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
