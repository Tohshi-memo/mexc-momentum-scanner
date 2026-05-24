# Decision Report

- generated_at: 2026-05-24T05:14:13.010584+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4811**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4811, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=-0.98%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.98% | **-0.98%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.00% | **+0.00%** |
| LIMIT_3PCT | 14/20 | 70.0% | -0.03% | **-0.02%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | -0.77% | **-0.27%** |
| LIMIT_2PCT | 15/20 | 75.0% | -0.49% | **-0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.56% | **+1.09%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.19% | **+0.71%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +1.58% | **+0.63%** |
| MARKET_LONG | 20/20 | 100.0% | +0.62% | **+0.62%** |
| ASK_LONG | 20/20 | 100.0% | +0.58% | **+0.58%** |

## 2. $100 Live Portfolio

- 残高: **$96.68** / 初期 $100.00 (-3.32%)
- 確定トレード: 63件 (TP 17 / SL 43 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.31** / 初期 $100.00 (+20.31%)
- 確定: 617件 (Win 150 / Loss 196 / Flat 271) / skip 755件
- 成長率目線: 平均log +0.000300 / 幾何平均 +0.030% per trade / maxDD +4.72%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BEAT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $120.31

## 4. Latest Market Context

- 更新: 2026-05-24T05:14:10.892988+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=76704.2
- Funnel: target 764 → liquid 115 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SUPER/USDT:USDT | +19.02% | $1,384,003.60 |
| GRASS/USDT:USDT | +18.73% | $8,420,017.94 |
| BLUAI/USDT:USDT | +15.01% | $1,769,053.03 |
| NIL/USDT:USDT | +14.59% | $2,312,239.02 |
| IN/USDT:USDT | +13.75% | $3,265,787.70 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SUPER/USDT:USDT | below_1h_threshold | +0.99% | +1.05% |
| BSB/USDT:USDT | below_1h_threshold | +0.58% | +0.64% |
| BLUAI/USDT:USDT | below_1h_threshold | +0.58% | +0.64% |
| MYX/USDT:USDT | below_1h_threshold | +0.54% | +0.59% |
| UB/USDT:USDT | below_1h_threshold | +0.44% | +0.50% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
