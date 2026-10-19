# Decision Report

- generated_at: 2026-10-19T13:06:25.450680+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17011**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.92% / filled 20/20。**
- 全期間 MARKET基準: n=17011, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.92% | **+2.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.92% | **+2.92%** |
| LIMIT_1PCT | 18/20 | 90.0% | +3.09% | **+2.78%** |
| LIMIT_2PCT | 15/20 | 75.0% | +2.57% | **+1.93%** |
| LIMIT_3PCT | 10/20 | 50.0% | +0.75% | **+0.38%** |
| LIMIT_ATR | 10/20 | 50.0% | +0.71% | **+0.35%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 7/20 | 35.0% | +2.92% | **+1.02%** |
| LIMIT_9PCT_LONG | 9/20 | 45.0% | +1.50% | **+0.67%** |
| LIMIT_8PCT_LONG | 12/20 | 60.0% | +1.00% | **+0.60%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | -0.33% | **-0.20%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -4.00% | **-0.40%** |

## 2. $100 Live Portfolio

- 残高: **$121.48** / 初期 $100.00 (+21.48%)
- 確定トレード: 246件 (TP 91 / SL 148 / EXP 7)
- 最新: ZEREBRO/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.48
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,263.57** / 初期 $100.00 (+1163.57%)
- 確定: 6456件 (Win 1872 / Loss 2062 / Flat 2522) / skip 7116件
- 成長率目線: 平均log +0.000393 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AGT/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,263.57

## 4. Robust Adaptive DryRun ($100)

- 残高: **$277.61** / 初期 $100.00 (+177.61%)
- 確定: 3776件 (Win 1038 / Loss 883 / Flat 1855) / skip 6646件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0341 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AGT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $277.61

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5170件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000095 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-19T13:06:13.335332+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=82684.0
- Funnel: target 1085 → liquid 157 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KORU/USDT:USDT | +22.03% | $82,279,745.08 |
| AVA/USDT:USDT | +20.22% | $2,083,878.07 |
| BR/USDT:USDT | +19.36% | $18,686,403.59 |
| ZEREBRO/USDT:USDT | +18.96% | $1,932,265.53 |
| AGT/USDT:USDT | +17.26% | $10,348,168.85 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LSK/USDT:USDT | below_1h_threshold | +1.65% | +1.51% |
| AVA/USDT:USDT | below_1h_threshold | +1.52% | +1.38% |
| NIL/USDT:USDT | below_1h_threshold | +1.16% | +1.02% |
| AGT/USDT:USDT | below_1h_threshold | +1.01% | +0.87% |
| QNTSTOCK/USDT:USDT | below_1h_threshold | +0.92% | +0.78% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
