# Decision Report

- generated_at: 2026-08-09T00:51:27.802295+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10903**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10903, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.84%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.84% | **-0.84%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +0.49% | **+0.47%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +4.60% | **+0.46%** |
| LIMIT_9PCT | 5/20 | 25.0% | +0.12% | **+0.03%** |
| LIMIT_8PCT | 5/20 | 25.0% | -0.06% | **-0.01%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | -0.09% | **-0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.82% | **+1.00%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.96% | **+0.78%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +2.02% | **+0.71%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.44% | **+0.57%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +1.60% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$648.45** / 初期 $100.00 (+548.45%)
- 確定: 3904件 (Win 1227 / Loss 1270 / Flat 1407) / skip 3560件
- 成長率目線: 平均log +0.000479 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TAKE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.42% 残高後 $648.45

## 4. Robust Adaptive DryRun ($100)

- 残高: **$142.00** / 初期 $100.00 (+42.00%)
- 確定: 1511件 (Win 424 / Loss 360 / Flat 727) / skip 2803件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0030 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CAT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $142.00

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.44** / 初期 $100.00 (+17.44%)
- 確定: 1248件 (Win 390 / Loss 480 / Flat 378) / pending 0件 / skip 1129件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000058 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CAP/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account -0.10% 残高後 $117.44

## 6. Latest Market Context

- 更新: 2026-08-09T00:51:13.790591+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=64929.7
- Funnel: target 961 → liquid 153 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.8 >= 65=1, 4h RSI 89.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TUT/USDT:USDT | +47.92% | $23,845,492.99 |
| COOKIE/USDT:USDT | +34.80% | $3,487,388.25 |
| BLUAI/USDT:USDT | +22.09% | $7,329,894.39 |
| BTW/USDT:USDT | +16.45% | $15,889,193.45 |
| CYS/USDT:USDT | +15.10% | $30,772,240.20 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +3.92% | +3.92% |
| US/USDT:USDT | below_1h_threshold | +3.53% | +3.52% |
| ZBT/USDT:USDT | below_1h_threshold | +2.76% | +2.75% |
| TAO/USDT:USDT | below_1h_threshold | +2.70% | +2.70% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.99% | +1.99% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
