# Decision Report

- generated_at: 2026-08-06T22:21:28.772800+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10635**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.60% / filled 20/20。**
- 全期間 MARKET基準: n=10635, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.60% | **+2.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.60% | **+2.60%** |
| LIMIT_BB3S | 7/17 | 41.2% | +1.74% | **+0.72%** |
| LIMIT_1PCT | 15/20 | 75.0% | +0.80% | **+0.60%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +1.37% | **+0.14%** |
| LIMIT_8PCT | 6/20 | 30.0% | -0.15% | **-0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.22% | **+0.44%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +0.44% | **+0.11%** |
| LIMIT_6PCT_LONG | 13/20 | 65.0% | -0.22% | **-0.14%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -2.25% | **-0.23%** |
| MARKET_LONG | 20/20 | 100.0% | -0.40% | **-0.40%** |

## 2. $100 Live Portfolio

- 残高: **$121.05** / 初期 $100.00 (+21.05%)
- 確定トレード: 175件 (TP 67 / SL 103 / EXP 5)
- 最新: COTI/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.05
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$595.60** / 初期 $100.00 (+495.60%)
- 確定: 3796件 (Win 1203 / Loss 1250 / Flat 1343) / skip 3400件
- 成長率目線: 平均log +0.000470 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BICO/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account -0.13% 残高後 $595.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$144.37** / 初期 $100.00 (+44.37%)
- 確定: 1453件 (Win 406 / Loss 342 / Flat 705) / skip 2593件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $144.37

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.09** / 初期 $100.00 (+17.09%)
- 確定: 1153件 (Win 368 / Loss 452 / Flat 333) / pending 6件 / skip 953件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000245 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CATE/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $117.09

## 6. Latest Market Context

- 更新: 2026-08-06T22:21:18.700945+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=64378.2
- Funnel: target 958 → liquid 186 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SKYAI/USDT:USDT | +23.23% | $44,966,015.82 |
| STG/USDT:USDT | +20.23% | $1,637,722.89 |
| TWLOSTOCK/USDT:USDT | +17.55% | $1,336,244.29 |
| NETSTOCK/USDT:USDT | +16.85% | $1,103,749.63 |
| CATE/USDT:USDT | +16.61% | $3,461,492.31 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +2.26% | +2.31% |
| BANK/USDT:USDT | below_1h_threshold | +2.24% | +2.29% |
| ZBT/USDT:USDT | below_1h_threshold | +2.13% | +2.18% |
| HEI/USDT:USDT | below_1h_threshold | +2.10% | +2.15% |
| CYS/USDT:USDT | below_1h_threshold | +1.96% | +2.01% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
