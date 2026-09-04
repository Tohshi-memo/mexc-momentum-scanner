# Decision Report

- generated_at: 2026-09-04T00:16:18.772155+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13558**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.53% / filled 20/20。**
- 全期間 MARKET基準: n=13558, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.53%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.53% | **+0.53%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 15/20 | 75.0% | +1.71% | **+1.28%** |
| LIMIT_3PCT | 14/20 | 70.0% | +1.38% | **+0.96%** |
| LIMIT_BB3S | 3/17 | 17.6% | +5.41% | **+0.96%** |
| LIMIT_5PCT | 10/20 | 50.0% | +1.66% | **+0.83%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.91% | **+0.73%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.57% | **+0.54%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| MARKET_LONG | 20/20 | 100.0% | +0.07% | **+0.07%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 199件 (TP 74 / SL 120 / EXP 5)
- 最新: MARSCOIN/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$859.66** / 初期 $100.00 (+759.66%)
- 確定: 5008件 (Win 1516 / Loss 1644 / Flat 1848) / skip 5111件
- 成長率目線: 平均log +0.000430 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BONER/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.36% 残高後 $859.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$184.99** / 初期 $100.00 (+84.99%)
- 確定: 2378件 (Win 674 / Loss 576 / Flat 1128) / skip 4591件
- 成長率目線: 平均log +0.000259 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0211 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $184.99

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.37** / 初期 $100.00 (+17.37%)
- 確定: 2220件 (Win 662 / Loss 869 / Flat 689) / pending 5件 / skip 2808件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000272 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $117.37

## 6. Latest Market Context

- 更新: 2026-09-04T00:16:09.149307+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=81267.0
- Funnel: target 1046 → liquid 167 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HNT/USDT:USDT | +32.95% | $9,000,468.23 |
| PONS/USDT:USDT | +19.73% | $8,794,123.51 |
| AKE/USDT:USDT | +12.55% | $26,336,362.68 |
| PROM/USDT:USDT | +9.04% | $3,646,315.90 |
| BASECAT/USDT:USDT | +8.78% | $1,790,826.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTR/USDT:USDT | below_1h_threshold | +3.88% | +3.84% |
| BASECAT/USDT:USDT | below_1h_threshold | +3.48% | +3.44% |
| CAKE/USDT:USDT | below_1h_threshold | +1.72% | +1.68% |
| PONS/USDT:USDT | below_1h_threshold | +1.62% | +1.58% |
| UNI/USDT:USDT | below_1h_threshold | +1.33% | +1.28% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
