# Decision Report

- generated_at: 2026-08-01T17:51:23.645832+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10116**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.82% / filled 20/20。**
- 全期間 MARKET基準: n=10116, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.82%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.82% | **+0.82%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.34% | **+0.82%** |
| MARKET | 20/20 | 100.0% | +0.82% | **+0.82%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/6 | 83.3% | +0.80% | **+0.67%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.64% | **+0.51%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.62% | **+0.47%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +1.28% | **+0.32%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | -0.03% | **-0.02%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$571.50** / 初期 $100.00 (+471.50%)
- 確定: 3640件 (Win 1159 / Loss 1191 / Flat 1290) / skip 3037件
- 成長率目線: 平均log +0.000479 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $571.50

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.81** / 初期 $100.00 (+40.81%)
- 確定: 1279件 (Win 359 / Loss 297 / Flat 623) / skip 2248件
- 成長率目線: 平均log +0.000268 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $140.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$111.62** / 初期 $100.00 (+11.62%)
- 確定: 925件 (Win 293 / Loss 362 / Flat 270) / pending 2件 / skip 659件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000250 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $111.62

## 6. Latest Market Context

- 更新: 2026-08-01T17:51:12.646379+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.20% price=62772.1
- Funnel: target 922 → liquid 141 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| UAI/USDT:USDT | +18.26% | $8,976,223.53 |
| 1000RATS/USDT:USDT | +9.66% | $21,518,824.79 |
| KAITO/USDT:USDT | +7.20% | $4,668,958.14 |
| AKE/USDT:USDT | +6.47% | $25,145,246.19 |
| BLESS/USDT:USDT | +6.33% | $1,334,761.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UAI/USDT:USDT | below_1h_threshold | +4.33% | +4.54% |
| TAG/USDT:USDT | below_1h_threshold | +3.29% | +3.50% |
| BLESS/USDT:USDT | below_1h_threshold | +2.91% | +3.11% |
| BULLA/USDT:USDT | below_1h_threshold | +1.94% | +2.14% |
| 1000RATS/USDT:USDT | below_1h_threshold | +1.82% | +2.02% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
