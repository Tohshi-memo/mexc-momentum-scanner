# Decision Report

- generated_at: 2026-05-23T13:59:29.054032+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4784**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4784, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=-0.69%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.69% | **-0.69%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_FIB1618 | 4/20 | 20.0% | +0.99% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.38% | **+2.02%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.34% | **+1.52%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.88% | **+1.22%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +5.26% | **+0.53%** |

## 2. $100 Live Portfolio

- 残高: **$96.68** / 初期 $100.00 (-3.32%)
- 確定トレード: 63件 (TP 17 / SL 43 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.91** / 初期 $100.00 (+20.91%)
- 確定: 616件 (Win 150 / Loss 195 / Flat 271) / skip 729件
- 成長率目線: 平均log +0.000308 / 幾何平均 +0.031% per trade / maxDD +4.25%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_7PCT_LONG` SL_HIT account -0.50% 残高後 $120.91

## 4. Latest Market Context

- 更新: 2026-05-23T13:59:27.032859+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.61% price=75179.2
- Funnel: target 764 → liquid 129 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=1, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +124.61% | $89,382,375.82 |
| IN/USDT:USDT | +37.14% | $3,099,167.41 |
| BEAT/USDT:USDT | +33.09% | $71,198,519.82 |
| GMTTOKEN/USDT:USDT | +25.21% | $3,593,908.32 |
| BILL/USDT:USDT | +21.25% | $17,151,032.09 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GMTTOKEN/USDT:USDT | below_relative_strength | +5.17% | +4.56% |
| GENIUS/USDT:USDT | below_1h_threshold | +4.93% | +4.32% |
| BANANAS31/USDT:USDT | below_1h_threshold | +3.76% | +3.15% |
| GRASS/USDT:USDT | below_1h_threshold | +3.73% | +3.13% |
| BEAT/USDT:USDT | below_1h_threshold | +3.39% | +2.78% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
