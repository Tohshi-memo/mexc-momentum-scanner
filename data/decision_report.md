# Decision Report

- generated_at: 2026-08-01T10:11:13.045313+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10081**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.26% / filled 20/20。**
- 全期間 MARKET基準: n=10081, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.26%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.26% | **+1.26%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.26% | **+1.26%** |
| LIMIT_2PCT | 17/20 | 85.0% | +1.31% | **+1.12%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.20% | **+0.72%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.48% | **+0.41%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.50% | **+0.20%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +0.19% | **+0.11%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.17% | **+0.09%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$576.58** / 初期 $100.00 (+476.58%)
- 確定: 3628件 (Win 1158 / Loss 1189 / Flat 1281) / skip 3014件
- 成長率目線: 平均log +0.000483 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_FIB1272_LONG` TP_HIT account +1.00% 残高後 $576.58

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.81** / 初期 $100.00 (+40.81%)
- 確定: 1279件 (Win 359 / Loss 297 / Flat 623) / skip 2213件
- 成長率目線: 平均log +0.000268 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $140.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$111.30** / 初期 $100.00 (+11.30%)
- 確定: 892件 (Win 285 / Loss 352 / Flat 255) / pending 5件 / skip 656件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000034 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $111.30

## 6. Latest Market Context

- 更新: 2026-08-01T10:11:07.119658+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=62965.0
- Funnel: target 921 → liquid 147 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KOMA/USDT:USDT | +41.31% | $16,589,260.67 |
| JIMOTHY/USDT:USDT | +40.20% | $1,398,556.60 |
| BTW/USDT:USDT | +39.54% | $6,210,732.56 |
| TAKE/USDT:USDT | +29.46% | $1,049,064.08 |
| ICNT/USDT:USDT | +25.54% | $1,011,588.29 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SATS/USDT:USDT | below_1h_threshold | +3.14% | +3.23% |
| JIMOTHY/USDT:USDT | below_1h_threshold | +1.99% | +2.08% |
| MYX/USDT:USDT | below_1h_threshold | +1.21% | +1.30% |
| TAKE/USDT:USDT | below_1h_threshold | +1.12% | +1.21% |
| ICNT/USDT:USDT | below_1h_threshold | +1.02% | +1.11% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
