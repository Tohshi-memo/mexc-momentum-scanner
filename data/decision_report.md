# Decision Report

- generated_at: 2026-07-13T11:21:09.939467+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8631**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.40% / filled 20/20。**
- 全期間 MARKET基準: n=8631, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.01% | **+0.91%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.64% | **+0.51%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |
| LIMIT_5PCT | 5/20 | 25.0% | +1.37% | **+0.34%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +2.67% | **+0.53%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.56% | **+0.42%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.03% | **+0.02%** |
| LIMIT_BB3S_LONG | 3/3 | 100.0% | -0.00% | **-0.00%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | -0.10% | **-0.08%** |

## 2. $100 Live Portfolio

- 残高: **$100.69** / 初期 $100.00 (+0.69%)
- 確定トレード: 92件 (TP 30 / SL 60 / EXP 2)
- 最新: TRIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.69
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$321.77** / 初期 $100.00 (+221.77%)
- 確定: 2799件 (Win 877 / Loss 923 / Flat 999) / skip 2393件
- 成長率目線: 平均log +0.000418 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DODO/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.12% 残高後 $321.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.11** / 初期 $100.00 (+5.11%)
- 確定: 645件 (Win 152 / Loss 159 / Flat 334) / skip 1397件
- 成長率目線: 平均log +0.000077 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ANSEM/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $105.11

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.49** / 初期 $100.00 (-0.51%)
- 確定: 36件 (Win 13 / Loss 23 / Flat 0) / pending 3件 / skip 62件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000499 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: DODO/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $99.49

## 6. Latest Market Context

- 更新: 2026-07-13T11:21:02.731888+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.20% price=62973.3
- Funnel: target 867 → liquid 142 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.5 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DODO/USDT:USDT | +41.22% | $8,472,169.07 |
| JCT/USDT:USDT | +27.46% | $1,577,309.00 |
| XEC/USDT:USDT | +26.92% | $5,198,704.28 |
| KITE/USDT:USDT | +20.45% | $3,363,855.13 |
| BILL/USDT:USDT | +10.06% | $13,758,021.34 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ALLO/USDT:USDT | below_1h_threshold | +3.08% | +2.88% |
| BILL/USDT:USDT | below_1h_threshold | +2.80% | +2.60% |
| XEC/USDT:USDT | below_1h_threshold | +2.09% | +1.88% |
| B/USDT:USDT | below_1h_threshold | +2.05% | +1.84% |
| BASED/USDT:USDT | below_1h_threshold | +1.54% | +1.33% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
