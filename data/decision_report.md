# Decision Report

- generated_at: 2026-07-12T03:21:12.507347+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8563**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.48% / filled 20/20。**
- 全期間 MARKET基準: n=8563, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.48%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.48% | **+0.48%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| MARKET | 20/20 | 100.0% | +0.48% | **+0.48%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +4.04% | **+0.40%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.28% | **+0.10%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.11% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.87% | **+1.59%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.55% | **+0.47%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +1.34% | **+0.34%** |
| MARKET_LONG | 20/20 | 100.0% | +0.24% | **+0.24%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.27% | **+0.16%** |

## 2. $100 Live Portfolio

- 残高: **$102.54** / 初期 $100.00 (+2.54%)
- 確定トレード: 86件 (TP 30 / SL 55 / EXP 1)
- 最新: ELSA/USDT:USDT SL_HIT PnL -3.75% 残高後 $102.54
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$318.75** / 初期 $100.00 (+218.75%)
- 確定: 2751件 (Win 868 / Loss 921 / Flat 962) / skip 2373件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: T/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $318.75

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.11** / 初期 $100.00 (+5.11%)
- 確定: 643件 (Win 152 / Loss 159 / Flat 332) / skip 1331件
- 成長率目線: 平均log +0.000078 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0117 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $105.11

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.17** / 初期 $100.00 (-0.83%)
- 確定: 26件 (Win 9 / Loss 17 / Flat 0) / pending 0件 / skip 7件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000199 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: T/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $99.17

## 6. Latest Market Context

- 更新: 2026-07-12T03:21:05.252976+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=64107.0
- Funnel: target 863 → liquid 145 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SXT/USDT:USDT | +27.75% | $13,852,731.87 |
| CASHCAT/USDT:USDT | +18.85% | $2,116,871.59 |
| T/USDT:USDT | +15.43% | $13,440,578.84 |
| FHE/USDT:USDT | +12.47% | $1,582,049.43 |
| BILL/USDT:USDT | +8.51% | $1,381,239.30 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| T/USDT:USDT | below_1h_threshold | +4.92% | +4.83% |
| CASHCAT/USDT:USDT | below_1h_threshold | +3.37% | +3.28% |
| EDGE/USDT:USDT | below_1h_threshold | +2.46% | +2.37% |
| VANRY/USDT:USDT | below_1h_threshold | +2.45% | +2.36% |
| FHE/USDT:USDT | below_1h_threshold | +2.38% | +2.29% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
