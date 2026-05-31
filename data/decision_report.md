# Decision Report

- generated_at: 2026-05-31T09:34:56.116543+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5183**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.56% / filled 20/20。**
- 全期間 MARKET基準: n=5183, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.56%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.56% | **+1.56%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.56% | **+1.56%** |
| ASK | 20/20 | 100.0% | +0.87% | **+0.87%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.83% | **+0.62%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 19/20 | 95.0% | +0.75% | **+0.71%** |
| LIMIT_ATR_LONG | 18/20 | 90.0% | +0.67% | **+0.60%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$97.61** / 初期 $100.00 (-2.39%)
- 確定トレード: 79件 (TP 23 / SL 53 / EXP 3)
- 最新: ID/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$122.83** / 初期 $100.00 (+22.83%)
- 確定: 818件 (Win 186 / Loss 245 / Flat 387) / skip 926件
- 成長率目線: 平均log +0.000251 / 幾何平均 +0.025% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.81% 残高後 $122.83

## 4. Latest Market Context

- 更新: 2026-05-31T09:34:53.651514+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=73941.5
- Funnel: target 773 → liquid 125 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PLAY/USDT:USDT | +46.15% | $3,477,791.45 |
| AIA/USDT:USDT | +33.86% | $1,884,670.60 |
| TA/USDT:USDT | +22.70% | $2,527,253.23 |
| PORTAL/USDT:USDT | +20.63% | $12,478,071.47 |
| MYX/USDT:USDT | +13.08% | $3,514,136.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +2.52% | +2.48% |
| TONCOIN/USDT:USDT | below_1h_threshold | +2.35% | +2.32% |
| ALGO/USDT:USDT | below_1h_threshold | +2.12% | +2.08% |
| LUNC/USDT:USDT | below_1h_threshold | +1.75% | +1.71% |
| BSB/USDT:USDT | below_1h_threshold | +1.58% | +1.54% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
