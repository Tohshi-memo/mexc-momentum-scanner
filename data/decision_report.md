# Decision Report

- generated_at: 2026-05-30T06:04:51.646530+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5106**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5106, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=-0.90%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.90% | **-0.90%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 5/20 | 25.0% | +7.32% | **+1.83%** |
| LIMIT_10PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_8PCT | 6/20 | 30.0% | +3.85% | **+1.16%** |
| LIMIT_7PCT | 6/20 | 30.0% | +1.40% | **+0.42%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.72% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/5 | 100.0% | +1.76% | **+1.76%** |
| MARKET_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |
| ASK_LONG | 20/20 | 100.0% | +1.23% | **+1.23%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.69% | **+0.93%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.53% | **+0.76%** |

## 2. $100 Live Portfolio

- 残高: **$98.10** / 初期 $100.00 (-1.90%)
- 確定トレード: 75件 (TP 22 / SL 50 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$126.00** / 初期 $100.00 (+26.00%)
- 確定: 763件 (Win 177 / Loss 228 / Flat 358) / skip 904件
- 成長率目線: 平均log +0.000303 / 幾何平均 +0.030% per trade / maxDD +4.72%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ID/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $126.00

## 4. Latest Market Context

- 更新: 2026-05-30T06:04:49.068356+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=73581.3
- Funnel: target 773 → liquid 137 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +56.81% | $12,333,054.40 |
| LAB/USDT:USDT | +22.95% | $127,647,856.36 |
| XLM/USDT:USDT | +22.51% | $460,084,771.63 |
| OL/USDT:USDT | +18.67% | $1,469,877.49 |
| ID/USDT:USDT | +18.17% | $6,535,364.98 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| OL/USDT:USDT | below_1h_threshold | +1.21% | +1.19% |
| XLM/USDT:USDT | below_1h_threshold | +0.96% | +0.94% |
| JTO/USDT:USDT | below_1h_threshold | +0.73% | +0.71% |
| LAB/USDT:USDT | below_1h_threshold | +0.63% | +0.61% |
| LIT/USDT:USDT | below_1h_threshold | +0.42% | +0.40% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
