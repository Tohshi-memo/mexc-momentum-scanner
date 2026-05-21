# Decision Report

- generated_at: 2026-05-21T19:19:18.337294+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4653**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.64% / filled 20/20。**
- 全期間 MARKET基準: n=4653, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+1.64%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.64% | **+1.64%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.64% | **+1.64%** |
| ASK | 20/20 | 100.0% | +1.14% | **+1.14%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.01% | **+0.85%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.10% | **+0.72%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.74% | **+0.56%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.00% | **+0.00%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | -0.20% | **-0.17%** |
| MARKET_LONG | 20/20 | 100.0% | -0.24% | **-0.24%** |

## 2. $100 Live Portfolio

- 残高: **$95.25** / 初期 $100.00 (-4.75%)
- 確定トレード: 60件 (TP 15 / SL 42 / EXP 3)
- 最新: STXSTOCK/USDT:USDT SL_HIT PnL -1.86% 残高後 $95.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定: 547件 (Win 138 / Loss 185 / Flat 224) / skip 667件
- 成長率目線: 平均log +0.000355 / 幾何平均 +0.035% per trade / maxDD +4.21%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SPOTSTOCK/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $121.41

## 4. Latest Market Context

- 更新: 2026-05-21T19:19:16.052569+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.24% price=77540.0
- Funnel: target 763 → liquid 141 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RIVER/USDT:USDT | +9.07% | $5,596,937.20 |
| JTO/USDT:USDT | +6.04% | $3,431,673.06 |
| INJ/USDT:USDT | +4.23% | $26,624,350.50 |
| SNDKSTOCK/USDT:USDT | +4.00% | $2,394,153.54 |
| GRASS/USDT:USDT | +3.78% | $1,668,942.10 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RIVER/USDT:USDT | below_1h_threshold | +2.53% | +2.29% |
| JTO/USDT:USDT | below_1h_threshold | +1.76% | +1.52% |
| XPL/USDT:USDT | below_1h_threshold | +1.46% | +1.22% |
| FARTCOIN/USDT:USDT | below_1h_threshold | +1.28% | +1.04% |
| NEAR/USDT:USDT | below_1h_threshold | +1.25% | +1.01% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
