# Decision Report

- generated_at: 2026-05-24T16:14:03.199261+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4828**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4828, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-1.65%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.65% | **-1.65%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 2/20 | 10.0% | +1.02% | **+0.10%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |
| LIMIT_FIB1272 | 12/20 | 60.0% | -0.10% | **-0.06%** |
| LIMIT_4PCT | 15/20 | 75.0% | -0.27% | **-0.20%** |
| LIMIT_3PCT | 16/20 | 80.0% | -0.60% | **-0.48%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +2.45% | **+2.45%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.62% | **+1.44%** |
| ASK_LONG | 20/20 | 100.0% | +1.31% | **+1.31%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +2.57% | **+1.16%** |
| MARKET_LONG | 20/20 | 100.0% | +1.03% | **+1.03%** |

## 2. $100 Live Portfolio

- 残高: **$96.68** / 初期 $100.00 (-3.32%)
- 確定トレード: 63件 (TP 17 / SL 43 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$123.52** / 初期 $100.00 (+23.52%)
- 確定: 634件 (Win 156 / Loss 199 / Flat 279) / skip 755件
- 成長率目線: 平均log +0.000333 / 幾何平均 +0.033% per trade / maxDD +4.72%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIL/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $123.52

## 4. Latest Market Context

- 更新: 2026-05-24T16:14:01.090527+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.28% price=76556.6
- Funnel: target 764 → liquid 113 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +4.32% | $41,989,571.99 |
| NIL/USDT:USDT | +3.68% | $6,707,215.02 |
| MYX/USDT:USDT | +2.38% | $2,963,547.80 |
| EDEN/USDT:USDT | +2.12% | $8,859,416.77 |
| LIT/USDT:USDT | +1.93% | $2,509,933.87 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +4.33% | +4.06% |
| NIL/USDT:USDT | below_1h_threshold | +3.69% | +3.41% |
| MYX/USDT:USDT | below_1h_threshold | +2.38% | +2.10% |
| EDEN/USDT:USDT | below_1h_threshold | +2.03% | +1.75% |
| LIT/USDT:USDT | below_1h_threshold | +1.93% | +1.66% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
