# Decision Report

- generated_at: 2026-09-24T21:36:29.132668+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15495**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.86% / filled 20/20。**
- 全期間 MARKET基準: n=15495, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.86%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.86% | **+0.86%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.86% | **+0.86%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.71% | **+0.67%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.39% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 7/11 | 63.6% | +2.69% | **+1.71%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.11% | **+0.84%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.77% | **+0.65%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.30% | **+0.65%** |
| MARKET_LONG | 20/20 | 100.0% | +0.62% | **+0.62%** |

## 2. $100 Live Portfolio

- 残高: **$120.08** / 初期 $100.00 (+20.08%)
- 確定トレード: 219件 (TP 79 / SL 135 / EXP 5)
- 最新: XPL/USDT:USDT SL_HIT PnL -3.85% 残高後 $120.08
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,197.79** / 初期 $100.00 (+1097.79%)
- 確定: 5900件 (Win 1739 / Loss 1890 / Flat 2271) / skip 6156件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SAGA/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $1,197.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$253.55** / 初期 $100.00 (+153.55%)
- 確定: 3438件 (Win 949 / Loss 792 / Flat 1697) / skip 5468件
- 成長率目線: 平均log +0.000271 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $253.55

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.26** / 初期 $100.00 (+21.26%)
- 確定: 3163件 (Win 933 / Loss 1248 / Flat 982) / pending 1件 / skip 3804件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000156 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: XAI/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $121.26

## 6. Latest Market Context

- 更新: 2026-09-24T21:36:15.153268+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=84453.3
- Funnel: target 1069 → liquid 174 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SAGA/USDT:USDT | +29.54% | $2,693,858.62 |
| XAI/USDT:USDT | +17.01% | $10,075,838.25 |
| LSK/USDT:USDT | +13.77% | $18,815,693.39 |
| XPL/USDT:USDT | +10.92% | $11,567,291.98 |
| CHIP/USDT:USDT | +10.85% | $1,217,080.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XPL/USDT:USDT | below_1h_threshold | +4.48% | +4.32% |
| CHIP/USDT:USDT | below_1h_threshold | +2.40% | +2.25% |
| ONDO/USDT:USDT | below_1h_threshold | +2.13% | +1.98% |
| AVAX/USDT:USDT | below_1h_threshold | +1.95% | +1.80% |
| 1000BONK/USDT:USDT | below_1h_threshold | +1.78% | +1.62% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
