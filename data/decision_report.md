# Decision Report

- generated_at: 2026-07-03T15:59:52.722313+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8169**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.85% / filled 20/20。**
- 全期間 MARKET基準: n=8169, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.85%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.85% | **+2.85%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.85% | **+2.85%** |
| ASK | 20/20 | 100.0% | +2.77% | **+2.77%** |
| LIMIT_1PCT | 16/20 | 80.0% | +2.34% | **+1.87%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_2PCT | 12/20 | 60.0% | +0.87% | **+0.52%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 13/20 | 65.0% | +0.03% | **+0.02%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | -0.20% | **-0.12%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | -0.19% | **-0.12%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | -1.45% | **-0.15%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | -0.44% | **-0.20%** |

## 2. $100 Live Portfolio

- 残高: **$102.61** / 初期 $100.00 (+2.61%)
- 確定トレード: 56件 (TP 20 / SL 35 / EXP 1)
- 最新: RIF/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$285.29** / 初期 $100.00 (+185.29%)
- 確定: 2490件 (Win 765 / Loss 832 / Flat 893) / skip 2240件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RIF/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $285.29

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.04** / 初期 $100.00 (+6.04%)
- 確定: 611件 (Win 147 / Loss 147 / Flat 317) / skip 969件
- 成長率目線: 平均log +0.000096 / 幾何平均 +0.010% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BAS/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $106.04

## 5. Latest Market Context

- 更新: 2026-07-03T15:59:45.689035+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.39% price=61898.4
- Funnel: target 834 → liquid 162 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| THE/USDT:USDT | +49.18% | $5,285,703.18 |
| NEX/USDT:USDT | +37.04% | $3,361,983.42 |
| ARPA/USDT:USDT | +31.63% | $6,658,283.34 |
| ZKP/USDT:USDT | +27.98% | $6,145,908.79 |
| RIF/USDT:USDT | +23.56% | $10,536,115.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AERO/USDT:USDT | below_1h_threshold | +3.79% | +4.18% |
| GUA/USDT:USDT | below_1h_threshold | +3.09% | +3.49% |
| JTO/USDT:USDT | below_1h_threshold | +2.95% | +3.34% |
| BICO/USDT:USDT | below_1h_threshold | +2.65% | +3.04% |
| MAGMA/USDT:USDT | below_1h_threshold | +2.62% | +3.01% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
