# Decision Report

- generated_at: 2026-05-28T14:09:45.318217+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4965**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.29% / filled 20/20。**
- 全期間 MARKET基準: n=4965, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+0.29%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.29% | **+0.29%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 17/20 | 85.0% | +0.86% | **+0.73%** |
| ASK | 20/20 | 100.0% | +0.56% | **+0.56%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.47% | **+0.43%** |
| MARKET | 20/20 | 100.0% | +0.29% | **+0.29%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.39% | **+0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |
| LIMIT_8PCT_LONG | 4/20 | 20.0% | +0.00% | **+0.00%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | -0.31% | **-0.09%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | -0.23% | **-0.11%** |
| MARKET_LONG | 20/20 | 100.0% | -0.19% | **-0.19%** |

## 2. $100 Live Portfolio

- 残高: **$98.61** / 初期 $100.00 (-1.39%)
- 確定トレード: 71件 (TP 21 / SL 47 / EXP 3)
- 最新: BILL/USDT:USDT TP_HIT PnL +8.00% 残高後 $98.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$126.79** / 初期 $100.00 (+26.79%)
- 確定: 700件 (Win 172 / Loss 220 / Flat 308) / skip 826件
- 成長率目線: 平均log +0.000339 / 幾何平均 +0.034% per trade / maxDD +4.72%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $126.79

## 4. Latest Market Context

- 更新: 2026-05-28T14:09:43.127613+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.30% price=72772.6
- Funnel: target 776 → liquid 156 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SNOWSTOCK/USDT:USDT | +33.77% | $11,278,852.49 |
| ONDSSTOCK/USDT:USDT | +24.03% | $1,160,768.22 |
| XLM/USDT:USDT | +19.62% | $211,882,055.22 |
| PRL/USDT:USDT | +13.40% | $2,449,105.48 |
| NBISSTOCK/USDT:USDT | +8.08% | $2,157,233.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +2.71% | +3.01% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +1.24% | +1.54% |
| DRAM/USDT:USDT | below_1h_threshold | +1.08% | +1.37% |
| STXSTOCK/USDT:USDT | below_1h_threshold | +0.99% | +1.29% |
| BEAT/USDT:USDT | below_1h_threshold | +0.94% | +1.24% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
