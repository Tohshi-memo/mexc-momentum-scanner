# Decision Report

- generated_at: 2026-07-30T12:41:29.294726+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9884**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.15% / filled 20/20。**
- 全期間 MARKET基準: n=9884, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.15%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.15% | **+1.15%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.15% | **+1.15%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +3.16% | **+0.79%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.16% | **+0.75%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +1.92% | **+1.25%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.08% | **+0.81%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.86% | **+0.56%** |

## 2. $100 Live Portfolio

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定トレード: 172件 (TP 67 / SL 100 / EXP 5)
- 最新: SNDKSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.41
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$494.05** / 初期 $100.00 (+394.05%)
- 確定: 3520件 (Win 1113 / Loss 1147 / Flat 1260) / skip 2925件
- 成長率目線: 平均log +0.000454 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UAI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $494.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$136.91** / 初期 $100.00 (+36.91%)
- 確定: 1242件 (Win 344 / Loss 283 / Flat 615) / skip 2053件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOXL/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $136.91

## 5. Causal Adaptive DryRun ($100)

- 残高: **$111.42** / 初期 $100.00 (+11.42%)
- 確定: 789件 (Win 258 / Loss 308 / Flat 223) / pending 4件 / skip 563件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000658 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SNXX/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $111.42

## 6. Latest Market Context

- 更新: 2026-07-30T12:41:19.448527+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=64816.0
- Funnel: target 917 → liquid 183 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 92.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KOMA/USDT:USDT | +68.97% | $2,214,182.38 |
| ESP/USDT:USDT | +24.72% | $4,529,968.60 |
| MMT/USDT:USDT | +22.13% | $1,534,942.80 |
| ROBO/USDT:USDT | +17.44% | $1,056,146.38 |
| CAP/USDT:USDT | +17.10% | $1,460,807.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UAI/USDT:USDT | below_1h_threshold | +4.92% | +4.84% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +4.37% | +4.29% |
| KORU/USDT:USDT | below_1h_threshold | +3.99% | +3.91% |
| SOXL/USDT:USDT | below_1h_threshold | +3.35% | +3.27% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +3.32% | +3.24% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
