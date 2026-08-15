# Decision Report

- generated_at: 2026-08-15T10:26:33.232797+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11656**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.20% / filled 20/20。**
- 全期間 MARKET基準: n=11656, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+3.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.20% | **+3.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.20% | **+3.20%** |
| LIMIT_2PCT | 15/20 | 75.0% | +4.02% | **+3.01%** |
| LIMIT_3PCT | 13/20 | 65.0% | +3.86% | **+2.51%** |
| LIMIT_1PCT | 17/20 | 85.0% | +2.66% | **+2.26%** |
| LIMIT_4PCT | 8/20 | 40.0% | +3.00% | **+1.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 7/20 | 35.0% | +4.63% | **+1.62%** |
| LIMIT_9PCT_LONG | 8/20 | 40.0% | +3.91% | **+1.56%** |
| LIMIT_8PCT_LONG | 13/20 | 65.0% | +1.85% | **+1.20%** |
| LIMIT_5PCT_LONG | 16/20 | 80.0% | +0.61% | **+0.48%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -0.37% | **-0.07%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$647.83** / 初期 $100.00 (+547.83%)
- 確定: 4124件 (Win 1290 / Loss 1353 / Flat 1481) / skip 4093件
- 成長率目線: 平均log +0.000453 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: COW/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $647.83

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.96** / 初期 $100.00 (+55.96%)
- 確定: 1719件 (Win 489 / Loss 411 / Flat 819) / skip 3348件
- 成長率目線: 平均log +0.000259 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1219 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: COW/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $155.96

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.51** / 初期 $100.00 (+18.51%)
- 確定: 1599件 (Win 486 / Loss 605 / Flat 508) / pending 3件 / skip 1525件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000398 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: COW/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $118.51

## 6. Latest Market Context

- 更新: 2026-08-15T10:26:20.201174+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=62996.1
- Funnel: target 985 → liquid 161 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 92.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COW/USDT:USDT | +59.10% | $2,711,067.04 |
| ANSEM/USDT:USDT | +27.76% | $1,356,883.90 |
| ROBO/USDT:USDT | +20.94% | $7,060,114.45 |
| US/USDT:USDT | +20.17% | $6,125,214.79 |
| VELVET/USDT:USDT | +19.37% | $33,924,223.49 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ANSEM/USDT:USDT | below_1h_threshold | +3.66% | +3.67% |
| US/USDT:USDT | below_1h_threshold | +2.89% | +2.90% |
| RE/USDT:USDT | below_1h_threshold | +1.73% | +1.73% |
| AIO/USDT:USDT | below_1h_threshold | +1.28% | +1.29% |
| ONE/USDT:USDT | below_1h_threshold | +0.95% | +0.96% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
