# Decision Report

- generated_at: 2026-06-24T21:59:13.829335+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7502**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.26% / filled 20/20。**
- 全期間 MARKET基準: n=7502, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.26%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.26% | **+0.26%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +0.34% | **+0.32%** |
| ASK | 20/20 | 100.0% | +0.28% | **+0.28%** |
| MARKET | 20/20 | 100.0% | +0.26% | **+0.26%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.21% | **+0.18%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.10% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.14% | **+0.74%** |
| MARKET_LONG | 20/20 | 100.0% | +0.54% | **+0.54%** |
| ASK_LONG | 20/20 | 100.0% | +0.53% | **+0.53%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.80% | **+0.52%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$102.43** / 初期 $100.00 (+2.43%)
- 確定トレード: 37件 (TP 14 / SL 23 / EXP 0)
- 最新: KORU/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.43
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$223.69** / 初期 $100.00 (+123.69%)
- 確定: 2121件 (Win 627 / Loss 709 / Flat 785) / skip 1942件
- 成長率目線: 平均log +0.000380 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $223.69

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.76** / 初期 $100.00 (+6.76%)
- 確定: 349件 (Win 98 / Loss 95 / Flat 156) / skip 564件
- 成長率目線: 平均log +0.000187 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: H/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $106.76

## 5. Latest Market Context

- 更新: 2026-06-24T21:59:07.694867+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.25% price=61076.6
- Funnel: target 808 → liquid 161 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.7 >= 65=1, 4h RSI 70.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KORU/USDT:USDT | +23.82% | $4,475,413.21 |
| MUSTOCK/USDT:USDT | +14.20% | $90,606,889.36 |
| DRAM/USDT:USDT | +13.92% | $7,735,994.20 |
| SOXL/USDT:USDT | +13.04% | $6,089,226.78 |
| MAVIA/USDT:USDT | +12.57% | $1,367,005.72 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LIT/USDT:USDT | below_relative_strength | +5.01% | +4.76% |
| UB/USDT:USDT | below_1h_threshold | +3.76% | +3.51% |
| JTO/USDT:USDT | below_1h_threshold | +2.61% | +2.37% |
| RESOLV/USDT:USDT | below_1h_threshold | +2.51% | +2.26% |
| AERO/USDT:USDT | below_1h_threshold | +2.31% | +2.06% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
