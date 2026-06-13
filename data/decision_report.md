# Decision Report

- generated_at: 2026-06-13T09:45:19.445726+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6574**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6574, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.42%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.42% | **-0.42%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +1.04% | **+0.36%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.28% | **+0.21%** |
| LIMIT_ATR | 17/20 | 85.0% | +0.21% | **+0.18%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.34% | **+0.17%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.16% | **+0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.70% | **+0.70%** |
| ASK_LONG | 20/20 | 100.0% | +0.67% | **+0.67%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +1.24% | **+0.50%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.44% | **+0.35%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +0.73% | **+0.29%** |

## 2. $100 Live Portfolio

- 残高: **$97.07** / 初期 $100.00 (-2.93%)
- 確定トレード: 25件 (TP 6 / SL 18 / EXP 1)
- 最新: SPCXSTOCK/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.07
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$164.48** / 初期 $100.00 (+64.48%)
- 確定: 1447件 (Win 389 / Loss 464 / Flat 594) / skip 1688件
- 成長率目線: 平均log +0.000344 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TRUMPOFFICIAL/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $164.48

## 4. Latest Market Context

- 更新: 2026-06-13T09:45:16.586454+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=63784.7
- Funnel: target 770 → liquid 158 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JCT/USDT:USDT | +59.87% | $4,192,267.28 |
| RIF/USDT:USDT | +25.39% | $2,506,870.38 |
| VVV/USDT:USDT | +16.74% | $6,351,178.84 |
| EDGE/USDT:USDT | +16.56% | $3,062,770.86 |
| NOT/USDT:USDT | +15.72% | $1,505,808.32 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NOT/USDT:USDT | below_1h_threshold | +4.59% | +4.57% |
| COAI/USDT:USDT | below_1h_threshold | +4.26% | +4.24% |
| TAO/USDT:USDT | below_1h_threshold | +3.01% | +2.99% |
| VVV/USDT:USDT | below_1h_threshold | +2.49% | +2.47% |
| BANANAS31/USDT:USDT | below_1h_threshold | +1.63% | +1.61% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
