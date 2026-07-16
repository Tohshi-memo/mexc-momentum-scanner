# Decision Report

- generated_at: 2026-07-16T09:46:13.610596+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8796**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.20% / filled 20/20。**
- 全期間 MARKET基準: n=8796, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.20% | **+1.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_3PCT | 15/20 | 75.0% | +1.02% | **+0.76%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.84% | **+0.76%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.77% | **+0.62%** |
| LIMIT_BB3S | 5/13 | 38.5% | +1.45% | **+0.56%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.84% | **+0.63%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +2.04% | **+0.51%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.82% | **+0.45%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.59% | **+0.41%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +0.57% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$106.87** / 初期 $100.00 (+6.87%)
- 確定トレード: 104件 (TP 38 / SL 64 / EXP 2)
- 最新: ROAM/USDT:USDT SL_HIT PnL -4.00% 残高後 $106.87
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$336.75** / 初期 $100.00 (+236.75%)
- 確定: 2911件 (Win 907 / Loss 945 / Flat 1059) / skip 2446件
- 成長率目線: 平均log +0.000417 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ROAM/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $336.75

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.05** / 初期 $100.00 (+7.05%)
- 確定: 758件 (Win 172 / Loss 169 / Flat 417) / skip 1449件
- 成長率目線: 平均log +0.000090 / 幾何平均 +0.009% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ROAM/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $107.05

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.31** / 初期 $100.00 (-1.69%)
- 確定: 68件 (Win 20 / Loss 44 / Flat 4) / pending 2件 / skip 198件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000453 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ROAM/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $98.31

## 6. Latest Market Context

- 更新: 2026-07-16T09:46:06.732481+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=64074.7
- Funnel: target 875 → liquid 170 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.2 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROAM/USDT:USDT | +23.15% | $5,846,700.72 |
| US/USDT:USDT | +17.50% | $15,787,436.94 |
| CAP/USDT:USDT | +15.97% | $2,895,740.39 |
| FLOCK/USDT:USDT | +13.07% | $1,074,523.48 |
| BANK/USDT:USDT | +11.98% | $2,555,664.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RAVE/USDT:USDT | below_1h_threshold | +4.37% | +4.40% |
| BANK/USDT:USDT | below_1h_threshold | +4.34% | +4.38% |
| BASED/USDT:USDT | below_1h_threshold | +3.05% | +3.08% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.91% | +1.95% |
| GOOGLSTOCK/USDT:USDT | below_1h_threshold | +1.54% | +1.57% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
