# Decision Report

- generated_at: 2026-05-07T20:12:38.766389+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3693**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3693, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/16 | 31.2% | +2.67% | **+0.83%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.08% | **+0.62%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| LIMIT_4PCT | 14/20 | 70.0% | -0.29% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.78% | **+1.81%** |
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +2.21% | **+1.66%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.87% | **+1.12%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.28% | **+1.02%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.82% | **+0.53%** |

## 2. $100 Live Portfolio

- 残高: **$99.82** / 初期 $100.00 (-0.18%)
- 確定トレード: 22件 (TP 6 / SL 14 / EXP 2)
- 最新: LAB/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.82
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.96** / 初期 $100.00 (+8.96%)
- 確定: 187件 (Win 48 / Loss 63 / Flat 76) / skip 67件
- 成長率目線: 平均log +0.000459 / 幾何平均 +0.046% per trade / maxDD +3.00%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DYDX/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $108.96

## 4. Latest Market Context

- 更新: 2026-05-07T20:12:35.633819+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=80139.6
- Funnel: target 766 → liquid 187 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +45.54% | $4,481,405.07 |
| JTO/USDT:USDT | +22.12% | $15,278,486.79 |
| NIL/USDT:USDT | +20.33% | $9,706,127.93 |
| DYDX/USDT:USDT | +17.87% | $7,921,772.10 |
| NOT/USDT:USDT | +16.69% | $9,374,464.07 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JTO/USDT:USDT | below_1h_threshold | +3.23% | +3.17% |
| STRK/USDT:USDT | below_1h_threshold | +2.04% | +1.98% |
| DYDX/USDT:USDT | below_1h_threshold | +2.02% | +1.96% |
| NIL/USDT:USDT | below_1h_threshold | +1.97% | +1.90% |
| HMSTR/USDT:USDT | below_1h_threshold | +1.87% | +1.81% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
