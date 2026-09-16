# Decision Report

- generated_at: 2026-09-16T14:01:25.936089+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14693**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14693, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.20% | **-1.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 5/20 | 25.0% | +8.00% | **+2.00%** |
| LIMIT_8PCT | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_9PCT | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.12% | **+0.53%** |
| LIMIT_7PCT | 6/20 | 30.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +3.48% | **+3.13%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +3.12% | **+2.97%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +3.15% | **+2.36%** |
| MARKET_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |
| LIMIT_BB3S_LONG | 5/9 | 55.6% | +2.63% | **+1.46%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,156.57** / 初期 $100.00 (+1056.57%)
- 確定: 5570件 (Win 1668 / Loss 1800 / Flat 2102) / skip 5684件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BR/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $1,156.57

## 4. Robust Adaptive DryRun ($100)

- 残高: **$239.01** / 初期 $100.00 (+139.01%)
- 確定: 3097件 (Win 857 / Loss 731 / Flat 1509) / skip 5007件
- 成長率目線: 平均log +0.000281 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1970 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BR/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $239.01

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.75** / 初期 $100.00 (+23.75%)
- 確定: 2955件 (Win 878 / Loss 1164 / Flat 913) / pending 1件 / skip 3208件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000410 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BTW/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $123.75

## 6. Latest Market Context

- 更新: 2026-09-16T14:01:15.773628+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=75578.7
- Funnel: target 1058 → liquid 153 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +114.70% | $24,330,917.25 |
| BR/USDT:USDT | +103.90% | $31,614,245.67 |
| LSK/USDT:USDT | +40.05% | $28,663,816.54 |
| USELESS/USDT:USDT | +16.34% | $7,854,161.18 |
| 4/USDT:USDT | +15.64% | $1,607,128.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +3.67% | +3.72% |
| ORCLSTOCK/USDT:USDT | below_1h_threshold | +3.43% | +3.47% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +2.13% | +2.17% |
| DELLSTOCK/USDT:USDT | below_1h_threshold | +1.93% | +1.98% |
| SOXL/USDT:USDT | below_1h_threshold | +1.62% | +1.67% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
