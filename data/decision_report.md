# Decision Report

- generated_at: 2026-08-09T08:46:54.830809+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10983**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=10983, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_9PCT | 5/20 | 25.0% | +2.52% | **+0.63%** |
| LIMIT_8PCT | 7/20 | 35.0% | +1.63% | **+0.57%** |
| LIMIT_10PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_7PCT | 7/20 | 35.0% | +0.40% | **+0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +5.60% | **+1.40%** |
| LIMIT_7PCT_LONG | 12/20 | 60.0% | +1.49% | **+0.89%** |
| LIMIT_FIB1272_LONG | 14/20 | 70.0% | +1.26% | **+0.88%** |
| LIMIT_6PCT_LONG | 13/20 | 65.0% | +1.05% | **+0.68%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | -0.18% | **-0.12%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$628.11** / 初期 $100.00 (+528.11%)
- 確定: 3931件 (Win 1230 / Loss 1281 / Flat 1420) / skip 3613件
- 成長率目線: 平均log +0.000467 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: XAI/USDT:USDT `LIMIT_FIB1272_LONG` SL_HIT account -0.50% 残高後 $628.11

## 4. Robust Adaptive DryRun ($100)

- 残高: **$142.00** / 初期 $100.00 (+42.00%)
- 確定: 1512件 (Win 424 / Loss 360 / Flat 728) / skip 2882件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0781 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TUT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $142.00

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.44** / 初期 $100.00 (+17.44%)
- 確定: 1248件 (Win 390 / Loss 480 / Flat 378) / pending 0件 / skip 1216件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000268 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CAP/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account -0.10% 残高後 $117.44

## 6. Latest Market Context

- 更新: 2026-08-09T08:46:33.977139+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=64769.4
- Funnel: target 961 → liquid 156 → pre 50 → checked 50 → surge 7 → strict 5
- Surge前reject: below_1h_threshold=43, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.6 >= 65=1, 4h RSI 90.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TUT/USDT:USDT | +160.44% | $60,239,942.35 |
| IOTX/USDT:USDT | +41.12% | $5,599,215.30 |
| BMT/USDT:USDT | +40.29% | $1,064,531.32 |
| MUBARAK/USDT:USDT | +24.00% | $1,728,346.10 |
| COOKIE/USDT:USDT | +23.92% | $4,898,095.41 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CAP/USDT:USDT | below_1h_threshold | +3.47% | +3.51% |
| MMT/USDT:USDT | below_1h_threshold | +2.90% | +2.93% |
| TUT/USDT:USDT | below_1h_threshold | +2.74% | +2.78% |
| CATI/USDT:USDT | below_1h_threshold | +2.42% | +2.45% |
| INX/USDT:USDT | below_1h_threshold | +2.22% | +2.25% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
