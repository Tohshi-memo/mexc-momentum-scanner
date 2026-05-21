# Decision Report

- generated_at: 2026-05-21T14:03:59.148303+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4634**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4634, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=-0.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.12% | **-0.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/16 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_5PCT | 5/20 | 25.0% | +2.36% | **+0.59%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.73% | **+0.40%** |
| LIMIT_3PCT | 12/20 | 60.0% | +0.51% | **+0.31%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.76% | **+0.88%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.18% | **+0.65%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +0.82% | **+0.45%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.51% | **+0.33%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +0.06% | **+0.01%** |

## 2. $100 Live Portfolio

- 残高: **$95.25** / 初期 $100.00 (-4.75%)
- 確定トレード: 60件 (TP 15 / SL 42 / EXP 3)
- 最新: STXSTOCK/USDT:USDT SL_HIT PnL -1.86% 残高後 $95.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定: 546件 (Win 138 / Loss 185 / Flat 223) / skip 649件
- 成長率目線: 平均log +0.000355 / 幾何平均 +0.036% per trade / maxDD +4.21%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PROVE/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $121.41

## 4. Latest Market Context

- 更新: 2026-05-21T14:03:56.518785+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=77194.5
- Funnel: target 766 → liquid 135 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NEX/USDT:USDT | +46.66% | $1,415,637.22 |
| FIDA/USDT:USDT | +43.76% | $13,877,362.30 |
| PROVE/USDT:USDT | +39.59% | $6,506,034.37 |
| EDEN/USDT:USDT | +39.33% | $33,194,952.60 |
| ROAM/USDT:USDT | +39.01% | $2,313,824.41 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FIDA/USDT:USDT | below_1h_threshold | +4.92% | +4.79% |
| NEX/USDT:USDT | below_1h_threshold | +2.06% | +1.93% |
| AVNT/USDT:USDT | below_1h_threshold | +0.99% | +0.85% |
| NIL/USDT:USDT | below_1h_threshold | +0.92% | +0.78% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +0.87% | +0.73% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
