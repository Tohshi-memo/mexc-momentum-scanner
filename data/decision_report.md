# Decision Report

- generated_at: 2026-09-22T07:26:26.378370+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15305**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.39% / filled 20/20。**
- 全期間 MARKET基準: n=15305, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.39% | **+0.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/16 | 37.5% | +3.93% | **+1.47%** |
| LIMIT_7PCT | 3/20 | 15.0% | +6.27% | **+0.94%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +2.24% | **+0.90%** |
| LIMIT_6PCT | 3/20 | 15.0% | +5.96% | **+0.89%** |
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +3.27% | **+0.65%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.71% | **+0.60%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.05% | **+0.47%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +2.99% | **+0.45%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.44% | **+0.39%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,172.08** / 初期 $100.00 (+1072.08%)
- 確定: 5796件 (Win 1723 / Loss 1867 / Flat 2206) / skip 6070件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: 4STOCK/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,172.08

## 4. Robust Adaptive DryRun ($100)

- 残高: **$247.83** / 初期 $100.00 (+147.83%)
- 確定: 3344件 (Win 923 / Loss 778 / Flat 1643) / skip 5372件
- 成長率目線: 平均log +0.000271 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: 4STOCK/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $247.83

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.55** / 初期 $100.00 (+22.55%)
- 確定: 3077件 (Win 904 / Loss 1205 / Flat 968) / pending 2件 / skip 3695件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000190 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: 4STOCK/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $122.55

## 6. Latest Market Context

- 更新: 2026-09-22T07:26:14.490525+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.16% price=85210.8
- Funnel: target 1056 → liquid 185 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +52.17% | $1,014,676.34 |
| 4STOCK/USDT:USDT | +36.30% | $1,446,752.18 |
| KERNEL/USDT:USDT | +32.44% | $3,185,958.44 |
| MUBARAK/USDT:USDT | +21.69% | $2,713,198.65 |
| GRASS/USDT:USDT | +19.78% | $2,893,642.79 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SAGA/USDT:USDT | below_1h_threshold | +3.13% | +3.29% |
| S/USDT:USDT | below_1h_threshold | +2.69% | +2.85% |
| FORM/USDT:USDT | below_1h_threshold | +2.44% | +2.60% |
| WIF/USDT:USDT | below_1h_threshold | +2.19% | +2.35% |
| USELESS/USDT:USDT | below_1h_threshold | +2.18% | +2.34% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
