# Decision Report

- generated_at: 2026-05-13T17:39:33.068051+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4239**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.55% / filled 20/20。**
- 全期間 MARKET基準: n=4239, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=+1.55%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.55% | **+1.55%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.55% | **+1.55%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.26% | **+1.13%** |
| ASK | 20/20 | 100.0% | +0.93% | **+0.93%** |
| LIMIT_2PCT | 13/20 | 65.0% | +1.24% | **+0.81%** |
| LIMIT_BB3S | 6/17 | 35.3% | +1.22% | **+0.43%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.57% | **+0.20%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.15% | **+0.11%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | -0.24% | **-0.06%** |

## 2. $100 Live Portfolio

- 残高: **$98.69** / 初期 $100.00 (-1.31%)
- 確定トレード: 38件 (TP 10 / SL 25 / EXP 3)
- 最新: BILL/USDT:USDT TP_HIT PnL +8.00% 残高後 $98.69
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.18** / 初期 $100.00 (+19.18%)
- 確定: 342件 (Win 94 / Loss 125 / Flat 123) / skip 458件
- 成長率目線: 平均log +0.000513 / 幾何平均 +0.051% per trade / maxDD +4.21%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: COS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $119.18

## 4. Latest Market Context

- 更新: 2026-05-13T17:39:27.133615+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.29% price=79299.9
- Funnel: target 761 → liquid 179 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TROLLSOL/USDT:USDT | +23.21% | $1,018,936.43 |
| GUA/USDT:USDT | +8.25% | $3,812,877.53 |
| UP/USDT:USDT | +8.09% | $5,205,677.46 |
| SAGA/USDT:USDT | +7.47% | $45,152,802.35 |
| BEAT/USDT:USDT | +7.02% | $1,348,798.19 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +4.81% | +4.52% |
| GIGA/USDT:USDT | below_1h_threshold | +3.62% | +3.33% |
| GUA/USDT:USDT | below_1h_threshold | +3.53% | +3.24% |
| VELO/USDT:USDT | below_1h_threshold | +3.15% | +2.86% |
| TRIA/USDT:USDT | below_1h_threshold | +2.56% | +2.26% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
