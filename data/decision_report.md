# Decision Report

- generated_at: 2026-05-18T20:38:00.663633+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4452**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4452, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.45%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.45% | **-0.45%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 16/20 | 80.0% | +0.71% | **+0.57%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.33% | **+0.17%** |
| LIMIT_BB3S | 5/18 | 27.8% | +0.19% | **+0.05%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |
| LIMIT_1PCT | 18/20 | 90.0% | -0.04% | **-0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 14/20 | 70.0% | +2.03% | **+1.42%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.30% | **+1.24%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.79% | **+0.80%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.07% | **+0.75%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +1.46% | **+0.58%** |

## 2. $100 Live Portfolio

- 残高: **$96.70** / 初期 $100.00 (-3.30%)
- 確定トレード: 54件 (TP 14 / SL 37 / EXP 3)
- 最新: DASH/USDT:USDT TP_HIT PnL +5.37% 残高後 $96.70
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定: 449件 (Win 117 / Loss 154 / Flat 178) / skip 564件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +4.21%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TRAC/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $120.68

## 4. Latest Market Context

- 更新: 2026-05-18T20:37:58.975611+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.24% price=77081.6
- Funnel: target 764 → liquid 142 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RON/USDT:USDT | +32.52% | $3,423,764.03 |
| TRAC/USDT:USDT | +7.55% | $1,315,293.83 |
| ZEC/USDT:USDT | +5.24% | $583,724,392.80 |
| OPENLEDGER/USDT:USDT | +4.77% | $1,751,927.57 |
| NEAR/USDT:USDT | +4.62% | $8,763,726.25 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ASTEROID/USDT:USDT | below_1h_threshold | +2.32% | +2.07% |
| KITE/USDT:USDT | below_1h_threshold | +1.72% | +1.48% |
| INJ/USDT:USDT | below_1h_threshold | +1.71% | +1.46% |
| ONDO/USDT:USDT | below_1h_threshold | +1.44% | +1.19% |
| PENGU/USDT:USDT | below_1h_threshold | +1.15% | +0.90% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
