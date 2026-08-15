# Decision Report

- generated_at: 2026-08-15T10:41:30.710616+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11658**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.80% / filled 20/20。**
- 全期間 MARKET基準: n=11658, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+3.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.80% | **+3.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.80% | **+3.80%** |
| LIMIT_2PCT | 14/20 | 70.0% | +4.44% | **+3.11%** |
| LIMIT_1PCT | 17/20 | 85.0% | +3.30% | **+2.81%** |
| LIMIT_3PCT | 12/20 | 60.0% | +3.51% | **+2.11%** |
| LIMIT_BB3S | 4/16 | 25.0% | +3.72% | **+0.93%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 8/20 | 40.0% | +4.33% | **+1.73%** |
| LIMIT_9PCT_LONG | 9/20 | 45.0% | +3.03% | **+1.36%** |
| LIMIT_8PCT_LONG | 14/20 | 70.0% | +1.43% | **+1.00%** |
| LIMIT_7PCT_LONG | 15/20 | 75.0% | -0.02% | **-0.02%** |
| LIMIT_FIB1272_LONG | 14/20 | 70.0% | -0.04% | **-0.03%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$644.59** / 初期 $100.00 (+544.59%)
- 確定: 4126件 (Win 1290 / Loss 1354 / Flat 1482) / skip 4093件
- 成長率目線: 平均log +0.000452 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ANSEM/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $644.59

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.41** / 初期 $100.00 (+55.41%)
- 確定: 1721件 (Win 489 / Loss 412 / Flat 820) / skip 3348件
- 成長率目線: 平均log +0.000256 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1149 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ANSEM/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $155.41

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.92** / 初期 $100.00 (+18.92%)
- 確定: 1600件 (Win 487 / Loss 605 / Flat 508) / pending 4件 / skip 1525件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000274 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: COW/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $118.92

## 6. Latest Market Context

- 更新: 2026-08-15T10:41:17.551732+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=63006.0
- Funnel: target 985 → liquid 161 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COW/USDT:USDT | +46.00% | $3,281,386.50 |
| ANSEM/USDT:USDT | +32.14% | $1,383,731.54 |
| ROBO/USDT:USDT | +24.17% | $7,129,792.52 |
| BMT/USDT:USDT | +22.00% | $1,097,696.66 |
| US/USDT:USDT | +20.20% | $6,158,584.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ROBO/USDT:USDT | below_1h_threshold | +3.48% | +3.47% |
| US/USDT:USDT | below_1h_threshold | +2.92% | +2.91% |
| AIO/USDT:USDT | below_1h_threshold | +2.16% | +2.15% |
| RE/USDT:USDT | below_1h_threshold | +1.86% | +1.85% |
| TUT/USDT:USDT | below_1h_threshold | +1.68% | +1.67% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
