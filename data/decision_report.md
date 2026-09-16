# Decision Report

- generated_at: 2026-09-16T11:36:40.858746+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14674**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14674, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-2.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.24% | **-2.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 7/20 | 35.0% | +2.34% | **+0.82%** |
| LIMIT_5PCT | 11/20 | 55.0% | +0.88% | **+0.49%** |
| LIMIT_6PCT | 8/20 | 40.0% | +1.18% | **+0.47%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +1.64% | **+0.33%** |
| LIMIT_9PCT | 4/20 | 20.0% | +1.15% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.96% | **+2.81%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +3.02% | **+1.81%** |
| MARKET_LONG | 20/20 | 100.0% | +1.59% | **+1.59%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.26% | **+1.58%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +3.63% | **+1.45%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,087.95** / 初期 $100.00 (+987.95%)
- 確定: 5552件 (Win 1657 / Loss 1794 / Flat 2101) / skip 5683件
- 成長率目線: 平均log +0.000430 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BULLA/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $1,087.95

## 4. Robust Adaptive DryRun ($100)

- 残高: **$229.10** / 初期 $100.00 (+129.10%)
- 確定: 3080件 (Win 846 / Loss 726 / Flat 1508) / skip 5005件
- 成長率目線: 平均log +0.000269 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0418 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $229.10

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.97** / 初期 $100.00 (+23.97%)
- 確定: 2954件 (Win 878 / Loss 1163 / Flat 913) / pending 2件 / skip 3193件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000139 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BR/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $123.97

## 6. Latest Market Context

- 更新: 2026-09-16T11:36:24.523827+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=76003.4
- Funnel: target 1058 → liquid 152 → pre 50 → checked 50 → surge 4 → strict 2
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.2 >= 65=1, 4h RSI 81.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +129.65% | $18,627,232.42 |
| BR/USDT:USDT | +93.70% | $22,011,929.92 |
| LSK/USDT:USDT | +60.70% | $24,958,014.23 |
| BULLA/USDT:USDT | +31.56% | $1,334,351.04 |
| USELESS/USDT:USDT | +14.56% | $7,632,303.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| 4/USDT:USDT | below_1h_threshold | +3.73% | +3.64% |
| IOST/USDT:USDT | below_1h_threshold | +3.56% | +3.47% |
| HYPE/USDT:USDT | below_1h_threshold | +1.96% | +1.87% |
| ARB/USDT:USDT | below_1h_threshold | +1.91% | +1.82% |
| LONGXIA/USDT:USDT | below_1h_threshold | +1.87% | +1.78% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
