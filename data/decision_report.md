# Decision Report

- generated_at: 2026-07-11T20:56:17.999492+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8549**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8549, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.59% | **-0.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +6.47% | **+1.29%** |
| LIMIT_BB3S | 2/15 | 13.3% | +8.00% | **+1.07%** |
| LIMIT_5PCT | 6/20 | 30.0% | +2.13% | **+0.64%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.64% | **+0.58%** |
| LIMIT_ATR | 9/20 | 45.0% | +0.69% | **+0.31%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.03% | **+1.32%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.51% | **+1.21%** |
| MARKET_LONG | 20/20 | 100.0% | +0.99% | **+0.99%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |

## 2. $100 Live Portfolio

- 残高: **$103.05** / 初期 $100.00 (+3.05%)
- 確定トレード: 85件 (TP 30 / SL 54 / EXP 1)
- 最新: CASHCAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.05
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$322.71** / 初期 $100.00 (+222.71%)
- 確定: 2737件 (Win 865 / Loss 916 / Flat 956) / skip 2373件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CASHCAT/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $322.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.11** / 初期 $100.00 (+5.11%)
- 確定: 643件 (Win 152 / Loss 159 / Flat 332) / skip 1317件
- 成長率目線: 平均log +0.000078 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0456 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $105.11

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.95** / 初期 $100.00 (-0.05%)
- 確定: 16件 (Win 7 / Loss 9 / Flat 0) / pending 4件 / skip 1件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000180 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CASHCAT/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $99.95

## 6. Latest Market Context

- 更新: 2026-07-11T20:56:08.132031+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=64364.6
- Funnel: target 863 → liquid 141 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.5 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SXT/USDT:USDT | +30.39% | $8,688,499.82 |
| CASHCAT/USDT:USDT | +16.86% | $1,722,241.31 |
| TAC/USDT:USDT | +12.86% | $2,681,340.18 |
| B/USDT:USDT | +10.07% | $47,968,204.52 |
| EVAA/USDT:USDT | +9.08% | $27,201,124.97 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EVAA/USDT:USDT | below_1h_threshold | +3.21% | +3.05% |
| SXT/USDT:USDT | below_1h_threshold | +3.06% | +2.90% |
| US/USDT:USDT | below_1h_threshold | +2.08% | +1.92% |
| RAVE/USDT:USDT | below_1h_threshold | +1.77% | +1.61% |
| XPL/USDT:USDT | below_1h_threshold | +1.73% | +1.57% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
