# Decision Report

- generated_at: 2026-07-16T03:21:16.320552+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8783**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.82% / filled 20/20。**
- 全期間 MARKET基準: n=8783, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.82%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.82% | **+1.82%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.82% | **+1.82%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.86% | **+1.77%** |
| LIMIT_2PCT | 17/20 | 85.0% | +1.67% | **+1.42%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.97% | **+1.28%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.15% | **+0.79%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +2.04% | **+0.51%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.82% | **+0.45%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.40% | **+0.20%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +0.10% | **+0.02%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | -1.63% | **-0.82%** |

## 2. $100 Live Portfolio

- 残高: **$106.34** / 初期 $100.00 (+6.34%)
- 確定トレード: 102件 (TP 37 / SL 63 / EXP 2)
- 最新: PI/USDT:USDT TP_HIT PnL +8.00% 残高後 $106.34
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$338.95** / 初期 $100.00 (+238.95%)
- 確定: 2899件 (Win 906 / Loss 943 / Flat 1050) / skip 2445件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: US/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $338.95

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.72** / 初期 $100.00 (+6.72%)
- 確定: 747件 (Win 170 / Loss 169 / Flat 408) / skip 1447件
- 成長率目線: 平均log +0.000087 / 幾何平均 +0.009% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0411 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: US/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.72

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.49** / 初期 $100.00 (-1.51%)
- 確定: 64件 (Win 19 / Loss 41 / Flat 4) / pending 0件 / skip 191件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000517 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: XEC/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account -0.09% 残高後 $98.49

## 6. Latest Market Context

- 更新: 2026-07-16T03:21:09.823289+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=64602.1
- Funnel: target 873 → liquid 171 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.7 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CAP/USDT:USDT | +18.71% | $2,034,255.09 |
| HOME/USDT:USDT | +15.89% | $2,055,551.51 |
| US/USDT:USDT | +13.07% | $10,245,299.59 |
| SKL/USDT:USDT | +11.72% | $1,890,711.44 |
| ROAM/USDT:USDT | +11.43% | $5,684,300.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BANK/USDT:USDT | below_1h_threshold | +4.61% | +4.64% |
| AKE/USDT:USDT | below_1h_threshold | +3.18% | +3.21% |
| SKL/USDT:USDT | below_1h_threshold | +2.82% | +2.84% |
| SOXL/USDT:USDT | below_1h_threshold | +2.08% | +2.10% |
| NICKEL/USDT:USDT | below_1h_threshold | +1.75% | +1.78% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
