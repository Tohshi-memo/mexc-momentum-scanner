# Decision Report

- generated_at: 2026-05-13T14:18:10.517427+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4228**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4228, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.48%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.48% | **-0.48%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 16/20 | 80.0% | -0.11% | **-0.09%** |
| LIMIT_5PCT | 5/20 | 25.0% | -1.03% | **-0.26%** |
| ASK | 20/20 | 100.0% | -0.29% | **-0.29%** |
| LIMIT_BB3S | 10/18 | 55.6% | -0.52% | **-0.29%** |
| LIMIT_FIB1618 | 4/20 | 20.0% | -1.99% | **-0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.31% | **+1.31%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.74% | **+1.13%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.72% | **+0.95%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.07% | **+0.70%** |
| LIMIT_7PCT_LONG | 4/20 | 20.0% | +3.46% | **+0.69%** |

## 2. $100 Live Portfolio

- 残高: **$97.71** / 初期 $100.00 (-2.29%)
- 確定トレード: 37件 (TP 9 / SL 25 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.78** / 初期 $100.00 (+19.78%)
- 確定: 341件 (Win 94 / Loss 124 / Flat 123) / skip 448件
- 成長率目線: 平均log +0.000529 / 幾何平均 +0.053% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UB/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.01% 残高後 $119.78

## 4. Latest Market Context

- 更新: 2026-05-13T14:18:07.428384+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=79699.9
- Funnel: target 765 → liquid 182 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +44.67% | $136,782,681.13 |
| COS/USDT:USDT | +35.99% | $1,861,245.70 |
| TRUTH/USDT:USDT | +29.81% | $3,873,114.29 |
| UB/USDT:USDT | +25.88% | $10,786,309.00 |
| JCT/USDT:USDT | +25.85% | $1,117,303.72 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +3.73% | +3.63% |
| FF/USDT:USDT | below_1h_threshold | +2.51% | +2.41% |
| TRUTH/USDT:USDT | below_1h_threshold | +2.29% | +2.18% |
| MITO/USDT:USDT | below_1h_threshold | +1.43% | +1.33% |
| RIVER/USDT:USDT | below_1h_threshold | +1.36% | +1.25% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
