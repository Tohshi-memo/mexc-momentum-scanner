# Decision Report

- generated_at: 2026-07-16T11:56:22.140645+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8805**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.54% / filled 20/20。**
- 全期間 MARKET基準: n=8805, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.54%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.54% | **+0.54%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.54% | **+0.54%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.47% | **+0.30%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.33% | **+0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +3.20% | **+2.40%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.67% | **+0.80%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.39% | **+0.25%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.33% | **+0.12%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +0.56% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$106.87** / 初期 $100.00 (+6.87%)
- 確定トレード: 104件 (TP 38 / SL 64 / EXP 2)
- 最新: ROAM/USDT:USDT SL_HIT PnL -4.00% 残高後 $106.87
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$338.75** / 初期 $100.00 (+238.75%)
- 確定: 2920件 (Win 911 / Loss 945 / Flat 1064) / skip 2446件
- 成長率目線: 平均log +0.000418 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: XEC/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $338.75

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.97** / 初期 $100.00 (+6.97%)
- 確定: 767件 (Win 176 / Loss 170 / Flat 421) / skip 1449件
- 成長率目線: 平均log +0.000088 / 幾何平均 +0.009% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0002 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: XEC/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.97

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.12** / 初期 $100.00 (-1.88%)
- 確定: 75件 (Win 22 / Loss 49 / Flat 4) / pending 3件 / skip 198件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000426 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $98.12

## 6. Latest Market Context

- 更新: 2026-07-16T11:56:14.529626+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=64185.0
- Funnel: target 880 → liquid 171 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.2 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +23.97% | $3,059,465.30 |
| US/USDT:USDT | +20.02% | $17,056,897.41 |
| AKE/USDT:USDT | +19.96% | $45,249,818.16 |
| BANK/USDT:USDT | +16.81% | $3,632,134.88 |
| ROAM/USDT:USDT | +16.31% | $5,981,477.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| US/USDT:USDT | below_1h_threshold | +3.11% | +3.11% |
| BASED/USDT:USDT | below_1h_threshold | +1.29% | +1.30% |
| EDGE/USDT:USDT | below_1h_threshold | +1.01% | +1.02% |
| PYTH/USDT:USDT | below_1h_threshold | +1.01% | +1.01% |
| ENJ/USDT:USDT | below_1h_threshold | +0.73% | +0.74% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
