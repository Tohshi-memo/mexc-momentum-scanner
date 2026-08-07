# Decision Report

- generated_at: 2026-08-07T02:21:31.610027+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10651**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.30% / filled 20/20。**
- 全期間 MARKET基準: n=10651, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.30%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.30% | **+0.30%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 15/20 | 75.0% | +0.58% | **+0.44%** |
| MARKET | 20/20 | 100.0% | +0.30% | **+0.30%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +1.64% | **+0.16%** |
| LIMIT_BB3S | 5/18 | 27.8% | +0.01% | **+0.00%** |
| LIMIT_10PCT | 3/20 | 15.0% | -0.36% | **-0.05%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +4.90% | **+4.90%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.56% | **+1.01%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.20% | **+0.72%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.02% | **+0.56%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$121.05** / 初期 $100.00 (+21.05%)
- 確定トレード: 175件 (TP 67 / SL 103 / EXP 5)
- 最新: COTI/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.05
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$595.60** / 初期 $100.00 (+495.60%)
- 確定: 3797件 (Win 1203 / Loss 1250 / Flat 1344) / skip 3415件
- 成長率目線: 平均log +0.000470 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: KMNO/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $595.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$144.37** / 初期 $100.00 (+44.37%)
- 確定: 1454件 (Win 406 / Loss 342 / Flat 706) / skip 2608件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AXTISTOCK/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $144.37

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.56** / 初期 $100.00 (+16.56%)
- 確定: 1157件 (Win 369 / Loss 455 / Flat 333) / pending 2件 / skip 970件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000250 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: RIVER/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $116.56

## 6. Latest Market Context

- 更新: 2026-08-07T02:21:19.489344+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=64414.0
- Funnel: target 958 → liquid 189 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.9 >= 65=1, 4h RSI 82.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +31.45% | $3,904,437.48 |
| STG/USDT:USDT | +28.52% | $4,603,918.89 |
| TWLOSTOCK/USDT:USDT | +17.30% | $1,386,780.95 |
| RIVER/USDT:USDT | +16.56% | $7,094,441.54 |
| NETSTOCK/USDT:USDT | +15.41% | $1,324,790.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STG/USDT:USDT | below_1h_threshold | +4.00% | +3.97% |
| BTW/USDT:USDT | below_1h_threshold | +2.67% | +2.64% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.53% | +2.50% |
| ACT/USDT:USDT | below_1h_threshold | +1.39% | +1.36% |
| NICKEL/USDT:USDT | below_1h_threshold | +1.08% | +1.05% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
