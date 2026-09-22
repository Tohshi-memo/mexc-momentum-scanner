# Decision Report

- generated_at: 2026-09-22T14:16:49.473134+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15332**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.86% / filled 20/20。**
- 全期間 MARKET基準: n=15332, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.86%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.86% | **+0.86%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.86% | **+0.86%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.86% | **+0.82%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.84% | **+0.67%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.76% | **+0.46%** |
| LIMIT_BB3S | 6/16 | 37.5% | +1.04% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +0.86% | **+0.86%** |
| MARKET_LONG | 20/20 | 100.0% | -0.06% | **-0.06%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -0.89% | **-0.09%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -0.60% | **-0.09%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -0.93% | **-0.09%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,169.49** / 初期 $100.00 (+1069.49%)
- 確定: 5821件 (Win 1727 / Loss 1873 / Flat 2221) / skip 6072件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,169.49

## 4. Robust Adaptive DryRun ($100)

- 残高: **$249.51** / 初期 $100.00 (+149.51%)
- 確定: 3353件 (Win 926 / Loss 781 / Flat 1646) / skip 5390件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KERNEL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $249.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.71** / 初期 $100.00 (+21.71%)
- 確定: 3102件 (Win 909 / Loss 1216 / Flat 977) / pending 6件 / skip 3703件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000100 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: 4STOCK/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $121.71

## 6. Latest Market Context

- 更新: 2026-09-22T14:16:35.340240+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=86276.1
- Funnel: target 1058 → liquid 180 → pre 50 → checked 50 → surge 8 → strict 0
- Surge前reject: below_1h_threshold=42, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.4 >= 65=1, 4h RSI 74.7 >= 65=1, 4h RSI 78.7 >= 65=1, 4h RSI 73.8 >= 65=1, 4h RSI 69.7 >= 65=1, 4h RSI 77.6 >= 65=1, 4h RSI 71.3 >= 65=1, 4h RSI 74.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| 4STOCK/USDT:USDT | +65.41% | $3,702,514.91 |
| MUBARAK/USDT:USDT | +51.54% | $6,856,491.75 |
| NIL/USDT:USDT | +30.36% | $3,966,407.41 |
| AGT/USDT:USDT | +26.09% | $1,955,335.78 |
| KERNEL/USDT:USDT | +24.30% | $5,780,928.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| 4STOCK/USDT:USDT | below_1h_threshold | +4.62% | +4.65% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +3.90% | +3.93% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +3.72% | +3.75% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +3.31% | +3.34% |
| MUBARAK/USDT:USDT | below_1h_threshold | +3.19% | +3.22% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
