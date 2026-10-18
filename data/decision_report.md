# Decision Report

- generated_at: 2026-10-18T04:51:21.587308+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16940**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.75% / filled 20/20。**
- 全期間 MARKET基準: n=16940, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.75%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.75% | **+1.75%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.75% | **+1.75%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +4.22% | **+1.69%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.13% | **+0.85%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.88% | **+0.75%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.99% | **+0.69%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +6.27% | **+1.25%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +1.00% | **+0.65%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +1.35% | **+0.61%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.76% | **+0.42%** |

## 2. $100 Live Portfolio

- 残高: **$121.72** / 初期 $100.00 (+21.72%)
- 確定トレード: 244件 (TP 91 / SL 146 / EXP 7)
- 最新: CLAUDIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.72
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,284.52** / 初期 $100.00 (+1184.52%)
- 確定: 6406件 (Win 1865 / Loss 2050 / Flat 2491) / skip 7095件
- 成長率目線: 平均log +0.000399 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CLAUDIA/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account +0.00% 残高後 $1,284.52

## 4. Robust Adaptive DryRun ($100)

- 残高: **$277.01** / 初期 $100.00 (+177.01%)
- 確定: 3705件 (Win 1031 / Loss 880 / Flat 1794) / skip 6646件
- 成長率目線: 平均log +0.000275 / 幾何平均 +0.028% per trade / maxDD +4.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0009 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CLAUDIA/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $277.01

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5101件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_8PCT` (selected_by_causal_log_growth) / causal_score +0.000151 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-18T04:51:07.401185+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.18% price=81767.7
- Funnel: target 1084 → liquid 138 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLAUDIA/USDT:USDT | +21.22% | $2,410,946.02 |
| AVA/USDT:USDT | +14.99% | $2,428,915.29 |
| BR/USDT:USDT | +12.34% | $11,079,367.10 |
| CYS/USDT:USDT | +10.99% | $1,170,132.87 |
| XMR/USDT:USDT | +9.17% | $7,165,452.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CLAUDIA/USDT:USDT | below_1h_threshold | +3.64% | +3.82% |
| AGT/USDT:USDT | below_1h_threshold | +2.10% | +2.29% |
| BTW/USDT:USDT | below_1h_threshold | +1.72% | +1.90% |
| SAND/USDT:USDT | below_1h_threshold | +1.53% | +1.71% |
| CYS/USDT:USDT | below_1h_threshold | +0.88% | +1.06% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
