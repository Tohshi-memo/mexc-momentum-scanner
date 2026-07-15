# Decision Report

- generated_at: 2026-07-15T01:46:13.988264+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8709**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.14% / filled 20/20。**
- 全期間 MARKET基準: n=8709, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.14%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.14% | **+1.14%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.14% | **+1.14%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.95% | **+0.71%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/6 | 83.3% | +1.92% | **+1.60%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +2.95% | **+0.44%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.50% | **+0.20%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.23% | **+0.18%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.29% | **+0.13%** |

## 2. $100 Live Portfolio

- 残高: **$102.71** / 初期 $100.00 (+2.71%)
- 確定トレード: 97件 (TP 33 / SL 62 / EXP 2)
- 最新: DODO/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.71
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$328.11** / 初期 $100.00 (+228.11%)
- 確定: 2865件 (Win 894 / Loss 932 / Flat 1039) / skip 2405件
- 成長率目線: 平均log +0.000415 / 幾何平均 +0.041% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DODO/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $328.11

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.12** / 初期 $100.00 (+5.12%)
- 確定: 694件 (Win 161 / Loss 163 / Flat 370) / skip 1426件
- 成長率目線: 平均log +0.000072 / 幾何平均 +0.007% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DODO/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $105.12

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.75** / 初期 $100.00 (-1.25%)
- 確定: 60件 (Win 19 / Loss 39 / Flat 2) / pending 0件 / skip 119件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000157 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AEHRSTOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $98.75

## 6. Latest Market Context

- 更新: 2026-07-15T01:46:07.705082+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.20% price=64672.7
- Funnel: target 862 → liquid 166 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.8 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AEHRSTOCK/USDT:USDT | +30.55% | $2,902,970.38 |
| DODO/USDT:USDT | +27.44% | $5,922,848.12 |
| MAGMA/USDT:USDT | +11.81% | $2,187,197.07 |
| PUMPFUN/USDT:USDT | +10.88% | $9,603,555.39 |
| VELVET/USDT:USDT | +6.25% | $32,814,679.93 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MAGMA/USDT:USDT | below_1h_threshold | +3.56% | +3.75% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +2.66% | +2.86% |
| FARTCOIN/USDT:USDT | below_1h_threshold | +2.13% | +2.33% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +1.38% | +1.57% |
| SOXL/USDT:USDT | below_1h_threshold | +1.26% | +1.46% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
