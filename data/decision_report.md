# Decision Report

- generated_at: 2026-05-24T21:18:19.451598+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4833**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4833, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 2/20 | 10.0% | +1.02% | **+0.10%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| LIMIT_FIB1272 | 12/20 | 60.0% | -0.16% | **-0.10%** |
| LIMIT_4PCT | 16/20 | 80.0% | -0.25% | **-0.20%** |
| LIMIT_3PCT | 16/20 | 80.0% | -1.16% | **-0.93%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +2.22% | **+2.22%** |
| MARKET_LONG | 20/20 | 100.0% | +1.40% | **+1.40%** |
| ASK_LONG | 20/20 | 100.0% | +1.28% | **+1.28%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +2.43% | **+1.21%** |
| LIMIT_1PCT_LONG | 12/20 | 60.0% | +1.53% | **+0.92%** |

## 2. $100 Live Portfolio

- 残高: **$96.68** / 初期 $100.00 (-3.32%)
- 確定トレード: 63件 (TP 17 / SL 43 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$122.81** / 初期 $100.00 (+22.81%)
- 確定: 639件 (Win 157 / Loss 202 / Flat 280) / skip 755件
- 成長率目線: 平均log +0.000322 / 幾何平均 +0.032% per trade / maxDD +4.72%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIL/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $122.81

## 4. Latest Market Context

- 更新: 2026-05-24T21:18:17.703514+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=76657.8
- Funnel: target 764 → liquid 107 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| UB/USDT:USDT | +8.30% | $4,209,516.47 |
| BILL/USDT:USDT | +7.55% | $13,764,380.93 |
| NIL/USDT:USDT | +3.88% | $12,527,440.96 |
| LUNC/USDT:USDT | +2.19% | $2,791,712.04 |
| PHA/USDT:USDT | +2.13% | $1,386,545.06 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TONCOIN/USDT:USDT | below_1h_threshold | +1.56% | +1.52% |
| UB/USDT:USDT | below_1h_threshold | +1.39% | +1.36% |
| NEAR/USDT:USDT | below_1h_threshold | +1.23% | +1.19% |
| SUPER/USDT:USDT | below_1h_threshold | +0.85% | +0.82% |
| LIT/USDT:USDT | below_1h_threshold | +0.63% | +0.60% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
