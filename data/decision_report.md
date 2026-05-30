# Decision Report

- generated_at: 2026-05-30T07:05:31.934930+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5108**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5108, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.34% | **-0.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 5/20 | 25.0% | +7.32% | **+1.83%** |
| LIMIT_10PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_8PCT | 5/20 | 25.0% | +3.88% | **+0.97%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.12% | **+0.28%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.74% | **+0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/5 | 100.0% | +1.76% | **+1.76%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| ASK_LONG | 20/20 | 100.0% | +0.89% | **+0.89%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.22% | **+0.73%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +2.12% | **+0.64%** |

## 2. $100 Live Portfolio

- 残高: **$98.10** / 初期 $100.00 (-1.90%)
- 確定トレード: 75件 (TP 22 / SL 50 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.37** / 初期 $100.00 (+25.37%)
- 確定: 764件 (Win 177 / Loss 229 / Flat 358) / skip 905件
- 成長率目線: 平均log +0.000296 / 幾何平均 +0.030% per trade / maxDD +4.72%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $125.37

## 4. Latest Market Context

- 更新: 2026-05-30T07:05:29.743890+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=73505.0
- Funnel: target 773 → liquid 132 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +59.31% | $13,589,924.54 |
| LAB/USDT:USDT | +23.18% | $120,883,006.37 |
| XLM/USDT:USDT | +19.39% | $444,155,339.71 |
| ID/USDT:USDT | +19.16% | $6,629,313.50 |
| BASED/USDT:USDT | +17.34% | $2,980,638.74 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MYX/USDT:USDT | below_1h_threshold | +0.55% | +0.61% |
| LAB/USDT:USDT | below_1h_threshold | +0.25% | +0.31% |
| XPL/USDT:USDT | below_1h_threshold | +0.21% | +0.28% |
| XLM/USDT:USDT | below_1h_threshold | +0.14% | +0.21% |
| ID/USDT:USDT | below_1h_threshold | +0.13% | +0.20% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
