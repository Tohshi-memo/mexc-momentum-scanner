# Decision Report

- generated_at: 2026-05-30T05:49:46.977213+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5105**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5105, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=-1.50%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.50% | **-1.50%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 6/20 | 30.0% | +7.43% | **+2.23%** |
| LIMIT_10PCT | 4/20 | 20.0% | +8.00% | **+1.60%** |
| LIMIT_8PCT | 7/20 | 35.0% | +2.73% | **+0.96%** |
| LIMIT_7PCT | 7/20 | 35.0% | +0.63% | **+0.22%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.20% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +3.20% | **+3.20%** |
| MARKET_LONG | 20/20 | 100.0% | +2.20% | **+2.20%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +2.73% | **+1.36%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.84% | **+1.29%** |
| ASK_LONG | 20/20 | 100.0% | +1.23% | **+1.23%** |

## 2. $100 Live Portfolio

- 残高: **$98.10** / 初期 $100.00 (-1.90%)
- 確定トレード: 75件 (TP 22 / SL 50 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$126.64** / 初期 $100.00 (+26.64%)
- 確定: 762件 (Win 177 / Loss 227 / Flat 358) / skip 904件
- 成長率目線: 平均log +0.000310 / 幾何平均 +0.031% per trade / maxDD +4.72%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_BB3S` EXPIRED account +0.00% 残高後 $126.64

## 4. Latest Market Context

- 更新: 2026-05-30T05:49:44.762289+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.31% price=73592.8
- Funnel: target 773 → liquid 143 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +56.81% | $12,528,933.78 |
| BASED/USDT:USDT | +24.73% | $2,888,311.23 |
| ID/USDT:USDT | +23.00% | $6,611,863.82 |
| LAB/USDT:USDT | +21.51% | $139,047,227.75 |
| XLM/USDT:USDT | +21.32% | $477,064,627.18 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BASED/USDT:USDT | below_1h_threshold | +3.96% | +3.65% |
| LAB/USDT:USDT | below_1h_threshold | +3.23% | +2.92% |
| INJ/USDT:USDT | below_1h_threshold | +2.63% | +2.32% |
| LIT/USDT:USDT | below_1h_threshold | +2.59% | +2.28% |
| JTO/USDT:USDT | below_1h_threshold | +2.28% | +1.97% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
