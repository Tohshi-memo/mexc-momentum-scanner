# Decision Report

- generated_at: 2026-05-24T17:39:14.793129+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4830**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4830, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-1.83%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.83% | **-1.83%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 2/20 | 10.0% | +1.02% | **+0.10%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| LIMIT_FIB1272 | 12/20 | 60.0% | -0.10% | **-0.06%** |
| LIMIT_4PCT | 16/20 | 80.0% | -0.25% | **-0.20%** |
| LIMIT_3PCT | 16/20 | 80.0% | -1.16% | **-0.93%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +2.45% | **+2.45%** |
| ASK_LONG | 20/20 | 100.0% | +1.75% | **+1.75%** |
| MARKET_LONG | 20/20 | 100.0% | +1.43% | **+1.43%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +2.55% | **+1.28%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +2.45% | **+0.98%** |

## 2. $100 Live Portfolio

- 残高: **$96.68** / 初期 $100.00 (-3.32%)
- 確定トレード: 63件 (TP 17 / SL 43 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$122.90** / 初期 $100.00 (+22.90%)
- 確定: 636件 (Win 156 / Loss 200 / Flat 280) / skip 755件
- 成長率目線: 平均log +0.000324 / 幾何平均 +0.032% per trade / maxDD +4.72%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIL/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $122.90

## 4. Latest Market Context

- 更新: 2026-05-24T17:39:12.090542+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=76636.3
- Funnel: target 764 → liquid 114 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIL/USDT:USDT | +13.82% | $8,326,668.94 |
| BEAT/USDT:USDT | +6.81% | $38,098,766.48 |
| UB/USDT:USDT | +6.37% | $3,456,702.33 |
| MYX/USDT:USDT | +4.46% | $3,051,238.49 |
| PHA/USDT:USDT | +3.05% | $1,293,916.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_1h_threshold | +4.52% | +4.53% |
| BEAT/USDT:USDT | below_1h_threshold | +3.58% | +3.59% |
| BILL/USDT:USDT | below_1h_threshold | +2.68% | +2.69% |
| PLUME/USDT:USDT | below_1h_threshold | +2.39% | +2.40% |
| INJ/USDT:USDT | below_1h_threshold | +1.52% | +1.53% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
