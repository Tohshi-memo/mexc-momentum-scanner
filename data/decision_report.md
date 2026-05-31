# Decision Report

- generated_at: 2026-05-31T13:40:01.762042+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5193**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.71% / filled 20/20。**
- 全期間 MARKET基準: n=5193, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.71%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.71% | **+0.71%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| MARKET | 20/20 | 100.0% | +0.71% | **+0.71%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.79% | **+0.71%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.68% | **+0.65%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.90% | **+0.72%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.60% | **+0.45%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.45% | **+0.42%** |

## 2. $100 Live Portfolio

- 残高: **$97.61** / 初期 $100.00 (-2.39%)
- 確定トレード: 79件 (TP 23 / SL 53 / EXP 3)
- 最新: ID/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.07** / 初期 $100.00 (+25.07%)
- 確定: 828件 (Win 189 / Loss 247 / Flat 392) / skip 926件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BILL/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $125.07

## 4. Latest Market Context

- 更新: 2026-05-31T13:39:56.308687+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=73871.0
- Funnel: target 773 → liquid 123 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIA/USDT:USDT | +46.21% | $3,608,778.83 |
| PLAY/USDT:USDT | +44.48% | $8,309,477.89 |
| GUN/USDT:USDT | +29.91% | $1,081,919.50 |
| PORTAL/USDT:USDT | +22.27% | $10,989,029.34 |
| TA/USDT:USDT | +21.77% | $2,480,361.03 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PORTAL/USDT:USDT | below_1h_threshold | +2.98% | +3.01% |
| AIA/USDT:USDT | below_1h_threshold | +2.25% | +2.27% |
| MYX/USDT:USDT | below_1h_threshold | +2.09% | +2.12% |
| HOME/USDT:USDT | below_1h_threshold | +1.90% | +1.93% |
| GUA/USDT:USDT | below_1h_threshold | +1.59% | +1.62% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
