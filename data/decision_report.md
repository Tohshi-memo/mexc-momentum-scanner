# Decision Report

- generated_at: 2026-09-04T18:26:29.193728+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13657**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13657, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.44%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.44% | **-1.44%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +1.96% | **+0.69%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.92% | **+0.67%** |
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.31% | **+0.22%** |
| LIMIT_2PCT | 19/20 | 95.0% | +0.08% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.71% | **+1.76%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.86% | **+1.67%** |
| LIMIT_BB3S_LONG | 6/8 | 75.0% | +2.05% | **+1.53%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.47% | **+1.36%** |
| MARKET_LONG | 20/20 | 100.0% | +1.04% | **+1.04%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 201件 (TP 75 / SL 121 / EXP 5)
- 最新: UAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$859.66** / 初期 $100.00 (+759.66%)
- 確定: 5011件 (Win 1516 / Loss 1644 / Flat 1851) / skip 5207件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASECAT/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $859.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$185.38** / 初期 $100.00 (+85.38%)
- 確定: 2421件 (Win 682 / Loss 577 / Flat 1162) / skip 4647件
- 成長率目線: 平均log +0.000255 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0377 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: 4/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $185.38

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.58** / 初期 $100.00 (+17.58%)
- 確定: 2296件 (Win 681 / Loss 881 / Flat 734) / pending 4件 / skip 2831件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000211 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $117.58

## 6. Latest Market Context

- 更新: 2026-09-04T18:26:17.235695+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=79545.0
- Funnel: target 1050 → liquid 162 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| 4/USDT:USDT | +37.24% | $2,681,427.81 |
| MARSCOIN/USDT:USDT | +20.03% | $7,457,754.09 |
| USELESS/USDT:USDT | +9.37% | $43,855,654.26 |
| SKR/USDT:USDT | +8.38% | $6,828,977.08 |
| UAI/USDT:USDT | +7.23% | $6,015,939.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| 4/USDT:USDT | below_1h_threshold | +3.31% | +3.17% |
| USELESS/USDT:USDT | below_1h_threshold | +2.77% | +2.63% |
| LIT/USDT:USDT | below_1h_threshold | +2.34% | +2.20% |
| UAI/USDT:USDT | below_1h_threshold | +2.23% | +2.09% |
| MUBARAK/USDT:USDT | below_1h_threshold | +2.04% | +1.89% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
