# Decision Report

- generated_at: 2026-11-10T14:41:43.342253+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18604**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18604, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.68%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.68% | **-0.68%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 12/20 | 60.0% | +1.54% | **+0.92%** |
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.89% | **+0.57%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.65% | **+0.29%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.29% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.57% | **+1.80%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.80% | **+0.99%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.10% | **+0.94%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +2.35% | **+0.82%** |
| MARKET_LONG | 20/20 | 100.0% | +0.69% | **+0.69%** |

## 2. $100 Live Portfolio

- 残高: **$121.13** / 初期 $100.00 (+21.13%)
- 確定トレード: 268件 (TP 97 / SL 163 / EXP 8)
- 最新: CRWVSTOCK/USDT:USDT SL_HIT PnL -2.78% 残高後 $121.13
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,691.39** / 初期 $100.00 (+1591.39%)
- 確定: 7201件 (Win 2072 / Loss 2299 / Flat 2830) / skip 7964件
- 成長率目線: 平均log +0.000393 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IDOL/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $1,691.39

## 4. Robust Adaptive DryRun ($100)

- 残高: **$395.86** / 初期 $100.00 (+295.86%)
- 確定: 4770件 (Win 1282 / Loss 1051 / Flat 2437) / skip 7245件
- 成長率目線: 平均log +0.000288 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0480 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: IDOL/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $395.86

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6764件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000287 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-10T14:41:23.507934+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.72% price=74245.0
- Funnel: target 1099 → liquid 148 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| INIT/USDT:USDT | +97.69% | $23,373,121.51 |
| ONE/USDT:USDT | +17.97% | $9,666,819.74 |
| ARIA/USDT:USDT | +16.79% | $2,715,736.83 |
| ZHIPUSTOCK/USDT:USDT | +10.38% | $1,618,964.83 |
| BR/USDT:USDT | +10.15% | $3,788,625.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXS/USDT:USDT | below_1h_threshold | +4.73% | +4.01% |
| LIT/USDT:USDT | below_1h_threshold | +3.89% | +3.17% |
| ARIA/USDT:USDT | below_1h_threshold | +3.80% | +3.08% |
| SQQQ/USDT:USDT | below_1h_threshold | +2.89% | +2.17% |
| PEPE/USDT:USDT | below_1h_threshold | +2.54% | +1.82% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
