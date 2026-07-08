# Decision Report

- generated_at: 2026-07-08T05:28:37.518534+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8468**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.89% / filled 20/20。**
- 全期間 MARKET基準: n=8468, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.89%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.89% | **+1.89%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.89% | **+1.89%** |
| ASK | 20/20 | 100.0% | +1.81% | **+1.81%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +4.94% | **+0.49%** |
| LIMIT_BB3S | 3/20 | 15.0% | +2.64% | **+0.40%** |
| LIMIT_9PCT | 3/20 | 15.0% | +1.72% | **+0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +0.63% | **+0.63%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +2.11% | **+0.32%** |
| MARKET_LONG | 20/20 | 100.0% | +0.05% | **+0.05%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.00% | **+0.00%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | -0.27% | **-0.07%** |

## 2. $100 Live Portfolio

- 残高: **$103.08** / 初期 $100.00 (+3.08%)
- 確定トレード: 73件 (TP 26 / SL 46 / EXP 1)
- 最新: DRAM/USDT:USDT TP_HIT PnL +5.87% 残高後 $103.08
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$320.19** / 初期 $100.00 (+220.19%)
- 確定: 2673件 (Win 848 / Loss 898 / Flat 927) / skip 2356件
- 成長率目線: 平均log +0.000435 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EDGE/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $320.19

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.48** / 初期 $100.00 (+5.48%)
- 確定: 641件 (Win 152 / Loss 158 / Flat 331) / skip 1238件
- 成長率目線: 平均log +0.000083 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $105.48

## 5. Latest Market Context

- 更新: 2026-07-08T05:28:30.108552+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=62701.0
- Funnel: target 847 → liquid 176 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +53.47% | $59,017,027.79 |
| EDGE/USDT:USDT | +23.09% | $13,573,528.18 |
| SYN/USDT:USDT | +15.49% | $4,540,337.46 |
| NES/USDT:USDT | +12.28% | $1,089,309.84 |
| LDO/USDT:USDT | +8.15% | $7,750,053.74 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UNI/USDT:USDT | below_1h_threshold | +2.82% | +2.93% |
| EVAA/USDT:USDT | below_1h_threshold | +2.73% | +2.84% |
| APE/USDT:USDT | below_1h_threshold | +2.11% | +2.22% |
| RIF/USDT:USDT | below_1h_threshold | +1.51% | +1.62% |
| EDGE/USDT:USDT | below_1h_threshold | +1.00% | +1.11% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
