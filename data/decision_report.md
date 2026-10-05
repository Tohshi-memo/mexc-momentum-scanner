# Decision Report

- generated_at: 2026-10-05T22:36:39.949845+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16172**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16172, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.19% | **-0.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +0.76% | **+0.76%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.83% | **+0.58%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_BB3S | 4/15 | 26.7% | +1.76% | **+0.47%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +1.54% | **+1.23%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.66% | **+0.83%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.78% | **+0.43%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +0.44% | **+0.13%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -0.60% | **-0.09%** |

## 2. $100 Live Portfolio

- 残高: **$120.15** / 初期 $100.00 (+20.15%)
- 確定トレード: 230件 (TP 82 / SL 141 / EXP 7)
- 最新: MOVR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.15
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,297.15** / 初期 $100.00 (+1197.15%)
- 確定: 6231件 (Win 1825 / Loss 1990 / Flat 2416) / skip 6502件
- 成長率目線: 平均log +0.000411 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RLC/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $1,297.15

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.46** / 初期 $100.00 (+174.46%)
- 確定: 3610件 (Win 1005 / Loss 845 / Flat 1760) / skip 5973件
- 成長率目線: 平均log +0.000280 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0416 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BATON/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $274.46

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4334件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000133 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-05T22:36:28.615889+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=85915.5
- Funnel: target 1074 → liquid 165 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 96.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RLC/USDT:USDT | +35.98% | $14,879,805.73 |
| ORCA/USDT:USDT | +16.89% | $1,491,609.96 |
| RAY/USDT:USDT | +11.24% | $3,595,424.71 |
| FILECOIN/USDT:USDT | +8.68% | $13,716,526.55 |
| BR/USDT:USDT | +8.31% | $13,358,028.55 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ORCA/USDT:USDT | below_1h_threshold | +2.63% | +2.62% |
| ADA/USDT:USDT | below_1h_threshold | +1.15% | +1.14% |
| RAY/USDT:USDT | below_1h_threshold | +0.94% | +0.93% |
| ZRO/USDT:USDT | below_1h_threshold | +0.88% | +0.87% |
| ONDO/USDT:USDT | below_1h_threshold | +0.72% | +0.71% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
