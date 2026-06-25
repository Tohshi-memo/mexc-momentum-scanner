# Decision Report

- generated_at: 2026-06-25T04:55:13.083488+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7526**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7526, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.37%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.37% | **-0.37%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 2/15 | 13.3% | +1.52% | **+0.20%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_4PCT | 9/20 | 45.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | -0.27% | **-0.09%** |
| LIMIT_2PCT | 14/20 | 70.0% | -0.17% | **-0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +3.49% | **+1.92%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.75% | **+1.31%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +1.44% | **+1.30%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +2.15% | **+1.08%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +2.45% | **+0.86%** |

## 2. $100 Live Portfolio

- 残高: **$103.45** / 初期 $100.00 (+3.45%)
- 確定トレード: 38件 (TP 15 / SL 23 / EXP 0)
- 最新: ARMSTOCK/USDT:USDT TP_HIT PnL +7.19% 残高後 $103.45
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$222.56** / 初期 $100.00 (+122.56%)
- 確定: 2126件 (Win 629 / Loss 712 / Flat 785) / skip 1961件
- 成長率目線: 平均log +0.000376 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $222.56

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.76** / 初期 $100.00 (+6.76%)
- 確定: 350件 (Win 98 / Loss 95 / Flat 157) / skip 587件
- 成長率目線: 平均log +0.000187 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BSB/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $106.76

## 5. Latest Market Context

- 更新: 2026-06-25T04:55:04.843570+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.53% price=61179.3
- Funnel: target 808 → liquid 161 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SLX/USDT:USDT | +28.95% | $13,153,046.77 |
| KORU/USDT:USDT | +18.39% | $5,766,067.79 |
| MUSTOCK/USDT:USDT | +18.38% | $104,563,844.76 |
| H/USDT:USDT | +14.97% | $22,535,880.62 |
| ID/USDT:USDT | +14.67% | $2,304,857.59 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ID/USDT:USDT | below_1h_threshold | +3.88% | +3.34% |
| RESOLV/USDT:USDT | below_1h_threshold | +3.63% | +3.10% |
| KIOXIASTOCK/USDT:USDT | below_1h_threshold | +2.75% | +2.22% |
| GRASS/USDT:USDT | below_1h_threshold | +2.39% | +1.86% |
| SYN/USDT:USDT | below_1h_threshold | +2.33% | +1.79% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
