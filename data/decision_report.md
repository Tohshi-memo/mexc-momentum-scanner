# Decision Report

- generated_at: 2026-08-07T22:51:22.877475+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10769**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10769, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.93%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.93% | **-0.93%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 18/20 | 90.0% | +1.13% | **+1.02%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +4.98% | **+0.75%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.47% | **+0.69%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.42% | **+0.64%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.57% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.16% | **+1.29%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.00% | **+1.20%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.62% | **+0.89%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.79% | **+0.67%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +1.07% | **+0.43%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$595.60** / 初期 $100.00 (+495.60%)
- 確定: 3800件 (Win 1203 / Loss 1250 / Flat 1347) / skip 3530件
- 成長率目線: 平均log +0.000470 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $595.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$144.23** / 初期 $100.00 (+44.23%)
- 確定: 1486件 (Win 419 / Loss 349 / Flat 718) / skip 2694件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0511 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $144.23

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.23** / 初期 $100.00 (+18.23%)
- 確定: 1181件 (Win 381 / Loss 467 / Flat 333) / pending 1件 / skip 1060件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000081 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MMT/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $118.23

## 6. Latest Market Context

- 更新: 2026-08-07T22:51:14.103738+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=64870.6
- Funnel: target 961 → liquid 185 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.9 >= 65=1, 4h RSI 70.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +94.60% | $2,969,786.24 |
| BLESS/USDT:USDT | +29.38% | $76,011,824.83 |
| GWEI/USDT:USDT | +25.26% | $1,645,350.70 |
| EPIC/USDT:USDT | +17.10% | $2,235,088.61 |
| CYS/USDT:USDT | +12.15% | $15,249,220.11 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BICO/USDT:USDT | below_1h_threshold | +4.74% | +4.78% |
| MMT/USDT:USDT | below_1h_threshold | +3.96% | +3.99% |
| BTW/USDT:USDT | below_1h_threshold | +3.86% | +3.90% |
| CYS/USDT:USDT | below_1h_threshold | +3.81% | +3.85% |
| HEI/USDT:USDT | below_1h_threshold | +2.27% | +2.30% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
