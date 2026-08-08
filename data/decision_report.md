# Decision Report

- generated_at: 2026-08-08T08:51:26.454733+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10824**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.40% / filled 20/20。**
- 全期間 MARKET基準: n=10824, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_7PCT | 6/20 | 30.0% | +1.40% | **+0.42%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.08% | **+0.38%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.36% | **+0.30%** |
| LIMIT_BB3S | 7/17 | 41.2% | +0.68% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +6.84% | **+1.71%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +3.70% | **+1.11%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +2.22% | **+1.00%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.75% | **+0.79%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.90% | **+0.72%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$627.68** / 初期 $100.00 (+527.68%)
- 確定: 3825件 (Win 1210 / Loss 1252 / Flat 1363) / skip 3560件
- 成長率目線: 平均log +0.000480 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TUT/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $627.68

## 4. Robust Adaptive DryRun ($100)

- 残高: **$142.00** / 初期 $100.00 (+42.00%)
- 確定: 1510件 (Win 424 / Loss 360 / Flat 726) / skip 2725件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1276 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $142.00

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.48** / 初期 $100.00 (+18.48%)
- 確定: 1194件 (Win 383 / Loss 468 / Flat 343) / pending 5件 / skip 1098件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000361 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TUT/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $118.48

## 6. Latest Market Context

- 更新: 2026-08-08T08:51:14.796111+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=64968.9
- Funnel: target 961 → liquid 175 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +253.52% | $8,393,883.30 |
| BLUAI/USDT:USDT | +58.30% | $1,450,513.51 |
| TUT/USDT:USDT | +43.26% | $3,564,435.59 |
| MMT/USDT:USDT | +31.66% | $4,746,690.86 |
| CYS/USDT:USDT | +31.64% | $18,808,752.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CYS/USDT:USDT | below_1h_threshold | +3.19% | +3.14% |
| CAP/USDT:USDT | below_1h_threshold | +2.56% | +2.51% |
| RE/USDT:USDT | below_1h_threshold | +2.50% | +2.45% |
| HEI/USDT:USDT | below_1h_threshold | +2.44% | +2.39% |
| AKE/USDT:USDT | below_1h_threshold | +2.22% | +2.17% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
