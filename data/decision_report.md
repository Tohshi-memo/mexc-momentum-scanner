# Decision Report

- generated_at: 2026-08-19T01:26:26.759400+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11934**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.47% / filled 20/20。**
- 全期間 MARKET基準: n=11934, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.47%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.47% | **+1.47%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.47% | **+1.47%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.71% | **+0.61%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 14/20 | 70.0% | +3.25% | **+2.28%** |
| LIMIT_3PCT_LONG | 17/20 | 85.0% | +1.30% | **+1.10%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +1.68% | **+0.92%** |
| LIMIT_4PCT_LONG | 15/20 | 75.0% | +0.99% | **+0.74%** |
| LIMIT_2PCT_LONG | 19/20 | 95.0% | +0.67% | **+0.63%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$614.51** / 初期 $100.00 (+514.51%)
- 確定: 4211件 (Win 1295 / Loss 1375 / Flat 1541) / skip 4284件
- 成長率目線: 平均log +0.000431 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIULAI/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $614.51

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.70** / 初期 $100.00 (+54.70%)
- 確定: 1821件 (Win 502 / Loss 428 / Flat 891) / skip 3524件
- 成長率目線: 平均log +0.000240 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UNITREE/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $154.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.12** / 初期 $100.00 (+18.12%)
- 確定: 1724件 (Win 516 / Loss 657 / Flat 551) / pending 0件 / skip 1681件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000208 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: GPS/USDT:USDT `MARKET` EXPIRED account +0.01% 残高後 $118.12

## 6. Latest Market Context

- 更新: 2026-08-19T01:26:16.549422+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=64431.6
- Funnel: target 993 → liquid 181 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| UNITREE/USDT:USDT | +27.31% | $2,124,163.65 |
| TRIA/USDT:USDT | +17.94% | $3,785,543.32 |
| BTW/USDT:USDT | +12.96% | $23,206,711.47 |
| NIULAI/USDT:USDT | +11.99% | $5,846,794.62 |
| PUMPFUN/USDT:USDT | +10.45% | $27,426,628.22 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CAP/USDT:USDT | below_1h_threshold | +3.09% | +3.13% |
| TRIA/USDT:USDT | below_1h_threshold | +1.46% | +1.50% |
| GPS/USDT:USDT | below_1h_threshold | +1.14% | +1.19% |
| SKDD/USDT:USDT | below_1h_threshold | +1.10% | +1.14% |
| FHE/USDT:USDT | below_1h_threshold | +0.87% | +0.92% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
