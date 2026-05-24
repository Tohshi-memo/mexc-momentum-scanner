# Decision Report

- generated_at: 2026-05-24T08:14:10.523293+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4813**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4813, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=-0.38%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.38% | **-0.38%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.04% | **+0.03%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | -0.79% | **-0.24%** |
| ASK | 20/20 | 100.0% | -0.25% | **-0.25%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.15% | **+0.69%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.23% | **+0.62%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.35% | **+0.61%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.83% | **+0.58%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.89% | **+0.58%** |

## 2. $100 Live Portfolio

- 残高: **$96.68** / 初期 $100.00 (-3.32%)
- 確定トレード: 63件 (TP 17 / SL 43 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.46** / 初期 $100.00 (+20.46%)
- 確定: 619件 (Win 151 / Loss 197 / Flat 271) / skip 755件
- 成長率目線: 平均log +0.000301 / 幾何平均 +0.030% per trade / maxDD +4.72%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIL/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $120.46

## 4. Latest Market Context

- 更新: 2026-05-24T08:14:08.410516+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=76706.1
- Funnel: target 764 → liquid 113 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +45.83% | $1,501,984.94 |
| PLUME/USDT:USDT | +25.73% | $1,913,685.77 |
| BSB/USDT:USDT | +15.42% | $55,729,098.27 |
| BLUAI/USDT:USDT | +14.90% | $1,741,677.95 |
| GRASS/USDT:USDT | +13.65% | $9,342,402.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +2.81% | +2.90% |
| MYX/USDT:USDT | below_1h_threshold | +2.43% | +2.51% |
| UB/USDT:USDT | below_1h_threshold | +1.38% | +1.47% |
| GENIUS/USDT:USDT | below_1h_threshold | +1.35% | +1.43% |
| ONDO/USDT:USDT | below_1h_threshold | +1.13% | +1.22% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
