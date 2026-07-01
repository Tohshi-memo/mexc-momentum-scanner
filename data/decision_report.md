# Decision Report

- generated_at: 2026-07-01T06:17:16.304854+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7956**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7956, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-0.57%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.57% | **-0.57%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 19/20 | 95.0% | +0.97% | **+0.92%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +3.20% | **+0.32%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.11% | **+0.11%** |
| LIMIT_5PCT | 5/20 | 25.0% | -0.04% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |
| ASK_LONG | 20/20 | 100.0% | +0.57% | **+0.57%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.32% | **+0.53%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +0.56% | **+0.28%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +0.76% | **+0.27%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 47件 (TP 17 / SL 29 / EXP 1)
- 最新: AGLD/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$256.55** / 初期 $100.00 (+156.55%)
- 確定: 2356件 (Win 714 / Loss 787 / Flat 855) / skip 2161件
- 成長率目線: 平均log +0.000400 / 幾何平均 +0.040% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIGENSYN/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $256.55

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.84** / 初期 $100.00 (+6.84%)
- 確定: 498件 (Win 127 / Loss 121 / Flat 250) / skip 869件
- 成長率目線: 平均log +0.000133 / 幾何平均 +0.013% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NES/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.84

## 5. Latest Market Context

- 更新: 2026-07-01T06:17:13.110815+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.32% price=58935.2
- Funnel: target 823 → liquid 149 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DYDX/USDT:USDT | +34.50% | $10,085,892.07 |
| TAIKO/USDT:USDT | +23.57% | $1,279,706.08 |
| AIGENSYN/USDT:USDT | +15.15% | $12,385,426.03 |
| BTW/USDT:USDT | +13.77% | $11,247,901.01 |
| BASED/USDT:USDT | +13.74% | $4,491,537.06 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +3.77% | +4.09% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +3.09% | +3.41% |
| BTW/USDT:USDT | below_1h_threshold | +2.17% | +2.49% |
| GRASS/USDT:USDT | below_1h_threshold | +1.15% | +1.47% |
| XLM/USDT:USDT | below_1h_threshold | +0.91% | +1.23% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
