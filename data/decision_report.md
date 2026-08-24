# Decision Report

- generated_at: 2026-08-24T20:11:31.880023+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12544**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12544, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 5/20 | 25.0% | +0.80% | **+0.20%** |
| LIMIT_9PCT | 6/20 | 30.0% | -0.00% | **-0.00%** |
| LIMIT_8PCT | 6/20 | 30.0% | -0.00% | **-0.00%** |
| LIMIT_3PCT | 15/20 | 75.0% | -0.19% | **-0.14%** |
| LIMIT_7PCT | 6/20 | 30.0% | -0.87% | **-0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +6.49% | **+1.95%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +4.80% | **+1.20%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.94% | **+1.17%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.00% | **+1.00%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$699.16** / 初期 $100.00 (+599.16%)
- 確定: 4528件 (Win 1382 / Loss 1485 / Flat 1661) / skip 4577件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $699.16

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.16** / 初期 $100.00 (+56.16%)
- 確定: 1973件 (Win 536 / Loss 471 / Flat 966) / skip 3982件
- 成長率目線: 平均log +0.000226 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $156.16

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.84** / 初期 $100.00 (+15.84%)
- 確定: 1910件 (Win 561 / Loss 725 / Flat 624) / pending 3件 / skip 2108件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000044 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: COTI/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $115.84

## 6. Latest Market Context

- 更新: 2026-08-24T20:11:22.955280+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=78753.6
- Funnel: target 1022 → liquid 184 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +71.24% | $2,682,745.01 |
| STORJ/USDT:USDT | +12.69% | $4,127,540.39 |
| TUT/USDT:USDT | +8.12% | $62,692,727.91 |
| MONAD/USDT:USDT | +6.15% | $3,450,884.82 |
| CYS/USDT:USDT | +5.58% | $2,414,081.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CATE/USDT:USDT | below_1h_threshold | +2.16% | +2.11% |
| PONS/USDT:USDT | below_1h_threshold | +1.95% | +1.91% |
| INJ/USDT:USDT | below_1h_threshold | +1.39% | +1.35% |
| BEAT/USDT:USDT | below_1h_threshold | +1.18% | +1.14% |
| ETHFI/USDT:USDT | below_1h_threshold | +1.11% | +1.07% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
