# Decision Report

- generated_at: 2026-09-09T10:51:26.979447+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14053**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.12% / filled 20/20。**
- 全期間 MARKET基準: n=14053, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.12% | **+1.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 17/20 | 85.0% | +1.34% | **+1.14%** |
| MARKET | 20/20 | 100.0% | +1.12% | **+1.12%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.81% | **+0.73%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.77% | **+0.50%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +0.59% | **+0.06%** |
| MARKET_LONG | 20/20 | 100.0% | +0.03% | **+0.03%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.00% | **+0.00%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | -0.39% | **-0.18%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$991.95** / 初期 $100.00 (+891.95%)
- 確定: 5313件 (Win 1594 / Loss 1715 / Flat 2004) / skip 5301件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IOST/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $991.95

## 4. Robust Adaptive DryRun ($100)

- 残高: **$190.39** / 初期 $100.00 (+90.39%)
- 確定: 2656件 (Win 729 / Loss 623 / Flat 1304) / skip 4808件
- 成長率目線: 平均log +0.000242 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CNPY/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $190.39

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.95** / 初期 $100.00 (+17.95%)
- 確定: 2619件 (Win 765 / Loss 1000 / Flat 854) / pending 1件 / skip 2905件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000194 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CRO/USDT:USDT `MARKET` EXPIRED account +0.11% 残高後 $117.95

## 6. Latest Market Context

- 更新: 2026-09-09T10:51:16.148489+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=78968.4
- Funnel: target 1064 → liquid 161 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.0 >= 65=1, 4h RSI 69.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +65.53% | $1,549,095.13 |
| IOST/USDT:USDT | +38.78% | $5,059,805.84 |
| OL/USDT:USDT | +18.79% | $2,309,469.33 |
| RAY/USDT:USDT | +16.78% | $5,608,424.43 |
| CNPY/USDT:USDT | +14.88% | $1,118,262.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UAI/USDT:USDT | below_1h_threshold | +4.98% | +4.91% |
| NEAR/USDT:USDT | below_1h_threshold | +4.36% | +4.29% |
| RAY/USDT:USDT | below_1h_threshold | +4.09% | +4.02% |
| IOST/USDT:USDT | below_1h_threshold | +2.72% | +2.65% |
| GRASS/USDT:USDT | below_1h_threshold | +2.01% | +1.94% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
