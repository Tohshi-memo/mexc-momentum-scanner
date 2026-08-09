# Decision Report

- generated_at: 2026-08-09T02:56:38.005443+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10921**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10921, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.52%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.52% | **-0.52%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +1.92% | **+0.67%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.37% | **+0.26%** |
| LIMIT_BB3S | 3/15 | 20.0% | +1.21% | **+0.24%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.35% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +1.77% | **+1.77%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.64% | **+1.14%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.85% | **+1.11%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.23% | **+0.62%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.21% | **+0.48%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$643.23** / 初期 $100.00 (+543.23%)
- 確定: 3922件 (Win 1229 / Loss 1275 / Flat 1418) / skip 3560件
- 成長率目線: 平均log +0.000475 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TUT/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $643.23

## 4. Robust Adaptive DryRun ($100)

- 残高: **$142.00** / 初期 $100.00 (+42.00%)
- 確定: 1511件 (Win 424 / Loss 360 / Flat 727) / skip 2821件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0239 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CAT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $142.00

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.44** / 初期 $100.00 (+17.44%)
- 確定: 1248件 (Win 390 / Loss 480 / Flat 378) / pending 0件 / skip 1150件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `見送り` (no_strategy_passed_causal_filters) / causal_score n/a / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CAP/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account -0.10% 残高後 $117.44

## 6. Latest Market Context

- 更新: 2026-08-09T02:56:24.527146+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=64795.9
- Funnel: target 961 → liquid 151 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.3 >= 65=1, 4h RSI 97.7 >= 65=1, 4h RSI 72.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TUT/USDT:USDT | +87.87% | $27,753,546.55 |
| IOTX/USDT:USDT | +53.88% | $2,051,274.69 |
| BLUAI/USDT:USDT | +24.96% | $7,692,073.62 |
| BICO/USDT:USDT | +23.46% | $30,765,371.49 |
| COOKIE/USDT:USDT | +22.89% | $3,962,823.88 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZBT/USDT:USDT | below_1h_threshold | +4.72% | +4.79% |
| FORM/USDT:USDT | below_1h_threshold | +4.68% | +4.75% |
| GIGGLE/USDT:USDT | below_1h_threshold | +3.66% | +3.73% |
| SAGA/USDT:USDT | below_1h_threshold | +3.53% | +3.60% |
| BLUAI/USDT:USDT | below_1h_threshold | +3.48% | +3.55% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
