# Decision Report

- generated_at: 2026-09-16T11:16:38.652015+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14671**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14671, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.04%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.04% | **-1.04%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +3.52% | **+0.88%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.48% | **+0.59%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.68% | **+2.41%** |
| LIMIT_BB3S_LONG | 4/8 | 50.0% | +3.72% | **+1.86%** |
| MARKET_LONG | 20/20 | 100.0% | +1.39% | **+1.39%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.82% | **+1.18%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.48% | **+0.81%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,088.03** / 初期 $100.00 (+988.03%)
- 確定: 5549件 (Win 1656 / Loss 1792 / Flat 2101) / skip 5683件
- 成長率目線: 平均log +0.000430 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LSK/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,088.03

## 4. Robust Adaptive DryRun ($100)

- 残高: **$228.17** / 初期 $100.00 (+128.17%)
- 確定: 3077件 (Win 844 / Loss 725 / Flat 1508) / skip 5005件
- 成長率目線: 平均log +0.000268 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0226 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $228.17

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.97** / 初期 $100.00 (+23.97%)
- 確定: 2954件 (Win 878 / Loss 1163 / Flat 913) / pending 2件 / skip 3190件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000151 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BR/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $123.97

## 6. Latest Market Context

- 更新: 2026-09-16T11:16:21.018111+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=75866.8
- Funnel: target 1058 → liquid 152 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +129.16% | $18,047,059.59 |
| BR/USDT:USDT | +83.09% | $19,906,998.59 |
| LSK/USDT:USDT | +59.59% | $24,236,070.95 |
| MARSCOIN/USDT:USDT | +15.03% | $1,788,016.03 |
| LONGXIA/USDT:USDT | +14.32% | $2,655,167.23 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MARSCOIN/USDT:USDT | below_1h_threshold | +3.01% | +3.10% |
| LONGXIA/USDT:USDT | below_1h_threshold | +2.06% | +2.15% |
| IOST/USDT:USDT | below_1h_threshold | +1.89% | +1.98% |
| MONAD/USDT:USDT | below_1h_threshold | +1.09% | +1.18% |
| HYPE/USDT:USDT | below_1h_threshold | +0.90% | +0.98% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
