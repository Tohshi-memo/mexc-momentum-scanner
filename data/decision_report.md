# Decision Report

- generated_at: 2026-09-15T03:46:31.567109+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14553**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.84% / filled 20/20。**
- 全期間 MARKET基準: n=14553, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.84%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.84% | **+1.84%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.84% | **+1.84%** |
| LIMIT_8PCT | 4/20 | 20.0% | +8.00% | **+1.60%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +4.11% | **+1.44%** |
| LIMIT_7PCT | 6/20 | 30.0% | +4.54% | **+1.36%** |
| LIMIT_BB3S | 4/16 | 25.0% | +2.05% | **+0.51%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +1.10% | **+0.73%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.44% | **+0.20%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.23% | **+0.12%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 213件 (TP 79 / SL 129 / EXP 5)
- 最新: STORJ/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,087.84** / 初期 $100.00 (+987.84%)
- 確定: 5455件 (Win 1641 / Loss 1770 / Flat 2044) / skip 5659件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SHROOM/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,087.84

## 4. Robust Adaptive DryRun ($100)

- 残高: **$229.67** / 初期 $100.00 (+129.67%)
- 確定: 2995件 (Win 832 / Loss 716 / Flat 1447) / skip 4969件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score +0.0348 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SHROOM/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $229.67

## 5. Causal Adaptive DryRun ($100)

- 残高: **$125.51** / 初期 $100.00 (+25.51%)
- 確定: 2899件 (Win 862 / Loss 1126 / Flat 911) / pending 6件 / skip 3121件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000347 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SHROOM/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $125.51

## 6. Latest Market Context

- 更新: 2026-09-15T03:46:16.070903+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.14% price=77769.6
- Funnel: target 1073 → liquid 158 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.0 >= 65=1, 4h RSI 68.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SHROOM/USDT:USDT | +51.32% | $1,342,486.38 |
| POWER/USDT:USDT | +44.97% | $6,868,878.87 |
| AIN/USDT:USDT | +29.56% | $7,880,307.50 |
| CNPY/USDT:USDT | +13.17% | $1,831,006.56 |
| STORJ/USDT:USDT | +12.35% | $1,073,198.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STORJ/USDT:USDT | below_1h_threshold | +4.93% | +5.07% |
| CYS/USDT:USDT | below_1h_threshold | +4.15% | +4.29% |
| OP/USDT:USDT | below_1h_threshold | +0.97% | +1.11% |
| RIVER/USDT:USDT | below_1h_threshold | +0.91% | +1.05% |
| KORU/USDT:USDT | below_1h_threshold | +0.81% | +0.95% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
