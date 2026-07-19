# Decision Report

- generated_at: 2026-07-19T06:11:09.570241+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9004**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9004, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.59% | **-0.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.50% | **+0.15%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.46% | **+2.34%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.49% | **+1.75%** |
| MARKET_LONG | 20/20 | 100.0% | +1.56% | **+1.56%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.07% | **+0.53%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +0.20% | **+0.13%** |

## 2. $100 Live Portfolio

- 残高: **$110.80** / 初期 $100.00 (+10.80%)
- 確定トレード: 117件 (TP 43 / SL 69 / EXP 5)
- 最新: SKYAI/USDT:USDT EXPIRED PnL +0.79% 残高後 $110.80
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$381.11** / 初期 $100.00 (+281.11%)
- 確定: 3066件 (Win 957 / Loss 977 / Flat 1132) / skip 2499件
- 成長率目線: 平均log +0.000436 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TLM/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $381.11

## 4. Robust Adaptive DryRun ($100)

- 残高: **$124.20** / 初期 $100.00 (+24.20%)
- 確定: 965件 (Win 245 / Loss 197 / Flat 523) / skip 1450件
- 成長率目線: 平均log +0.000225 / 幾何平均 +0.022% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2300 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TLM/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $124.20

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.81** / 初期 $100.00 (-0.19%)
- 確定: 207件 (Win 66 / Loss 109 / Flat 32) / pending 5件 / skip 264件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000555 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TLM/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $99.81

## 6. Latest Market Context

- 更新: 2026-07-19T06:11:03.424239+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=64670.1
- Funnel: target 885 → liquid 122 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +118.63% | $39,251,895.40 |
| BANK/USDT:USDT | +45.25% | $17,471,496.48 |
| B/USDT:USDT | +32.65% | $37,271,972.19 |
| TAG/USDT:USDT | +29.36% | $1,489,583.02 |
| TLM/USDT:USDT | +25.83% | $3,542,384.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| B/USDT:USDT | below_1h_threshold | +2.91% | +2.95% |
| TAG/USDT:USDT | below_1h_threshold | +2.58% | +2.62% |
| ANSEM/USDT:USDT | below_1h_threshold | +1.57% | +1.60% |
| BANK/USDT:USDT | below_1h_threshold | +1.42% | +1.46% |
| AKE/USDT:USDT | below_1h_threshold | +1.41% | +1.45% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
