# Decision Report

- generated_at: 2026-09-23T03:26:23.423375+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15386**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.36% / filled 20/20。**
- 全期間 MARKET基準: n=15386, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.36%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.36% | **+0.36%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.36% | **+0.36%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.23% | **+0.21%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.48% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/6 | 83.3% | +1.68% | **+1.40%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.82% | **+0.65%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.96% | **+0.62%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.46% | **+0.39%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.48% | **+0.36%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,167.35** / 初期 $100.00 (+1067.35%)
- 確定: 5863件 (Win 1731 / Loss 1881 / Flat 2251) / skip 6084件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIL/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $1,167.35

## 4. Robust Adaptive DryRun ($100)

- 残高: **$249.51** / 初期 $100.00 (+149.51%)
- 確定: 3353件 (Win 926 / Loss 781 / Flat 1646) / skip 5444件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KERNEL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $249.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.35** / 初期 $100.00 (+22.35%)
- 確定: 3124件 (Win 919 / Loss 1226 / Flat 979) / pending 5件 / skip 3735件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `見送り` (no_strategy_passed_causal_filters) / causal_score n/a / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: NIL/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $122.35

## 6. Latest Market Context

- 更新: 2026-09-23T03:26:12.421521+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.19% price=86669.9
- Funnel: target 1058 → liquid 191 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SHROOM/USDT:USDT | +68.33% | $1,125,775.87 |
| NIL/USDT:USDT | +24.84% | $5,880,287.72 |
| ALLO/USDT:USDT | +18.99% | $2,525,908.59 |
| ARB/USDT:USDT | +18.08% | $55,148,188.23 |
| UNI/USDT:USDT | +16.74% | $57,792,636.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIL/USDT:USDT | below_1h_threshold | +3.45% | +3.26% |
| PHA/USDT:USDT | below_1h_threshold | +2.97% | +2.79% |
| HNT/USDT:USDT | below_1h_threshold | +2.64% | +2.45% |
| PENGU/USDT:USDT | below_1h_threshold | +2.39% | +2.20% |
| FARTCOIN/USDT:USDT | below_1h_threshold | +2.35% | +2.16% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
