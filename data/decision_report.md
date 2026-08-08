# Decision Report

- generated_at: 2026-08-08T03:31:25.786754+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10798**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10798, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.18%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.18% | **+0.18%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 6/20 | 30.0% | +1.43% | **+0.43%** |
| LIMIT_7PCT | 8/20 | 40.0% | +0.70% | **+0.28%** |
| LIMIT_6PCT | 8/20 | 40.0% | +0.47% | **+0.19%** |
| MARKET | 20/20 | 100.0% | +0.18% | **+0.18%** |
| LIMIT_BB3S | 4/18 | 22.2% | +0.18% | **+0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +2.29% | **+1.14%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +3.14% | **+1.10%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +5.24% | **+1.05%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +1.83% | **+0.82%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +1.38% | **+0.69%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$598.55** / 初期 $100.00 (+498.55%)
- 確定: 3802件 (Win 1204 / Loss 1251 / Flat 1347) / skip 3557件
- 成長率目線: 平均log +0.000471 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.50% 残高後 $598.55

## 4. Robust Adaptive DryRun ($100)

- 残高: **$142.00** / 初期 $100.00 (+42.00%)
- 確定: 1510件 (Win 424 / Loss 360 / Flat 726) / skip 2699件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0448 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $142.00

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.02** / 初期 $100.00 (+18.02%)
- 確定: 1182件 (Win 381 / Loss 468 / Flat 333) / pending 0件 / skip 1087件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000107 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AXTISTOCK/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $118.02

## 6. Latest Market Context

- 更新: 2026-08-08T03:31:16.014551+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.17% price=64996.9
- Funnel: target 961 → liquid 180 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +194.72% | $4,917,259.61 |
| BLESS/USDT:USDT | +35.34% | $93,943,527.23 |
| MMT/USDT:USDT | +14.66% | $1,315,145.90 |
| SLX/USDT:USDT | +14.43% | $2,466,301.20 |
| BSB/USDT:USDT | +13.31% | $2,923,246.10 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RBRKSTOCK/USDT:USDT | below_1h_threshold | +4.20% | +4.04% |
| SLX/USDT:USDT | below_1h_threshold | +3.82% | +3.65% |
| UB/USDT:USDT | below_1h_threshold | +3.63% | +3.46% |
| CAP/USDT:USDT | below_1h_threshold | +2.15% | +1.99% |
| TUT/USDT:USDT | below_1h_threshold | +2.11% | +1.94% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
