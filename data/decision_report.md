# Decision Report

- generated_at: 2026-07-27T20:21:22.614637+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9648**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.48% / filled 20/20。**
- 全期間 MARKET基準: n=9648, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.48%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.48% | **+0.48%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +1.48% | **+1.48%** |
| LIMIT_2PCT | 17/20 | 85.0% | +1.06% | **+0.90%** |
| MARKET | 20/20 | 100.0% | +0.48% | **+0.48%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.43% | **+0.28%** |
| LIMIT_4PCT | 10/20 | 50.0% | -0.19% | **-0.10%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/6 | 50.0% | +4.20% | **+2.10%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.66% | **+0.75%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.18% | **+0.53%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.89% | **+0.49%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.74% | **+0.44%** |

## 2. $100 Live Portfolio

- 残高: **$106.39** / 初期 $100.00 (+6.39%)
- 確定トレード: 146件 (TP 50 / SL 91 / EXP 5)
- 最新: RIF/USDT:USDT SL_HIT PnL -4.00% 残高後 $106.39
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$461.56** / 初期 $100.00 (+361.56%)
- 確定: 3434件 (Win 1088 / Loss 1118 / Flat 1228) / skip 2775件
- 成長率目線: 平均log +0.000445 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: QBTSSTOCK/USDT:USDT `LIMIT_3PCT_LONG` TP_HIT account +1.00% 残高後 $461.56

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1224件 (Win 338 / Loss 275 / Flat 611) / skip 1835件
- 成長率目線: 平均log +0.000259 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0089 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOXS/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$108.80** / 初期 $100.00 (+8.80%)
- 確定: 668件 (Win 220 / Loss 254 / Flat 194) / pending 4件 / skip 447件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000343 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: QBTSSTOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.30% 残高後 $108.80

## 6. Latest Market Context

- 更新: 2026-07-27T20:21:13.354701+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=64906.4
- Funnel: target 902 → liquid 177 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LA/USDT:USDT | +39.25% | $3,997,407.65 |
| RIF/USDT:USDT | +27.38% | $5,961,378.07 |
| AEON1/USDT:USDT | +13.52% | $1,607,544.70 |
| SOONNETWORK/USDT:USDT | +13.52% | $1,028,361.97 |
| JIMOTHY/USDT:USDT | +10.07% | $1,954,989.58 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| QBTSSTOCK/USDT:USDT | below_1h_threshold | +4.29% | +4.37% |
| KORU/USDT:USDT | below_1h_threshold | +2.81% | +2.89% |
| ALLO/USDT:USDT | below_1h_threshold | +2.57% | +2.65% |
| BANK/USDT:USDT | below_1h_threshold | +2.47% | +2.56% |
| SOXL/USDT:USDT | below_1h_threshold | +2.22% | +2.30% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
