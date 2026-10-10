# Decision Report

- generated_at: 2026-10-10T17:06:13.024663+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16505**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16505, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.19% | **+0.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 3/11 | 27.3% | +2.05% | **+0.56%** |
| MARKET | 20/20 | 100.0% | +0.19% | **+0.19%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_FIB1618 | 4/20 | 20.0% | +0.78% | **+0.16%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.08% | **+0.81%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.88% | **+0.57%** |
| MARKET_LONG | 20/20 | 100.0% | +0.36% | **+0.36%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +0.31% | **+0.17%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +0.30% | **+0.16%** |

## 2. $100 Live Portfolio

- 残高: **$121.24** / 初期 $100.00 (+21.24%)
- 確定トレード: 236件 (TP 87 / SL 142 / EXP 7)
- 最新: STRK/USDT:USDT SL_HIT PnL -3.05% 残高後 $121.24
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,298.24** / 初期 $100.00 (+1198.24%)
- 確定: 6287件 (Win 1845 / Loss 2015 / Flat 2427) / skip 6779件
- 成長率目線: 平均log +0.000408 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CFX/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.39% 残高後 $1,298.24

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.04** / 初期 $100.00 (+174.04%)
- 確定: 3636件 (Win 1010 / Loss 853 / Flat 1773) / skip 6280件
- 成長率目線: 平均log +0.000277 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MINA/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $274.04

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4665件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000336 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-10T17:06:03.277039+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=83029.4
- Funnel: target 1087 → liquid 155 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RLC/USDT:USDT | +14.00% | $34,313,338.89 |
| CHIP/USDT:USDT | +4.60% | $1,872,813.65 |
| BAT/USDT:USDT | +3.99% | $26,270,886.53 |
| SI/USDT:USDT | +3.94% | $1,090,634.82 |
| BR/USDT:USDT | +3.67% | $5,568,582.09 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RLC/USDT:USDT | below_1h_threshold | +4.07% | +4.01% |
| JCT/USDT:USDT | below_1h_threshold | +1.27% | +1.20% |
| CFX/USDT:USDT | below_1h_threshold | +1.00% | +0.94% |
| OGN/USDT:USDT | below_1h_threshold | +0.83% | +0.76% |
| BAT/USDT:USDT | below_1h_threshold | +0.76% | +0.70% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
