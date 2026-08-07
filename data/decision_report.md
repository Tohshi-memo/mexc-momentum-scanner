# Decision Report

- generated_at: 2026-08-07T15:51:20.082397+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10729**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.24% / filled 20/20。**
- 全期間 MARKET基準: n=10729, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.24% | **+2.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.24% | **+2.24%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.41% | **+1.13%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.09% | **+0.60%** |
| LIMIT_3PCT | 9/20 | 45.0% | +1.19% | **+0.54%** |
| LIMIT_BB3S | 8/20 | 40.0% | +0.81% | **+0.32%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.02% | **+0.41%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -0.60% | **-0.12%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | -0.86% | **-0.39%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | -0.90% | **-0.68%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$595.60** / 初期 $100.00 (+495.60%)
- 確定: 3799件 (Win 1203 / Loss 1250 / Flat 1346) / skip 3491件
- 成長率目線: 平均log +0.000470 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AXTISTOCK/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $595.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$144.49** / 初期 $100.00 (+44.49%)
- 確定: 1457件 (Win 407 / Loss 342 / Flat 708) / skip 2683件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $144.49

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.07** / 初期 $100.00 (+19.07%)
- 確定: 1174件 (Win 380 / Loss 461 / Flat 333) / pending 1件 / skip 1027件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000364 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: DKNGSTOCK/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $119.07

## 6. Latest Market Context

- 更新: 2026-08-07T15:51:12.293319+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=64988.5
- Funnel: target 961 → liquid 193 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BICO/USDT:USDT | +41.02% | $32,960,963.36 |
| CATE/USDT:USDT | +38.82% | $4,314,004.93 |
| SKYAI/USDT:USDT | +36.29% | $85,230,666.58 |
| TUT/USDT:USDT | +35.29% | $1,384,147.33 |
| TST/USDT:USDT | +32.01% | $1,337,051.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +4.94% | +4.85% |
| TWLOSTOCK/USDT:USDT | below_1h_threshold | +4.06% | +3.96% |
| CATE/USDT:USDT | below_1h_threshold | +3.19% | +3.09% |
| DKNGSTOCK/USDT:USDT | below_1h_threshold | +3.11% | +3.01% |
| TTWOSTOCK/USDT:USDT | below_1h_threshold | +3.05% | +2.96% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
