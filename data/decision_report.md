# Decision Report

- generated_at: 2026-10-08T11:11:24.877583+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16327**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.17% / filled 20/20。**
- 全期間 MARKET基準: n=16327, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.17% | **+2.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.17% | **+2.17%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.81% | **+1.63%** |
| LIMIT_BB3S | 5/13 | 38.5% | +2.56% | **+0.99%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +3.07% | **+1.07%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +1.91% | **+0.48%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.80% | **+0.40%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | -0.46% | **-0.23%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | -0.76% | **-0.46%** |

## 2. $100 Live Portfolio

- 残高: **$121.36** / 初期 $100.00 (+21.36%)
- 確定トレード: 235件 (TP 87 / SL 141 / EXP 7)
- 最新: RLC/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.36
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,315.82** / 初期 $100.00 (+1215.82%)
- 確定: 6279件 (Win 1845 / Loss 2012 / Flat 2422) / skip 6609件
- 成長率目線: 平均log +0.000410 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RLC/USDT:USDT `LIMIT_BB3S` SL_HIT account -0.50% 残高後 $1,315.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.04** / 初期 $100.00 (+174.04%)
- 確定: 3632件 (Win 1010 / Loss 853 / Flat 1769) / skip 6106件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ETHFI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $274.04

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4487件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000273 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-08T11:11:13.717340+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.31% price=82435.2
- Funnel: target 1082 → liquid 174 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| OGN/USDT:USDT | +46.66% | $1,004,286.54 |
| MET/USDT:USDT | +45.18% | $29,701,228.37 |
| JUP/USDT:USDT | +18.88% | $39,803,053.69 |
| UAI/USDT:USDT | +15.70% | $2,825,439.96 |
| ALGO/USDT:USDT | +14.46% | $10,789,817.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXS/USDT:USDT | below_1h_threshold | +1.62% | +1.93% |
| W/USDT:USDT | below_1h_threshold | +0.98% | +1.28% |
| UKOIL/USDT:USDT | below_1h_threshold | +0.68% | +0.98% |
| USOIL/USDT:USDT | below_1h_threshold | +0.65% | +0.96% |
| NGAS/USDT:USDT | below_1h_threshold | +0.51% | +0.81% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
