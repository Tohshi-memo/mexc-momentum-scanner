# Decision Report

- generated_at: 2026-06-25T14:10:38.237894+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7564**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.02% / filled 20/20。**
- 全期間 MARKET基準: n=7564, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+1.02%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.02% | **+1.02%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.07% | **+1.07%** |
| MARKET | 20/20 | 100.0% | +1.02% | **+1.02%** |
| LIMIT_BB3S | 6/14 | 42.9% | +1.93% | **+0.83%** |
| LIMIT_8PCT | 4/20 | 20.0% | +2.85% | **+0.57%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.44% | **+0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.62% | **+1.62%** |
| MARKET_LONG | 20/20 | 100.0% | +0.97% | **+0.97%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.10% | **+0.27%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.06% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$102.94** / 初期 $100.00 (+2.94%)
- 確定トレード: 39件 (TP 15 / SL 24 / EXP 0)
- 最新: MUSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.94
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$219.24** / 初期 $100.00 (+119.24%)
- 確定: 2132件 (Win 629 / Loss 715 / Flat 788) / skip 1993件
- 成長率目線: 平均log +0.000368 / 幾何平均 +0.037% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UB/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $219.24

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.51** / 初期 $100.00 (+7.51%)
- 確定: 369件 (Win 102 / Loss 100 / Flat 167) / skip 606件
- 成長率目線: 平均log +0.000196 / 幾何平均 +0.020% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $107.51

## 5. Latest Market Context

- 更新: 2026-06-25T14:10:33.551328+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +2.27% price=59579.9
- Funnel: target 806 → liquid 163 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=3, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SLX/USDT:USDT | +43.46% | $21,981,169.67 |
| SYN/USDT:USDT | +39.02% | $26,756,970.42 |
| HEI/USDT:USDT | +35.90% | $3,909,163.76 |
| RESOLV/USDT:USDT | +27.68% | $4,536,866.75 |
| IDOL/USDT:USDT | +17.22% | $1,028,853.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KORU/USDT:USDT | below_relative_strength | +7.09% | +4.83% |
| SOXL/USDT:USDT | below_relative_strength | +6.49% | +4.23% |
| RESOLV/USDT:USDT | below_relative_strength | +6.35% | +4.08% |
| OP/USDT:USDT | below_1h_threshold | +4.91% | +2.65% |
| ETHFI/USDT:USDT | below_1h_threshold | +4.83% | +2.56% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
