# Decision Report

- generated_at: 2026-05-24T22:14:18.592493+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4835**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4835, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.97%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.97% | **-0.97%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 2/20 | 10.0% | +1.02% | **+0.10%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| LIMIT_FIB1272 | 12/20 | 60.0% | -0.15% | **-0.09%** |
| LIMIT_4PCT | 14/20 | 70.0% | -0.29% | **-0.20%** |
| LIMIT_3PCT | 16/20 | 80.0% | -0.57% | **-0.45%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.97% | **+0.97%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.70% | **+0.94%** |
| ASK_LONG | 20/20 | 100.0% | +0.88% | **+0.88%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.81% | **+0.81%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +1.25% | **+0.56%** |

## 2. $100 Live Portfolio

- 残高: **$96.68** / 初期 $100.00 (-3.32%)
- 確定トレード: 63件 (TP 17 / SL 43 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$123.02** / 初期 $100.00 (+23.02%)
- 確定: 641件 (Win 158 / Loss 203 / Flat 280) / skip 755件
- 成長率目線: 平均log +0.000323 / 幾何平均 +0.032% per trade / maxDD +4.72%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SUPER/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.67% 残高後 $123.02

## 4. Latest Market Context

- 更新: 2026-05-24T22:14:16.159698+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +1.13% price=76968.7
- Funnel: target 764 → liquid 109 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SUPER/USDT:USDT | +10.43% | $2,858,293.24 |
| NIL/USDT:USDT | +3.52% | $12,940,012.23 |
| BILL/USDT:USDT | +2.65% | $13,612,343.45 |
| SAGA/USDT:USDT | +1.67% | $1,368,482.16 |
| LUNC/USDT:USDT | +1.65% | $2,924,972.17 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PENDLE/USDT:USDT | below_1h_threshold | +2.66% | +1.52% |
| RENDER/USDT:USDT | below_1h_threshold | +2.52% | +1.39% |
| ZEC/USDT:USDT | below_1h_threshold | +2.40% | +1.27% |
| ATOM/USDT:USDT | below_1h_threshold | +2.14% | +1.01% |
| IP/USDT:USDT | below_1h_threshold | +2.05% | +0.92% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
