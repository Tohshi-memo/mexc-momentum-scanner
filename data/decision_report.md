# Decision Report

- generated_at: 2026-09-11T16:01:27.481833+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14234**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.24% / filled 20/20。**
- 全期間 MARKET基準: n=14234, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.24% | **+0.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_BB3S | 3/15 | 20.0% | +1.66% | **+0.33%** |
| LIMIT_5PCT | 6/20 | 30.0% | +1.02% | **+0.31%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.85% | **+0.26%** |
| MARKET | 20/20 | 100.0% | +0.24% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +3.03% | **+2.42%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.12% | **+0.50%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +0.34% | **+0.19%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.37% | **+0.17%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.31% | **+0.12%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 209件 (TP 78 / SL 126 / EXP 5)
- 最新: RIVER/USDT:USDT SL_HIT PnL -3.59% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,063.05** / 初期 $100.00 (+963.05%)
- 確定: 5393件 (Win 1623 / Loss 1746 / Flat 2024) / skip 5402件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CNPY/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $1,063.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$205.62** / 初期 $100.00 (+105.62%)
- 確定: 2811件 (Win 770 / Loss 654 / Flat 1387) / skip 4834件
- 成長率目線: 平均log +0.000256 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0011 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CNPY/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $205.62

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.27** / 初期 $100.00 (+23.27%)
- 確定: 2730件 (Win 807 / Loss 1046 / Flat 877) / pending 5件 / skip 2975件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000208 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $123.27

## 6. Latest Market Context

- 更新: 2026-09-11T16:01:14.847620+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.24% price=77877.5
- Funnel: target 1067 → liquid 160 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STORJ/USDT:USDT | +1.74% | $5,559,950.75 |
| RIVER/USDT:USDT | +1.62% | $2,058,270.36 |
| USELESS/USDT:USDT | +1.22% | $10,386,420.33 |
| MARSCOIN/USDT:USDT | +1.10% | $3,480,232.27 |
| MET/USDT:USDT | +1.02% | $1,545,073.43 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STORJ/USDT:USDT | below_1h_threshold | +1.82% | +1.58% |
| RIVER/USDT:USDT | below_1h_threshold | +1.63% | +1.39% |
| USELESS/USDT:USDT | below_1h_threshold | +1.33% | +1.08% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +1.08% | +0.84% |
| MET/USDT:USDT | below_1h_threshold | +1.02% | +0.78% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
