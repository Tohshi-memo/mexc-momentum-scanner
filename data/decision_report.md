# Decision Report

- generated_at: 2026-11-15T00:51:15.014894+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18923**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.62% / filled 20/20。**
- 全期間 MARKET基準: n=18923, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.62%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.62% | **+0.62%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 9/20 | 45.0% | +1.74% | **+0.78%** |
| MARKET | 20/20 | 100.0% | +0.62% | **+0.62%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_ATR | 9/20 | 45.0% | +0.34% | **+0.15%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.32% | **+0.92%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.29% | **+0.80%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.19% | **+0.72%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.89% | **+0.58%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.24% | **+0.56%** |

## 2. $100 Live Portfolio

- 残高: **$121.01** / 初期 $100.00 (+21.01%)
- 確定トレード: 275件 (TP 99 / SL 168 / EXP 8)
- 最新: JCT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.01
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,746.38** / 初期 $100.00 (+1646.38%)
- 確定: 7327件 (Win 2106 / Loss 2344 / Flat 2877) / skip 8157件
- 成長率目線: 平均log +0.000390 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JCT/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $1,746.38

## 4. Robust Adaptive DryRun ($100)

- 残高: **$427.39** / 初期 $100.00 (+327.39%)
- 確定: 4931件 (Win 1318 / Loss 1080 / Flat 2533) / skip 7403件
- 成長率目線: 平均log +0.000295 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0385 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JCT/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $427.39

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7084件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000215 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-15T00:51:04.054014+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.90% price=63554.9
- Funnel: target 1071 → liquid 136 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SOPH/USDT:USDT | +17.00% | $3,863,710.23 |
| JCT/USDT:USDT | +9.07% | $5,142,102.64 |
| SHELL/USDT:USDT | +8.35% | $2,452,395.56 |
| ARIA/USDT:USDT | +6.85% | $2,347,089.62 |
| INIT/USDT:USDT | +4.99% | $1,978,436.07 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SHELL/USDT:USDT | below_1h_threshold | +4.84% | +5.73% |
| JCT/USDT:USDT | below_1h_threshold | +2.97% | +3.87% |
| INIT/USDT:USDT | below_1h_threshold | +2.97% | +3.86% |
| ARIA/USDT:USDT | below_1h_threshold | +2.72% | +3.61% |
| SOXL/USDT:USDT | below_1h_threshold | +1.73% | +2.62% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
