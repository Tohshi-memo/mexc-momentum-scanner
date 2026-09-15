# Decision Report

- generated_at: 2026-09-15T03:51:41.574234+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14555**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.24% / filled 20/20。**
- 全期間 MARKET基準: n=14555, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.24% | **+1.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +4.54% | **+1.36%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +4.33% | **+1.30%** |
| MARKET | 20/20 | 100.0% | +1.24% | **+1.24%** |
| LIMIT_8PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_BB3S | 4/16 | 25.0% | +3.00% | **+0.75%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +1.10% | **+0.73%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +0.47% | **+0.21%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.50% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 213件 (TP 79 / SL 129 / EXP 5)
- 最新: STORJ/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,087.84** / 初期 $100.00 (+987.84%)
- 確定: 5457件 (Win 1641 / Loss 1770 / Flat 2046) / skip 5659件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SHROOM/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,087.84

## 4. Robust Adaptive DryRun ($100)

- 残高: **$229.67** / 初期 $100.00 (+129.67%)
- 確定: 2997件 (Win 832 / Loss 716 / Flat 1449) / skip 4969件
- 成長率目線: 平均log +0.000277 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0551 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SHROOM/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $229.67

## 5. Causal Adaptive DryRun ($100)

- 残高: **$125.07** / 初期 $100.00 (+25.07%)
- 確定: 2901件 (Win 862 / Loss 1128 / Flat 911) / pending 6件 / skip 3123件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000233 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SHROOM/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $125.07

## 6. Latest Market Context

- 更新: 2026-09-15T03:51:18.787466+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.22% price=77708.3
- Funnel: target 1073 → liquid 158 → pre 50 → checked 50 → surge 5 → strict 3
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.0 >= 65=1, 4h RSI 69.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SHROOM/USDT:USDT | +57.19% | $1,358,503.61 |
| POWER/USDT:USDT | +51.13% | $7,036,119.04 |
| AIN/USDT:USDT | +28.25% | $7,899,152.06 |
| CNPY/USDT:USDT | +14.30% | $1,836,776.30 |
| CYS/USDT:USDT | +12.11% | $1,591,785.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +3.19% | +3.41% |
| STORJ/USDT:USDT | below_1h_threshold | +2.77% | +2.99% |
| KOMA/USDT:USDT | below_1h_threshold | +1.16% | +1.38% |
| CRV/USDT:USDT | below_1h_threshold | +1.09% | +1.31% |
| RIVER/USDT:USDT | below_1h_threshold | +0.83% | +1.05% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
