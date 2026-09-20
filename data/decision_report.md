# Decision Report

- generated_at: 2026-09-20T19:01:23.550186+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15206**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.38% / filled 20/20。**
- 全期間 MARKET基準: n=15206, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.38%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.38% | **+0.38%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 15/20 | 75.0% | +1.36% | **+1.02%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.94% | **+0.80%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.96% | **+0.69%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.98% | **+0.59%** |
| LIMIT_BB3S | 8/14 | 57.1% | +0.87% | **+0.50%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +3.86% | **+0.96%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +6.07% | **+0.91%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +5.83% | **+0.87%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.50% | **+0.60%** |
| MARKET_LONG | 20/20 | 100.0% | +0.31% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,173.63** / 初期 $100.00 (+1073.63%)
- 確定: 5717件 (Win 1705 / Loss 1845 / Flat 2167) / skip 6050件
- 成長率目線: 平均log +0.000431 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: OFC/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $1,173.63

## 4. Robust Adaptive DryRun ($100)

- 残高: **$247.68** / 初期 $100.00 (+147.68%)
- 確定: 3295件 (Win 911 / Loss 764 / Flat 1620) / skip 5322件
- 成長率目線: 平均log +0.000275 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0020 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AR/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $247.68

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.51** / 初期 $100.00 (+21.51%)
- 確定: 2992件 (Win 883 / Loss 1182 / Flat 927) / pending 5件 / skip 3687件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000241 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $121.51

## 6. Latest Market Context

- 更新: 2026-09-20T19:01:12.019014+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=81018.9
- Funnel: target 1050 → liquid 144 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LUNANEW/USDT:USDT | +17.80% | $1,915,999.47 |
| SAGA/USDT:USDT | +17.14% | $4,874,550.99 |
| AKE/USDT:USDT | +16.00% | $82,661,378.45 |
| NIL/USDT:USDT | +15.28% | $1,188,065.63 |
| STRK/USDT:USDT | +9.78% | $3,554,728.02 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LUNANEW/USDT:USDT | below_1h_threshold | +0.80% | +0.77% |
| SAGA/USDT:USDT | below_1h_threshold | +0.39% | +0.37% |
| RAY/USDT:USDT | below_1h_threshold | +0.30% | +0.27% |
| ONE/USDT:USDT | below_1h_threshold | +0.28% | +0.25% |
| B2/USDT:USDT | below_1h_threshold | +0.26% | +0.24% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
