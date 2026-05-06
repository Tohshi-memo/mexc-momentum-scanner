# Decision Report

- generated_at: 2026-05-06T10:52:27.844313+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3444**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3444, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-1.31%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.31% | **-1.31%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | -0.03% | **-0.01%** |
| LIMIT_BB3S | 5/12 | 41.7% | -0.31% | **-0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.66% | **+1.32%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.72% | **+0.95%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.87% | **+0.94%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.51% | **+0.91%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +2.12% | **+0.85%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定: 6件 (Win 0 / Loss 2 / Flat 4) / skip 0件
- 成長率目線: 平均log -0.001671 / 幾何平均 -0.167% per trade / maxDD +1.00%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B3/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $99.00

## 4. Latest Market Context

- 更新: 2026-05-06T10:52:25.098453+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.22% price=82135.7
- Funnel: target 769 → liquid 203 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=1, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IO/USDT:USDT | +54.42% | $12,252,820.12 |
| B3/USDT:USDT | +41.01% | $1,510,278.58 |
| BILL/USDT:USDT | +37.37% | $1,895,004.49 |
| ZEC/USDT:USDT | +34.96% | $764,509,824.67 |
| STORJ/USDT:USDT | +32.70% | $2,773,504.56 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| B3/USDT:USDT | below_relative_strength | +5.09% | +4.88% |
| IO/USDT:USDT | below_1h_threshold | +4.01% | +3.79% |
| VVV/USDT:USDT | below_1h_threshold | +3.77% | +3.55% |
| TONCOIN/USDT:USDT | below_1h_threshold | +3.69% | +3.48% |
| XMR/USDT:USDT | below_1h_threshold | +3.02% | +2.81% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
