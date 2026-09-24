# Decision Report

- generated_at: 2026-09-24T21:41:32.832403+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15496**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.33% / filled 20/20。**
- 全期間 MARKET基準: n=15496, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.33%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.33% | **+0.33%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 4/20 | 20.0% | +4.15% | **+0.83%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| MARKET | 20/20 | 100.0% | +0.33% | **+0.33%** |
| LIMIT_8PCT | 4/20 | 20.0% | +0.93% | **+0.19%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.14% | **+0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/10 | 60.0% | +3.69% | **+2.22%** |
| MARKET_LONG | 20/20 | 100.0% | +1.18% | **+1.18%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.43% | **+1.00%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.03% | **+0.82%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.81% | **+0.81%** |

## 2. $100 Live Portfolio

- 残高: **$120.08** / 初期 $100.00 (+20.08%)
- 確定トレード: 219件 (TP 79 / SL 135 / EXP 5)
- 最新: XPL/USDT:USDT SL_HIT PnL -3.85% 残高後 $120.08
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,197.79** / 初期 $100.00 (+1097.79%)
- 確定: 5900件 (Win 1739 / Loss 1890 / Flat 2271) / skip 6157件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SAGA/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $1,197.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$253.55** / 初期 $100.00 (+153.55%)
- 確定: 3438件 (Win 949 / Loss 792 / Flat 1697) / skip 5469件
- 成長率目線: 平均log +0.000271 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $253.55

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.05** / 初期 $100.00 (+21.05%)
- 確定: 3164件 (Win 933 / Loss 1249 / Flat 982) / pending 1件 / skip 3804件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000151 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SAGA/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $121.05

## 6. Latest Market Context

- 更新: 2026-09-24T21:41:19.480902+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=84395.3
- Funnel: target 1069 → liquid 174 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SAGA/USDT:USDT | +33.27% | $2,970,082.89 |
| XAI/USDT:USDT | +15.81% | $10,227,560.51 |
| LSK/USDT:USDT | +13.39% | $18,931,394.29 |
| CHIP/USDT:USDT | +11.23% | $1,242,032.32 |
| XPL/USDT:USDT | +9.46% | $11,823,409.02 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XPL/USDT:USDT | below_1h_threshold | +3.10% | +3.01% |
| CHIP/USDT:USDT | below_1h_threshold | +2.74% | +2.65% |
| ONDO/USDT:USDT | below_1h_threshold | +2.47% | +2.38% |
| AVAX/USDT:USDT | below_1h_threshold | +1.92% | +1.84% |
| QNT/USDT:USDT | below_1h_threshold | +1.50% | +1.41% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
