# Decision Report

- generated_at: 2026-05-10T12:37:39.267174+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3962**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3962, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-0.43%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.43% | **-0.43%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +0.25% | **+0.04%** |
| LIMIT_3PCT | 16/20 | 80.0% | -0.02% | **-0.02%** |
| LIMIT_4PCT | 14/20 | 70.0% | -0.27% | **-0.19%** |
| LIMIT_2PCT | 17/20 | 85.0% | -0.31% | **-0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +3.53% | **+1.77%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.73% | **+0.55%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.53% | **+0.43%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +1.04% | **+0.42%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.79% | **+0.39%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.73** / 初期 $100.00 (+7.73%)
- 確定: 197件 (Win 48 / Loss 66 / Flat 83) / skip 326件
- 成長率目線: 平均log +0.000378 / 幾何平均 +0.038% per trade / maxDD +4.09%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAYER/USDT:USDT `LIMIT_5PCT_LONG` EXPIRED account +0.00% 残高後 $107.73

## 4. Latest Market Context

- 更新: 2026-05-10T12:37:36.336143+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=80868.0
- Funnel: target 769 → liquid 161 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TROLLSOL/USDT:USDT | +66.57% | $2,083,495.31 |
| LAYER/USDT:USDT | +36.17% | $9,010,548.09 |
| GIGA/USDT:USDT | +22.38% | $1,234,321.45 |
| XEC/USDT:USDT | +22.35% | $3,059,023.60 |
| INX/USDT:USDT | +16.79% | $17,984,023.99 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TROLLSOL/USDT:USDT | below_1h_threshold | +2.24% | +2.14% |
| BASED/USDT:USDT | below_1h_threshold | +2.11% | +2.00% |
| TAG/USDT:USDT | below_1h_threshold | +1.86% | +1.75% |
| INX/USDT:USDT | below_1h_threshold | +1.70% | +1.60% |
| M/USDT:USDT | below_1h_threshold | +1.62% | +1.51% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
