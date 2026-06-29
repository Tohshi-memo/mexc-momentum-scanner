# Decision Report

- generated_at: 2026-06-29T17:06:02.124053+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7828**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.09% / filled 20/20。**
- 全期間 MARKET基準: n=7828, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+2.09%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.09% | **+2.09%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.09% | **+2.09%** |
| ASK | 20/20 | 100.0% | +1.82% | **+1.82%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.76% | **+0.46%** |
| LIMIT_2PCT | 13/20 | 65.0% | +0.66% | **+0.43%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +0.36% | **+0.16%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | -0.44% | **-0.20%** |
| MARKET_LONG | 20/20 | 100.0% | -0.41% | **-0.41%** |

## 2. $100 Live Portfolio

- 残高: **$101.63** / 初期 $100.00 (+1.63%)
- 確定トレード: 43件 (TP 15 / SL 27 / EXP 1)
- 最新: HEI/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.63
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$261.80** / 初期 $100.00 (+161.80%)
- 確定: 2332件 (Win 708 / Loss 776 / Flat 848) / skip 2057件
- 成長率目線: 平均log +0.000413 / 幾何平均 +0.041% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASED/USDT:USDT `MARKET_LONG` EXPIRED account -0.29% 残高後 $261.80

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.45** / 初期 $100.00 (+6.45%)
- 確定: 457件 (Win 120 / Loss 119 / Flat 218) / skip 782件
- 成長率目線: 平均log +0.000137 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0381 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: GWEI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.45

## 5. Latest Market Context

- 更新: 2026-06-29T17:05:56.377847+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.59% price=60225.6
- Funnel: target 811 → liquid 148 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +4.46% | $2,694,426.45 |
| SOXL/USDT:USDT | +3.52% | $7,962,182.67 |
| MSTRSTOCK/USDT:USDT | +3.26% | $5,249,916.67 |
| MYX/USDT:USDT | +3.26% | $2,353,585.69 |
| ORDI/USDT:USDT | +3.17% | $13,820,638.21 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +2.56% | +1.97% |
| ORDI/USDT:USDT | below_1h_threshold | +2.01% | +1.41% |
| VVV/USDT:USDT | below_1h_threshold | +1.49% | +0.89% |
| AVAX/USDT:USDT | below_1h_threshold | +1.42% | +0.83% |
| ACT/USDT:USDT | below_1h_threshold | +1.39% | +0.80% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
