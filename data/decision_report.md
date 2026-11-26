# Decision Report

- generated_at: 2026-11-26T03:01:19.377889+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19665**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19665, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.90%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.90% | **-0.90%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 18/20 | 90.0% | +0.96% | **+0.86%** |
| LIMIT_5PCT | 5/20 | 25.0% | +2.36% | **+0.59%** |
| LIMIT_2PCT | 19/20 | 95.0% | +0.34% | **+0.32%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_BB3S | 2/15 | 13.3% | +1.72% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +5.41% | **+1.89%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +5.32% | **+1.60%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.48% | **+1.04%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.97% | **+0.82%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.09% | **+0.65%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 289件 (TP 105 / SL 176 / EXP 8)
- 最新: AKE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,978.37** / 初期 $100.00 (+1878.37%)
- 確定: 7613件 (Win 2191 / Loss 2451 / Flat 2971) / skip 8613件
- 成長率目線: 平均log +0.000392 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $1,978.37

## 4. Robust Adaptive DryRun ($100)

- 残高: **$465.65** / 初期 $100.00 (+365.65%)
- 確定: 5221件 (Win 1389 / Loss 1125 / Flat 2707) / skip 7855件
- 成長率目線: 平均log +0.000295 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $465.65

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7828件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000048 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-26T03:01:07.472914+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=60715.0
- Funnel: target 1097 → liquid 154 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SI/USDT:USDT | +44.55% | $1,060,195.42 |
| BULLA/USDT:USDT | +38.36% | $1,464,090.99 |
| SOXL/USDT:USDT | +28.29% | $1,850,095,617.49 |
| MVLL/USDT:USDT | +22.96% | $5,112,674.82 |
| SNXX/USDT:USDT | +21.53% | $31,946,847.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PIEVERSE/USDT:USDT | below_1h_threshold | +1.11% | +1.07% |
| SI/USDT:USDT | below_1h_threshold | +0.62% | +0.57% |
| KOR/USDT:USDT | below_1h_threshold | +0.61% | +0.56% |
| SLX/USDT:USDT | below_1h_threshold | +0.47% | +0.42% |
| TQQQ/USDT:USDT | below_1h_threshold | +0.33% | +0.28% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
