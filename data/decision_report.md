# Decision Report

- generated_at: 2026-09-20T07:06:15.281332+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15149**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.34% / filled 20/20。**
- 全期間 MARKET基準: n=15149, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.34% | **+1.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.91% | **+1.72%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.87% | **+1.40%** |
| MARKET | 20/20 | 100.0% | +1.34% | **+1.34%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.32% | **+0.86%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +3.86% | **+0.96%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +5.93% | **+0.89%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +1.10% | **+0.66%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.35% | **+0.17%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,199.19** / 初期 $100.00 (+1099.19%)
- 確定: 5675件 (Win 1700 / Loss 1834 / Flat 2141) / skip 6035件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: G/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $1,199.19

## 4. Robust Adaptive DryRun ($100)

- 残高: **$248.00** / 初期 $100.00 (+148.00%)
- 確定: 3262件 (Win 904 / Loss 762 / Flat 1596) / skip 5298件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0232 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: G/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $248.00

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.37** / 初期 $100.00 (+21.37%)
- 確定: 2978件 (Win 880 / Loss 1179 / Flat 919) / pending 0件 / skip 3644件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000233 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $121.37

## 6. Latest Market Context

- 更新: 2026-09-20T07:06:04.814984+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=80276.3
- Funnel: target 1050 → liquid 147 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CELR/USDT:USDT | +94.20% | $5,217,689.40 |
| G/USDT:USDT | +34.61% | $13,015,105.09 |
| OFC/USDT:USDT | +26.82% | $2,365,536.85 |
| ONE/USDT:USDT | +26.63% | $48,425,502.91 |
| EVAA/USDT:USDT | +15.49% | $1,716,116.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +1.92% | +1.92% |
| EVAA/USDT:USDT | below_1h_threshold | +1.52% | +1.53% |
| 4STOCK/USDT:USDT | below_1h_threshold | +0.94% | +0.94% |
| AIN/USDT:USDT | below_1h_threshold | +0.81% | +0.82% |
| HBAR/USDT:USDT | below_1h_threshold | +0.77% | +0.77% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
