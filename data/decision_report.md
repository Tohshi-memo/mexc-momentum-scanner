# Decision Report

- generated_at: 2026-09-09T11:36:32.280945+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14056**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.32% / filled 20/20。**
- 全期間 MARKET基準: n=14056, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.32% | **+2.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.32% | **+2.32%** |
| LIMIT_1PCT | 18/20 | 90.0% | +2.09% | **+1.88%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.64% | **+1.23%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.75% | **+0.96%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -0.18% | **-0.04%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -0.89% | **-0.09%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -0.94% | **-0.14%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | -0.36% | **-0.20%** |
| LIMIT_7PCT_LONG | 12/20 | 60.0% | -0.81% | **-0.48%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$991.95** / 初期 $100.00 (+891.95%)
- 確定: 5313件 (Win 1594 / Loss 1715 / Flat 2004) / skip 5304件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IOST/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $991.95

## 4. Robust Adaptive DryRun ($100)

- 残高: **$190.39** / 初期 $100.00 (+90.39%)
- 確定: 2657件 (Win 729 / Loss 623 / Flat 1305) / skip 4810件
- 成長率目線: 平均log +0.000242 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: IOST/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $190.39

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.95** / 初期 $100.00 (+17.95%)
- 確定: 2619件 (Win 765 / Loss 1000 / Flat 854) / pending 1件 / skip 2908件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000316 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CRO/USDT:USDT `MARKET` EXPIRED account +0.11% 残高後 $117.95

## 6. Latest Market Context

- 更新: 2026-09-09T11:36:17.945070+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=79007.7
- Funnel: target 1064 → liquid 161 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.0 >= 65=1, 4h RSI 81.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +53.89% | $1,601,155.79 |
| IOST/USDT:USDT | +32.08% | $5,674,971.59 |
| NIULAI/USDT:USDT | +29.10% | $2,199,704.46 |
| OL/USDT:USDT | +22.28% | $2,323,038.31 |
| BR/USDT:USDT | +19.43% | $1,215,318.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| OL/USDT:USDT | below_1h_threshold | +3.66% | +3.51% |
| VVV/USDT:USDT | below_1h_threshold | +2.98% | +2.82% |
| BR/USDT:USDT | below_1h_threshold | +2.76% | +2.60% |
| ZEN/USDT:USDT | below_1h_threshold | +2.49% | +2.33% |
| ZEC/USDT:USDT | below_1h_threshold | +2.42% | +2.26% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
