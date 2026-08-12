# Decision Report

- generated_at: 2026-08-12T02:51:26.417909+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11323**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11323, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.56%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.56% | **-0.56%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 7/15 | 46.7% | +0.57% | **+0.27%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.16% | **+0.11%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.03% | **+0.02%** |
| LIMIT_6PCT | 5/20 | 25.0% | -0.47% | **-0.12%** |
| LIMIT_10PCT | 3/20 | 15.0% | -0.85% | **-0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +5.76% | **+0.86%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.91% | **+0.77%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.84% | **+0.63%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.94% | **+0.56%** |
| MARKET_LONG | 20/20 | 100.0% | +0.53% | **+0.53%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 180件 (TP 69 / SL 106 / EXP 5)
- 最新: JIMOTHY/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$616.77** / 初期 $100.00 (+516.77%)
- 確定: 3939件 (Win 1230 / Loss 1285 / Flat 1424) / skip 3945件
- 成長率目線: 平均log +0.000462 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BEAT/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $616.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$143.44** / 初期 $100.00 (+43.44%)
- 確定: 1569件 (Win 437 / Loss 364 / Flat 768) / skip 3165件
- 成長率目線: 平均log +0.000230 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DODO/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $143.44

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.63** / 初期 $100.00 (+14.63%)
- 確定: 1341件 (Win 408 / Loss 527 / Flat 406) / pending 5件 / skip 1452件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000111 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PROM/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $114.63

## 6. Latest Market Context

- 更新: 2026-08-12T02:51:16.510513+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=63746.3
- Funnel: target 967 → liquid 190 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PROM/USDT:USDT | +59.98% | $7,430,148.21 |
| HOLO/USDT:USDT | +33.56% | $5,796,853.97 |
| JIMOTHY/USDT:USDT | +26.14% | $1,871,612.18 |
| CRWVSTOCK/USDT:USDT | +16.83% | $3,899,355.24 |
| LSK/USDT:USDT | +15.90% | $3,427,596.59 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +3.94% | +4.02% |
| BTW/USDT:USDT | below_1h_threshold | +3.92% | +4.00% |
| KORU/USDT:USDT | below_1h_threshold | +3.11% | +3.19% |
| SNXX/USDT:USDT | below_1h_threshold | +2.70% | +2.78% |
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +2.59% | +2.67% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
