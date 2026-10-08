# Decision Report

- generated_at: 2026-10-08T13:01:41.449560+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16333**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.93% / filled 20/20。**
- 全期間 MARKET基準: n=16333, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.93%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.93% | **+0.93%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.93% | **+0.93%** |
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_BB3S | 5/9 | 55.6% | +1.02% | **+0.57%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.49% | **+0.44%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +3.86% | **+0.96%** |
| MARKET_LONG | 20/20 | 100.0% | +0.83% | **+0.83%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.37% | **+0.29%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.31% | **+0.12%** |

## 2. $100 Live Portfolio

- 残高: **$121.24** / 初期 $100.00 (+21.24%)
- 確定トレード: 236件 (TP 87 / SL 142 / EXP 7)
- 最新: STRK/USDT:USDT SL_HIT PnL -3.05% 残高後 $121.24
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,315.82** / 初期 $100.00 (+1215.82%)
- 確定: 6279件 (Win 1845 / Loss 2012 / Flat 2422) / skip 6615件
- 成長率目線: 平均log +0.000410 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RLC/USDT:USDT `LIMIT_BB3S` SL_HIT account -0.50% 残高後 $1,315.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.04** / 初期 $100.00 (+174.04%)
- 確定: 3632件 (Win 1010 / Loss 853 / Flat 1769) / skip 6112件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ETHFI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $274.04

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4494件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000165 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-08T13:01:29.734953+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=82231.6
- Funnel: target 1082 → liquid 171 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| OGN/USDT:USDT | +91.94% | $3,231,831.43 |
| MET/USDT:USDT | +39.12% | $32,419,065.90 |
| UAI/USDT:USDT | +16.79% | $3,163,407.63 |
| W/USDT:USDT | +15.92% | $6,160,766.07 |
| STRK/USDT:USDT | +15.14% | $6,887,348.23 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +1.43% | +1.49% |
| BSPSTOCK/USDT:USDT | below_1h_threshold | +1.13% | +1.18% |
| BATON/USDT:USDT | below_1h_threshold | +0.87% | +0.92% |
| GOOGLSTOCK/USDT:USDT | below_1h_threshold | +0.83% | +0.88% |
| MRNASTOCK/USDT:USDT | below_1h_threshold | +0.72% | +0.77% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
