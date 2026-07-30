# Decision Report

- generated_at: 2026-07-30T12:11:27.087775+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9880**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.51% / filled 20/20。**
- 全期間 MARKET基準: n=9880, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.51%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.51% | **+2.51%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.51% | **+2.51%** |
| LIMIT_2PCT | 13/20 | 65.0% | +2.23% | **+1.45%** |
| LIMIT_1PCT | 15/20 | 75.0% | +1.92% | **+1.44%** |
| LIMIT_ATR | 11/20 | 55.0% | +2.53% | **+1.39%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +4.86% | **+0.73%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +2.25% | **+0.67%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +0.64% | **+0.45%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.89% | **+0.40%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.64% | **+0.35%** |

## 2. $100 Live Portfolio

- 残高: **$121.53** / 初期 $100.00 (+21.53%)
- 確定トレード: 171件 (TP 67 / SL 99 / EXP 5)
- 最新: AMZU/USDT:USDT SL_HIT PnL -2.81% 残高後 $121.53
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$494.05** / 初期 $100.00 (+394.05%)
- 確定: 3520件 (Win 1113 / Loss 1147 / Flat 1260) / skip 2921件
- 成長率目線: 平均log +0.000454 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UAI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $494.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$136.91** / 初期 $100.00 (+36.91%)
- 確定: 1242件 (Win 344 / Loss 283 / Flat 615) / skip 2049件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOXL/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $136.91

## 5. Causal Adaptive DryRun ($100)

- 残高: **$111.63** / 初期 $100.00 (+11.63%)
- 確定: 785件 (Win 257 / Loss 305 / Flat 223) / pending 5件 / skip 562件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000838 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $111.63

## 6. Latest Market Context

- 更新: 2026-07-30T12:11:19.593324+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.18% price=64884.4
- Funnel: target 917 → liquid 182 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KOMA/USDT:USDT | +58.48% | $1,842,860.67 |
| ESP/USDT:USDT | +28.66% | $4,254,708.60 |
| MMT/USDT:USDT | +22.54% | $1,476,959.34 |
| ROBO/USDT:USDT | +17.06% | $1,031,170.27 |
| MSFU/USDT:USDT | +16.74% | $3,004,910.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NBISSTOCK/USDT:USDT | below_1h_threshold | +4.37% | +4.19% |
| KORU/USDT:USDT | below_1h_threshold | +3.99% | +3.81% |
| SOXL/USDT:USDT | below_1h_threshold | +3.35% | +3.16% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +3.32% | +3.13% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +2.71% | +2.53% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
