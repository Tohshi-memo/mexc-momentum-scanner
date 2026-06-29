# Decision Report

- generated_at: 2026-06-29T23:58:17.050229+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7841**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.71% / filled 20/20。**
- 全期間 MARKET基準: n=7841, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.71%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.71% | **+0.71%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 16/20 | 80.0% | +0.95% | **+0.76%** |
| MARKET | 20/20 | 100.0% | +0.71% | **+0.71%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.78% | **+0.70%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.89% | **+0.58%** |
| ASK | 20/20 | 100.0% | +0.51% | **+0.51%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 9/9 | 100.0% | +0.52% | **+0.52%** |
| MARKET_LONG | 20/20 | 100.0% | +0.27% | **+0.27%** |
| ASK_LONG | 20/20 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.00% | **+0.00%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | -0.24% | **-0.18%** |

## 2. $100 Live Portfolio

- 残高: **$102.13** / 初期 $100.00 (+2.13%)
- 確定トレード: 45件 (TP 16 / SL 28 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.13
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$264.38** / 初期 $100.00 (+164.38%)
- 確定: 2345件 (Win 714 / Loss 781 / Flat 850) / skip 2057件
- 成長率目線: 平均log +0.000415 / 幾何平均 +0.041% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $264.38

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.45** / 初期 $100.00 (+6.45%)
- 確定: 457件 (Win 120 / Loss 119 / Flat 218) / skip 795件
- 成長率目線: 平均log +0.000137 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0281 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: GWEI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.45

## 5. Latest Market Context

- 更新: 2026-06-29T23:58:09.634983+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.20% price=60207.1
- Funnel: target 811 → liquid 151 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 94.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIGENSYN/USDT:USDT | +26.11% | $2,578,036.28 |
| SYN/USDT:USDT | +18.47% | $21,524,684.21 |
| AVAVSTOCK/USDT:USDT | +17.16% | $1,770,288.42 |
| BILL/USDT:USDT | +16.92% | $2,935,213.23 |
| CAP/USDT:USDT | +16.28% | $1,308,245.61 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RE/USDT:USDT | below_1h_threshold | +3.66% | +3.86% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +2.76% | +2.96% |
| BILL/USDT:USDT | below_1h_threshold | +2.57% | +2.77% |
| AGLD/USDT:USDT | below_1h_threshold | +2.12% | +2.32% |
| UB/USDT:USDT | below_1h_threshold | +1.88% | +2.07% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
