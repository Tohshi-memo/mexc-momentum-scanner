# Decision Report

- generated_at: 2026-05-07T01:57:32.235501+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3529**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3529, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-0.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.32% | **-0.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 4/20 | 20.0% | +3.29% | **+0.66%** |
| LIMIT_8PCT | 4/20 | 20.0% | +1.78% | **+0.36%** |
| LIMIT_7PCT | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.36% | **+0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.89% | **+1.70%** |
| MARKET_LONG | 20/20 | 100.0% | +1.63% | **+1.63%** |
| ASK_LONG | 20/20 | 100.0% | +1.62% | **+1.62%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.75% | **+1.31%** |
| LIMIT_BB3S_LONG | 2/6 | 33.3% | +2.73% | **+0.91%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$101.63** / 初期 $100.00 (+1.63%)
- 確定: 24件 (Win 8 / Loss 9 / Flat 7) / skip 66件
- 成長率目線: 平均log +0.000675 / 幾何平均 +0.068% per trade / maxDD +2.48%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PENGUIN/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $101.63

## 4. Latest Market Context

- 更新: 2026-05-07T01:57:28.174835+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.22% price=81142.2
- Funnel: target 770 → liquid 190 → pre 50 → checked 50 → surge 6 → strict 0
- Surge前reject: below_1h_threshold=44, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.9 >= 65=1, 4h RSI 78.3 >= 65=1, 4h RSI 78.1 >= 65=1, 4h RSI 71.0 >= 65=1, 4h RSI 74.1 >= 65=1, 4h RSI 97.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +129.33% | $1,047,037.70 |
| DOGS/USDT:USDT | +67.34% | $6,960,615.51 |
| FHE/USDT:USDT | +31.83% | $16,396,739.06 |
| PENGUIN/USDT:USDT | +27.96% | $1,062,720.04 |
| TONCOIN/USDT:USDT | +11.83% | $253,570,605.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SATO/USDT:USDT | below_1h_threshold | +3.48% | +3.26% |
| ALBSTOCK/USDT:USDT | below_1h_threshold | +1.29% | +1.07% |
| SILVER/USDT:USDT | below_1h_threshold | +1.23% | +1.01% |
| AR/USDT:USDT | below_1h_threshold | +0.78% | +0.56% |
| SIREN/USDT:USDT | below_1h_threshold | +0.77% | +0.55% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
