# Decision Report

- generated_at: 2026-07-11T19:51:07.933442+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8547**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8547, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.16% | **-0.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 4/4 | 100.0% | +3.28% | **+3.28%** |
| LIMIT_6PCT | 4/20 | 20.0% | +6.47% | **+1.29%** |
| LIMIT_BB3S | 2/15 | 13.3% | +8.00% | **+1.07%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.79% | **+0.67%** |
| LIMIT_5PCT | 5/20 | 25.0% | +2.36% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.25% | **+0.81%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.94% | **+0.75%** |
| MARKET_LONG | 20/20 | 100.0% | +0.59% | **+0.59%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +0.60% | **+0.18%** |

## 2. $100 Live Portfolio

- 残高: **$103.05** / 初期 $100.00 (+3.05%)
- 確定トレード: 85件 (TP 30 / SL 54 / EXP 1)
- 最新: CASHCAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.05
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$321.10** / 初期 $100.00 (+221.10%)
- 確定: 2735件 (Win 864 / Loss 916 / Flat 955) / skip 2373件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SXT/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $321.10

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.11** / 初期 $100.00 (+5.11%)
- 確定: 643件 (Win 152 / Loss 159 / Flat 332) / skip 1315件
- 成長率目線: 平均log +0.000078 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0475 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $105.11

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.44** / 初期 $100.00 (-0.56%)
- 確定: 14件 (Win 5 / Loss 9 / Flat 0) / pending 3件 / skip 1件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000200 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SXT/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $99.44

## 6. Latest Market Context

- 更新: 2026-07-11T19:51:02.005426+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=64238.6
- Funnel: target 863 → liquid 142 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SXT/USDT:USDT | +29.28% | $6,332,531.04 |
| B/USDT:USDT | +12.98% | $48,225,681.70 |
| CASHCAT/USDT:USDT | +11.38% | $1,623,390.82 |
| CLO/USDT:USDT | +8.72% | $1,385,327.14 |
| BSB/USDT:USDT | +6.12% | $1,887,126.22 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CASHCAT/USDT:USDT | below_1h_threshold | +3.71% | +3.80% |
| CLO/USDT:USDT | below_1h_threshold | +3.45% | +3.54% |
| VANRY/USDT:USDT | below_1h_threshold | +2.44% | +2.53% |
| XPIN/USDT:USDT | below_1h_threshold | +1.79% | +1.89% |
| MYX/USDT:USDT | below_1h_threshold | +1.73% | +1.82% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
