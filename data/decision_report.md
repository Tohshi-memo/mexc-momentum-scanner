# Decision Report

- generated_at: 2026-09-18T03:01:21.830285+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14857**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.84% / filled 20/20。**
- 全期間 MARKET基準: n=14857, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.84%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.84% | **+0.84%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_10PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| MARKET | 20/20 | 100.0% | +0.84% | **+0.84%** |
| LIMIT_BB3S | 8/16 | 50.0% | +1.32% | **+0.66%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +2.31% | **+1.38%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.44% | **+1.08%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.09% | **+0.82%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.12% | **+0.62%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +1.27% | **+0.38%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,159.77** / 初期 $100.00 (+1059.77%)
- 確定: 5604件 (Win 1679 / Loss 1814 / Flat 2111) / skip 5814件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ARB/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $1,159.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$244.71** / 初期 $100.00 (+144.71%)
- 確定: 3146件 (Win 876 / Loss 750 / Flat 1520) / skip 5122件
- 成長率目線: 平均log +0.000284 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1252 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CNPY/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $244.71

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.53** / 初期 $100.00 (+23.53%)
- 確定: 2959件 (Win 878 / Loss 1165 / Flat 916) / pending 1件 / skip 3366件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000372 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ARB/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $123.53

## 6. Latest Market Context

- 更新: 2026-09-18T03:01:11.182504+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=76956.8
- Funnel: target 1052 → liquid 151 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CNPY/USDT:USDT | +35.24% | $3,377,347.38 |
| ARB/USDT:USDT | +19.93% | $75,980,107.81 |
| COTI/USDT:USDT | +18.22% | $6,783,602.24 |
| NEAR/USDT:USDT | +17.04% | $120,609,370.58 |
| ONE/USDT:USDT | +15.44% | $49,334,023.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UAI/USDT:USDT | below_1h_threshold | +1.43% | +1.42% |
| USELESS/USDT:USDT | below_1h_threshold | +0.62% | +0.61% |
| G/USDT:USDT | below_1h_threshold | +0.54% | +0.53% |
| EIGEN/USDT:USDT | below_1h_threshold | +0.49% | +0.48% |
| UNI/USDT:USDT | below_1h_threshold | +0.38% | +0.37% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
