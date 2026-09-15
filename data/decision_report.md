# Decision Report

- generated_at: 2026-09-15T04:06:31.351270+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14561**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14561, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.04%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.04% | **+0.04%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +4.54% | **+1.36%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +5.15% | **+1.29%** |
| LIMIT_8PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_BB3S | 5/19 | 26.3% | +1.81% | **+0.48%** |
| LIMIT_6PCT | 8/20 | 40.0% | +1.15% | **+0.46%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.51% | **+0.41%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.67% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 213件 (TP 79 / SL 129 / EXP 5)
- 最新: STORJ/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,086.69** / 初期 $100.00 (+986.69%)
- 確定: 5463件 (Win 1641 / Loss 1771 / Flat 2051) / skip 5659件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: POWER/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,086.69

## 4. Robust Adaptive DryRun ($100)

- 残高: **$229.67** / 初期 $100.00 (+129.67%)
- 確定: 3002件 (Win 832 / Loss 716 / Flat 1454) / skip 4970件
- 成長率目線: 平均log +0.000277 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0576 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: POWER/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $229.67

## 5. Causal Adaptive DryRun ($100)

- 残高: **$124.42** / 初期 $100.00 (+24.42%)
- 確定: 2906件 (Win 862 / Loss 1131 / Flat 913) / pending 3件 / skip 3125件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000201 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: POWER/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $124.42

## 6. Latest Market Context

- 更新: 2026-09-15T04:06:15.052046+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=77710.5
- Funnel: target 1073 → liquid 158 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SHROOM/USDT:USDT | +70.64% | $1,383,144.37 |
| POWER/USDT:USDT | +63.47% | $7,071,613.03 |
| CNPY/USDT:USDT | +15.06% | $1,840,145.06 |
| CYS/USDT:USDT | +10.94% | $1,583,852.72 |
| CATE/USDT:USDT | +9.17% | $1,670,286.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SHROOM/USDT:USDT | below_1h_threshold | +3.34% | +3.27% |
| AKE/USDT:USDT | below_1h_threshold | +1.96% | +1.89% |
| CATE/USDT:USDT | below_1h_threshold | +1.76% | +1.69% |
| PONS/USDT:USDT | below_1h_threshold | +0.93% | +0.86% |
| ZEC/USDT:USDT | below_1h_threshold | +0.47% | +0.40% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
