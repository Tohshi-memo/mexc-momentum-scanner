# Decision Report

- generated_at: 2026-05-10T14:57:47.096374+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3967**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3967, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-0.94%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.94% | **-0.94%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.17% | **+0.13%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +0.25% | **+0.04%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.02% | **+0.01%** |
| LIMIT_ATR | 13/20 | 65.0% | -0.15% | **-0.10%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +3.59% | **+1.97%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.99% | **+0.79%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.50% | **+0.75%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.95% | **+0.66%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.32% | **+0.59%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.73** / 初期 $100.00 (+7.73%)
- 確定: 198件 (Win 48 / Loss 66 / Flat 84) / skip 330件
- 成長率目線: 平均log +0.000376 / 幾何平均 +0.038% per trade / maxDD +4.09%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BILL/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $107.73

## 4. Latest Market Context

- 更新: 2026-05-10T14:57:44.004830+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=80921.0
- Funnel: target 769 → liquid 165 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TROLLSOL/USDT:USDT | +61.89% | $2,462,458.25 |
| LAYER/USDT:USDT | +37.43% | $9,760,512.04 |
| GIGA/USDT:USDT | +32.33% | $1,348,848.48 |
| TRUTH/USDT:USDT | +24.97% | $1,113,307.13 |
| BILL/USDT:USDT | +18.91% | $44,334,298.56 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FHE/USDT:USDT | below_1h_threshold | +4.43% | +4.45% |
| BASED/USDT:USDT | below_1h_threshold | +3.40% | +3.41% |
| TRUTH/USDT:USDT | below_1h_threshold | +3.05% | +3.06% |
| LUNC/USDT:USDT | below_1h_threshold | +2.73% | +2.75% |
| M/USDT:USDT | below_1h_threshold | +2.48% | +2.50% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
