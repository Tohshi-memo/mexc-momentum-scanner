# Decision Report

- generated_at: 2026-11-22T08:11:25.964821+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19365**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.86% / filled 20/20。**
- 全期間 MARKET基準: n=19365, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.86%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.86% | **+0.86%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 8/17 | 47.1% | +3.39% | **+1.59%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.56% | **+1.49%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.34% | **+1.01%** |
| MARKET | 20/20 | 100.0% | +0.86% | **+0.86%** |
| LIMIT_5PCT | 7/20 | 35.0% | +2.26% | **+0.79%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +1.92% | **+1.92%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +2.29% | **+1.60%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +2.22% | **+1.00%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.84% | **+0.92%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.84% | **+0.71%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 283件 (TP 103 / SL 172 / EXP 8)
- 最新: INTCSTOCK/USDT:USDT TP_HIT PnL +5.26% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,778.01** / 初期 $100.00 (+1678.01%)
- 確定: 7481件 (Win 2149 / Loss 2408 / Flat 2924) / skip 8445件
- 成長率目線: 平均log +0.000385 / 幾何平均 +0.038% per trade / maxDD +9.04%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ENSO/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,778.01

## 4. Robust Adaptive DryRun ($100)

- 残高: **$449.65** / 初期 $100.00 (+349.65%)
- 確定: 5130件 (Win 1365 / Loss 1103 / Flat 2662) / skip 7646件
- 成長率目線: 平均log +0.000293 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0425 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $449.65

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7525件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000388 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-22T08:11:15.853316+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=59180.0
- Funnel: target 1086 → liquid 105 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLAUDIA/USDT:USDT | +36.38% | $2,245,377.77 |
| PIEVERSE/USDT:USDT | +31.71% | $7,823,897.98 |
| BLESS/USDT:USDT | +24.34% | $56,233,950.22 |
| SKYAI/USDT:USDT | +24.23% | $1,938,507.14 |
| BTW/USDT:USDT | +9.47% | $5,479,620.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_1h_threshold | +3.41% | +3.35% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +3.25% | +3.19% |
| CLAUDIA/USDT:USDT | below_1h_threshold | +2.28% | +2.22% |
| DODO/USDT:USDT | below_1h_threshold | +1.21% | +1.15% |
| IRYS/USDT:USDT | below_1h_threshold | +1.14% | +1.08% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
