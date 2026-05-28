# Decision Report

- generated_at: 2026-05-28T03:04:41.598982+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4950**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4950, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=-0.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.06% | **-0.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 14/20 | 70.0% | +3.67% | **+2.57%** |
| LIMIT_2PCT | 16/20 | 80.0% | +2.07% | **+1.66%** |
| LIMIT_4PCT | 10/20 | 50.0% | +2.87% | **+1.44%** |
| LIMIT_5PCT | 4/20 | 20.0% | +3.25% | **+0.65%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.63% | **+0.50%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +4.03% | **+1.81%** |
| LIMIT_10PCT_LONG | 6/20 | 30.0% | +5.15% | **+1.55%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +3.36% | **+1.18%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.97% | **+0.98%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.29% | **+0.97%** |

## 2. $100 Live Portfolio

- 残高: **$97.15** / 初期 $100.00 (-2.85%)
- 確定トレード: 68件 (TP 19 / SL 46 / EXP 3)
- 最新: B/USDT:USDT TP_HIT PnL +6.46% 残高後 $97.15
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$126.79** / 初期 $100.00 (+26.79%)
- 確定: 686件 (Win 172 / Loss 220 / Flat 294) / skip 825件
- 成長率目線: 平均log +0.000346 / 幾何平均 +0.035% per trade / maxDD +4.72%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GENIUS/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $126.79

## 4. Latest Market Context

- 更新: 2026-05-28T03:04:39.105967+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=74245.7
- Funnel: target 775 → liquid 149 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SNOWSTOCK/USDT:USDT | +35.09% | $7,074,105.58 |
| GENIUS/USDT:USDT | +17.59% | $1,799,050.82 |
| NBISSTOCK/USDT:USDT | +13.72% | $1,535,980.69 |
| XLM/USDT:USDT | +9.32% | $81,945,183.47 |
| RIVER/USDT:USDT | +5.77% | $13,513,626.35 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GENIUS/USDT:USDT | below_1h_threshold | +0.80% | +0.81% |
| XLM/USDT:USDT | below_1h_threshold | +0.60% | +0.61% |
| RIF/USDT:USDT | below_1h_threshold | +0.30% | +0.31% |
| NIGHT/USDT:USDT | below_1h_threshold | +0.20% | +0.21% |
| SEI/USDT:USDT | below_1h_threshold | +0.16% | +0.17% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
