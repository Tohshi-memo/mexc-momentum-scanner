# Decision Report

- generated_at: 2026-06-16T08:05:41.039406+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6848**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6848, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.95%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.95% | **-0.95%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.16% | **+0.41%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.29% | **+0.10%** |
| LIMIT_ATR | 15/20 | 75.0% | -0.17% | **-0.13%** |
| LIMIT_4PCT | 14/20 | 70.0% | -0.26% | **-0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +2.86% | **+1.00%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.13% | **+0.85%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +2.11% | **+0.84%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.29% | **+0.58%** |

## 2. $100 Live Portfolio

- 残高: **$102.50** / 初期 $100.00 (+2.50%)
- 確定トレード: 10件 (TP 5 / SL 5 / EXP 0)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.50
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$184.74** / 初期 $100.00 (+84.74%)
- 確定: 1721件 (Win 449 / Loss 536 / Flat 736) / skip 1688件
- 成長率目線: 平均log +0.000357 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SIREN/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $184.74

## 4. Robust Adaptive DryRun ($100)

- 残高: **$97.60** / 初期 $100.00 (-2.40%)
- 確定: 156件 (Win 28 / Loss 30 / Flat 98) / skip 103件
- 成長率目線: 平均log -0.000155 / 幾何平均 -0.016% per trade / maxDD +3.03%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0671 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $97.60

## 5. Latest Market Context

- 更新: 2026-06-16T08:05:36.935144+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=66346.2
- Funnel: target 777 → liquid 157 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROAM/USDT:USDT | +59.37% | $4,123,215.58 |
| VELVET/USDT:USDT | +32.97% | $16,218,846.08 |
| SPACE/USDT:USDT | +30.76% | $3,866,395.09 |
| BSB/USDT:USDT | +29.55% | $26,465,072.18 |
| ASTEROID/USDT:USDT | +26.45% | $4,954,434.19 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RIF/USDT:USDT | below_1h_threshold | +1.96% | +1.95% |
| STG/USDT:USDT | below_1h_threshold | +1.96% | +1.95% |
| SIREN/USDT:USDT | below_1h_threshold | +1.83% | +1.82% |
| WLFI/USDT:USDT | below_1h_threshold | +1.50% | +1.50% |
| FOLKS/USDT:USDT | below_1h_threshold | +1.43% | +1.43% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
