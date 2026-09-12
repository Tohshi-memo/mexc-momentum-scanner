# Decision Report

- generated_at: 2026-09-12T13:11:25.343348+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14309**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14309, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.34% | **-0.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.98% | **+0.29%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.22% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +2.09% | **+1.46%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.70% | **+1.27%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.36% | **+0.75%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +0.92% | **+0.37%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.48% | **+0.35%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,080.43** / 初期 $100.00 (+980.43%)
- 確定: 5428件 (Win 1635 / Loss 1760 / Flat 2033) / skip 5442件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LONGXIA/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $1,080.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$209.84** / 初期 $100.00 (+109.84%)
- 確定: 2834件 (Win 780 / Loss 656 / Flat 1398) / skip 4886件
- 成長率目線: 平均log +0.000262 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0480 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $209.84

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.33** / 初期 $100.00 (+23.33%)
- 確定: 2767件 (Win 818 / Loss 1064 / Flat 885) / pending 0件 / skip 3012件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000327 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SOPH/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $123.33

## 6. Latest Market Context

- 更新: 2026-09-12T13:11:14.647869+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=77318.1
- Funnel: target 1068 → liquid 142 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LONGXIA/USDT:USDT | +140.96% | $6,563,375.31 |
| LSK/USDT:USDT | +90.43% | $22,033,575.48 |
| STORJ/USDT:USDT | +48.71% | $25,703,942.04 |
| LAB/USDT:USDT | +23.97% | $17,874,475.07 |
| VTHO/USDT:USDT | +20.44% | $2,565,211.83 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LSK/USDT:USDT | below_1h_threshold | +3.31% | +3.28% |
| PONS/USDT:USDT | below_1h_threshold | +1.38% | +1.35% |
| VTHO/USDT:USDT | below_1h_threshold | +1.34% | +1.32% |
| LONGXIA/USDT:USDT | below_1h_threshold | +0.90% | +0.87% |
| EGLD/USDT:USDT | below_1h_threshold | +0.46% | +0.44% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
