# Decision Report

- generated_at: 2026-09-04T05:26:35.732617+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13585**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.69% / filled 20/20。**
- 全期間 MARKET基準: n=13585, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.69%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.69% | **+0.69%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 14/20 | 70.0% | +1.06% | **+0.74%** |
| MARKET | 20/20 | 100.0% | +0.69% | **+0.69%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.68% | **+0.65%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.87% | **+0.61%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.70% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +0.23% | **+0.10%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.22% | **+0.08%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 199件 (TP 74 / SL 120 / EXP 5)
- 最新: MARSCOIN/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$859.66** / 初期 $100.00 (+759.66%)
- 確定: 5009件 (Win 1516 / Loss 1644 / Flat 1849) / skip 5137件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASECAT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $859.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$185.77** / 初期 $100.00 (+85.77%)
- 確定: 2401件 (Win 680 / Loss 576 / Flat 1145) / skip 4595件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0468 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: USELESS/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $185.77

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.39** / 初期 $100.00 (+16.39%)
- 確定: 2238件 (Win 666 / Loss 876 / Flat 696) / pending 4件 / skip 2814件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000144 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: USELESS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.39

## 6. Latest Market Context

- 更新: 2026-09-04T05:26:24.016336+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=81026.3
- Funnel: target 1046 → liquid 164 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HNT/USDT:USDT | +25.72% | $12,117,806.55 |
| TRIA/USDT:USDT | +22.06% | $2,702,505.39 |
| USELESS/USDT:USDT | +20.87% | $30,742,698.21 |
| PROM/USDT:USDT | +15.79% | $2,566,522.05 |
| BASECAT/USDT:USDT | +12.02% | $2,191,216.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEST/USDT:USDT | below_1h_threshold | +2.88% | +2.90% |
| TRIA/USDT:USDT | below_1h_threshold | +2.74% | +2.75% |
| USELESS/USDT:USDT | below_1h_threshold | +2.40% | +2.41% |
| HNT/USDT:USDT | below_1h_threshold | +2.32% | +2.33% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +1.75% | +1.76% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
