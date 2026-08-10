# Decision Report

- generated_at: 2026-08-10T04:01:20.658689+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11122**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11122, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 19/20 | 95.0% | +1.17% | **+1.11%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.89% | **+0.71%** |
| LIMIT_BB3S | 2/17 | 11.8% | +5.72% | **+0.67%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.51% | **+0.51%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +6.16% | **+6.16%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +3.37% | **+1.68%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.94% | **+1.17%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +3.21% | **+0.80%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.78% | **+0.62%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$624.97** / 初期 $100.00 (+524.97%)
- 確定: 3933件 (Win 1230 / Loss 1282 / Flat 1421) / skip 3750件
- 成長率目線: 平均log +0.000466 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TUT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $624.97

## 4. Robust Adaptive DryRun ($100)

- 残高: **$141.89** / 初期 $100.00 (+41.89%)
- 確定: 1513件 (Win 424 / Loss 361 / Flat 728) / skip 3020件
- 成長率目線: 平均log +0.000231 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TST/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.08% 残高後 $141.89

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.30** / 初期 $100.00 (+17.30%)
- 確定: 1283件 (Win 397 / Loss 493 / Flat 393) / pending 0件 / skip 1314件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000050 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `MARKET` EXPIRED account +0.20% 残高後 $117.30

## 6. Latest Market Context

- 更新: 2026-08-10T04:01:13.541709+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=64945.2
- Funnel: target 961 → liquid 159 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TUT/USDT:USDT | +58.92% | $81,152,031.00 |
| BMT/USDT:USDT | +56.98% | $19,336,080.29 |
| CAP/USDT:USDT | +27.47% | $2,813,493.58 |
| TST/USDT:USDT | +16.77% | $2,823,503.49 |
| NIL/USDT:USDT | +15.85% | $2,447,785.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BMT/USDT:USDT | below_1h_threshold | +1.21% | +1.22% |
| TUT/USDT:USDT | below_1h_threshold | +1.15% | +1.15% |
| BANANAS31/USDT:USDT | below_1h_threshold | +0.85% | +0.85% |
| LAB/USDT:USDT | below_1h_threshold | +0.41% | +0.41% |
| SOXL/USDT:USDT | below_1h_threshold | +0.39% | +0.40% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
