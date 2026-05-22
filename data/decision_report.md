# Decision Report

- generated_at: 2026-05-22T06:09:18.508822+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4668**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.29% / filled 20/20。**
- 全期間 MARKET基準: n=4668, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+2.29%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.29% | **+2.29%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.29% | **+2.29%** |
| LIMIT_1PCT | 18/20 | 90.0% | +2.28% | **+2.05%** |
| LIMIT_2PCT | 15/20 | 75.0% | +2.66% | **+2.00%** |
| ASK | 20/20 | 100.0% | +1.81% | **+1.81%** |
| LIMIT_3PCT | 12/20 | 60.0% | +2.51% | **+1.51%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/6 | 50.0% | +3.75% | **+1.88%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +0.01% | **+0.01%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | -0.26% | **-0.14%** |

## 2. $100 Live Portfolio

- 残高: **$95.25** / 初期 $100.00 (-4.75%)
- 確定トレード: 60件 (TP 15 / SL 42 / EXP 3)
- 最新: STXSTOCK/USDT:USDT SL_HIT PnL -1.86% 残高後 $95.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定: 548件 (Win 138 / Loss 185 / Flat 225) / skip 681件
- 成長率目線: 平均log +0.000354 / 幾何平均 +0.035% per trade / maxDD +4.21%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $121.41

## 4. Latest Market Context

- 更新: 2026-05-22T06:09:16.347665+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=77410.1
- Funnel: target 766 → liquid 141 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BUILDONBOB/USDT:USDT | +66.84% | $2,459,549.17 |
| NEAR/USDT:USDT | +21.48% | $68,777,174.10 |
| GRASS/USDT:USDT | +16.64% | $4,163,630.86 |
| EDEN/USDT:USDT | +11.69% | $18,862,554.85 |
| PLUME/USDT:USDT | +10.69% | $1,785,536.45 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PEAQ/USDT:USDT | below_1h_threshold | +0.80% | +0.85% |
| FET/USDT:USDT | below_1h_threshold | +0.48% | +0.53% |
| JUP/USDT:USDT | below_1h_threshold | +0.37% | +0.42% |
| LAB/USDT:USDT | below_1h_threshold | +0.34% | +0.39% |
| JTO/USDT:USDT | below_1h_threshold | +0.19% | +0.24% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
