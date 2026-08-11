# Decision Report

- generated_at: 2026-08-11T09:26:23.508104+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11235**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.57% / filled 20/20。**
- 全期間 MARKET基準: n=11235, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.57%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.57% | **+0.57%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 14/20 | 70.0% | +1.16% | **+0.81%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| MARKET | 20/20 | 100.0% | +0.57% | **+0.57%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.67% | **+0.33%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.34% | **+0.32%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.68% | **+0.93%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +5.35% | **+0.80%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.11% | **+0.61%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.00% | **+0.60%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.70% | **+0.56%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 177件 (TP 68 / SL 104 / EXP 5)
- 最新: EPIC/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.17
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$616.77** / 初期 $100.00 (+516.77%)
- 確定: 3937件 (Win 1230 / Loss 1285 / Flat 1422) / skip 3859件
- 成長率目線: 平均log +0.000462 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLUAI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $616.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$141.89** / 初期 $100.00 (+41.89%)
- 確定: 1514件 (Win 424 / Loss 361 / Flat 729) / skip 3132件
- 成長率目線: 平均log +0.000231 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLUAI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $141.89

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.04** / 初期 $100.00 (+15.04%)
- 確定: 1329件 (Win 407 / Loss 523 / Flat 399) / pending 2件 / skip 1378件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000158 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BLUAI/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $115.04

## 6. Latest Market Context

- 更新: 2026-08-11T09:26:14.123204+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=64167.5
- Funnel: target 963 → liquid 195 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLUAI/USDT:USDT | +89.99% | $19,045,072.19 |
| BTR/USDT:USDT | +37.88% | $1,150,984.44 |
| TOAD/USDT:USDT | +29.06% | $1,444,367.49 |
| VELVET/USDT:USDT | +20.24% | $1,791,758.05 |
| CYS/USDT:USDT | +19.44% | $26,784,629.02 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSV/USDT:USDT | below_1h_threshold | +2.90% | +2.81% |
| HEI/USDT:USDT | below_1h_threshold | +2.42% | +2.33% |
| BANANAS31/USDT:USDT | below_1h_threshold | +2.22% | +2.13% |
| LINK/USDT:USDT | below_1h_threshold | +2.22% | +2.13% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.05% | +1.96% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
