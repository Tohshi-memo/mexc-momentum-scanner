# Decision Report

- generated_at: 2026-06-27T19:18:50.090287+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7715**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7715, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.76%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.76% | **-0.76%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 3/20 | 15.0% | +4.61% | **+0.69%** |
| LIMIT_10PCT | 2/20 | 10.0% | +0.73% | **+0.07%** |
| LIMIT_9PCT | 2/20 | 10.0% | +0.29% | **+0.03%** |
| LIMIT_5PCT | 7/20 | 35.0% | -0.46% | **-0.16%** |
| LIMIT_7PCT | 3/20 | 15.0% | -1.72% | **-0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.16% | **+2.16%** |
| ASK_LONG | 20/20 | 100.0% | +2.05% | **+2.05%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +1.45% | **+0.94%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +1.45% | **+0.80%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +0.01% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$239.56** / 初期 $100.00 (+139.56%)
- 確定: 2224件 (Win 668 / Loss 741 / Flat 815) / skip 2052件
- 成長率目線: 平均log +0.000393 / 幾何平均 +0.039% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: O/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $239.56

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.77** / 初期 $100.00 (+7.77%)
- 確定: 446件 (Win 119 / Loss 114 / Flat 213) / skip 680件
- 成長率目線: 平均log +0.000168 / 幾何平均 +0.017% per trade / maxDD +3.03%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0377 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: O/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $107.77

## 5. Latest Market Context

- 更新: 2026-06-27T19:18:45.436903+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=60535.1
- Funnel: target 806 → liquid 124 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SLX/USDT:USDT | +18.63% | $16,274,385.81 |
| S/USDT:USDT | +13.43% | $2,697,442.50 |
| RE/USDT:USDT | +8.04% | $5,986,642.85 |
| O/USDT:USDT | +6.39% | $3,895,548.57 |
| BAS/USDT:USDT | +5.55% | $1,795,490.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SLX/USDT:USDT | below_1h_threshold | +2.89% | +2.90% |
| H/USDT:USDT | below_1h_threshold | +2.20% | +2.21% |
| O/USDT:USDT | below_1h_threshold | +1.43% | +1.44% |
| BICO/USDT:USDT | below_1h_threshold | +1.19% | +1.20% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +0.99% | +1.00% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
