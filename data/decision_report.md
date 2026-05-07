# Decision Report

- generated_at: 2026-05-07T19:22:51.064733+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3688**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3688, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.60% | **+0.56%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_BB3S | 4/15 | 26.7% | +1.11% | **+0.30%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +3.66% | **+2.93%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +3.47% | **+2.08%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +2.63% | **+1.84%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.14% | **+0.97%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.23% | **+0.89%** |

## 2. $100 Live Portfolio

- 残高: **$99.82** / 初期 $100.00 (-0.18%)
- 確定トレード: 22件 (TP 6 / SL 14 / EXP 2)
- 最新: LAB/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.82
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$109.51** / 初期 $100.00 (+9.51%)
- 確定: 182件 (Win 48 / Loss 62 / Flat 72) / skip 67件
- 成長率目線: 平均log +0.000499 / 幾何平均 +0.050% per trade / maxDD +2.62%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DOGS/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $109.51

## 4. Latest Market Context

- 更新: 2026-05-07T19:22:48.320554+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=80006.1
- Funnel: target 766 → liquid 182 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +39.74% | $3,393,108.24 |
| JTO/USDT:USDT | +23.34% | $14,647,673.47 |
| NOT/USDT:USDT | +15.42% | $8,908,164.08 |
| DYDX/USDT:USDT | +14.15% | $7,101,593.25 |
| SATO/USDT:USDT | +14.05% | $6,134,981.16 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DYDX/USDT:USDT | below_1h_threshold | +2.25% | +2.45% |
| JTO/USDT:USDT | below_1h_threshold | +1.62% | +1.81% |
| TONCOIN/USDT:USDT | below_1h_threshold | +1.28% | +1.47% |
| LIGHT/USDT:USDT | below_1h_threshold | +1.02% | +1.21% |
| NAORIS/USDT:USDT | below_1h_threshold | +1.01% | +1.20% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
