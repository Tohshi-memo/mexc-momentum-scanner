# Decision Report

- generated_at: 2026-09-09T08:41:18.027364+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14045**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.59% / filled 20/20。**
- 全期間 MARKET基準: n=14045, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.59% | **+0.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 16/20 | 80.0% | +1.22% | **+0.98%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.01% | **+0.81%** |
| MARKET | 20/20 | 100.0% | +0.59% | **+0.59%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.09% | **+0.38%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.23% | **+0.23%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -0.60% | **-0.09%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | -0.21% | **-0.15%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | -0.38% | **-0.17%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,001.97** / 初期 $100.00 (+901.97%)
- 確定: 5309件 (Win 1593 / Loss 1712 / Flat 2004) / skip 5297件
- 成長率目線: 平均log +0.000434 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CRO/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $1,001.97

## 4. Robust Adaptive DryRun ($100)

- 残高: **$190.26** / 初期 $100.00 (+90.26%)
- 確定: 2648件 (Win 728 / Loss 623 / Flat 1297) / skip 4808件
- 成長率目線: 平均log +0.000243 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0047 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CRO/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $190.26

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.95** / 初期 $100.00 (+17.95%)
- 確定: 2619件 (Win 765 / Loss 1000 / Flat 854) / pending 1件 / skip 2898件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000174 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CRO/USDT:USDT `MARKET` EXPIRED account +0.11% 残高後 $117.95

## 6. Latest Market Context

- 更新: 2026-09-09T08:41:09.226064+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.46% price=79609.5
- Funnel: target 1064 → liquid 159 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +67.88% | $1,367,969.97 |
| IOST/USDT:USDT | +34.27% | $3,279,375.59 |
| CNPY/USDT:USDT | +20.41% | $1,071,330.29 |
| OL/USDT:USDT | +18.54% | $2,243,877.63 |
| RAY/USDT:USDT | +15.14% | $5,003,095.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IOST/USDT:USDT | below_relative_strength | +5.19% | +4.73% |
| CATE/USDT:USDT | below_1h_threshold | +4.44% | +3.98% |
| ATOM/USDT:USDT | below_1h_threshold | +3.13% | +2.67% |
| ETHFI/USDT:USDT | below_1h_threshold | +2.32% | +1.86% |
| ARX/USDT:USDT | below_1h_threshold | +1.42% | +0.96% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
