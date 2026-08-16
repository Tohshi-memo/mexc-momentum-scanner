# Decision Report

- generated_at: 2026-08-16T01:46:31.496211+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11706**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.74% / filled 20/20。**
- 全期間 MARKET基準: n=11706, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.74%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.74% | **+0.74%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 17/20 | 85.0% | +2.68% | **+2.28%** |
| LIMIT_ATR | 13/20 | 65.0% | +3.08% | **+2.00%** |
| LIMIT_3PCT | 14/20 | 70.0% | +2.75% | **+1.93%** |
| LIMIT_1PCT | 20/20 | 100.0% | +1.65% | **+1.65%** |
| MARKET | 20/20 | 100.0% | +0.74% | **+0.74%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.65% | **+0.74%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.86% | **+0.39%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.46% | **+0.18%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$121.53** / 初期 $100.00 (+21.53%)
- 確定トレード: 183件 (TP 71 / SL 107 / EXP 5)
- 最新: MOVR/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.53
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$636.73** / 初期 $100.00 (+536.73%)
- 確定: 4174件 (Win 1291 / Loss 1357 / Flat 1526) / skip 4093件
- 成長率目線: 平均log +0.000444 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEMI/USDT:USDT `LIMIT_FIB1272_LONG` SL_HIT account -0.50% 残高後 $636.73

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.38** / 初期 $100.00 (+55.38%)
- 確定: 1762件 (Win 493 / Loss 413 / Flat 856) / skip 3355件
- 成長率目線: 平均log +0.000250 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ROBO/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $155.38

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.28** / 初期 $100.00 (+19.28%)
- 確定: 1626件 (Win 495 / Loss 618 / Flat 513) / pending 0件 / skip 1552件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000133 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: H/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $119.28

## 6. Latest Market Context

- 更新: 2026-08-16T01:46:20.211768+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=63037.8
- Funnel: target 985 → liquid 138 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SPORTFUN/USDT:USDT | +20.75% | $4,099,251.02 |
| H/USDT:USDT | +12.38% | $6,040,738.95 |
| CROSS/USDT:USDT | +11.05% | $1,259,922.35 |
| CHIP/USDT:USDT | +9.71% | $1,454,958.62 |
| BULLA/USDT:USDT | +9.52% | $2,627,804.93 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +2.60% | +2.62% |
| ANSEM/USDT:USDT | below_1h_threshold | +2.00% | +2.02% |
| AIO/USDT:USDT | below_1h_threshold | +1.99% | +2.01% |
| US/USDT:USDT | below_1h_threshold | +1.04% | +1.07% |
| AEON1/USDT:USDT | below_1h_threshold | +0.98% | +1.00% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
