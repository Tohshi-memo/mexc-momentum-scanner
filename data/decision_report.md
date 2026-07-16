# Decision Report

- generated_at: 2026-07-16T04:51:18.099187+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8788**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.33% / filled 20/20。**
- 全期間 MARKET基準: n=8788, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.33%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.33% | **+2.33%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.33% | **+2.33%** |
| LIMIT_1PCT | 18/20 | 90.0% | +2.03% | **+1.83%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.51% | **+1.13%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.66% | **+1.08%** |
| LIMIT_BB3S | 6/11 | 54.5% | +1.53% | **+0.84%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +5.11% | **+1.02%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +1.33% | **+0.60%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +0.10% | **+0.02%** |
| LIMIT_BB3S_LONG | 7/7 | 100.0% | -0.48% | **-0.48%** |

## 2. $100 Live Portfolio

- 残高: **$107.41** / 初期 $100.00 (+7.41%)
- 確定トレード: 103件 (TP 38 / SL 63 / EXP 2)
- 最新: DEXE/USDT:USDT TP_HIT PnL +8.00% 残高後 $107.41
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$338.95** / 初期 $100.00 (+238.95%)
- 確定: 2903件 (Win 906 / Loss 943 / Flat 1054) / skip 2446件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: US/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $338.95

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.89** / 初期 $100.00 (+6.89%)
- 確定: 752件 (Win 171 / Loss 169 / Flat 412) / skip 1447件
- 成長率目線: 平均log +0.000089 / 幾何平均 +0.009% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0503 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: US/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.89

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.49** / 初期 $100.00 (-1.51%)
- 確定: 64件 (Win 19 / Loss 41 / Flat 4) / pending 0件 / skip 195件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000535 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: XEC/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account -0.09% 残高後 $98.49

## 6. Latest Market Context

- 更新: 2026-07-16T04:51:10.416376+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=64595.4
- Funnel: target 873 → liquid 173 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.2 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +25.09% | $11,887,593.68 |
| CAP/USDT:USDT | +15.03% | $2,350,875.83 |
| ROAM/USDT:USDT | +12.49% | $5,710,942.64 |
| HOME/USDT:USDT | +11.90% | $2,138,388.41 |
| SKL/USDT:USDT | +11.68% | $1,921,617.57 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +4.02% | +4.01% |
| ALCH/USDT:USDT | below_1h_threshold | +3.17% | +3.17% |
| MAGMA/USDT:USDT | below_1h_threshold | +2.72% | +2.71% |
| ROAM/USDT:USDT | below_1h_threshold | +2.60% | +2.60% |
| RIVER/USDT:USDT | below_1h_threshold | +2.13% | +2.12% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
