# Decision Report

- generated_at: 2026-06-30T02:18:49.998740+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7848**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.92% / filled 20/20。**
- 全期間 MARKET基準: n=7848, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+1.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.92% | **+1.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.92% | **+1.92%** |
| ASK | 20/20 | 100.0% | +1.84% | **+1.84%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.29% | **+1.03%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.34% | **+0.94%** |
| LIMIT_3PCT | 11/20 | 55.0% | +0.92% | **+0.51%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +1.50% | **+0.15%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.00% | **+0.00%** |
| LIMIT_ATR_LONG | 18/20 | 90.0% | -0.04% | **-0.04%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | -0.46% | **-0.21%** |

## 2. $100 Live Portfolio

- 残高: **$101.62** / 初期 $100.00 (+1.62%)
- 確定トレード: 46件 (TP 16 / SL 29 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.62
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$260.44** / 初期 $100.00 (+160.44%)
- 確定: 2352件 (Win 714 / Loss 784 / Flat 854) / skip 2057件
- 成長率目線: 平均log +0.000407 / 幾何平均 +0.041% per trade / maxDD +8.13%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CAP/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $260.44

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.45** / 初期 $100.00 (+6.45%)
- 確定: 457件 (Win 120 / Loss 119 / Flat 218) / skip 802件
- 成長率目線: 平均log +0.000137 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: GWEI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.45

## 5. Latest Market Context

- 更新: 2026-06-30T02:18:43.013281+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.27% price=59759.2
- Funnel: target 811 → liquid 153 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 92.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CAP/USDT:USDT | +26.49% | $2,079,659.09 |
| AIGENSYN/USDT:USDT | +26.32% | $3,728,842.90 |
| ANSEM/USDT:USDT | +21.14% | $1,030,098.80 |
| SYN/USDT:USDT | +19.00% | $22,414,218.99 |
| AVAVSTOCK/USDT:USDT | +17.50% | $1,841,289.20 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| M/USDT:USDT | below_1h_threshold | +2.81% | +3.07% |
| ARX/USDT:USDT | below_1h_threshold | +1.15% | +1.41% |
| NES/USDT:USDT | below_1h_threshold | +0.73% | +1.00% |
| ZRO/USDT:USDT | below_1h_threshold | +0.58% | +0.84% |
| XLM/USDT:USDT | below_1h_threshold | +0.49% | +0.75% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
