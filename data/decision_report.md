# Decision Report

- generated_at: 2026-06-29T18:18:47.920780+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7831**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.74% / filled 20/20。**
- 全期間 MARKET基準: n=7831, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+1.74%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.74% | **+1.74%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.74% | **+1.74%** |
| ASK | 20/20 | 100.0% | +1.45% | **+1.45%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.82% | **+0.57%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.00% | **+0.00%** |
| MARKET_LONG | 20/20 | 100.0% | -0.01% | **-0.01%** |
| LIMIT_BB3S_LONG | 5/5 | 100.0% | -0.05% | **-0.05%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | -0.61% | **-0.30%** |

## 2. $100 Live Portfolio

- 残高: **$101.63** / 初期 $100.00 (+1.63%)
- 確定トレード: 43件 (TP 15 / SL 27 / EXP 1)
- 最新: HEI/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.63
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$261.79** / 初期 $100.00 (+161.79%)
- 確定: 2335件 (Win 709 / Loss 777 / Flat 849) / skip 2057件
- 成長率目線: 平均log +0.000412 / 幾何平均 +0.041% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AGLD/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $261.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.45** / 初期 $100.00 (+6.45%)
- 確定: 457件 (Win 120 / Loss 119 / Flat 218) / skip 785件
- 成長率目線: 平均log +0.000137 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0341 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: GWEI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.45

## 5. Latest Market Context

- 更新: 2026-06-29T18:18:43.264441+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=60379.7
- Funnel: target 811 → liquid 152 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MYX/USDT:USDT | +7.29% | $2,522,827.67 |
| ORDI/USDT:USDT | +7.13% | $17,467,338.11 |
| SYN/USDT:USDT | +7.07% | $11,773,416.15 |
| H/USDT:USDT | +6.89% | $4,034,137.98 |
| BILL/USDT:USDT | +6.85% | $1,385,207.94 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KAS/USDT:USDT | below_1h_threshold | +1.61% | +1.63% |
| KORU/USDT:USDT | below_1h_threshold | +1.40% | +1.42% |
| UB/USDT:USDT | below_1h_threshold | +1.17% | +1.19% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +0.93% | +0.95% |
| ORDI/USDT:USDT | below_1h_threshold | +0.82% | +0.83% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
