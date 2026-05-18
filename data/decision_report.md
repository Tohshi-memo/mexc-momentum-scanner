# Decision Report

- generated_at: 2026-05-18T22:33:35.180262+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4455**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4455, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.70%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.70% | **-0.70%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 15/20 | 75.0% | +1.02% | **+0.77%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.71% | **+0.36%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 15/20 | 75.0% | +2.16% | **+1.62%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.46% | **+1.11%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +2.24% | **+0.90%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.87% | **+0.78%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.28% | **+0.77%** |

## 2. $100 Live Portfolio

- 残高: **$96.70** / 初期 $100.00 (-3.30%)
- 確定トレード: 54件 (TP 14 / SL 37 / EXP 3)
- 最新: DASH/USDT:USDT TP_HIT PnL +5.37% 残高後 $96.70
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.88** / 初期 $100.00 (+20.88%)
- 確定: 452件 (Win 118 / Loss 155 / Flat 179) / skip 564件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +4.21%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ONDO/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.67% 残高後 $120.88

## 4. Latest Market Context

- 更新: 2026-05-18T22:33:33.215751+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=77090.7
- Funnel: target 763 → liquid 142 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RON/USDT:USDT | +47.73% | $5,669,600.90 |
| ONDO/USDT:USDT | +10.26% | $37,819,382.10 |
| AKT/USDT:USDT | +8.39% | $1,507,318.08 |
| INJ/USDT:USDT | +7.34% | $19,234,106.48 |
| NEAR/USDT:USDT | +6.47% | $9,440,836.27 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RON/USDT:USDT | below_1h_threshold | +4.18% | +4.14% |
| MONAD/USDT:USDT | below_1h_threshold | +1.69% | +1.65% |
| PENDLE/USDT:USDT | below_1h_threshold | +1.66% | +1.63% |
| ZEC/USDT:USDT | below_1h_threshold | +1.40% | +1.36% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +1.22% | +1.18% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
