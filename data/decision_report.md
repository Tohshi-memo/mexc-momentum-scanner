# Decision Report

- generated_at: 2026-06-11T10:55:36.083251+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6342**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=6342, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| ASK | 20/20 | 100.0% | +0.74% | **+0.74%** |
| LIMIT_BB3S | 6/16 | 37.5% | +0.78% | **+0.29%** |
| LIMIT_5PCT | 11/20 | 55.0% | +0.50% | **+0.28%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.91% | **+0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.61% | **+0.52%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | -0.56% | **-0.17%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$147.45** / 初期 $100.00 (+47.45%)
- 確定: 1271件 (Win 319 / Loss 401 / Flat 551) / skip 1632件
- 成長率目線: 平均log +0.000306 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STG/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $147.45

## 4. Latest Market Context

- 更新: 2026-06-11T10:55:32.623238+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.26% price=63059.3
- Funnel: target 782 → liquid 152 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| H/USDT:USDT | +76.70% | $15,528,580.93 |
| VELVET/USDT:USDT | +74.87% | $78,338,286.77 |
| BEAT/USDT:USDT | +47.38% | $221,574,567.61 |
| COLLECT/USDT:USDT | +44.82% | $1,952,780.23 |
| AIO/USDT:USDT | +39.84% | $7,387,404.04 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FIGHT/USDT:USDT | below_1h_threshold | +3.82% | +3.56% |
| RUNE/USDT:USDT | below_1h_threshold | +2.92% | +2.66% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +2.80% | +2.54% |
| WLD/USDT:USDT | below_1h_threshold | +1.76% | +1.50% |
| ATOM/USDT:USDT | below_1h_threshold | +1.45% | +1.19% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
