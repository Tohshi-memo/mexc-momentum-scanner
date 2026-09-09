# Decision Report

- generated_at: 2026-09-09T06:06:19.928151+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14036**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.70% / filled 20/20。**
- 全期間 MARKET基準: n=14036, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.70%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.70% | **+0.70%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 16/20 | 80.0% | +1.55% | **+1.24%** |
| LIMIT_2PCT | 17/20 | 85.0% | +1.42% | **+1.21%** |
| LIMIT_3PCT | 14/20 | 70.0% | +1.65% | **+1.15%** |
| LIMIT_BB3S | 3/15 | 20.0% | +3.52% | **+0.70%** |
| MARKET | 20/20 | 100.0% | +0.70% | **+0.70%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.56% | **+0.31%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.70% | **+0.25%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.57% | **+0.20%** |
| LIMIT_BB3S_LONG | 2/5 | 40.0% | +0.11% | **+0.04%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,012.11** / 初期 $100.00 (+912.11%)
- 確定: 5300件 (Win 1591 / Loss 1708 / Flat 2001) / skip 5297件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IOST/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $1,012.11

## 4. Robust Adaptive DryRun ($100)

- 残高: **$190.12** / 初期 $100.00 (+90.12%)
- 確定: 2639件 (Win 727 / Loss 623 / Flat 1289) / skip 4808件
- 成長率目線: 平均log +0.000243 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0088 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: IOST/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $190.12

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.23** / 初期 $100.00 (+18.23%)
- 確定: 2616件 (Win 764 / Loss 998 / Flat 854) / pending 4件 / skip 2887件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000183 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: IOST/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $118.23

## 6. Latest Market Context

- 更新: 2026-09-09T06:06:07.939543+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=78900.0
- Funnel: target 1070 → liquid 165 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +75.00% | $1,053,999.60 |
| OL/USDT:USDT | +23.24% | $2,129,905.76 |
| IOST/USDT:USDT | +19.62% | $2,314,930.02 |
| NIULAI/USDT:USDT | +18.95% | $1,313,405.49 |
| RAY/USDT:USDT | +17.54% | $2,976,595.11 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIULAI/USDT:USDT | below_1h_threshold | +3.04% | +3.05% |
| IOST/USDT:USDT | below_1h_threshold | +3.00% | +3.01% |
| CATE/USDT:USDT | below_1h_threshold | +1.14% | +1.15% |
| BTR/USDT:USDT | below_1h_threshold | +0.51% | +0.52% |
| ZEC/USDT:USDT | below_1h_threshold | +0.44% | +0.45% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
