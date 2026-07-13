# Decision Report

- generated_at: 2026-07-13T08:06:07.622426+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8625**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.68% / filled 20/20。**
- 全期間 MARKET基準: n=8625, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.68%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.68% | **+2.68%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.68% | **+2.68%** |
| LIMIT_1PCT | 18/20 | 90.0% | +2.42% | **+2.18%** |
| LIMIT_2PCT | 15/20 | 75.0% | +2.06% | **+1.55%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.90% | **+0.87%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.24% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +1.67% | **+1.33%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +0.20% | **+0.05%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -2.30% | **-0.35%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | -0.42% | **-0.36%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | -0.80% | **-0.40%** |

## 2. $100 Live Portfolio

- 残高: **$101.20** / 初期 $100.00 (+1.20%)
- 確定トレード: 91件 (TP 30 / SL 59 / EXP 2)
- 最新: ANSEM/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.20
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$321.39** / 初期 $100.00 (+221.39%)
- 確定: 2794件 (Win 876 / Loss 923 / Flat 995) / skip 2392件
- 成長率目線: 平均log +0.000418 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLAST/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $321.39

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.11** / 初期 $100.00 (+5.11%)
- 確定: 645件 (Win 152 / Loss 159 / Flat 334) / skip 1391件
- 成長率目線: 平均log +0.000077 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ANSEM/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $105.11

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.02** / 初期 $100.00 (+0.02%)
- 確定: 30件 (Win 12 / Loss 18 / Flat 0) / pending 2件 / skip 62件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000677 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BLAST/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $100.02

## 6. Latest Market Context

- 更新: 2026-07-13T08:06:01.435879+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=62970.2
- Funnel: target 863 → liquid 144 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| XEC/USDT:USDT | +31.30% | $3,806,629.74 |
| DODO/USDT:USDT | +23.86% | $7,029,963.98 |
| JCT/USDT:USDT | +23.02% | $1,053,871.54 |
| KITE/USDT:USDT | +15.63% | $1,659,137.64 |
| BLAST/USDT:USDT | +9.07% | $2,979,605.41 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_1h_threshold | +2.49% | +2.46% |
| DODO/USDT:USDT | below_1h_threshold | +1.56% | +1.53% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +1.35% | +1.32% |
| TRIA/USDT:USDT | below_1h_threshold | +1.10% | +1.07% |
| CAP/USDT:USDT | below_1h_threshold | +0.73% | +0.70% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
