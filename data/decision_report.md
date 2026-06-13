# Decision Report

- generated_at: 2026-06-13T13:08:27.270679+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6579**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6579, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.07%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.07% | **-1.07%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.24% | **+0.18%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.01% | **+0.01%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | -0.15% | **-0.07%** |
| LIMIT_ATR | 17/20 | 85.0% | -0.23% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +0.75% | **+0.75%** |
| MARKET_LONG | 20/20 | 100.0% | +0.74% | **+0.74%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +2.23% | **+0.67%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +1.26% | **+0.51%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.45% | **+0.36%** |

## 2. $100 Live Portfolio

- 残高: **$97.07** / 初期 $100.00 (-2.93%)
- 確定トレード: 25件 (TP 6 / SL 18 / EXP 1)
- 最新: SPCXSTOCK/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.07
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$164.48** / 初期 $100.00 (+64.48%)
- 確定: 1452件 (Win 389 / Loss 464 / Flat 599) / skip 1688件
- 成長率目線: 平均log +0.000343 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JCT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $164.48

## 4. Latest Market Context

- 更新: 2026-06-13T13:08:24.450643+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=64102.0
- Funnel: target 770 → liquid 150 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JCT/USDT:USDT | +37.22% | $8,380,559.67 |
| RIF/USDT:USDT | +26.87% | $4,132,429.94 |
| COAI/USDT:USDT | +18.01% | $4,869,364.85 |
| VVV/USDT:USDT | +17.13% | $7,897,244.19 |
| TAO/USDT:USDT | +16.86% | $158,055,191.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MEGA/USDT:USDT | below_1h_threshold | +1.46% | +1.46% |
| WLD/USDT:USDT | below_1h_threshold | +1.28% | +1.28% |
| SQD/USDT:USDT | below_1h_threshold | +1.25% | +1.25% |
| NOT/USDT:USDT | below_1h_threshold | +1.24% | +1.24% |
| COAI/USDT:USDT | below_1h_threshold | +1.21% | +1.21% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
