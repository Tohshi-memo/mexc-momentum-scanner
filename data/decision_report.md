# Decision Report

- generated_at: 2026-05-12T21:18:06.852680+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4164**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4164, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-0.18%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.18% | **-0.18%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.12% | **+0.74%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_9PCT | 2/20 | 10.0% | +0.29% | **+0.03%** |
| LIMIT_BB3S | 9/18 | 50.0% | -0.16% | **-0.08%** |
| LIMIT_5PCT | 7/20 | 35.0% | -0.46% | **-0.16%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.23% | **+0.92%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.77% | **+0.70%** |
| MARKET_LONG | 20/20 | 100.0% | +0.58% | **+0.58%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.52% | **+0.53%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$98.69** / 初期 $100.00 (-1.31%)
- 確定トレード: 35件 (TP 9 / SL 23 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -3.91% 残高後 $98.69
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$122.40** / 初期 $100.00 (+22.40%)
- 確定: 300件 (Win 88 / Loss 103 / Flat 109) / skip 425件
- 成長率目線: 平均log +0.000674 / 幾何平均 +0.067% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DYM/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $122.40

## 4. Latest Market Context

- 更新: 2026-05-12T21:18:03.461076+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=80650.1
- Funnel: target 757 → liquid 188 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SAGA/USDT:USDT | +17.55% | $59,345,582.88 |
| DYM/USDT:USDT | +17.34% | $2,255,440.08 |
| LAB/USDT:USDT | +13.58% | $119,862,569.23 |
| AKT/USDT:USDT | +10.00% | $2,212,458.07 |
| PEAQ/USDT:USDT | +9.99% | $2,027,811.25 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DYM/USDT:USDT | below_1h_threshold | +3.04% | +3.04% |
| LAB/USDT:USDT | below_1h_threshold | +1.69% | +1.69% |
| AERO/USDT:USDT | below_1h_threshold | +1.54% | +1.55% |
| UB/USDT:USDT | below_1h_threshold | +1.32% | +1.32% |
| AKT/USDT:USDT | below_1h_threshold | +1.17% | +1.17% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
