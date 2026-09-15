# Decision Report

- generated_at: 2026-09-15T03:56:43.085295+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14557**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.64% / filled 20/20。**
- 全期間 MARKET基準: n=14557, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.64%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.64% | **+0.64%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +4.54% | **+1.36%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +4.33% | **+1.30%** |
| LIMIT_8PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| MARKET | 20/20 | 100.0% | +0.64% | **+0.64%** |
| LIMIT_BB3S | 5/16 | 31.2% | +1.81% | **+0.57%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +1.10% | **+0.73%** |
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.57% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 213件 (TP 79 / SL 129 / EXP 5)
- 最新: STORJ/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,087.84** / 初期 $100.00 (+987.84%)
- 確定: 5459件 (Win 1641 / Loss 1770 / Flat 2048) / skip 5659件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SHROOM/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,087.84

## 4. Robust Adaptive DryRun ($100)

- 残高: **$229.67** / 初期 $100.00 (+129.67%)
- 確定: 2999件 (Win 832 / Loss 716 / Flat 1451) / skip 4969件
- 成長率目線: 平均log +0.000277 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0531 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SHROOM/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $229.67

## 5. Causal Adaptive DryRun ($100)

- 残高: **$124.63** / 初期 $100.00 (+24.63%)
- 確定: 2903件 (Win 862 / Loss 1130 / Flat 911) / pending 6件 / skip 3124件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000216 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SHROOM/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $124.63

## 6. Latest Market Context

- 更新: 2026-09-15T03:56:20.533689+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.29% price=77651.1
- Funnel: target 1073 → liquid 158 → pre 50 → checked 50 → surge 5 → strict 3
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.0 >= 65=1, 4h RSI 68.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SHROOM/USDT:USDT | +63.25% | $1,370,675.10 |
| POWER/USDT:USDT | +53.62% | $7,231,475.98 |
| AIN/USDT:USDT | +25.44% | $7,930,085.92 |
| CNPY/USDT:USDT | +14.76% | $1,845,274.28 |
| CYS/USDT:USDT | +12.34% | $1,596,661.29 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STORJ/USDT:USDT | below_1h_threshold | +3.83% | +4.13% |
| RIVER/USDT:USDT | below_1h_threshold | +1.41% | +1.70% |
| CRV/USDT:USDT | below_1h_threshold | +0.89% | +1.18% |
| KORU/USDT:USDT | below_1h_threshold | +0.81% | +1.10% |
| OP/USDT:USDT | below_1h_threshold | +0.57% | +0.87% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
