# Decision Report

- generated_at: 2026-08-01T17:46:22.954299+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10115**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.22% / filled 20/20。**
- 全期間 MARKET基準: n=10115, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.22%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.22% | **+0.22%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +6.93% | **+1.39%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +2.25% | **+0.90%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +2.00% | **+1.60%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.95% | **+0.71%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.95% | **+0.67%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +1.28% | **+0.32%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.27% | **+0.23%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$571.50** / 初期 $100.00 (+471.50%)
- 確定: 3640件 (Win 1159 / Loss 1191 / Flat 1290) / skip 3036件
- 成長率目線: 平均log +0.000479 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $571.50

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.81** / 初期 $100.00 (+40.81%)
- 確定: 1279件 (Win 359 / Loss 297 / Flat 623) / skip 2247件
- 成長率目線: 平均log +0.000268 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $140.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$111.82** / 初期 $100.00 (+11.82%)
- 確定: 924件 (Win 293 / Loss 361 / Flat 270) / pending 3件 / skip 659件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000257 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $111.82

## 6. Latest Market Context

- 更新: 2026-08-01T17:46:13.762931+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.17% price=62789.9
- Funnel: target 922 → liquid 140 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +29.33% | $23,497,031.04 |
| UAI/USDT:USDT | +17.57% | $8,867,457.32 |
| IDOL/USDT:USDT | +11.15% | $1,578,378.20 |
| 1000RATS/USDT:USDT | +9.71% | $21,487,408.86 |
| KAITO/USDT:USDT | +7.10% | $4,546,296.31 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAG/USDT:USDT | below_1h_threshold | +3.99% | +4.17% |
| UAI/USDT:USDT | below_1h_threshold | +3.91% | +4.08% |
| BLESS/USDT:USDT | below_1h_threshold | +3.00% | +3.18% |
| IDOL/USDT:USDT | below_1h_threshold | +2.56% | +2.73% |
| BULLA/USDT:USDT | below_1h_threshold | +2.44% | +2.62% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
