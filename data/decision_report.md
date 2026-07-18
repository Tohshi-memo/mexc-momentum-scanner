# Decision Report

- generated_at: 2026-07-18T07:11:18.431782+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8918**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.56% / filled 20/20。**
- 全期間 MARKET基準: n=8918, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.56%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.56% | **+1.56%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.56% | **+1.56%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.57% | **+1.49%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.71% | **+0.94%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.86% | **+0.64%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.33% | **+0.58%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +0.93% | **+0.84%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +0.73% | **+0.58%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.94% | **+0.38%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +0.08% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$112.37** / 初期 $100.00 (+12.37%)
- 確定トレード: 113件 (TP 43 / SL 66 / EXP 4)
- 最新: CASHCAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $112.37
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$365.51** / 初期 $100.00 (+265.51%)
- 確定: 3033件 (Win 942 / Loss 965 / Flat 1126) / skip 2446件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TRADOOR/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $365.51

## 4. Robust Adaptive DryRun ($100)

- 残高: **$111.04** / 初期 $100.00 (+11.04%)
- 確定: 880件 (Win 207 / Loss 179 / Flat 494) / skip 1449件
- 成長率目線: 平均log +0.000119 / 幾何平均 +0.012% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0123 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TRADOOR/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $111.04

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.58** / 初期 $100.00 (-0.42%)
- 確定: 175件 (Win 55 / Loss 93 / Flat 27) / pending 6件 / skip 212件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000298 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TRADOOR/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $99.58

## 6. Latest Market Context

- 更新: 2026-07-18T07:11:10.675760+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=63966.4
- Funnel: target 885 → liquid 164 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.5 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +57.48% | $53,139,772.54 |
| ESPORTS/USDT:USDT | +40.51% | $13,658,271.69 |
| TRADOOR/USDT:USDT | +33.86% | $2,027,283.95 |
| BSB/USDT:USDT | +11.12% | $1,274,293.59 |
| VVV/USDT:USDT | +10.15% | $2,790,413.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STAR/USDT:USDT | below_1h_threshold | +3.48% | +3.46% |
| AKE/USDT:USDT | below_1h_threshold | +2.98% | +2.96% |
| BANK/USDT:USDT | below_1h_threshold | +1.93% | +1.91% |
| ALLO/USDT:USDT | below_1h_threshold | +1.81% | +1.80% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.08% | +1.06% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
