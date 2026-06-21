# Decision Report

- generated_at: 2026-06-21T04:30:38.678761+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7289**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7289, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.50%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.50% | **-0.50%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +2.80% | **+0.70%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | -0.27% | **-0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.95% | **+1.37%** |
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +1.64% | **+1.23%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.76% | **+0.97%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.79% | **+0.51%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +0.86% | **+0.47%** |

## 2. $100 Live Portfolio

- 残高: **$102.46** / 初期 $100.00 (+2.46%)
- 確定トレード: 25件 (TP 10 / SL 15 / EXP 0)
- 最新: AGT/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.46
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$235.02** / 初期 $100.00 (+135.02%)
- 確定: 2018件 (Win 597 / Loss 662 / Flat 759) / skip 1832件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +7.25%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ALICE/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $235.02

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 311件 (Win 89 / Loss 87 / Flat 135) / skip 389件
- 成長率目線: 平均log +0.000188 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SLX/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-21T04:23:16.050574+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=64454.5
- Funnel: target 796 → liquid 134 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BICO/USDT:USDT | +49.85% | $49,347,986.89 |
| ALICE/USDT:USDT | +26.11% | $3,277,669.30 |
| RESOLV/USDT:USDT | +21.07% | $3,894,787.66 |
| VELVET/USDT:USDT | +9.57% | $16,981,305.54 |
| ASTEROID/USDT:USDT | +9.05% | $1,528,656.18 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VELVET/USDT:USDT | below_1h_threshold | +2.22% | +2.13% |
| TAO/USDT:USDT | below_1h_threshold | +1.54% | +1.45% |
| JTO/USDT:USDT | below_1h_threshold | +1.25% | +1.16% |
| EIGEN/USDT:USDT | below_1h_threshold | +0.61% | +0.53% |
| AAVE/USDT:USDT | below_1h_threshold | +0.35% | +0.27% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
