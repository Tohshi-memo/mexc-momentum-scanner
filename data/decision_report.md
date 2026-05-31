# Decision Report

- generated_at: 2026-05-31T10:15:07.148546+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5185**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.12% / filled 20/20。**
- 全期間 MARKET基準: n=5185, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.12% | **+1.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.12% | **+1.12%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.66% | **+0.52%** |
| ASK | 20/20 | 100.0% | +0.50% | **+0.50%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +0.92% | **+0.83%** |
| LIMIT_ATR_LONG | 17/20 | 85.0% | +0.86% | **+0.73%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.35% | **+0.35%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$97.61** / 初期 $100.00 (-2.39%)
- 確定トレード: 79件 (TP 23 / SL 53 / EXP 3)
- 最新: ID/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$123.84** / 初期 $100.00 (+23.84%)
- 確定: 820件 (Win 187 / Loss 245 / Flat 388) / skip 926件
- 成長率目線: 平均log +0.000261 / 幾何平均 +0.026% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $123.84

## 4. Latest Market Context

- 更新: 2026-05-31T10:15:04.709699+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=73829.9
- Funnel: target 773 → liquid 126 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIA/USDT:USDT | +51.59% | $2,096,636.67 |
| PLAY/USDT:USDT | +40.00% | $4,815,346.01 |
| PORTAL/USDT:USDT | +26.94% | $12,272,092.00 |
| TA/USDT:USDT | +23.28% | $2,482,987.34 |
| MYX/USDT:USDT | +16.35% | $3,539,017.56 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +2.34% | +2.32% |
| PORTAL/USDT:USDT | below_1h_threshold | +1.94% | +1.92% |
| BILL/USDT:USDT | below_1h_threshold | +1.81% | +1.79% |
| TA/USDT:USDT | below_1h_threshold | +1.50% | +1.48% |
| MYX/USDT:USDT | below_1h_threshold | +1.15% | +1.13% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
