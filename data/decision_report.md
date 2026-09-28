# Decision Report

- generated_at: 2026-09-28T22:36:28.916219+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15747**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.83% / filled 20/20。**
- 全期間 MARKET基準: n=15747, expectancy=+0.01%
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
| LIMIT_1PCT | 16/20 | 80.0% | +1.37% | **+1.10%** |
| LIMIT_2PCT | 13/20 | 65.0% | +0.68% | **+0.44%** |
| LIMIT_BB3S | 6/16 | 37.5% | +0.73% | **+0.27%** |
| LIMIT_3PCT | 10/20 | 50.0% | +0.52% | **+0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.45% | **+0.22%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | -0.01% | **-0.01%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -0.60% | **-0.09%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | -0.22% | **-0.12%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | -0.26% | **-0.17%** |

## 2. $100 Live Portfolio

- 残高: **$120.75** / 初期 $100.00 (+20.75%)
- 確定トレード: 225件 (TP 82 / SL 136 / EXP 7)
- 最新: XLM/USDT:USDT SL_HIT PnL -2.52% 残高後 $120.75
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,227.24** / 初期 $100.00 (+1127.24%)
- 確定: 5984件 (Win 1766 / Loss 1925 / Flat 2293) / skip 6324件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NMR/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $1,227.24

## 4. Robust Adaptive DryRun ($100)

- 残高: **$263.08** / 初期 $100.00 (+163.08%)
- 確定: 3534件 (Win 974 / Loss 812 / Flat 1748) / skip 5624件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: QNT/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $263.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.98** / 初期 $100.00 (+17.98%)
- 確定: 3307件 (Win 958 / Loss 1301 / Flat 1048) / pending 3件 / skip 3909件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000132 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: NMR/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $117.98

## 6. Latest Market Context

- 更新: 2026-09-28T22:36:18.070254+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.18% price=83322.6
- Funnel: target 1066 → liquid 175 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NMR/USDT:USDT | +27.14% | $3,258,639.41 |
| BTW/USDT:USDT | +13.74% | $18,221,167.45 |
| CRV/USDT:USDT | +10.67% | $9,978,229.09 |
| MARSCOIN/USDT:USDT | +7.70% | $4,290,572.78 |
| GRASS/USDT:USDT | +6.66% | $4,703,607.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GRASS/USDT:USDT | below_1h_threshold | +2.15% | +1.97% |
| BTW/USDT:USDT | below_1h_threshold | +2.04% | +1.87% |
| SAGA/USDT:USDT | below_1h_threshold | +1.60% | +1.42% |
| ICP/USDT:USDT | below_1h_threshold | +1.34% | +1.16% |
| XMR/USDT:USDT | below_1h_threshold | +1.31% | +1.13% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
