# Decision Report

- generated_at: 2026-07-21T22:26:22.111255+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9216**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9216, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.09%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.09% | **-0.09%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +0.41% | **+0.12%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.10% | **+0.03%** |
| LIMIT_8PCT | 5/20 | 25.0% | +0.11% | **+0.03%** |
| MARKET | 20/20 | 100.0% | -0.09% | **-0.09%** |
| LIMIT_9PCT | 4/20 | 20.0% | -0.79% | **-0.16%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.65% | **+0.65%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.48% | **+0.41%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.71% | **+0.35%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.60% | **+0.27%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +0.62% | **+0.25%** |

## 2. $100 Live Portfolio

- 残高: **$104.85** / 初期 $100.00 (+4.85%)
- 確定トレード: 131件 (TP 44 / SL 82 / EXP 5)
- 最新: NIGHT/USDT:USDT SL_HIT PnL -4.00% 残高後 $104.85
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$419.29** / 初期 $100.00 (+319.29%)
- 確定: 3250件 (Win 1021 / Loss 1039 / Flat 1190) / skip 2527件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BNCSTOCK/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $419.29

## 4. Robust Adaptive DryRun ($100)

- 残高: **$131.28** / 初期 $100.00 (+31.28%)
- 確定: 1159件 (Win 312 / Loss 252 / Flat 595) / skip 1468件
- 成長率目線: 平均log +0.000235 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RIF/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $131.28

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.03** / 初期 $100.00 (+1.03%)
- 確定: 363件 (Win 123 / Loss 155 / Flat 85) / pending 5件 / skip 324件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `見送り` (no_strategy_passed_causal_filters) / causal_score n/a / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: FWDISTOCK/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $101.03

## 6. Latest Market Context

- 更新: 2026-07-21T22:26:14.026695+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.20% price=66219.5
- Funnel: target 885 → liquid 179 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.6 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SMCISTOCK/USDT:USDT | +19.50% | $3,107,588.70 |
| FWDISTOCK/USDT:USDT | +12.84% | $3,813,364.58 |
| SNXX/USDT:USDT | +10.20% | $1,729,933.03 |
| NIGHT/USDT:USDT | +8.29% | $6,975,914.88 |
| LAB/USDT:USDT | +8.16% | $6,969,878.09 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +2.44% | +2.64% |
| AKE/USDT:USDT | below_1h_threshold | +2.28% | +2.48% |
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +1.53% | +1.73% |
| BANK/USDT:USDT | below_1h_threshold | +1.33% | +1.53% |
| KORU/USDT:USDT | below_1h_threshold | +1.13% | +1.33% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
