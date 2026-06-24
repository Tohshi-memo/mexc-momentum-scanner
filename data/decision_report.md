# Decision Report

- generated_at: 2026-06-24T19:56:15.168971+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7493**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.60% / filled 20/20。**
- 全期間 MARKET基準: n=7493, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+2.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.60% | **+2.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +3.22% | **+3.22%** |
| MARKET | 20/20 | 100.0% | +2.60% | **+2.60%** |
| LIMIT_1PCT | 18/20 | 90.0% | +2.34% | **+2.11%** |
| LIMIT_2PCT | 16/20 | 80.0% | +2.27% | **+1.82%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.79% | **+1.16%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 11/20 | 55.0% | +0.73% | **+0.40%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.10% | **+0.33%** |
| LIMIT_7PCT_LONG | 12/20 | 60.0% | +0.19% | **+0.12%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -3.56% | **-0.53%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | -1.75% | **-1.05%** |

## 2. $100 Live Portfolio

- 残高: **$103.46** / 初期 $100.00 (+3.46%)
- 確定トレード: 35件 (TP 14 / SL 21 / EXP 0)
- 最新: H/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.46
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$223.69** / 初期 $100.00 (+123.69%)
- 確定: 2121件 (Win 627 / Loss 709 / Flat 785) / skip 1933件
- 成長率目線: 平均log +0.000380 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $223.69

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.76** / 初期 $100.00 (+6.76%)
- 確定: 349件 (Win 98 / Loss 95 / Flat 156) / skip 555件
- 成長率目線: 平均log +0.000187 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: H/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $106.76

## 5. Latest Market Context

- 更新: 2026-06-24T19:56:09.456805+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.42% price=59820.9
- Funnel: target 808 → liquid 162 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| H/USDT:USDT | +16.81% | $16,463,067.92 |
| MAVIA/USDT:USDT | +8.73% | $1,241,048.08 |
| BSB/USDT:USDT | +6.71% | $6,229,318.96 |
| CLO/USDT:USDT | +4.16% | $3,301,108.81 |
| VELVET/USDT:USDT | +4.16% | $5,896,923.94 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MAVIA/USDT:USDT | below_1h_threshold | +3.98% | +3.56% |
| ARMSTOCK/USDT:USDT | below_1h_threshold | +3.23% | +2.81% |
| LIT/USDT:USDT | below_1h_threshold | +3.15% | +2.73% |
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +2.99% | +2.56% |
| BR/USDT:USDT | below_1h_threshold | +2.97% | +2.55% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
