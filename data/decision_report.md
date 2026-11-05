# Decision Report

- generated_at: 2026-11-05T12:21:20.532753+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18178**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.66% / filled 20/20。**
- 全期間 MARKET基準: n=18178, expectancy=+0.03%
- 直近20件 MARKET基準: n=20, expectancy=+3.66%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.66% | **+3.66%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.66% | **+3.66%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_3PCT | 9/20 | 45.0% | +0.72% | **+0.32%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 9/20 | 45.0% | +3.03% | **+1.36%** |
| LIMIT_10PCT_LONG | 7/20 | 35.0% | +3.75% | **+1.31%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | +1.09% | **+0.60%** |
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | -0.44% | **-0.13%** |
| LIMIT_BB3S_LONG | 4/4 | 100.0% | -0.88% | **-0.88%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 262件 (TP 96 / SL 158 / EXP 8)
- 最新: SOXS/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,502.99** / 初期 $100.00 (+1402.99%)
- 確定: 6997件 (Win 2020 / Loss 2243 / Flat 2734) / skip 7742件
- 成長率目線: 平均log +0.000387 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LYN/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $1,502.99

## 4. Robust Adaptive DryRun ($100)

- 残高: **$372.54** / 初期 $100.00 (+272.54%)
- 確定: 4570件 (Win 1225 / Loss 1030 / Flat 2315) / skip 7019件
- 成長率目線: 平均log +0.000288 / 幾何平均 +0.029% per trade / maxDD +4.25%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0087 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LYN/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $372.54

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6336件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000436 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-05T12:21:09.750588+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.30% price=80149.0
- Funnel: target 1077 → liquid 180 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIO/USDT:USDT | +42.43% | $1,016,390.17 |
| APPSTOCK/USDT:USDT | +20.09% | $1,839,723.11 |
| FLUID/USDT:USDT | +19.34% | $7,317,184.27 |
| UAI/USDT:USDT | +15.60% | $7,227,598.93 |
| ARIA/USDT:USDT | +15.16% | $1,552,816.03 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ARIA/USDT:USDT | below_1h_threshold | +4.08% | +4.38% |
| ELSA/USDT:USDT | below_1h_threshold | +2.62% | +2.92% |
| APPSTOCK/USDT:USDT | below_1h_threshold | +2.46% | +2.76% |
| MRNASTOCK/USDT:USDT | below_1h_threshold | +1.02% | +1.32% |
| UAI/USDT:USDT | below_1h_threshold | +0.99% | +1.29% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
