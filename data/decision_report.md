# Decision Report

- generated_at: 2026-07-16T03:51:41.867024+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8785**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.73% / filled 20/20。**
- 全期間 MARKET基準: n=8785, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.73%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.73% | **+1.73%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.73% | **+1.73%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.71% | **+1.63%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.93% | **+1.25%** |
| LIMIT_2PCT | 17/20 | 85.0% | +1.44% | **+1.23%** |
| LIMIT_BB3S | 6/9 | 66.7% | +1.53% | **+1.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +2.04% | **+0.51%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.82% | **+0.45%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.40% | **+0.20%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +0.10% | **+0.02%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | -0.70% | **-0.52%** |

## 2. $100 Live Portfolio

- 残高: **$106.34** / 初期 $100.00 (+6.34%)
- 確定トレード: 102件 (TP 37 / SL 63 / EXP 2)
- 最新: PI/USDT:USDT TP_HIT PnL +8.00% 残高後 $106.34
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$338.95** / 初期 $100.00 (+238.95%)
- 確定: 2901件 (Win 906 / Loss 943 / Flat 1052) / skip 2445件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: US/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $338.95

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.89** / 初期 $100.00 (+6.89%)
- 確定: 749件 (Win 171 / Loss 169 / Flat 409) / skip 1447件
- 成長率目線: 平均log +0.000089 / 幾何平均 +0.009% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0512 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: US/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.89

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.49** / 初期 $100.00 (-1.51%)
- 確定: 64件 (Win 19 / Loss 41 / Flat 4) / pending 0件 / skip 194件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000517 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: XEC/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account -0.09% 残高後 $98.49

## 6. Latest Market Context

- 更新: 2026-07-16T03:51:30.770514+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=64553.4
- Funnel: target 873 → liquid 172 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.6 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CAP/USDT:USDT | +21.33% | $2,130,608.09 |
| US/USDT:USDT | +21.02% | $10,880,607.74 |
| HOME/USDT:USDT | +13.93% | $2,083,451.14 |
| SKL/USDT:USDT | +11.04% | $1,903,445.46 |
| ROAM/USDT:USDT | +10.76% | $5,691,233.97 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SXT/USDT:USDT | below_1h_threshold | +4.51% | +4.61% |
| BANK/USDT:USDT | below_1h_threshold | +4.41% | +4.51% |
| SKL/USDT:USDT | below_1h_threshold | +2.22% | +2.32% |
| SOXL/USDT:USDT | below_1h_threshold | +2.08% | +2.18% |
| AKE/USDT:USDT | below_1h_threshold | +2.07% | +2.17% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
