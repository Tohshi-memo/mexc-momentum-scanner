# Decision Report

- generated_at: 2026-06-29T17:59:49.216384+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7830**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.34% / filled 20/20。**
- 全期間 MARKET基準: n=7830, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+2.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.34% | **+2.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.34% | **+2.34%** |
| ASK | 20/20 | 100.0% | +2.05% | **+2.05%** |
| LIMIT_2PCT | 13/20 | 65.0% | +1.03% | **+0.67%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | -0.44% | **-0.20%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | -0.61% | **-0.30%** |
| MARKET_LONG | 20/20 | 100.0% | -0.41% | **-0.41%** |

## 2. $100 Live Portfolio

- 残高: **$101.63** / 初期 $100.00 (+1.63%)
- 確定トレード: 43件 (TP 15 / SL 27 / EXP 1)
- 最新: HEI/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.63
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$260.49** / 初期 $100.00 (+160.49%)
- 確定: 2334件 (Win 708 / Loss 777 / Flat 849) / skip 2057件
- 成長率目線: 平均log +0.000410 / 幾何平均 +0.041% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $260.49

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.45** / 初期 $100.00 (+6.45%)
- 確定: 457件 (Win 120 / Loss 119 / Flat 218) / skip 784件
- 成長率目線: 平均log +0.000137 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0341 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: GWEI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.45

## 5. Latest Market Context

- 更新: 2026-06-29T17:59:39.792821+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.90% price=60406.9
- Funnel: target 811 → liquid 153 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BILL/USDT:USDT | +9.11% | $1,289,016.41 |
| MYX/USDT:USDT | +8.27% | $2,588,457.46 |
| H/USDT:USDT | +7.99% | $4,000,971.18 |
| BAS/USDT:USDT | +6.80% | $2,153,458.13 |
| ORDI/USDT:USDT | +6.34% | $17,041,536.82 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +5.00% | +4.10% |
| ORDI/USDT:USDT | below_1h_threshold | +4.97% | +4.07% |
| SYN/USDT:USDT | below_1h_threshold | +4.75% | +3.86% |
| BILL/USDT:USDT | below_1h_threshold | +4.71% | +3.81% |
| ACT/USDT:USDT | below_1h_threshold | +4.02% | +3.12% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
