# Decision Report

- generated_at: 2026-08-29T16:21:31.705760+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12952**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12952, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.41%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.41% | **-0.41%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +1.89% | **+0.57%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_3PCT | 17/20 | 85.0% | +0.25% | **+0.21%** |
| LIMIT_FIB1272 | 11/20 | 55.0% | +0.36% | **+0.20%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.40% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.38% | **+2.02%** |
| MARKET_LONG | 20/20 | 100.0% | +1.80% | **+1.80%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +3.95% | **+1.38%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.75% | **+1.13%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.70% | **+0.81%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$737.28** / 初期 $100.00 (+637.28%)
- 確定: 4722件 (Win 1432 / Loss 1550 / Flat 1740) / skip 4791件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZKP/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $737.28

## 4. Robust Adaptive DryRun ($100)

- 残高: **$160.74** / 初期 $100.00 (+60.74%)
- 確定: 2036件 (Win 557 / Loss 488 / Flat 991) / skip 4327件
- 成長率目線: 平均log +0.000233 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0956 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ZKP/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $160.74

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.05** / 初期 $100.00 (+15.05%)
- 確定: 2037件 (Win 597 / Loss 794 / Flat 646) / pending 0件 / skip 2385件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000123 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $115.05

## 6. Latest Market Context

- 更新: 2026-08-29T16:21:19.855037+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.22% price=77992.5
- Funnel: target 1023 → liquid 136 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.9 >= 65=1, 4h RSI 66.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PROM/USDT:USDT | +12.28% | $3,347,613.73 |
| OPG/USDT:USDT | +5.86% | $1,038,135.28 |
| TAC/USDT:USDT | +2.02% | $1,045,214.99 |
| EDEN/USDT:USDT | +2.00% | $2,200,001.02 |
| LIGHT/USDT:USDT | +1.85% | $4,600,451.34 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAC/USDT:USDT | below_1h_threshold | +2.02% | +1.81% |
| EDEN/USDT:USDT | below_1h_threshold | +2.01% | +1.79% |
| LIGHT/USDT:USDT | below_1h_threshold | +1.95% | +1.73% |
| VVV/USDT:USDT | below_1h_threshold | +1.81% | +1.60% |
| DASH/USDT:USDT | below_1h_threshold | +1.60% | +1.39% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
