# Decision Report

- generated_at: 2026-07-15T06:01:21.480995+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8713**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.98% / filled 20/20。**
- 全期間 MARKET基準: n=8713, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.98%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.98% | **+1.98%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.98% | **+1.98%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.28% | **+1.09%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.41% | **+0.99%** |
| LIMIT_ATR | 14/20 | 70.0% | +1.30% | **+0.91%** |
| LIMIT_BB3S | 5/14 | 35.7% | +1.16% | **+0.41%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +2.23% | **+0.45%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.44% | **+0.20%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.15% | **+0.08%** |
| LIMIT_BB3S_LONG | 5/6 | 83.3% | +0.09% | **+0.07%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$102.71** / 初期 $100.00 (+2.71%)
- 確定トレード: 97件 (TP 33 / SL 62 / EXP 2)
- 最新: DODO/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.71
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$329.97** / 初期 $100.00 (+229.97%)
- 確定: 2867件 (Win 896 / Loss 932 / Flat 1039) / skip 2407件
- 成長率目線: 平均log +0.000416 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AEHRSTOCK/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.03% 残高後 $329.97

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.12** / 初期 $100.00 (+5.12%)
- 確定: 695件 (Win 161 / Loss 163 / Flat 371) / skip 1429件
- 成長率目線: 平均log +0.000072 / 幾何平均 +0.007% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AEHRSTOCK/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $105.12

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.75** / 初期 $100.00 (-1.25%)
- 確定: 60件 (Win 19 / Loss 39 / Flat 2) / pending 0件 / skip 126件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000031 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AEHRSTOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $98.75

## 6. Latest Market Context

- 更新: 2026-07-15T06:01:16.213262+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=64885.5
- Funnel: target 864 → liquid 168 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.7 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +91.85% | $1,173,329.86 |
| DODO/USDT:USDT | +38.32% | $8,627,150.32 |
| AEHRSTOCK/USDT:USDT | +31.22% | $3,166,542.56 |
| MAGMA/USDT:USDT | +18.68% | $2,637,770.16 |
| US/USDT:USDT | +12.58% | $2,052,771.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| COPSTOCK/USDT:USDT | below_1h_threshold | +0.66% | +0.71% |
| DODO/USDT:USDT | below_1h_threshold | +0.56% | +0.61% |
| VELVET/USDT:USDT | below_1h_threshold | +0.52% | +0.57% |
| XEC/USDT:USDT | below_1h_threshold | +0.51% | +0.57% |
| SOXL/USDT:USDT | below_1h_threshold | +0.50% | +0.55% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
