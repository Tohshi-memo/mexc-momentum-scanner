# Decision Report

- generated_at: 2026-05-16T19:23:22.639183+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4369**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.47% / filled 20/20。**
- 全期間 MARKET基準: n=4369, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+1.47%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.47% | **+1.47%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.47% | **+1.47%** |
| ASK | 20/20 | 100.0% | +1.44% | **+1.44%** |
| LIMIT_1PCT | 15/20 | 75.0% | +0.86% | **+0.65%** |
| LIMIT_ATR | 11/20 | 55.0% | +0.89% | **+0.49%** |
| LIMIT_5PCT | 3/20 | 15.0% | +0.95% | **+0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +1.20% | **+0.66%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.19% | **+0.48%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -0.38% | **-0.08%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | -0.16% | **-0.11%** |

## 2. $100 Live Portfolio

- 残高: **$97.20** / 初期 $100.00 (-2.80%)
- 確定トレード: 47件 (TP 12 / SL 32 / EXP 3)
- 最新: NAORIS/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.20
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$117.99** / 初期 $100.00 (+17.99%)
- 確定: 392件 (Win 97 / Loss 136 / Flat 159) / skip 538件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +4.21%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $117.99

## 4. Latest Market Context

- 更新: 2026-05-16T19:23:19.362032+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=78185.1
- Funnel: target 760 → liquid 129 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CGPT/USDT:USDT | +8.65% | $1,286,006.49 |
| BSB/USDT:USDT | +8.06% | $2,944,887.24 |
| ASTEROID/USDT:USDT | +7.05% | $5,459,742.61 |
| UB/USDT:USDT | +5.51% | $18,255,110.04 |
| LUNC/USDT:USDT | +4.70% | $9,288,503.73 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ASTEROID/USDT:USDT | below_1h_threshold | +1.49% | +1.51% |
| SAGA/USDT:USDT | below_1h_threshold | +1.29% | +1.31% |
| RIVER/USDT:USDT | below_1h_threshold | +0.91% | +0.93% |
| ZEC/USDT:USDT | below_1h_threshold | +0.82% | +0.84% |
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +0.77% | +0.79% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
