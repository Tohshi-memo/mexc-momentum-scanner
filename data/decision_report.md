# Decision Report

- generated_at: 2026-09-22T23:31:27.358614+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15371**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.12% / filled 20/20。**
- 全期間 MARKET基準: n=15371, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.12% | **+1.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 17/20 | 85.0% | +2.00% | **+1.70%** |
| LIMIT_2PCT | 14/20 | 70.0% | +2.23% | **+1.56%** |
| LIMIT_3PCT | 12/20 | 60.0% | +2.32% | **+1.39%** |
| MARKET | 20/20 | 100.0% | +1.12% | **+1.12%** |
| LIMIT_BB3S | 8/13 | 61.5% | +1.72% | **+1.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 17/20 | 85.0% | +1.66% | **+1.41%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +2.91% | **+1.31%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +3.10% | **+1.24%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.50% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,161.60** / 初期 $100.00 (+1061.60%)
- 確定: 5849件 (Win 1730 / Loss 1880 / Flat 2239) / skip 6083件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FOLKS/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $1,161.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$249.51** / 初期 $100.00 (+149.51%)
- 確定: 3353件 (Win 926 / Loss 781 / Flat 1646) / skip 5429件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KERNEL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $249.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.50** / 初期 $100.00 (+22.50%)
- 確定: 3119件 (Win 917 / Loss 1223 / Flat 979) / pending 4件 / skip 3724件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000039 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: FOLKS/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $122.50

## 6. Latest Market Context

- 更新: 2026-09-22T23:31:15.732399+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=86172.1
- Funnel: target 1058 → liquid 189 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FOLKS/USDT:USDT | +27.80% | $2,621,142.98 |
| DRIFT/USDT:USDT | +25.69% | $1,659,626.97 |
| 4/USDT:USDT | +21.43% | $2,375,032.51 |
| USELESS/USDT:USDT | +16.34% | $10,564,421.39 |
| ALLO/USDT:USDT | +15.88% | $1,775,949.21 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEC/USDT:USDT | below_1h_threshold | +4.82% | +4.72% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +3.40% | +3.29% |
| ARB/USDT:USDT | below_1h_threshold | +3.39% | +3.29% |
| ALLO/USDT:USDT | below_1h_threshold | +3.14% | +3.03% |
| FOLKS/USDT:USDT | below_1h_threshold | +3.06% | +2.96% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
