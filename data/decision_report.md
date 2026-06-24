# Decision Report

- generated_at: 2026-06-24T12:14:42.495758+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7474**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7474, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.82% | **+0.82%** |
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.89% | **+0.57%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.94% | **+0.42%** |
| MARKET_LONG | 20/20 | 100.0% | +0.40% | **+0.40%** |
| ASK_LONG | 20/20 | 100.0% | +0.31% | **+0.31%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +0.39% | **+0.06%** |

## 2. $100 Live Portfolio

- 残高: **$101.42** / 初期 $100.00 (+1.42%)
- 確定トレード: 33件 (TP 12 / SL 21 / EXP 0)
- 最新: O/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.42
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$230.80** / 初期 $100.00 (+130.80%)
- 確定: 2105件 (Win 623 / Loss 698 / Flat 784) / skip 1930件
- 成長率目線: 平均log +0.000397 / 幾何平均 +0.040% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SLX/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $230.80

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.88** / 初期 $100.00 (+6.88%)
- 確定: 337件 (Win 95 / Loss 91 / Flat 151) / skip 548件
- 成長率目線: 平均log +0.000197 / 幾何平均 +0.020% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0161 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SLX/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.88

## 5. Latest Market Context

- 更新: 2026-06-24T12:14:37.940810+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=62812.8
- Funnel: target 808 → liquid 157 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +44.62% | $17,508,757.90 |
| SLX/USDT:USDT | +38.63% | $5,657,800.69 |
| BAS/USDT:USDT | +34.53% | $1,525,163.12 |
| O/USDT:USDT | +24.57% | $4,219,978.88 |
| ID/USDT:USDT | +18.56% | $1,700,829.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SYN/USDT:USDT | below_1h_threshold | +3.31% | +3.43% |
| O/USDT:USDT | below_1h_threshold | +2.55% | +2.67% |
| LIGHT/USDT:USDT | below_1h_threshold | +1.86% | +1.98% |
| RAVE/USDT:USDT | below_1h_threshold | +1.68% | +1.79% |
| JTO/USDT:USDT | below_1h_threshold | +1.65% | +1.77% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
