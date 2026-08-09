# Decision Report

- generated_at: 2026-08-09T04:26:24.722773+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10934**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.60% / filled 20/20。**
- 全期間 MARKET基準: n=10934, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.60% | **+1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 11/20 | 55.0% | +3.14% | **+1.73%** |
| MARKET | 20/20 | 100.0% | +1.60% | **+1.60%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.29% | **+1.16%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.05% | **+0.84%** |
| LIMIT_3PCT | 12/20 | 60.0% | +1.02% | **+0.61%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +3.21% | **+0.64%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.59% | **+0.26%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | -0.00% | **-0.00%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | -0.40% | **-0.12%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | -0.67% | **-0.30%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$631.27** / 初期 $100.00 (+531.27%)
- 確定: 3930件 (Win 1230 / Loss 1280 / Flat 1420) / skip 3565件
- 成長率目線: 平均log +0.000469 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TST/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $631.27

## 4. Robust Adaptive DryRun ($100)

- 残高: **$142.00** / 初期 $100.00 (+42.00%)
- 確定: 1511件 (Win 424 / Loss 360 / Flat 727) / skip 2834件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score -0.0075 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CAT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $142.00

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.44** / 初期 $100.00 (+17.44%)
- 確定: 1248件 (Win 390 / Loss 480 / Flat 378) / pending 0件 / skip 1161件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000069 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CAP/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account -0.10% 残高後 $117.44

## 6. Latest Market Context

- 更新: 2026-08-09T04:26:16.072238+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=64785.0
- Funnel: target 961 → liquid 152 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.1 >= 65=1, 4h RSI 75.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TUT/USDT:USDT | +100.91% | $31,041,092.68 |
| SAGA/USDT:USDT | +36.02% | $1,751,843.65 |
| BLUAI/USDT:USDT | +35.99% | $8,033,522.83 |
| IOTX/USDT:USDT | +35.43% | $3,006,297.04 |
| COOKIE/USDT:USDT | +24.43% | $4,168,407.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +4.19% | +4.15% |
| TUT/USDT:USDT | below_1h_threshold | +2.75% | +2.71% |
| COOKIE/USDT:USDT | below_1h_threshold | +2.19% | +2.15% |
| PIXEL/USDT:USDT | below_1h_threshold | +2.16% | +2.12% |
| UB/USDT:USDT | below_1h_threshold | +1.77% | +1.73% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
