# Decision Report

- generated_at: 2026-07-16T03:36:18.288531+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8784**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.82% / filled 20/20。**
- 全期間 MARKET基準: n=8784, expectancy=+0.01%
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
| LIMIT_1PCT | 19/20 | 95.0% | +1.80% | **+1.71%** |
| LIMIT_2PCT | 17/20 | 85.0% | +1.55% | **+1.31%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.89% | **+1.23%** |
| LIMIT_6PCT | 6/20 | 30.0% | +2.94% | **+0.88%** |

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
- 確定: 2900件 (Win 906 / Loss 943 / Flat 1051) / skip 2445件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: US/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $338.95

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.89** / 初期 $100.00 (+6.89%)
- 確定: 748件 (Win 171 / Loss 169 / Flat 408) / skip 1447件
- 成長率目線: 平均log +0.000089 / 幾何平均 +0.009% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0452 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: US/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.15% 残高後 $106.89

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.49** / 初期 $100.00 (-1.51%)
- 確定: 64件 (Win 19 / Loss 41 / Flat 4) / pending 0件 / skip 192件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000517 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: XEC/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account -0.09% 残高後 $98.49

## 6. Latest Market Context

- 更新: 2026-07-16T03:36:11.853411+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=64694.9
- Funnel: target 873 → liquid 171 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.9 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CAP/USDT:USDT | +22.14% | $2,090,387.91 |
| HOME/USDT:USDT | +15.31% | $2,063,188.13 |
| US/USDT:USDT | +12.55% | $10,502,346.46 |
| ROAM/USDT:USDT | +10.89% | $5,687,589.91 |
| LDO/USDT:USDT | +10.20% | $7,872,229.12 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CAP/USDT:USDT | below_1h_threshold | +2.46% | +2.33% |
| BANK/USDT:USDT | below_1h_threshold | +2.19% | +2.06% |
| SOXL/USDT:USDT | below_1h_threshold | +2.08% | +1.96% |
| NICKEL/USDT:USDT | below_1h_threshold | +1.75% | +1.63% |
| SNXX/USDT:USDT | below_1h_threshold | +1.70% | +1.58% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
