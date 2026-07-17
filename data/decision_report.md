# Decision Report

- generated_at: 2026-07-17T15:51:26.619961+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8865**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8865, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 4/20 | 20.0% | +8.00% | **+1.60%** |
| LIMIT_8PCT | 5/20 | 25.0% | +6.28% | **+1.57%** |
| LIMIT_7PCT | 5/20 | 25.0% | +4.88% | **+1.22%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +3.02% | **+1.21%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.92% | **+0.67%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.60% | **+1.12%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +3.12% | **+1.09%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.45% | **+0.80%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +2.49% | **+0.75%** |

## 2. $100 Live Portfolio

- 残高: **$112.93** / 初期 $100.00 (+12.93%)
- 確定トレード: 112件 (TP 43 / SL 65 / EXP 4)
- 最新: BSB/USDT:USDT TP_HIT PnL +8.00% 残高後 $112.93
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$355.37** / 初期 $100.00 (+255.37%)
- 確定: 2980件 (Win 928 / Loss 950 / Flat 1102) / skip 2446件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DODO/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.04% 残高後 $355.37

## 4. Robust Adaptive DryRun ($100)

- 残高: **$109.68** / 初期 $100.00 (+9.68%)
- 確定: 827件 (Win 196 / Loss 172 / Flat 459) / skip 1449件
- 成長率目線: 平均log +0.000112 / 幾何平均 +0.011% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0650 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DODO/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $109.68

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.06** / 初期 $100.00 (-0.94%)
- 確定: 131件 (Win 42 / Loss 75 / Flat 14) / pending 4件 / skip 201件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000187 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: DODO/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $99.06

## 6. Latest Market Context

- 更新: 2026-07-17T15:51:17.167585+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=63158.2
- Funnel: target 885 → liquid 179 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.3 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LRC/USDT:USDT | +66.45% | $5,716,704.82 |
| AKE/USDT:USDT | +23.38% | $40,589,937.57 |
| XEC/USDT:USDT | +22.45% | $2,475,700.52 |
| KAITO/USDT:USDT | +17.75% | $5,875,404.25 |
| LUMIA/USDT:USDT | +17.60% | $3,132,584.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| T/USDT:USDT | below_1h_threshold | +3.90% | +3.88% |
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +3.78% | +3.76% |
| O/USDT:USDT | below_1h_threshold | +3.08% | +3.06% |
| AEHRSTOCK/USDT:USDT | below_1h_threshold | +2.81% | +2.79% |
| DRAM/USDT:USDT | below_1h_threshold | +2.51% | +2.49% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
