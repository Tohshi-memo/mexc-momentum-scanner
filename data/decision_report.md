# Decision Report

- generated_at: 2026-08-01T01:21:26.647442+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10041**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.69% / filled 20/20。**
- 全期間 MARKET基準: n=10041, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.69%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.69% | **+0.69%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.04% | **+0.94%** |
| MARKET | 20/20 | 100.0% | +0.69% | **+0.69%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_BB3S | 4/20 | 20.0% | +1.52% | **+0.30%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.91% | **+0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.68% | **+0.48%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +0.68% | **+0.41%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.86% | **+0.39%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.64% | **+0.38%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.41% | **+0.33%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$569.73** / 初期 $100.00 (+469.73%)
- 確定: 3593件 (Win 1149 / Loss 1175 / Flat 1269) / skip 3009件
- 成長率目線: 平均log +0.000484 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GIGGLE/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $569.73

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.81** / 初期 $100.00 (+40.81%)
- 確定: 1279件 (Win 359 / Loss 297 / Flat 623) / skip 2173件
- 成長率目線: 平均log +0.000268 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $140.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$111.78** / 初期 $100.00 (+11.78%)
- 確定: 864件 (Win 280 / Loss 342 / Flat 242) / pending 6件 / skip 648件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000236 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: GIGGLE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $111.78

## 6. Latest Market Context

- 更新: 2026-08-01T01:21:16.258423+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=62930.6
- Funnel: target 921 → liquid 169 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +25.71% | $1,137,182.77 |
| GIGGLE/USDT:USDT | +18.68% | $22,122,611.42 |
| US/USDT:USDT | +17.73% | $2,433,009.18 |
| 1000RATS/USDT:USDT | +16.57% | $17,798,759.70 |
| KOMA/USDT:USDT | +16.24% | $17,917,871.43 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZAMA/USDT:USDT | below_1h_threshold | +2.85% | +2.81% |
| JIMOTHY/USDT:USDT | below_1h_threshold | +1.92% | +1.88% |
| AXTISTOCK/USDT:USDT | below_1h_threshold | +1.63% | +1.60% |
| BANK/USDT:USDT | below_1h_threshold | +1.51% | +1.47% |
| LAB/USDT:USDT | below_1h_threshold | +1.32% | +1.29% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
