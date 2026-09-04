# Decision Report

- generated_at: 2026-09-04T05:51:21.040326+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13586**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.29% / filled 20/20。**
- 全期間 MARKET基準: n=13586, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.29%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.29% | **+1.29%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.29% | **+1.29%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.31% | **+1.25%** |
| LIMIT_2PCT | 17/20 | 85.0% | +1.41% | **+1.20%** |
| LIMIT_3PCT | 14/20 | 70.0% | +1.70% | **+1.19%** |
| LIMIT_ATR | 14/20 | 70.0% | +1.48% | **+1.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.00% | **+0.40%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.06% | **+0.02%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | -0.04% | **-0.03%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 199件 (TP 74 / SL 120 / EXP 5)
- 最新: MARSCOIN/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$859.66** / 初期 $100.00 (+759.66%)
- 確定: 5009件 (Win 1516 / Loss 1644 / Flat 1849) / skip 5138件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASECAT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $859.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$185.77** / 初期 $100.00 (+85.77%)
- 確定: 2402件 (Win 680 / Loss 576 / Flat 1146) / skip 4595件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0294 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $185.77

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.18** / 初期 $100.00 (+16.18%)
- 確定: 2239件 (Win 666 / Loss 877 / Flat 696) / pending 4件 / skip 2814件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000143 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.18

## 6. Latest Market Context

- 更新: 2026-09-04T05:51:13.239671+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.25% price=80840.1
- Funnel: target 1048 → liquid 165 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HNT/USDT:USDT | +25.14% | $12,355,757.66 |
| TRIA/USDT:USDT | +22.27% | $2,930,747.34 |
| USELESS/USDT:USDT | +19.99% | $31,174,451.38 |
| PROM/USDT:USDT | +16.63% | $2,606,694.82 |
| MARSCOIN/USDT:USDT | +12.88% | $9,843,111.57 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MARSCOIN/USDT:USDT | below_1h_threshold | +4.42% | +4.67% |
| ZEST/USDT:USDT | below_1h_threshold | +3.32% | +3.57% |
| TRIA/USDT:USDT | below_1h_threshold | +3.02% | +3.27% |
| HNT/USDT:USDT | below_1h_threshold | +1.84% | +2.09% |
| USELESS/USDT:USDT | below_1h_threshold | +1.75% | +2.00% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
