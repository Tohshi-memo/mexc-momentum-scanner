# Decision Report

- generated_at: 2026-05-07T19:37:31.850435+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3689**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3689, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/15 | 33.3% | +2.49% | **+0.83%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.60% | **+0.56%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +3.66% | **+2.93%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.89% | **+1.88%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +2.63% | **+1.84%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.14% | **+0.97%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.45% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$99.82** / 初期 $100.00 (-0.18%)
- 確定トレード: 22件 (TP 6 / SL 14 / EXP 2)
- 最新: LAB/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.82
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.96** / 初期 $100.00 (+8.96%)
- 確定: 183件 (Win 48 / Loss 63 / Flat 72) / skip 67件
- 成長率目線: 平均log +0.000469 / 幾何平均 +0.047% per trade / maxDD +3.00%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BILL/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $108.96

## 4. Latest Market Context

- 更新: 2026-05-07T19:37:28.811721+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.16% price=80029.1
- Funnel: target 766 → liquid 184 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +39.69% | $3,620,973.31 |
| JTO/USDT:USDT | +21.86% | $14,850,822.21 |
| NOT/USDT:USDT | +15.90% | $9,100,775.61 |
| DYDX/USDT:USDT | +15.53% | $7,313,690.45 |
| SATO/USDT:USDT | +14.92% | $6,218,303.83 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DYDX/USDT:USDT | below_1h_threshold | +3.38% | +3.55% |
| IO/USDT:USDT | below_1h_threshold | +2.08% | +2.24% |
| D/USDT:USDT | below_1h_threshold | +2.05% | +2.21% |
| TONCOIN/USDT:USDT | below_1h_threshold | +1.90% | +2.06% |
| STRK/USDT:USDT | below_1h_threshold | +1.63% | +1.80% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
