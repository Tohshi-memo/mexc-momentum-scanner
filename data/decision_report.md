# Decision Report

- generated_at: 2026-08-06T23:21:30.283974+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10641**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.56% / filled 20/20。**
- 全期間 MARKET基準: n=10641, expectancy=-0.02%
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
| LIMIT_FIB1618 | 2/20 | 10.0% | +1.37% | **+0.14%** |
| LIMIT_BB3S | 6/18 | 33.3% | +0.27% | **+0.09%** |
| LIMIT_8PCT | 5/20 | 25.0% | -0.92% | **-0.23%** |
| LIMIT_10PCT | 4/20 | 20.0% | -1.64% | **-0.33%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -0.60% | **-0.09%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | -0.48% | **-0.21%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -2.25% | **-0.23%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | -0.58% | **-0.35%** |

## 2. $100 Live Portfolio

- 残高: **$121.05** / 初期 $100.00 (+21.05%)
- 確定トレード: 175件 (TP 67 / SL 103 / EXP 5)
- 最新: COTI/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.05
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$595.60** / 初期 $100.00 (+495.60%)
- 確定: 3796件 (Win 1203 / Loss 1250 / Flat 1343) / skip 3406件
- 成長率目線: 平均log +0.000470 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BICO/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account -0.13% 残高後 $595.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$144.37** / 初期 $100.00 (+44.37%)
- 確定: 1454件 (Win 406 / Loss 342 / Flat 706) / skip 2598件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AXTISTOCK/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $144.37

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.77** / 初期 $100.00 (+16.77%)
- 確定: 1156件 (Win 369 / Loss 454 / Flat 333) / pending 3件 / skip 956件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000194 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AXTISTOCK/USDT:USDT `MARKET_LONG` EXPIRED account +0.07% 残高後 $116.77

## 6. Latest Market Context

- 更新: 2026-08-06T23:21:22.513569+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=64251.5
- Funnel: target 958 → liquid 187 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SKYAI/USDT:USDT | +25.56% | $47,375,971.38 |
| STG/USDT:USDT | +22.31% | $2,710,030.12 |
| TWLOSTOCK/USDT:USDT | +18.39% | $1,354,070.86 |
| NETSTOCK/USDT:USDT | +14.96% | $1,239,708.72 |
| RIVER/USDT:USDT | +14.91% | $4,741,264.10 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +2.15% | +2.26% |
| COOKIE/USDT:USDT | below_1h_threshold | +1.96% | +2.06% |
| AXTISTOCK/USDT:USDT | below_1h_threshold | +1.51% | +1.61% |
| AKAMSTOCK/USDT:USDT | below_1h_threshold | +1.29% | +1.39% |
| UAI/USDT:USDT | below_1h_threshold | +1.28% | +1.38% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
