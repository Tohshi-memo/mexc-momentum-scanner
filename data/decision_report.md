# Decision Report

- generated_at: 2026-05-07T05:17:47.589374+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3571**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3571, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.13%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.13% | **-0.13%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.50% | **+0.50%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.45% | **+0.43%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.10% | **+0.02%** |
| LIMIT_BB3S | 6/14 | 42.9% | -0.26% | **-0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.28% | **+1.09%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.20% | **+0.72%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.86% | **+0.60%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.85% | **+0.55%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.55% | **+0.33%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$106.96** / 初期 $100.00 (+6.96%)
- 確定: 65件 (Win 24 / Loss 24 / Flat 17) / skip 67件
- 成長率目線: 平均log +0.001036 / 幾何平均 +0.104% per trade / maxDD +2.48%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PENGUIN/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $106.96

## 4. Latest Market Context

- 更新: 2026-05-07T05:17:44.699500+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.22% price=81116.6
- Funnel: target 770 → liquid 186 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +211.31% | $1,667,895.84 |
| B3/USDT:USDT | +125.66% | $9,028,170.09 |
| DOGS/USDT:USDT | +81.49% | $11,125,911.37 |
| PENGUIN/USDT:USDT | +54.30% | $1,334,437.64 |
| FHE/USDT:USDT | +29.48% | $16,658,326.30 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PENGUIN/USDT:USDT | below_1h_threshold | +3.43% | +3.21% |
| HMSTR/USDT:USDT | below_1h_threshold | +3.13% | +2.92% |
| B/USDT:USDT | below_1h_threshold | +2.51% | +2.29% |
| DOGS/USDT:USDT | below_1h_threshold | +2.21% | +1.99% |
| S/USDT:USDT | below_1h_threshold | +2.11% | +1.89% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
