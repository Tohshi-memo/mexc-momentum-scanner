# Decision Report

- generated_at: 2026-08-01T17:16:14.524753+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10107**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.22% / filled 20/20。**
- 全期間 MARKET基準: n=10107, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.22%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.22% | **+0.22%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +4.32% | **+0.43%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.24% | **+0.23%** |
| MARKET | 20/20 | 100.0% | +0.22% | **+0.22%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.04% | **+0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.09% | **+1.04%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.28% | **+1.02%** |
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +0.93% | **+0.75%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +2.60% | **+0.52%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.35% | **+0.26%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$570.82** / 初期 $100.00 (+470.82%)
- 確定: 3638件 (Win 1158 / Loss 1191 / Flat 1289) / skip 3030件
- 成長率目線: 平均log +0.000479 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $570.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.81** / 初期 $100.00 (+40.81%)
- 確定: 1279件 (Win 359 / Loss 297 / Flat 623) / skip 2239件
- 成長率目線: 平均log +0.000268 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $140.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$111.24** / 初期 $100.00 (+11.24%)
- 確定: 916件 (Win 290 / Loss 359 / Flat 267) / pending 3件 / skip 659件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000072 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $111.24

## 6. Latest Market Context

- 更新: 2026-08-01T17:16:07.873548+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=62836.6
- Funnel: target 922 → liquid 138 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| UAI/USDT:USDT | +13.81% | $7,692,899.93 |
| AKE/USDT:USDT | +10.69% | $17,625,579.94 |
| IDOL/USDT:USDT | +8.46% | $1,539,282.19 |
| 1000RATS/USDT:USDT | +7.24% | $21,299,698.34 |
| AEVO/USDT:USDT | +6.83% | $1,662,388.51 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAG/USDT:USDT | below_1h_threshold | +3.01% | +3.11% |
| AKE/USDT:USDT | below_1h_threshold | +2.88% | +2.98% |
| KAITO/USDT:USDT | below_1h_threshold | +2.47% | +2.57% |
| BULLA/USDT:USDT | below_1h_threshold | +1.41% | +1.51% |
| GIGGLE/USDT:USDT | below_1h_threshold | +0.94% | +1.04% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
