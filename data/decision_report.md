# Decision Report

- generated_at: 2026-05-20T04:23:46.905642+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4522**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4522, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=-0.58%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.58% | **-0.58%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +2.97% | **+1.04%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_4PCT | 12/20 | 60.0% | +1.06% | **+0.63%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.24% | **+0.56%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.73% | **+1.77%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +2.00% | **+1.10%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.27% | **+0.82%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.56% | **+0.71%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +3.27% | **+0.65%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 55件 (TP 14 / SL 38 / EXP 3)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.04** / 初期 $100.00 (+25.04%)
- 確定: 484件 (Win 128 / Loss 166 / Flat 190) / skip 599件
- 成長率目線: 平均log +0.000462 / 幾何平均 +0.046% per trade / maxDD +4.21%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UP/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $125.04

## 4. Latest Market Context

- 更新: 2026-05-20T04:23:44.898815+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=76788.7
- Funnel: target 764 → liquid 137 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EDEN/USDT:USDT | +39.83% | $19,530,560.55 |
| PROMPT/USDT:USDT | +30.70% | $12,996,291.78 |
| LIT/USDT:USDT | +24.94% | $6,738,719.39 |
| FIDA/USDT:USDT | +17.91% | $1,344,545.61 |
| ZEST/USDT:USDT | +16.93% | $1,936,706.17 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEST/USDT:USDT | below_1h_threshold | +4.90% | +4.76% |
| FIDA/USDT:USDT | below_1h_threshold | +2.98% | +2.85% |
| KITE/USDT:USDT | below_1h_threshold | +2.57% | +2.44% |
| UP/USDT:USDT | below_1h_threshold | +1.91% | +1.78% |
| DYDX/USDT:USDT | below_1h_threshold | +1.36% | +1.23% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
