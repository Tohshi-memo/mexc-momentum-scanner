# Decision Report

- generated_at: 2026-05-19T23:03:41.987305+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4511**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4511, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +3.60% | **+1.44%** |
| LIMIT_6PCT | 4/20 | 20.0% | +4.94% | **+0.99%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.86% | **+0.60%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +2.35% | **+0.35%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.34% | **+1.52%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.45% | **+0.80%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.97% | **+0.73%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +4.00% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 55件 (TP 14 / SL 38 / EXP 3)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$123.31** / 初期 $100.00 (+23.31%)
- 確定: 476件 (Win 126 / Loss 165 / Flat 185) / skip 596件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +4.21%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PROMPT/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $123.31

## 4. Latest Market Context

- 更新: 2026-05-19T23:03:39.989436+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=76706.7
- Funnel: target 760 → liquid 137 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PROMPT/USDT:USDT | +41.46% | $10,318,272.99 |
| EDEN/USDT:USDT | +29.78% | $15,897,124.81 |
| BSB/USDT:USDT | +13.58% | $35,151,328.07 |
| BANANAS31/USDT:USDT | +13.42% | $1,362,029.34 |
| LIT/USDT:USDT | +13.13% | $3,479,863.49 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PROMPT/USDT:USDT | below_1h_threshold | +0.70% | +0.66% |
| FIDA/USDT:USDT | below_1h_threshold | +0.48% | +0.44% |
| PYTH/USDT:USDT | below_1h_threshold | +0.36% | +0.32% |
| LAB/USDT:USDT | below_1h_threshold | +0.35% | +0.31% |
| BIANRENSHENG/USDT:USDT | below_1h_threshold | +0.35% | +0.31% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
