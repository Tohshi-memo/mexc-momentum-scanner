# Decision Report

- generated_at: 2026-10-30T04:31:21.898813+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17824**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.44% / filled 20/20。**
- 全期間 MARKET基準: n=17824, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.44%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.44% | **+0.44%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.44% | **+0.44%** |
| LIMIT_BB3S | 2/16 | 12.5% | +2.63% | **+0.33%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.22% | **+0.05%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.02% | **+0.01%** |
| LIMIT_4PCT | 11/20 | 55.0% | -0.15% | **-0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.68% | **+0.55%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.12% | **+0.50%** |
| MARKET_LONG | 20/20 | 100.0% | +0.19% | **+0.19%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 256件 (TP 94 / SL 154 / EXP 8)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,523.56** / 初期 $100.00 (+1423.56%)
- 確定: 6805件 (Win 1975 / Loss 2181 / Flat 2649) / skip 7580件
- 成長率目線: 平均log +0.000400 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `MARKET` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EVAA/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,523.56

## 4. Robust Adaptive DryRun ($100)

- 残高: **$363.77** / 初期 $100.00 (+263.77%)
- 確定: 4341件 (Win 1168 / Loss 980 / Flat 2193) / skip 6894件
- 成長率目線: 平均log +0.000297 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0028 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: Q/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $363.77

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5984件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000325 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-30T04:31:09.042483+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.21% price=78363.0
- Funnel: target 1086 → liquid 194 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PARTI/USDT:USDT | +61.92% | $7,274,791.13 |
| Q/USDT:USDT | +39.75% | $24,097,332.13 |
| SOXS/USDT:USDT | +17.97% | $69,607,691.91 |
| BLESS/USDT:USDT | +11.28% | $14,197,079.42 |
| RUNE/USDT:USDT | +8.51% | $1,254,378.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PREDICT/USDT:USDT | below_1h_threshold | +2.83% | +2.62% |
| INIT/USDT:USDT | below_1h_threshold | +1.09% | +0.88% |
| XPD/USDT:USDT | below_1h_threshold | +0.46% | +0.25% |
| GOOGLSTOCK/USDT:USDT | below_1h_threshold | +0.42% | +0.21% |
| BULLA/USDT:USDT | below_1h_threshold | +0.41% | +0.20% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
