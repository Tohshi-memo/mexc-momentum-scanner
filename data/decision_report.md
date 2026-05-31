# Decision Report

- generated_at: 2026-05-31T20:01:57.273812+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5223**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5223, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.32% | **-1.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 8/20 | 40.0% | +2.65% | **+1.06%** |
| LIMIT_7PCT | 3/20 | 15.0% | +6.27% | **+0.94%** |
| LIMIT_5PCT | 10/20 | 50.0% | +1.66% | **+0.83%** |
| LIMIT_BB3S | 10/19 | 52.6% | +0.39% | **+0.20%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.24% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.86% | **+1.57%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.34% | **+1.29%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.53% | **+0.92%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.03% | **+0.91%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.89% | **+0.72%** |

## 2. $100 Live Portfolio

- 残高: **$98.09** / 初期 $100.00 (-1.91%)
- 確定トレード: 81件 (TP 24 / SL 54 / EXP 3)
- 最新: GUN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.09
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.16** / 初期 $100.00 (+31.16%)
- 確定: 858件 (Win 199 / Loss 255 / Flat 404) / skip 926件
- 成長率目線: 平均log +0.000316 / 幾何平均 +0.032% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STG/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $131.16

## 4. Latest Market Context

- 更新: 2026-05-31T20:01:54.298379+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=73616.8
- Funnel: target 773 → liquid 128 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STG/USDT:USDT | +33.57% | $14,141,082.75 |
| BSB/USDT:USDT | +11.38% | $4,742,897.94 |
| UB/USDT:USDT | +11.29% | $6,881,505.77 |
| BIANRENSHENG/USDT:USDT | +11.01% | $2,812,323.87 |
| ZORA/USDT:USDT | +10.31% | $1,334,115.14 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JUP/USDT:USDT | below_1h_threshold | +1.38% | +1.25% |
| BSB/USDT:USDT | below_1h_threshold | +1.00% | +0.87% |
| DYDX/USDT:USDT | below_1h_threshold | +0.93% | +0.80% |
| POL/USDT:USDT | below_1h_threshold | +0.72% | +0.59% |
| MONAD/USDT:USDT | below_1h_threshold | +0.69% | +0.57% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
