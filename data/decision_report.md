# Decision Report

- generated_at: 2026-06-21T08:05:51.867204+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7297**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7297, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.21%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.21% | **-0.21%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +2.80% | **+0.56%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_BB3S | 4/14 | 28.6% | -0.21% | **-0.06%** |
| ASK | 20/20 | 100.0% | -0.10% | **-0.10%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.43% | **+1.00%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.24% | **+0.87%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.72% | **+0.61%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.14% | **+0.57%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$102.46** / 初期 $100.00 (+2.46%)
- 確定トレード: 25件 (TP 10 / SL 15 / EXP 0)
- 最新: AGT/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.46
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$235.27** / 初期 $100.00 (+135.27%)
- 確定: 2026件 (Win 599 / Loss 664 / Flat 763) / skip 1832件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EIGEN/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $235.27

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 311件 (Win 89 / Loss 87 / Flat 135) / skip 397件
- 成長率目線: 平均log +0.000188 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SLX/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-21T08:05:47.393101+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=64172.6
- Funnel: target 796 → liquid 130 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TNSR/USDT:USDT | +70.93% | $4,248,188.31 |
| LAB/USDT:USDT | +22.39% | $21,141,770.85 |
| BICO/USDT:USDT | +16.44% | $51,937,457.13 |
| UB/USDT:USDT | +15.67% | $1,208,615.93 |
| RESOLV/USDT:USDT | +14.89% | $4,374,044.94 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PUMPFUN/USDT:USDT | below_1h_threshold | +1.76% | +1.76% |
| EIGEN/USDT:USDT | below_1h_threshold | +1.75% | +1.74% |
| JTO/USDT:USDT | below_1h_threshold | +1.23% | +1.22% |
| TNSR/USDT:USDT | below_1h_threshold | +1.22% | +1.21% |
| BASED/USDT:USDT | below_1h_threshold | +0.90% | +0.89% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
