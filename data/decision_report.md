# Decision Report

- generated_at: 2026-07-02T21:25:05.050982+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8109**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.05% / filled 20/20。**
- 全期間 MARKET基準: n=8109, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.05% | **+1.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.13% | **+1.13%** |
| MARKET | 20/20 | 100.0% | +1.05% | **+1.05%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.43% | **+0.15%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.59% | **+0.15%** |
| LIMIT_1PCT | 15/20 | 75.0% | +0.15% | **+0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.56% | **+1.15%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +0.70% | **+0.56%** |
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +0.51% | **+0.38%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.58% | **+0.32%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | -0.08% | **-0.04%** |

## 2. $100 Live Portfolio

- 残高: **$103.14** / 初期 $100.00 (+3.14%)
- 確定トレード: 52件 (TP 19 / SL 32 / EXP 1)
- 最新: TAIKO/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.14
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$284.67** / 初期 $100.00 (+184.67%)
- 確定: 2444件 (Win 754 / Loss 816 / Flat 874) / skip 2226件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $284.67

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.12** / 初期 $100.00 (+5.12%)
- 確定: 568件 (Win 137 / Loss 133 / Flat 298) / skip 952件
- 成長率目線: 平均log +0.000088 / 幾何平均 +0.009% per trade / maxDD +3.55%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0538 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MERL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $105.12

## 5. Latest Market Context

- 更新: 2026-07-02T21:25:00.182379+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=61515.0
- Funnel: target 834 → liquid 173 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MAGMA/USDT:USDT | +18.33% | $4,643,997.98 |
| LAB/USDT:USDT | +14.87% | $12,013,314.06 |
| BASED/USDT:USDT | +12.91% | $14,627,661.18 |
| PIPPIN/USDT:USDT | +12.82% | $3,874,437.55 |
| TAIKO/USDT:USDT | +9.47% | $101,388,986.56 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_1h_threshold | +3.61% | +3.68% |
| LAB/USDT:USDT | below_1h_threshold | +2.65% | +2.71% |
| BIRB/USDT:USDT | below_1h_threshold | +2.37% | +2.43% |
| NES/USDT:USDT | below_1h_threshold | +2.13% | +2.20% |
| FARTCOIN/USDT:USDT | below_1h_threshold | +1.73% | +1.80% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
