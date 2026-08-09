# Decision Report

- generated_at: 2026-08-09T03:36:33.583700+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10927**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.77% / filled 20/20。**
- 全期間 MARKET基準: n=10927, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.77%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.77% | **+0.77%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 13/20 | 65.0% | +1.96% | **+1.27%** |
| MARKET | 20/20 | 100.0% | +0.77% | **+0.77%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.92% | **+0.58%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_BB3S | 3/15 | 20.0% | +1.21% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.77% | **+0.73%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +4.10% | **+0.62%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +0.45% | **+0.14%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.04% | **+0.03%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.03% | **+0.01%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$637.63** / 初期 $100.00 (+537.63%)
- 確定: 3928件 (Win 1230 / Loss 1278 / Flat 1420) / skip 3560件
- 成長率目線: 平均log +0.000472 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BEAT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $637.63

## 4. Robust Adaptive DryRun ($100)

- 残高: **$142.00** / 初期 $100.00 (+42.00%)
- 確定: 1511件 (Win 424 / Loss 360 / Flat 727) / skip 2827件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0203 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CAT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $142.00

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.44** / 初期 $100.00 (+17.44%)
- 確定: 1248件 (Win 390 / Loss 480 / Flat 378) / pending 0件 / skip 1155件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `見送り` (no_strategy_passed_causal_filters) / causal_score n/a / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CAP/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account -0.10% 残高後 $117.44

## 6. Latest Market Context

- 更新: 2026-08-09T03:36:21.790493+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=64749.3
- Funnel: target 961 → liquid 152 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 97.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TUT/USDT:USDT | +93.40% | $29,944,744.88 |
| IOTX/USDT:USDT | +40.26% | $2,582,182.76 |
| BLUAI/USDT:USDT | +25.40% | $7,815,347.75 |
| SAGA/USDT:USDT | +22.16% | $1,467,067.29 |
| COOKIE/USDT:USDT | +21.35% | $4,024,098.93 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TST/USDT:USDT | below_1h_threshold | +3.02% | +3.09% |
| SAGA/USDT:USDT | below_1h_threshold | +1.86% | +1.93% |
| CAP/USDT:USDT | below_1h_threshold | +1.58% | +1.65% |
| DODO/USDT:USDT | below_1h_threshold | +1.23% | +1.30% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.18% | +1.26% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
