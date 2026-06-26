# Decision Report

- generated_at: 2026-06-26T06:20:01.116695+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7609**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7609, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-0.58%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.58% | **-0.58%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.29% | **+0.20%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |
| LIMIT_ATR | 14/20 | 70.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.46% | **+1.02%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.28% | **+0.83%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.89% | **+0.72%** |
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |
| ASK_LONG | 20/20 | 100.0% | +0.51% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$220.62** / 初期 $100.00 (+120.62%)
- 確定: 2138件 (Win 630 / Loss 715 / Flat 793) / skip 2032件
- 成長率目線: 平均log +0.000370 / 幾何平均 +0.037% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ARX/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $220.62

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.60** / 初期 $100.00 (+7.60%)
- 確定: 380件 (Win 103 / Loss 100 / Flat 177) / skip 640件
- 成長率目線: 平均log +0.000193 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $107.60

## 5. Latest Market Context

- 更新: 2026-06-26T06:19:55.381180+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.24% price=59780.2
- Funnel: target 810 → liquid 158 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| G/USDT:USDT | +26.56% | $6,607,833.69 |
| BEAT/USDT:USDT | +22.95% | $39,942,626.55 |
| ARX/USDT:USDT | +17.45% | $2,596,345.14 |
| AIN/USDT:USDT | +16.80% | $4,131,340.19 |
| IDOL/USDT:USDT | +16.63% | $1,760,994.47 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ARX/USDT:USDT | below_1h_threshold | +4.91% | +5.15% |
| HEI/USDT:USDT | below_1h_threshold | +2.58% | +2.82% |
| BAS/USDT:USDT | below_1h_threshold | +1.52% | +1.75% |
| AIN/USDT:USDT | below_1h_threshold | +1.00% | +1.24% |
| G/USDT:USDT | below_1h_threshold | +0.92% | +1.16% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
