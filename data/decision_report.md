# Decision Report

- generated_at: 2026-05-26T22:54:25.923985+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4910**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.31% / filled 20/20。**
- 全期間 MARKET基準: n=4910, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+1.31%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.31% | **+1.31%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.31% | **+1.31%** |
| ASK | 20/20 | 100.0% | +1.25% | **+1.25%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.70% | **+0.59%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +2.97% | **+2.23%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +1.06% | **+0.85%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +0.56% | **+0.45%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +0.05% | **+0.03%** |

## 2. $100 Live Portfolio

- 残高: **$97.16** / 初期 $100.00 (-2.84%)
- 確定トレード: 65件 (TP 18 / SL 44 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.16
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.01** / 初期 $100.00 (+30.01%)
- 確定: 678件 (Win 172 / Loss 215 / Flat 291) / skip 793件
- 成長率目線: 平均log +0.000387 / 幾何平均 +0.039% per trade / maxDD +4.72%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PHA/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.61% 残高後 $130.01

## 4. Latest Market Context

- 更新: 2026-05-26T22:54:23.796014+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=75725.7
- Funnel: target 766 → liquid 138 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LUNC/USDT:USDT | +9.39% | $4,361,481.49 |
| PLAY/USDT:USDT | +6.09% | $8,241,999.07 |
| MYX/USDT:USDT | +5.54% | $1,267,040.60 |
| MUSTOCK/USDT:USDT | +4.38% | $21,600,662.23 |
| SIREN/USDT:USDT | +4.18% | $1,126,810.09 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ASTSSTOCK/USDT:USDT | below_1h_threshold | +2.11% | +2.30% |
| PHA/USDT:USDT | below_1h_threshold | +1.98% | +2.17% |
| LUNC/USDT:USDT | below_1h_threshold | +1.74% | +1.93% |
| IO/USDT:USDT | below_1h_threshold | +1.72% | +1.90% |
| DYDX/USDT:USDT | below_1h_threshold | +1.15% | +1.33% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
