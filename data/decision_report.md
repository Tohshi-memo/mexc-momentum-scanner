# Decision Report

- generated_at: 2026-05-19T23:43:43.499459+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4512**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4512, expectancy=-0.10%
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
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.86% | **+0.60%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +2.62% | **+0.52%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +2.75% | **+1.92%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +2.00% | **+1.20%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.41% | **+1.13%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.61% | **+0.88%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.24% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 55件 (TP 14 / SL 38 / EXP 3)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$124.54** / 初期 $100.00 (+24.54%)
- 確定: 477件 (Win 127 / Loss 165 / Flat 185) / skip 596件
- 成長率目線: 平均log +0.000460 / 幾何平均 +0.046% per trade / maxDD +4.21%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PROMPT/USDT:USDT `LIMIT_3PCT_LONG` TP_HIT account +1.00% 残高後 $124.54

## 4. Latest Market Context

- 更新: 2026-05-19T23:43:41.510402+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.26% price=76876.8
- Funnel: target 760 → liquid 139 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PROMPT/USDT:USDT | +41.74% | $11,294,090.41 |
| EDEN/USDT:USDT | +29.35% | $16,283,586.08 |
| LIT/USDT:USDT | +15.59% | $3,847,738.68 |
| BANANAS31/USDT:USDT | +12.43% | $1,399,711.79 |
| BSB/USDT:USDT | +12.04% | $35,737,272.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FIDA/USDT:USDT | below_1h_threshold | +2.54% | +2.28% |
| LIT/USDT:USDT | below_1h_threshold | +2.53% | +2.26% |
| GUA/USDT:USDT | below_1h_threshold | +1.94% | +1.68% |
| ALGO/USDT:USDT | below_1h_threshold | +1.89% | +1.63% |
| HOME/USDT:USDT | below_1h_threshold | +1.49% | +1.22% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
