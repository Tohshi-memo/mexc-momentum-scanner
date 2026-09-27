# Decision Report

- generated_at: 2026-09-27T22:01:23.456248+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15664**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15664, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.75%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.75% | **-0.75%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +6.86% | **+1.03%** |
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.80% | **+0.56%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.30% | **+0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +2.19% | **+1.75%** |
| MARKET_LONG | 20/20 | 100.0% | +1.05% | **+1.05%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.37% | **+0.96%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +1.46% | **+0.58%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.14% | **+0.57%** |

## 2. $100 Live Portfolio

- 残高: **$120.87** / 初期 $100.00 (+20.87%)
- 確定トレード: 224件 (TP 82 / SL 135 / EXP 7)
- 最新: UNI/USDT:USDT EXPIRED PnL +1.69% 残高後 $120.87
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,239.61** / 初期 $100.00 (+1139.61%)
- 確定: 5981件 (Win 1766 / Loss 1923 / Flat 2292) / skip 6244件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GRT/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $1,239.61

## 4. Robust Adaptive DryRun ($100)

- 残高: **$263.08** / 初期 $100.00 (+163.08%)
- 確定: 3534件 (Win 974 / Loss 812 / Flat 1748) / skip 5541件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: QNT/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $263.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.76** / 初期 $100.00 (+18.76%)
- 確定: 3240件 (Win 946 / Loss 1277 / Flat 1017) / pending 1件 / skip 3896件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000114 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: GRT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $118.76

## 6. Latest Market Context

- 更新: 2026-09-27T22:01:10.337743+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=84676.2
- Funnel: target 1069 → liquid 136 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BATON/USDT:USDT | +39.24% | $1,097,841.01 |
| QNT/USDT:USDT | +27.75% | $215,885,055.99 |
| GRT/USDT:USDT | +24.47% | $5,295,611.81 |
| ONE/USDT:USDT | +17.24% | $3,150,590.05 |
| RARE/USDT:USDT | +11.00% | $1,580,353.30 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RARE/USDT:USDT | below_1h_threshold | +0.89% | +0.85% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +0.32% | +0.27% |
| SKY/USDT:USDT | below_1h_threshold | +0.18% | +0.13% |
| BATON/USDT:USDT | below_1h_threshold | +0.13% | +0.08% |
| ARB/USDT:USDT | below_1h_threshold | +0.12% | +0.08% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
