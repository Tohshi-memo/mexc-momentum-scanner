# Decision Report

- generated_at: 2026-05-06T11:07:24.695894+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3445**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3445, expectancy=-0.14%
- 直近20件 MARKET基準: n=20, expectancy=-0.71%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.71% | **-0.71%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.47% | **+0.19%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.00% | **+0.00%** |
| LIMIT_BB3S | 5/12 | 41.7% | -0.31% | **-0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.25% | **+0.75%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.34% | **+0.74%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.91% | **+0.72%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +2.03% | **+0.71%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.09% | **+0.71%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$98.51** / 初期 $100.00 (-1.49%)
- 確定: 7件 (Win 0 / Loss 3 / Flat 4) / skip 0件
- 成長率目線: 平均log -0.002148 / 幾何平均 -0.215% per trade / maxDD +1.49%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BILL/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $98.51

## 4. Latest Market Context

- 更新: 2026-05-06T11:07:22.068575+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.20% price=82404.5
- Funnel: target 770 → liquid 199 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IO/USDT:USDT | +49.31% | $12,553,381.75 |
| B3/USDT:USDT | +41.85% | $1,510,242.20 |
| BILL/USDT:USDT | +39.61% | $2,131,124.66 |
| ZEC/USDT:USDT | +34.39% | $758,092,003.91 |
| LAB/USDT:USDT | +34.36% | $119,574,771.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +3.26% | +3.06% |
| BILL/USDT:USDT | below_1h_threshold | +2.80% | +2.61% |
| TAG/USDT:USDT | below_1h_threshold | +2.40% | +2.21% |
| TONCOIN/USDT:USDT | below_1h_threshold | +1.79% | +1.59% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +1.16% | +0.96% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
