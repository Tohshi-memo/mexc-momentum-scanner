# Decision Report

- generated_at: 2026-11-26T21:46:26.146924+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19733**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.52% / filled 20/20。**
- 全期間 MARKET基準: n=19733, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.52%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.52% | **+1.52%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.52% | **+1.52%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.12% | **+0.45%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +4.45% | **+0.44%** |
| LIMIT_BB3S | 2/20 | 10.0% | +4.04% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.44% | **+0.20%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.21% | **+0.19%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.29% | **+0.13%** |

## 2. $100 Live Portfolio

- 残高: **$121.68** / 初期 $100.00 (+21.68%)
- 確定トレード: 291件 (TP 106 / SL 176 / EXP 9)
- 最新: AXTISTOCK/USDT:USDT EXPIRED PnL -1.62% 残高後 $121.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,948.16** / 初期 $100.00 (+1848.16%)
- 確定: 7639件 (Win 2199 / Loss 2459 / Flat 2981) / skip 8655件
- 成長率目線: 平均log +0.000389 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BULLA/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,948.16

## 4. Robust Adaptive DryRun ($100)

- 残高: **$467.87** / 初期 $100.00 (+367.87%)
- 確定: 5258件 (Win 1402 / Loss 1128 / Flat 2728) / skip 7886件
- 成長率目線: 平均log +0.000293 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $467.87

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7892件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000237 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-26T21:46:09.306765+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.21% price=60869.0
- Funnel: target 1097 → liquid 120 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BULLA/USDT:USDT | +19.75% | $12,163,014.17 |
| INIT/USDT:USDT | +11.38% | $9,349,624.02 |
| NES/USDT:USDT | +10.13% | $1,356,903.57 |
| AKE/USDT:USDT | +8.17% | $10,876,305.05 |
| ZRO/USDT:USDT | +5.93% | $2,383,774.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MANTRA/USDT:USDT | below_1h_threshold | +4.83% | +4.61% |
| INIT/USDT:USDT | below_1h_threshold | +2.69% | +2.48% |
| SSV/USDT:USDT | below_1h_threshold | +2.69% | +2.48% |
| SKY/USDT:USDT | below_1h_threshold | +1.53% | +1.32% |
| BIGTIME/USDT:USDT | below_1h_threshold | +1.40% | +1.18% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
