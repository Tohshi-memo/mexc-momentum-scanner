# Decision Report

- generated_at: 2026-05-22T11:13:53.838288+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4689**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4689, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.72%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.72% | **-0.72%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +1.96% | **+0.29%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | -0.49% | **-0.19%** |
| LIMIT_4PCT | 14/20 | 70.0% | -0.29% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.52% | **+1.52%** |
| ASK_LONG | 20/20 | 100.0% | +1.30% | **+1.30%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.19% | **+0.83%** |
| LIMIT_BB3S_LONG | 6/8 | 75.0% | +1.02% | **+0.76%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$95.25** / 初期 $100.00 (-4.75%)
- 確定トレード: 60件 (TP 15 / SL 42 / EXP 3)
- 最新: STXSTOCK/USDT:USDT SL_HIT PnL -1.86% 残高後 $95.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.99** / 初期 $100.00 (+21.99%)
- 確定: 559件 (Win 142 / Loss 185 / Flat 232) / skip 691件
- 成長率目線: 平均log +0.000356 / 幾何平均 +0.036% per trade / maxDD +4.21%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UB/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $121.99

## 4. Latest Market Context

- 更新: 2026-05-22T11:13:51.769842+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=77277.1
- Funnel: target 768 → liquid 135 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BUILDONBOB/USDT:USDT | +51.76% | $3,760,541.08 |
| ALT/USDT:USDT | +34.61% | $1,903,063.99 |
| EDEN/USDT:USDT | +32.16% | $22,301,698.14 |
| GENIUS/USDT:USDT | +31.91% | $1,612,466.39 |
| BEAT/USDT:USDT | +29.42% | $12,734,964.22 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_1h_threshold | +4.29% | +4.29% |
| WLD/USDT:USDT | below_1h_threshold | +1.09% | +1.10% |
| GRASS/USDT:USDT | below_1h_threshold | +0.70% | +0.71% |
| PENDLE/USDT:USDT | below_1h_threshold | +0.61% | +0.62% |
| ONDO/USDT:USDT | below_1h_threshold | +0.59% | +0.59% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
