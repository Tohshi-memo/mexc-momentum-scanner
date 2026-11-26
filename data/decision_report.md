# Decision Report

- generated_at: 2026-11-26T00:41:22.823955+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19659**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19659, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.67%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.67% | **-0.67%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 2/20 | 10.0% | +0.95% | **+0.10%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.03% | **+0.02%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | -0.24% | **-0.11%** |
| LIMIT_ATR | 15/20 | 75.0% | -0.33% | **-0.25%** |
| LIMIT_2PCT | 17/20 | 85.0% | -0.29% | **-0.25%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.17% | **+1.17%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.02% | **+0.77%** |
| LIMIT_5PCT_LONG | 6/20 | 30.0% | +2.14% | **+0.64%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |

## 2. $100 Live Portfolio

- 残高: **$121.61** / 初期 $100.00 (+21.61%)
- 確定トレード: 288件 (TP 105 / SL 175 / EXP 8)
- 最新: SOXS/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,978.37** / 初期 $100.00 (+1878.37%)
- 確定: 7613件 (Win 2191 / Loss 2451 / Flat 2971) / skip 8607件
- 成長率目線: 平均log +0.000392 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $1,978.37

## 4. Robust Adaptive DryRun ($100)

- 残高: **$465.65** / 初期 $100.00 (+365.65%)
- 確定: 5221件 (Win 1389 / Loss 1125 / Flat 2707) / skip 7849件
- 成長率目線: 平均log +0.000295 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $465.65

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7820件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000343 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-26T00:41:09.326734+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.44% price=60694.4
- Funnel: target 1097 → liquid 154 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BULLA/USDT:USDT | +33.54% | $1,364,570.76 |
| SOXL/USDT:USDT | +30.70% | $1,901,423,764.31 |
| MANTRA/USDT:USDT | +25.60% | $4,015,135.73 |
| SNXX/USDT:USDT | +24.65% | $34,200,990.70 |
| MVLL/USDT:USDT | +23.09% | $5,172,198.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JCT/USDT:USDT | below_1h_threshold | +4.28% | +3.84% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +4.11% | +3.67% |
| MANTRA/USDT:USDT | below_1h_threshold | +2.59% | +2.15% |
| KOR/USDT:USDT | below_1h_threshold | +2.08% | +1.64% |
| VVV/USDT:USDT | below_1h_threshold | +2.07% | +1.63% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
