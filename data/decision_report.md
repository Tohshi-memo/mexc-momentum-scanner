# Decision Report

- generated_at: 2026-05-07T20:22:47.978634+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3694**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3694, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.34% | **-0.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/16 | 25.0% | +1.33% | **+0.33%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.53% | **+0.16%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +2.21% | **+1.66%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.45% | **+1.59%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.01% | **+0.81%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.31% | **+0.72%** |
| MARKET_LONG | 20/20 | 100.0% | +0.34% | **+0.34%** |

## 2. $100 Live Portfolio

- 残高: **$99.82** / 初期 $100.00 (-0.18%)
- 確定トレード: 22件 (TP 6 / SL 14 / EXP 2)
- 最新: LAB/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.82
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.96** / 初期 $100.00 (+8.96%)
- 確定: 188件 (Win 48 / Loss 63 / Flat 77) / skip 67件
- 成長率目線: 平均log +0.000456 / 幾何平均 +0.046% per trade / maxDD +3.00%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RKLBSTOCK/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $108.96

## 4. Latest Market Context

- 更新: 2026-05-07T20:22:41.812468+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=80075.7
- Funnel: target 766 → liquid 189 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +44.95% | $4,684,683.27 |
| NIL/USDT:USDT | +20.74% | $10,046,998.82 |
| JTO/USDT:USDT | +19.77% | $15,431,546.79 |
| NOT/USDT:USDT | +17.40% | $9,445,129.64 |
| DYDX/USDT:USDT | +16.79% | $8,017,850.04 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HMSTR/USDT:USDT | below_1h_threshold | +2.72% | +2.74% |
| NIL/USDT:USDT | below_1h_threshold | +2.16% | +2.18% |
| STRK/USDT:USDT | below_1h_threshold | +1.82% | +1.84% |
| JTO/USDT:USDT | below_1h_threshold | +1.55% | +1.57% |
| JUP/USDT:USDT | below_1h_threshold | +1.12% | +1.14% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
