# Decision Report

- generated_at: 2026-07-30T07:41:31.518833+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9870**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +4.20% / filled 20/20。**
- 全期間 MARKET基準: n=9870, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+4.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +4.20% | **+4.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +4.20% | **+4.20%** |
| LIMIT_1PCT | 15/20 | 75.0% | +4.02% | **+3.01%** |
| LIMIT_2PCT | 9/20 | 45.0% | +3.26% | **+1.46%** |
| LIMIT_3PCT | 6/20 | 30.0% | +2.65% | **+0.80%** |
| LIMIT_BB3S | 5/17 | 29.4% | +1.86% | **+0.55%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +0.76% | **+0.51%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.40% | **+0.42%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +1.18% | **+0.29%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | +0.36% | **+0.20%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | -1.34% | **-0.74%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 170件 (TP 67 / SL 98 / EXP 5)
- 最新: LASERTECSTOCK/USDT:USDT TP_HIT PnL +3.98% 残高後 $121.65
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$494.05** / 初期 $100.00 (+394.05%)
- 確定: 3519件 (Win 1113 / Loss 1147 / Flat 1259) / skip 2912件
- 成長率目線: 平均log +0.000454 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $494.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$136.91** / 初期 $100.00 (+36.91%)
- 確定: 1242件 (Win 344 / Loss 283 / Flat 615) / skip 2039件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOXL/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $136.91

## 5. Causal Adaptive DryRun ($100)

- 残高: **$111.46** / 初期 $100.00 (+11.46%)
- 確定: 777件 (Win 254 / Loss 300 / Flat 223) / pending 1件 / skip 562件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000962 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ESP/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $111.46

## 6. Latest Market Context

- 更新: 2026-07-30T07:41:20.046363+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=64015.1
- Funnel: target 916 → liquid 183 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESP/USDT:USDT | +30.46% | $1,291,026.04 |
| MMT/USDT:USDT | +16.92% | $1,108,091.36 |
| RE/USDT:USDT | +14.46% | $9,206,131.39 |
| MSFU/USDT:USDT | +12.13% | $2,843,098.25 |
| ADVANTESTSTOCK/USDT:USDT | +10.60% | $1,302,562.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HOLO/USDT:USDT | below_1h_threshold | +2.08% | +2.02% |
| ZIL/USDT:USDT | below_1h_threshold | +1.90% | +1.84% |
| SOXS/USDT:USDT | below_1h_threshold | +1.86% | +1.80% |
| FET/USDT:USDT | below_1h_threshold | +1.61% | +1.54% |
| MMT/USDT:USDT | below_1h_threshold | +1.33% | +1.27% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
