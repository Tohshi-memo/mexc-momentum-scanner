# Decision Report

- generated_at: 2026-09-20T00:26:28.434790+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15112**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.76% / filled 20/20。**
- 全期間 MARKET基準: n=15112, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.76%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.76% | **+0.76%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.76% | **+0.76%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.65% | **+0.61%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.25% | **+0.44%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.88% | **+0.79%** |
| MARKET_LONG | 20/20 | 100.0% | +0.42% | **+0.42%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.45% | **+0.34%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.41% | **+0.26%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -0.89% | **-0.09%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,196.82** / 初期 $100.00 (+1096.82%)
- 確定: 5641件 (Win 1692 / Loss 1829 / Flat 2120) / skip 6032件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: G/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.12% 残高後 $1,196.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$244.76** / 初期 $100.00 (+144.76%)
- 確定: 3225件 (Win 894 / Loss 762 / Flat 1569) / skip 5298件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0221 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: G/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $244.76

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.58** / 初期 $100.00 (+21.58%)
- 確定: 2977件 (Win 880 / Loss 1178 / Flat 919) / pending 1件 / skip 3606件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000251 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CNPY/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $121.58

## 6. Latest Market Context

- 更新: 2026-09-20T00:26:15.001456+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=81236.5
- Funnel: target 1050 → liquid 141 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| OFC/USDT:USDT | +48.10% | $1,849,111.24 |
| CELR/USDT:USDT | +35.22% | $1,396,300.72 |
| ONE/USDT:USDT | +27.53% | $46,681,641.93 |
| BANK/USDT:USDT | +18.86% | $2,644,309.14 |
| PIEVERSE/USDT:USDT | +17.93% | $1,179,137.56 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PIEVERSE/USDT:USDT | below_1h_threshold | +3.74% | +3.72% |
| AVAX/USDT:USDT | below_1h_threshold | +3.55% | +3.54% |
| MYX/USDT:USDT | below_1h_threshold | +2.48% | +2.46% |
| TAG/USDT:USDT | below_1h_threshold | +2.05% | +2.03% |
| STRK/USDT:USDT | below_1h_threshold | +2.01% | +1.99% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
