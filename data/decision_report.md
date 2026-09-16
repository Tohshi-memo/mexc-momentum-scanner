# Decision Report

- generated_at: 2026-09-16T11:11:34.283424+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14670**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14670, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.64%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.64% | **-1.64%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +2.27% | **+0.68%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.87% | **+0.39%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.94% | **+0.28%** |
| LIMIT_9PCT | 4/20 | 20.0% | +1.15% | **+0.23%** |
| LIMIT_8PCT | 4/20 | 20.0% | +0.93% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +3.34% | **+3.01%** |
| MARKET_LONG | 20/20 | 100.0% | +1.99% | **+1.99%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.75% | **+1.78%** |
| LIMIT_BB3S_LONG | 4/9 | 44.4% | +3.72% | **+1.65%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.57% | **+1.41%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,093.50** / 初期 $100.00 (+993.50%)
- 確定: 5548件 (Win 1656 / Loss 1791 / Flat 2101) / skip 5683件
- 成長率目線: 平均log +0.000431 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LSK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $1,093.50

## 4. Robust Adaptive DryRun ($100)

- 残高: **$228.97** / 初期 $100.00 (+128.97%)
- 確定: 3076件 (Win 844 / Loss 724 / Flat 1508) / skip 5005件
- 成長率目線: 平均log +0.000269 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0226 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $228.97

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.97** / 初期 $100.00 (+23.97%)
- 確定: 2954件 (Win 878 / Loss 1163 / Flat 913) / pending 2件 / skip 3188件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000151 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BR/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $123.97

## 6. Latest Market Context

- 更新: 2026-09-16T11:11:14.914523+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=75911.8
- Funnel: target 1058 → liquid 151 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +112.74% | $17,720,537.23 |
| BR/USDT:USDT | +83.03% | $19,154,787.89 |
| LSK/USDT:USDT | +68.41% | $23,830,681.15 |
| USELESS/USDT:USDT | +14.01% | $7,538,769.33 |
| LONGXIA/USDT:USDT | +13.33% | $2,652,085.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IOST/USDT:USDT | below_1h_threshold | +1.96% | +1.99% |
| HYPE/USDT:USDT | below_1h_threshold | +1.40% | +1.43% |
| LONGXIA/USDT:USDT | below_1h_threshold | +0.91% | +0.94% |
| CNPY/USDT:USDT | below_1h_threshold | +0.71% | +0.74% |
| SYN/USDT:USDT | below_1h_threshold | +0.46% | +0.49% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
