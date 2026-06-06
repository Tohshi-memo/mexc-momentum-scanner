# Decision Report

- generated_at: 2026-06-06T11:06:39.732615+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5815**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5815, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +3.20% | **+1.12%** |
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.12% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +2.39% | **+1.92%** |
| ASK_LONG | 20/20 | 100.0% | +1.81% | **+1.81%** |
| MARKET_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.17% | **+1.41%** |
| LIMIT_BB3S_LONG | 6/7 | 85.7% | +1.36% | **+1.17%** |

## 2. $100 Live Portfolio

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定トレード: 0件 (TP 0 / SL 0 / EXP 0)

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.54** / 初期 $100.00 (+30.54%)
- 確定: 1013件 (Win 239 / Loss 313 / Flat 461) / skip 1363件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +7.25%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HOME/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $130.54

## 4. Latest Market Context

- 更新: 2026-06-06T11:06:36.796528+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.20% price=60683.8
- Funnel: target 771 → liquid 149 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ALLO/USDT:USDT | +107.70% | $32,731,757.57 |
| BLUAI/USDT:USDT | +53.46% | $2,706,892.40 |
| VELVET/USDT:USDT | +41.04% | $2,970,705.63 |
| HEI/USDT:USDT | +33.92% | $2,714,494.39 |
| ZEST/USDT:USDT | +16.44% | $1,943,016.07 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VELVET/USDT:USDT | below_1h_threshold | +3.03% | +2.83% |
| ALLO/USDT:USDT | below_1h_threshold | +2.62% | +2.42% |
| BLUAI/USDT:USDT | below_1h_threshold | +2.42% | +2.22% |
| HOME/USDT:USDT | below_1h_threshold | +1.88% | +1.69% |
| VVV/USDT:USDT | below_1h_threshold | +1.81% | +1.61% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
