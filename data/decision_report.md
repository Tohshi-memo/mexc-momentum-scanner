# Decision Report

- generated_at: 2026-09-19T03:06:17.649170+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14983**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.91% / filled 20/20。**
- 全期間 MARKET基準: n=14983, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.91%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.91% | **+0.91%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.91% | **+0.91%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.92% | **+0.87%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +4.00% | **+4.00%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +2.53% | **+1.26%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +2.75% | **+1.10%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.29% | **+0.80%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +0.83% | **+0.33%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,213.51** / 初期 $100.00 (+1113.51%)
- 確定: 5636件 (Win 1691 / Loss 1826 / Flat 2119) / skip 5908件
- 成長率目線: 平均log +0.000443 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MYX/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,213.51

## 4. Robust Adaptive DryRun ($100)

- 残高: **$239.14** / 初期 $100.00 (+139.14%)
- 確定: 3178件 (Win 878 / Loss 760 / Flat 1540) / skip 5216件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1023 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ONE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $239.14

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.52** / 初期 $100.00 (+23.52%)
- 確定: 2962件 (Win 879 / Loss 1167 / Flat 916) / pending 0件 / skip 3495件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000343 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $123.52

## 6. Latest Market Context

- 更新: 2026-09-19T03:06:06.870546+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=81320.6
- Funnel: target 1050 → liquid 168 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +65.49% | $38,489,434.40 |
| ONE/USDT:USDT | +57.73% | $25,399,252.67 |
| AR/USDT:USDT | +27.25% | $4,430,621.17 |
| MAGMA/USDT:USDT | +23.76% | $1,254,633.25 |
| CATE/USDT:USDT | +22.70% | $1,343,233.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STRK/USDT:USDT | below_1h_threshold | +1.68% | +1.59% |
| JTO/USDT:USDT | below_1h_threshold | +1.43% | +1.35% |
| EIGEN/USDT:USDT | below_1h_threshold | +1.23% | +1.15% |
| AAVE/USDT:USDT | below_1h_threshold | +1.21% | +1.13% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +1.04% | +0.96% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
