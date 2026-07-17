# Decision Report

- generated_at: 2026-07-17T08:21:16.905340+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8833**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.83% / filled 20/20。**
- 全期間 MARKET基準: n=8833, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.83%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.83% | **+1.83%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.83% | **+1.83%** |
| LIMIT_5PCT | 7/20 | 35.0% | +3.58% | **+1.25%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.27% | **+1.08%** |
| LIMIT_4PCT | 9/20 | 45.0% | +1.48% | **+0.66%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +2.83% | **+0.57%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.55% | **+0.64%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.93% | **+0.33%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +0.24% | **+0.05%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | -0.24% | **-0.19%** |

## 2. $100 Live Portfolio

- 残高: **$110.71** / 初期 $100.00 (+10.71%)
- 確定トレード: 110件 (TP 41 / SL 65 / EXP 4)
- 最新: AERO/USDT:USDT SL_HIT PnL -3.73% 残高後 $110.71
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$342.42** / 初期 $100.00 (+242.42%)
- 確定: 2948件 (Win 917 / Loss 947 / Flat 1084) / skip 2446件
- 成長率目線: 平均log +0.000418 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.12% 残高後 $342.42

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.95** / 初期 $100.00 (+7.95%)
- 確定: 795件 (Win 184 / Loss 171 / Flat 440) / skip 1449件
- 成長率目線: 平均log +0.000096 / 幾何平均 +0.010% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0214 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $107.95

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.86** / 初期 $100.00 (-1.14%)
- 確定: 100件 (Win 32 / Loss 64 / Flat 4) / pending 4件 / skip 200件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000230 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $98.86

## 6. Latest Market Context

- 更新: 2026-07-17T08:21:06.465830+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=62761.4
- Funnel: target 885 → liquid 184 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.0 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LUMIA/USDT:USDT | +27.34% | $2,159,806.28 |
| SOXS/USDT:USDT | +15.86% | $1,657,242.62 |
| AKE/USDT:USDT | +15.22% | $41,632,600.36 |
| KAITO/USDT:USDT | +14.28% | $4,078,888.10 |
| TAC/USDT:USDT | +12.55% | $3,420,544.27 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| US/USDT:USDT | below_1h_threshold | +3.14% | +3.19% |
| SOXS/USDT:USDT | below_1h_threshold | +2.26% | +2.31% |
| BANK/USDT:USDT | below_1h_threshold | +2.01% | +2.06% |
| CAP/USDT:USDT | below_1h_threshold | +1.24% | +1.29% |
| VELVET/USDT:USDT | below_1h_threshold | +0.87% | +0.92% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
