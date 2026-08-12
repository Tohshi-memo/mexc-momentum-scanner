# Decision Report

- generated_at: 2026-08-12T02:36:29.625115+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11320**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11320, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.02%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.02% | **+0.02%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 18/20 | 90.0% | +0.78% | **+0.70%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.82% | **+0.53%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.47% | **+0.44%** |
| LIMIT_BB3S | 8/16 | 50.0% | +0.31% | **+0.15%** |
| MARKET | 20/20 | 100.0% | +0.02% | **+0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +5.76% | **+0.86%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.05% | **+0.74%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.43% | **+0.35%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.39% | **+0.33%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.57% | **+0.26%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 180件 (TP 69 / SL 106 / EXP 5)
- 最新: JIMOTHY/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$616.77** / 初期 $100.00 (+516.77%)
- 確定: 3939件 (Win 1230 / Loss 1285 / Flat 1424) / skip 3942件
- 成長率目線: 平均log +0.000462 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BEAT/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $616.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$143.44** / 初期 $100.00 (+43.44%)
- 確定: 1569件 (Win 437 / Loss 364 / Flat 768) / skip 3162件
- 成長率目線: 平均log +0.000230 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DODO/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $143.44

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.63** / 初期 $100.00 (+14.63%)
- 確定: 1338件 (Win 408 / Loss 527 / Flat 403) / pending 5件 / skip 1452件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000111 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PROM/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $114.63

## 6. Latest Market Context

- 更新: 2026-08-12T02:36:19.210639+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=63794.8
- Funnel: target 967 → liquid 189 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.9 >= 65=1, 4h RSI 72.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PROM/USDT:USDT | +38.99% | $7,145,021.51 |
| HOLO/USDT:USDT | +28.41% | $5,689,816.77 |
| JIMOTHY/USDT:USDT | +26.96% | $1,857,374.09 |
| LSK/USDT:USDT | +18.32% | $3,389,230.40 |
| CRWVSTOCK/USDT:USDT | +17.01% | $3,892,439.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +4.66% | +4.66% |
| KORU/USDT:USDT | below_1h_threshold | +3.11% | +3.11% |
| SNXX/USDT:USDT | below_1h_threshold | +2.70% | +2.70% |
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +2.59% | +2.59% |
| GRVT/USDT:USDT | below_1h_threshold | +2.31% | +2.31% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
