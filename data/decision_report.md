# Decision Report

- generated_at: 2026-07-31T06:21:14.818373+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9968**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9968, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.99%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.99% | **-0.99%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 4/20 | 20.0% | +3.83% | **+0.77%** |
| LIMIT_8PCT | 4/20 | 20.0% | +3.61% | **+0.72%** |
| LIMIT_7PCT | 6/20 | 30.0% | +2.06% | **+0.62%** |
| LIMIT_10PCT | 3/20 | 15.0% | +3.57% | **+0.54%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.30% | **+0.52%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.87% | **+1.69%** |
| MARKET_LONG | 20/20 | 100.0% | +1.52% | **+1.52%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.17% | **+0.82%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +0.71% | **+0.35%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.53% | **+0.32%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$555.03** / 初期 $100.00 (+455.03%)
- 確定: 3559件 (Win 1137 / Loss 1159 / Flat 1263) / skip 2970件
- 成長率目線: 平均log +0.000482 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZHIPUSTOCK/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $555.03

## 4. Robust Adaptive DryRun ($100)

- 残高: **$141.99** / 初期 $100.00 (+41.99%)
- 確定: 1262件 (Win 355 / Loss 289 / Flat 618) / skip 2117件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1724 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ZHIPUSTOCK/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $141.99

## 5. Causal Adaptive DryRun ($100)

- 残高: **$110.57** / 初期 $100.00 (+10.57%)
- 確定: 805件 (Win 262 / Loss 320 / Flat 223) / pending 2件 / skip 634件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000546 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ARMSTOCK/USDT:USDT `MARKET` EXPIRED account -0.04% 残高後 $110.57

## 6. Latest Market Context

- 更新: 2026-07-31T06:21:07.735721+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=64361.7
- Funnel: target 920 → liquid 172 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KOMA/USDT:USDT | +52.89% | $9,827,660.53 |
| MMT/USDT:USDT | +36.76% | $11,605,584.11 |
| AXTISTOCK/USDT:USDT | +32.92% | $4,314,979.83 |
| SNXX/USDT:USDT | +23.30% | $12,699,719.56 |
| BULLA/USDT:USDT | +20.62% | $1,181,096.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +3.80% | +3.75% |
| GIGGLE/USDT:USDT | below_1h_threshold | +3.53% | +3.49% |
| KORU/USDT:USDT | below_1h_threshold | +3.16% | +3.11% |
| CAP/USDT:USDT | below_1h_threshold | +3.11% | +3.07% |
| SNXX/USDT:USDT | below_1h_threshold | +3.02% | +2.98% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
