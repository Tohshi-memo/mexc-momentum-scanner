# Decision Report

- generated_at: 2026-06-24T20:19:20.410943+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7494**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.60% / filled 20/20。**
- 全期間 MARKET基準: n=7494, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+2.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.60% | **+2.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.62% | **+2.62%** |
| MARKET | 20/20 | 100.0% | +2.60% | **+2.60%** |
| LIMIT_1PCT | 18/20 | 90.0% | +2.34% | **+2.11%** |
| LIMIT_2PCT | 16/20 | 80.0% | +2.14% | **+1.71%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.56% | **+1.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 11/20 | 55.0% | +0.73% | **+0.40%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.10% | **+0.33%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | -0.52% | **-0.28%** |
| ASK_LONG | 20/20 | 100.0% | -0.50% | **-0.50%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -3.56% | **-0.53%** |

## 2. $100 Live Portfolio

- 残高: **$103.46** / 初期 $100.00 (+3.46%)
- 確定トレード: 35件 (TP 14 / SL 21 / EXP 0)
- 最新: H/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.46
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$223.69** / 初期 $100.00 (+123.69%)
- 確定: 2121件 (Win 627 / Loss 709 / Flat 785) / skip 1934件
- 成長率目線: 平均log +0.000380 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $223.69

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.76** / 初期 $100.00 (+6.76%)
- 確定: 349件 (Win 98 / Loss 95 / Flat 156) / skip 556件
- 成長率目線: 平均log +0.000187 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: H/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $106.76

## 5. Latest Market Context

- 更新: 2026-06-24T20:19:02.404513+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +1.31% price=60709.4
- Funnel: target 808 → liquid 161 → pre 50 → checked 50 → surge 7 → strict 6
- Surge前reject: below_1h_threshold=42, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| H/USDT:USDT | +16.61% | $16,416,287.90 |
| KORU/USDT:USDT | +12.28% | $2,788,935.81 |
| MUSTOCK/USDT:USDT | +9.82% | $78,957,297.32 |
| MVLL/USDT:USDT | +9.82% | $2,475,743.14 |
| MAVIA/USDT:USDT | +9.09% | $1,298,316.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SAMSUNGSTOCK/USDT:USDT | below_relative_strength | +5.75% | +4.44% |
| DYDX/USDT:USDT | below_1h_threshold | +3.27% | +1.97% |
| RESOLV/USDT:USDT | below_1h_threshold | +3.19% | +1.88% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +3.18% | +1.87% |
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +3.16% | +1.85% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
