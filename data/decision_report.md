# Decision Report

- generated_at: 2026-06-07T15:01:50.888396+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5966**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5966, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=-1.93%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.93% | **-1.93%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +1.02% | **+0.15%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +4.70% | **+3.29%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +4.86% | **+3.16%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +3.87% | **+2.90%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +5.17% | **+2.07%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +3.71% | **+1.48%** |

## 2. $100 Live Portfolio

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定トレード: 5件 (TP 1 / SL 4 / EXP 0)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.00
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$148.82** / 初期 $100.00 (+48.82%)
- 確定: 1083件 (Win 264 / Loss 327 / Flat 492) / skip 1444件
- 成長率目線: 平均log +0.000367 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $148.82

## 4. Latest Market Context

- 更新: 2026-06-07T15:01:48.002446+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=61801.8
- Funnel: target 768 → liquid 122 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +64.40% | $10,097,498.61 |
| FIDA/USDT:USDT | +62.90% | $9,238,169.33 |
| SIREN/USDT:USDT | +60.66% | $24,061,613.62 |
| BLESS/USDT:USDT | +43.01% | $5,744,495.12 |
| LAB/USDT:USDT | +38.73% | $62,981,631.74 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +1.82% | +1.93% |
| EDEN/USDT:USDT | below_1h_threshold | +0.61% | +0.72% |
| H/USDT:USDT | below_1h_threshold | +0.60% | +0.71% |
| PI/USDT:USDT | below_1h_threshold | +0.39% | +0.50% |
| BLESS/USDT:USDT | below_1h_threshold | +0.30% | +0.41% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
