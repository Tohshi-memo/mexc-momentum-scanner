# Decision Report

- generated_at: 2026-07-19T07:06:14.328094+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9007**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9007, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.16% | **-1.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.41% | **+0.10%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.79% | **+2.51%** |
| MARKET_LONG | 20/20 | 100.0% | +1.93% | **+1.93%** |
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +1.83% | **+1.83%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +2.25% | **+1.24%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +0.83% | **+0.33%** |

## 2. $100 Live Portfolio

- 残高: **$110.80** / 初期 $100.00 (+10.80%)
- 確定トレード: 117件 (TP 43 / SL 69 / EXP 5)
- 最新: SKYAI/USDT:USDT EXPIRED PnL +0.79% 残高後 $110.80
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$386.03** / 初期 $100.00 (+286.03%)
- 確定: 3069件 (Win 959 / Loss 977 / Flat 1133) / skip 2499件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $386.03

## 4. Robust Adaptive DryRun ($100)

- 残高: **$124.20** / 初期 $100.00 (+24.20%)
- 確定: 968件 (Win 245 / Loss 197 / Flat 526) / skip 1450件
- 成長率目線: 平均log +0.000224 / 幾何平均 +0.022% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2146 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $124.20

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.81** / 初期 $100.00 (-0.19%)
- 確定: 210件 (Win 66 / Loss 109 / Flat 35) / pending 4件 / skip 264件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000555 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $99.81

## 6. Latest Market Context

- 更新: 2026-07-19T07:06:05.931359+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=64677.3
- Funnel: target 885 → liquid 122 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +145.18% | $39,923,825.15 |
| BANK/USDT:USDT | +44.11% | $17,173,988.29 |
| B/USDT:USDT | +29.75% | $38,415,665.05 |
| TLM/USDT:USDT | +27.26% | $3,864,568.16 |
| TAG/USDT:USDT | +23.09% | $3,018,289.11 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +3.34% | +3.35% |
| BULLA/USDT:USDT | below_1h_threshold | +1.44% | +1.45% |
| KAITO/USDT:USDT | below_1h_threshold | +1.18% | +1.19% |
| TAG/USDT:USDT | below_1h_threshold | +0.68% | +0.69% |
| ALLO/USDT:USDT | below_1h_threshold | +0.65% | +0.65% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
