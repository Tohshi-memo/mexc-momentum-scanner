# Decision Report

- generated_at: 2026-04-30T22:26:07.150993+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2738**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2738, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=-1.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.05% | **-1.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.92% | **+0.67%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.60% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +3.56% | **+2.67%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.58% | **+2.32%** |
| ASK_LONG | 20/20 | 100.0% | +1.45% | **+1.45%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.55% | **+1.40%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.49% | **+1.37%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: GRIFFAIN/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-04-30T22:26:03.216913+00:00 / 保存件数 119/288
- BTC: BULLISH 1h +0.20% price=76357.3
- Funnel: target 756 → liquid 219 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BR/USDT:USDT | +19.55% | $13,443,685.89 |
| ORCA/USDT:USDT | +19.01% | $3,201,231.22 |
| AIOT/USDT:USDT | +17.88% | $17,582,853.69 |
| DRIFT/USDT:USDT | +13.70% | $1,315,071.55 |
| RDDTSTOCK/USDT:USDT | +11.89% | $3,813,741.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZBCN/USDT:USDT | below_1h_threshold | +3.11% | +2.91% |
| UB/USDT:USDT | below_1h_threshold | +2.89% | +2.69% |
| DRIFT/USDT:USDT | below_1h_threshold | +2.30% | +2.10% |
| RDDTSTOCK/USDT:USDT | below_1h_threshold | +1.91% | +1.71% |
| BR/USDT:USDT | below_1h_threshold | +1.79% | +1.59% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
