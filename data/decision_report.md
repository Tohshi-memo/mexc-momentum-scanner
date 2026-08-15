# Decision Report

- generated_at: 2026-08-15T13:16:26.303057+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11668**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.00% / filled 20/20。**
- 全期間 MARKET基準: n=11668, expectancy=-0.01%
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
| LIMIT_2PCT | 14/20 | 70.0% | +1.31% | **+0.91%** |
| LIMIT_1PCT | 15/20 | 75.0% | +0.41% | **+0.31%** |
| LIMIT_4PCT | 10/20 | 50.0% | +0.40% | **+0.20%** |
| LIMIT_3PCT | 12/20 | 60.0% | +0.27% | **+0.16%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +3.29% | **+0.82%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +1.61% | **+0.56%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +0.16% | **+0.03%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | -0.08% | **-0.05%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | -0.38% | **-0.23%** |

## 2. $100 Live Portfolio

- 残高: **$121.53** / 初期 $100.00 (+21.53%)
- 確定トレード: 183件 (TP 71 / SL 107 / EXP 5)
- 最新: MOVR/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.53
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$641.37** / 初期 $100.00 (+541.37%)
- 確定: 4136件 (Win 1290 / Loss 1355 / Flat 1491) / skip 4093件
- 成長率目線: 平均log +0.000449 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MOVR/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $641.37

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.13** / 初期 $100.00 (+55.13%)
- 確定: 1731件 (Win 491 / Loss 413 / Flat 827) / skip 3348件
- 成長率目線: 平均log +0.000254 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1078 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MOVR/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $155.13

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.74** / 初期 $100.00 (+18.74%)
- 確定: 1610件 (Win 490 / Loss 610 / Flat 510) / pending 5件 / skip 1525件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000507 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MOVR/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $118.74

## 6. Latest Market Context

- 更新: 2026-08-15T13:16:14.665304+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=63049.2
- Funnel: target 985 → liquid 150 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COW/USDT:USDT | +53.60% | $7,361,356.02 |
| MOVR/USDT:USDT | +39.80% | $1,402,310.52 |
| WAL/USDT:USDT | +27.64% | $1,405,405.94 |
| ANSEM/USDT:USDT | +23.94% | $1,667,386.65 |
| VELVET/USDT:USDT | +23.58% | $31,029,505.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIO/USDT:USDT | below_1h_threshold | +3.86% | +3.83% |
| H/USDT:USDT | below_1h_threshold | +3.09% | +3.06% |
| PRL/USDT:USDT | below_1h_threshold | +2.46% | +2.42% |
| TUT/USDT:USDT | below_1h_threshold | +2.06% | +2.03% |
| ANSEM/USDT:USDT | below_1h_threshold | +1.05% | +1.02% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
