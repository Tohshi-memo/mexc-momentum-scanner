# Decision Report

- generated_at: 2026-05-13T20:20:12.856877+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4251**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.36% / filled 20/20。**
- 全期間 MARKET基準: n=4251, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+1.36%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.36% | **+1.36%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.36% | **+1.36%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.46% | **+1.32%** |
| ASK | 20/20 | 100.0% | +0.74% | **+0.74%** |
| LIMIT_BB3S | 3/15 | 20.0% | +1.42% | **+0.28%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.67% | **+0.73%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.62% | **+0.73%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.00% | **+0.40%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.17% | **+0.15%** |

## 2. $100 Live Portfolio

- 残高: **$98.19** / 初期 $100.00 (-1.81%)
- 確定トレード: 39件 (TP 10 / SL 26 / EXP 3)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.19
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.18** / 初期 $100.00 (+19.18%)
- 確定: 342件 (Win 94 / Loss 125 / Flat 123) / skip 470件
- 成長率目線: 平均log +0.000513 / 幾何平均 +0.051% per trade / maxDD +4.21%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: COS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $119.18

## 4. Latest Market Context

- 更新: 2026-05-13T20:20:09.355131+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=79679.4
- Funnel: target 760 → liquid 171 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TROLLSOL/USDT:USDT | +22.00% | $1,457,679.54 |
| CSCOSTOCK/USDT:USDT | +13.90% | $2,356,116.55 |
| AIN/USDT:USDT | +13.56% | $1,743,386.66 |
| GUA/USDT:USDT | +13.43% | $3,701,132.71 |
| BB/USDT:USDT | +12.61% | $1,704,786.45 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| USELESS/USDT:USDT | below_1h_threshold | +2.23% | +2.14% |
| CFX/USDT:USDT | below_1h_threshold | +1.82% | +1.72% |
| JCT/USDT:USDT | below_1h_threshold | +1.63% | +1.53% |
| SAGA/USDT:USDT | below_1h_threshold | +1.61% | +1.52% |
| AKT/USDT:USDT | below_1h_threshold | +1.47% | +1.38% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
