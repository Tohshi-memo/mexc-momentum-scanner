# Decision Report

- generated_at: 2026-09-14T09:06:11.112519+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14504**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.62% / filled 20/20。**
- 全期間 MARKET基準: n=14504, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.62%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.62% | **+1.62%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.62% | **+1.62%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.26% | **+1.13%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.30% | **+1.04%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.86% | **+0.74%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.87% | **+0.56%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +2.84% | **+1.42%** |
| LIMIT_4PCT_LONG | 16/20 | 80.0% | +1.73% | **+1.38%** |
| LIMIT_3PCT_LONG | 17/20 | 85.0% | +1.24% | **+1.05%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +3.91% | **+0.78%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,072.58** / 初期 $100.00 (+972.58%)
- 確定: 5437件 (Win 1636 / Loss 1764 / Flat 2037) / skip 5628件
- 成長率目線: 平均log +0.000436 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $1,072.58

## 4. Robust Adaptive DryRun ($100)

- 残高: **$227.62** / 初期 $100.00 (+127.62%)
- 確定: 2991件 (Win 830 / Loss 716 / Flat 1445) / skip 4924件
- 成長率目線: 平均log +0.000275 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $227.62

## 5. Causal Adaptive DryRun ($100)

- 残高: **$126.20** / 初期 $100.00 (+26.20%)
- 確定: 2884件 (Win 859 / Loss 1117 / Flat 908) / pending 6件 / skip 3088件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000081 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CVC/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $126.20

## 6. Latest Market Context

- 更新: 2026-09-14T09:06:02.681762+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=77715.2
- Funnel: target 1068 → liquid 147 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIN/USDT:USDT | +56.53% | $2,311,849.53 |
| CATE/USDT:USDT | +47.00% | $1,906,522.86 |
| BR/USDT:USDT | +41.58% | $6,497,617.52 |
| ARK/USDT:USDT | +32.44% | $4,295,579.69 |
| MTL/USDT:USDT | +31.60% | $1,291,190.57 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXS/USDT:USDT | below_1h_threshold | +2.26% | +2.24% |
| AIN/USDT:USDT | below_1h_threshold | +1.45% | +1.43% |
| ARK/USDT:USDT | below_1h_threshold | +1.31% | +1.29% |
| POWR/USDT:USDT | below_1h_threshold | +1.12% | +1.10% |
| POWER/USDT:USDT | below_1h_threshold | +1.07% | +1.05% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
