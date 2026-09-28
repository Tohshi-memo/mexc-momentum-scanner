# Decision Report

- generated_at: 2026-09-28T14:31:24.014081+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15728**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15728, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.53%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.53% | **-1.53%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/18 | 22.2% | +5.57% | **+1.24%** |
| LIMIT_9PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_10PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +1.88% | **+0.94%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +5.59% | **+5.59%** |
| MARKET_LONG | 20/20 | 100.0% | +1.93% | **+1.93%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +1.33% | **+0.86%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +1.44% | **+0.72%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +1.25% | **+0.56%** |

## 2. $100 Live Portfolio

- 残高: **$120.75** / 初期 $100.00 (+20.75%)
- 確定トレード: 225件 (TP 82 / SL 136 / EXP 7)
- 最新: XLM/USDT:USDT SL_HIT PnL -2.52% 残高後 $120.75
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,227.24** / 初期 $100.00 (+1127.24%)
- 確定: 5983件 (Win 1766 / Loss 1925 / Flat 2292) / skip 6306件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BATON/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $1,227.24

## 4. Robust Adaptive DryRun ($100)

- 残高: **$263.08** / 初期 $100.00 (+163.08%)
- 確定: 3534件 (Win 974 / Loss 812 / Flat 1748) / skip 5605件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: QNT/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $263.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.84** / 初期 $100.00 (+18.84%)
- 確定: 3294件 (Win 955 / Loss 1292 / Flat 1047) / pending 4件 / skip 3903件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000207 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SI/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $118.84

## 6. Latest Market Context

- 更新: 2026-09-28T14:31:12.634438+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.41% price=83261.0
- Funnel: target 1065 → liquid 170 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SI/USDT:USDT | +69.90% | $1,107,967.63 |
| BATON/USDT:USDT | +62.06% | $1,621,110.75 |
| QNT/USDT:USDT | +31.76% | $332,368,898.88 |
| HBAR/USDT:USDT | +27.55% | $109,053,828.25 |
| NMR/USDT:USDT | +16.63% | $1,251,858.03 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| OKTASTOCK/USDT:USDT | below_1h_threshold | +3.16% | +3.57% |
| NMR/USDT:USDT | below_1h_threshold | +2.92% | +3.33% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +2.80% | +3.21% |
| SOXS/USDT:USDT | below_1h_threshold | +2.28% | +2.69% |
| BATON/USDT:USDT | below_1h_threshold | +1.65% | +2.06% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
