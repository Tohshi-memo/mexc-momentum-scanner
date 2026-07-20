# Decision Report

- generated_at: 2026-07-20T13:31:29.794034+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9110**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9110, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 7/20 | 35.0% | +3.55% | **+1.24%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_6PCT | 8/20 | 40.0% | +1.15% | **+0.46%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.46% | **+0.23%** |
| LIMIT_BB3S | 6/15 | 40.0% | +0.51% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +7.03% | **+4.22%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.84% | **+1.57%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +3.12% | **+1.56%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +3.66% | **+1.28%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +4.00% | **+1.20%** |

## 2. $100 Live Portfolio

- 残高: **$109.14** / 初期 $100.00 (+9.14%)
- 確定トレード: 123件 (TP 44 / SL 74 / EXP 5)
- 最新: US/USDT:USDT TP_HIT PnL +8.00% 残高後 $109.14
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$403.40** / 初期 $100.00 (+303.40%)
- 確定: 3172件 (Win 991 / Loss 1006 / Flat 1175) / skip 2499件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PROM/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $403.40

## 4. Robust Adaptive DryRun ($100)

- 残高: **$126.87** / 初期 $100.00 (+26.87%)
- 確定: 1071件 (Win 279 / Loss 219 / Flat 573) / skip 1450件
- 成長率目線: 平均log +0.000222 / 幾何平均 +0.022% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0703 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PROM/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $126.87

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.52** / 初期 $100.00 (+1.52%)
- 確定: 309件 (Win 105 / Loss 135 / Flat 69) / pending 4件 / skip 268件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000259 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PROM/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $101.52

## 6. Latest Market Context

- 更新: 2026-07-20T13:31:20.804807+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=64532.7
- Funnel: target 887 → liquid 145 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 94.9 >= 65=1, 4h RSI 74.9 >= 65=1, 4h RSI 67.7 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ACE/USDT:USDT | +83.83% | $24,921,706.73 |
| BANK/USDT:USDT | +69.29% | $122,613,560.08 |
| PROM/USDT:USDT | +56.83% | $5,145,012.47 |
| EVAA/USDT:USDT | +21.05% | $7,767,094.13 |
| B/USDT:USDT | +17.63% | $33,476,878.25 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VIRTUAL/USDT:USDT | below_1h_threshold | +2.35% | +2.50% |
| ANSEM/USDT:USDT | below_1h_threshold | +2.00% | +2.15% |
| PI/USDT:USDT | below_1h_threshold | +1.42% | +1.57% |
| BEAT/USDT:USDT | below_1h_threshold | +1.28% | +1.43% |
| CHZ/USDT:USDT | below_1h_threshold | +1.12% | +1.26% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
