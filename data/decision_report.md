# Decision Report

- generated_at: 2026-09-22T07:21:24.166488+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15304**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.23% / filled 20/20。**
- 全期間 MARKET基準: n=15304, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.23% | **+0.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/16 | 37.5% | +3.65% | **+1.37%** |
| LIMIT_7PCT | 3/20 | 15.0% | +6.27% | **+0.94%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +2.24% | **+0.90%** |
| LIMIT_6PCT | 3/20 | 15.0% | +5.96% | **+0.89%** |
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.31% | **+0.52%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +2.25% | **+0.45%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.44% | **+0.39%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.70% | **+0.25%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.28% | **+0.21%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,177.97** / 初期 $100.00 (+1077.97%)
- 確定: 5795件 (Win 1723 / Loss 1866 / Flat 2206) / skip 6070件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: 4STOCK/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $1,177.97

## 4. Robust Adaptive DryRun ($100)

- 残高: **$248.70** / 初期 $100.00 (+148.70%)
- 確定: 3343件 (Win 923 / Loss 777 / Flat 1643) / skip 5372件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: 4STOCK/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.69% 残高後 $248.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.76** / 初期 $100.00 (+22.76%)
- 確定: 3076件 (Win 904 / Loss 1204 / Flat 968) / pending 2件 / skip 3695件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000191 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: 4STOCK/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $122.76

## 6. Latest Market Context

- 更新: 2026-09-22T07:21:13.127066+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=85306.0
- Funnel: target 1056 → liquid 184 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +53.16% | $1,007,061.66 |
| KERNEL/USDT:USDT | +33.45% | $3,173,247.51 |
| 4STOCK/USDT:USDT | +33.36% | $1,412,587.02 |
| MUBARAK/USDT:USDT | +22.44% | $2,661,291.96 |
| ALCH/USDT:USDT | +20.90% | $2,581,198.23 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| USELESS/USDT:USDT | below_1h_threshold | +2.63% | +2.68% |
| SAGA/USDT:USDT | below_1h_threshold | +2.41% | +2.46% |
| WIF/USDT:USDT | below_1h_threshold | +2.31% | +2.36% |
| FORM/USDT:USDT | below_1h_threshold | +2.21% | +2.26% |
| AGT/USDT:USDT | below_1h_threshold | +2.14% | +2.19% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
