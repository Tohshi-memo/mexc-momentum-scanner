# Decision Report

- generated_at: 2026-09-23T11:46:22.277339+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15429**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.32% / filled 20/20。**
- 全期間 MARKET基準: n=15429, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.32% | **+1.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/13 | 46.2% | +4.38% | **+2.02%** |
| LIMIT_3PCT | 15/20 | 75.0% | +2.60% | **+1.95%** |
| LIMIT_5PCT | 7/20 | 35.0% | +5.28% | **+1.85%** |
| LIMIT_ATR | 16/20 | 80.0% | +2.14% | **+1.71%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.88% | **+1.50%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 18/20 | 90.0% | +1.48% | **+1.33%** |
| LIMIT_3PCT_LONG | 18/20 | 90.0% | +1.23% | **+1.10%** |
| LIMIT_5PCT_LONG | 14/20 | 70.0% | +0.81% | **+0.57%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +0.51% | **+0.31%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +0.38% | **+0.27%** |

## 2. $100 Live Portfolio

- 残高: **$120.32** / 初期 $100.00 (+20.32%)
- 確定トレード: 217件 (TP 79 / SL 133 / EXP 5)
- 最新: LONGXIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.32
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,197.79** / 初期 $100.00 (+1097.79%)
- 確定: 5895件 (Win 1739 / Loss 1890 / Flat 2266) / skip 6095件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BR/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $1,197.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$249.06** / 初期 $100.00 (+149.06%)
- 確定: 3376件 (Win 931 / Loss 789 / Flat 1656) / skip 5464件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0416 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TAKE/USDT:USDT `LIMIT_5PCT` TP_HIT account +0.69% 残高後 $249.06

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.57** / 初期 $100.00 (+21.57%)
- 確定: 3136件 (Win 923 / Loss 1234 / Flat 979) / pending 0件 / skip 3765件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000206 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: GRASS/USDT:USDT `MARKET` EXPIRED account -0.14% 残高後 $121.57

## 6. Latest Market Context

- 更新: 2026-09-23T11:46:11.000296+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.44% price=85497.5
- Funnel: target 1061 → liquid 191 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KIMISTOCK/USDT:USDT | +784.71% | $1,450,095.33 |
| TAKE/USDT:USDT | +229.60% | $6,166,845.93 |
| SHROOM/USDT:USDT | +62.59% | $1,395,628.79 |
| MET/USDT:USDT | +37.32% | $1,632,765.91 |
| ALLO/USDT:USDT | +28.30% | $4,322,044.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ALLO/USDT:USDT | below_1h_threshold | +4.60% | +5.04% |
| TAKE/USDT:USDT | below_1h_threshold | +1.96% | +2.41% |
| RAY/USDT:USDT | below_1h_threshold | +1.90% | +2.34% |
| SAGA/USDT:USDT | below_1h_threshold | +1.50% | +1.94% |
| COTI/USDT:USDT | below_1h_threshold | +1.23% | +1.68% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
