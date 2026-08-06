# Decision Report

- generated_at: 2026-08-06T22:26:39.420900+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10636**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.00% / filled 20/20。**
- 全期間 MARKET基準: n=10636, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.00% | **+2.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.00% | **+2.00%** |
| LIMIT_BB3S | 7/17 | 41.2% | +1.74% | **+0.72%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +1.37% | **+0.14%** |
| LIMIT_1PCT | 15/20 | 75.0% | +0.07% | **+0.05%** |
| LIMIT_8PCT | 6/20 | 30.0% | -0.15% | **-0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.22% | **+0.44%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +0.44% | **+0.11%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +0.21% | **+0.09%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +0.02% | **+0.01%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | -0.06% | **-0.04%** |

## 2. $100 Live Portfolio

- 残高: **$121.05** / 初期 $100.00 (+21.05%)
- 確定トレード: 175件 (TP 67 / SL 103 / EXP 5)
- 最新: COTI/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.05
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$595.60** / 初期 $100.00 (+495.60%)
- 確定: 3796件 (Win 1203 / Loss 1250 / Flat 1343) / skip 3401件
- 成長率目線: 平均log +0.000470 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BICO/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account -0.13% 残高後 $595.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$144.37** / 初期 $100.00 (+44.37%)
- 確定: 1453件 (Win 406 / Loss 342 / Flat 705) / skip 2594件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $144.37

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.89** / 初期 $100.00 (+16.89%)
- 確定: 1154件 (Win 368 / Loss 453 / Flat 333) / pending 5件 / skip 953件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000244 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HEI/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $116.89

## 6. Latest Market Context

- 更新: 2026-08-06T22:26:26.947463+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=64325.6
- Funnel: target 958 → liquid 186 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SKYAI/USDT:USDT | +23.86% | $45,213,139.78 |
| STG/USDT:USDT | +23.42% | $1,688,825.38 |
| TWLOSTOCK/USDT:USDT | +17.93% | $1,339,158.84 |
| NETSTOCK/USDT:USDT | +16.49% | $1,110,957.23 |
| RIVER/USDT:USDT | +14.10% | $4,234,553.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HEI/USDT:USDT | below_1h_threshold | +3.27% | +3.41% |
| ZBT/USDT:USDT | below_1h_threshold | +2.98% | +3.11% |
| STG/USDT:USDT | below_1h_threshold | +2.11% | +2.24% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.76% | +1.90% |
| RIVER/USDT:USDT | below_1h_threshold | +1.69% | +1.82% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
