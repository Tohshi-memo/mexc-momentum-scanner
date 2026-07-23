# Decision Report

- generated_at: 2026-07-23T16:01:19.362175+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9376**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9376, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.03% | **+0.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 8/19 | 42.1% | +2.15% | **+0.90%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.89% | **+0.71%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.69% | **+0.66%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.83% | **+0.33%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.31% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.90% | **+0.72%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.61% | **+0.52%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +0.80% | **+0.40%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.23% | **+0.25%** |
| MARKET_LONG | 20/20 | 100.0% | +0.20% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$103.79** / 初期 $100.00 (+3.79%)
- 確定トレード: 136件 (TP 45 / SL 86 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -2.63% 残高後 $103.79
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$426.05** / 初期 $100.00 (+326.05%)
- 確定: 3321件 (Win 1048 / Loss 1075 / Flat 1198) / skip 2616件
- 成長率目線: 平均log +0.000436 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $426.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.36** / 初期 $100.00 (+30.36%)
- 確定: 1162件 (Win 312 / Loss 254 / Flat 596) / skip 1625件
- 成長率目線: 平均log +0.000228 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BROCCOLIF3B/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $130.36

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.92** / 初期 $100.00 (+0.92%)
- 確定: 442件 (Win 146 / Loss 181 / Flat 115) / pending 4件 / skip 401件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000048 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.17% 残高後 $100.92

## 6. Latest Market Context

- 更新: 2026-07-23T16:01:09.968361+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=64922.8
- Funnel: target 897 → liquid 177 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RIF/USDT:USDT | +2.52% | $10,763,982.20 |
| JIMOTHY/USDT:USDT | +1.85% | $5,783,756.49 |
| RE/USDT:USDT | +1.30% | $11,207,589.24 |
| BANK/USDT:USDT | +0.46% | $108,850,251.87 |
| TLM/USDT:USDT | +0.33% | $1,299,048.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RIF/USDT:USDT | below_1h_threshold | +2.67% | +2.69% |
| RE/USDT:USDT | below_1h_threshold | +1.96% | +1.98% |
| JIMOTHY/USDT:USDT | below_1h_threshold | +1.47% | +1.50% |
| GOOGLSTOCK/USDT:USDT | below_1h_threshold | +0.77% | +0.79% |
| SNXX/USDT:USDT | below_1h_threshold | +0.74% | +0.77% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
