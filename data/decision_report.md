# Decision Report

- generated_at: 2026-09-11T22:36:24.542272+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14260**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14260, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.12% | **-0.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 17/20 | 85.0% | +0.73% | **+0.62%** |
| LIMIT_ATR | 16/20 | 80.0% | +0.61% | **+0.49%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +3.86% | **+1.16%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.34% | **+1.01%** |
| MARKET_LONG | 20/20 | 100.0% | +0.33% | **+0.33%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +0.84% | **+0.29%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,102.39** / 初期 $100.00 (+1002.39%)
- 確定: 5417件 (Win 1634 / Loss 1754 / Flat 2029) / skip 5404件
- 成長率目線: 平均log +0.000443 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HPQSTOCK/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $1,102.39

## 4. Robust Adaptive DryRun ($100)

- 残高: **$210.43** / 初期 $100.00 (+110.43%)
- 確定: 2830件 (Win 779 / Loss 655 / Flat 1396) / skip 4841件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1110 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: STORJ/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $210.43

## 5. Causal Adaptive DryRun ($100)

- 残高: **$124.22** / 初期 $100.00 (+24.22%)
- 確定: 2751件 (Win 815 / Loss 1054 / Flat 882) / pending 3件 / skip 2976件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000318 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: DELLSTOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $124.22

## 6. Latest Market Context

- 更新: 2026-09-11T22:36:14.092500+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=77044.9
- Funnel: target 1067 → liquid 160 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STORJ/USDT:USDT | +36.21% | $13,856,330.83 |
| LAB/USDT:USDT | +29.93% | $11,335,331.34 |
| BEAT/USDT:USDT | +15.71% | $11,050,350.11 |
| LSK/USDT:USDT | +13.83% | $3,096,244.73 |
| RIVER/USDT:USDT | +8.71% | $4,930,933.88 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +2.86% | +2.91% |
| RIVER/USDT:USDT | below_1h_threshold | +2.85% | +2.90% |
| 4/USDT:USDT | below_1h_threshold | +2.72% | +2.77% |
| LSK/USDT:USDT | below_1h_threshold | +2.60% | +2.64% |
| STONK/USDT:USDT | below_1h_threshold | +1.79% | +1.83% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
