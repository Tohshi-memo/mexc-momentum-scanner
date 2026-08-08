# Decision Report

- generated_at: 2026-08-08T03:51:34.373086+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10804**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10804, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.02%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.02% | **-1.02%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 8/20 | 40.0% | +1.57% | **+0.63%** |
| LIMIT_8PCT | 10/20 | 50.0% | +1.14% | **+0.57%** |
| LIMIT_10PCT | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_BB3S | 6/15 | 40.0% | +0.79% | **+0.32%** |
| LIMIT_7PCT | 11/20 | 55.0% | -0.11% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +5.00% | **+4.00%** |
| LIMIT_9PCT_LONG | 8/20 | 40.0% | +5.48% | **+2.19%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +4.50% | **+2.02%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +3.36% | **+1.85%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +5.79% | **+1.45%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$607.53** / 初期 $100.00 (+507.53%)
- 確定: 3806件 (Win 1206 / Loss 1252 / Flat 1348) / skip 3559件
- 成長率目線: 平均log +0.000474 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $607.53

## 4. Robust Adaptive DryRun ($100)

- 残高: **$142.00** / 初期 $100.00 (+42.00%)
- 確定: 1510件 (Win 424 / Loss 360 / Flat 726) / skip 2705件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0922 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $142.00

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.02** / 初期 $100.00 (+18.02%)
- 確定: 1182件 (Win 381 / Loss 468 / Flat 333) / pending 0件 / skip 1094件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000223 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AXTISTOCK/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $118.02

## 6. Latest Market Context

- 更新: 2026-08-08T03:51:23.460971+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.17% price=64999.0
- Funnel: target 961 → liquid 180 → pre 50 → checked 50 → surge 4 → strict 0
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.3 >= 65=1, 4h RSI 84.0 >= 65=1, 4h RSI 78.5 >= 65=1, 4h RSI 93.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +283.06% | $5,469,863.42 |
| BLESS/USDT:USDT | +27.48% | $95,311,315.91 |
| MMT/USDT:USDT | +19.32% | $1,374,264.33 |
| TUT/USDT:USDT | +16.09% | $2,403,826.08 |
| BSB/USDT:USDT | +15.66% | $3,045,427.47 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RBRKSTOCK/USDT:USDT | below_1h_threshold | +4.20% | +4.04% |
| CYS/USDT:USDT | below_1h_threshold | +3.05% | +2.88% |
| BSB/USDT:USDT | below_1h_threshold | +2.88% | +2.71% |
| CAP/USDT:USDT | below_1h_threshold | +2.23% | +2.07% |
| SLX/USDT:USDT | below_1h_threshold | +2.20% | +2.03% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
