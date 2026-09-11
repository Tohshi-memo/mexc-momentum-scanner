# Decision Report

- generated_at: 2026-09-11T16:26:22.990747+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14235**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.84% / filled 20/20。**
- 全期間 MARKET基準: n=14235, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.84%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.84% | **+0.84%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.84% | **+0.84%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_BB3S | 3/16 | 18.8% | +1.66% | **+0.31%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.37% | **+0.30%** |
| LIMIT_5PCT | 5/20 | 25.0% | +1.03% | **+0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +2.65% | **+1.99%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.61% | **+0.30%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.16% | **+0.07%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +0.02% | **+0.01%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 209件 (TP 78 / SL 126 / EXP 5)
- 最新: RIVER/USDT:USDT SL_HIT PnL -3.59% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,063.05** / 初期 $100.00 (+963.05%)
- 確定: 5393件 (Win 1623 / Loss 1746 / Flat 2024) / skip 5403件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CNPY/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $1,063.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$205.62** / 初期 $100.00 (+105.62%)
- 確定: 2811件 (Win 770 / Loss 654 / Flat 1387) / skip 4835件
- 成長率目線: 平均log +0.000256 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0009 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CNPY/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $205.62

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.06** / 初期 $100.00 (+23.06%)
- 確定: 2731件 (Win 807 / Loss 1047 / Flat 877) / pending 5件 / skip 2975件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000154 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $123.06

## 6. Latest Market Context

- 更新: 2026-09-11T16:26:10.817674+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=77602.3
- Funnel: target 1067 → liquid 160 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MET/USDT:USDT | +3.70% | $1,610,584.19 |
| LAB/USDT:USDT | +3.56% | $3,657,906.56 |
| STORJ/USDT:USDT | +3.49% | $5,821,972.19 |
| RIVER/USDT:USDT | +3.33% | $2,241,294.53 |
| BEAT/USDT:USDT | +1.73% | $7,474,430.09 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +3.84% | +3.95% |
| MET/USDT:USDT | below_1h_threshold | +3.70% | +3.82% |
| STORJ/USDT:USDT | below_1h_threshold | +3.50% | +3.61% |
| RIVER/USDT:USDT | below_1h_threshold | +3.42% | +3.53% |
| POL/USDT:USDT | below_1h_threshold | +1.72% | +1.83% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
