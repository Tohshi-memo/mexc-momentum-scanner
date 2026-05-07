# Decision Report

- generated_at: 2026-05-07T07:37:16.518313+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3587**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3587, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +0.80% | **+0.76%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| ASK | 20/20 | 100.0% | +0.29% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.84% | **+1.56%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +2.26% | **+1.13%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +1.54% | **+1.00%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +3.86% | **+0.96%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +1.55% | **+0.77%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$105.76** / 初期 $100.00 (+5.76%)
- 確定: 81件 (Win 29 / Loss 34 / Flat 18) / skip 67件
- 成長率目線: 平均log +0.000691 / 幾何平均 +0.069% per trade / maxDD +2.48%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SATO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $105.76

## 4. Latest Market Context

- 更新: 2026-05-07T07:37:13.386171+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.24% price=81590.0
- Funnel: target 771 → liquid 188 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.9 >= 65=1, 4h RSI 90.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +220.01% | $1,918,160.43 |
| PENGUIN/USDT:USDT | +80.40% | $1,548,469.67 |
| DOGS/USDT:USDT | +72.24% | $12,917,433.38 |
| B3/USDT:USDT | +71.26% | $10,004,254.48 |
| D/USDT:USDT | +67.65% | $1,002,953.17 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| D/USDT:USDT | below_1h_threshold | +4.77% | +4.53% |
| SIREN/USDT:USDT | below_1h_threshold | +2.88% | +2.64% |
| BILL/USDT:USDT | below_1h_threshold | +2.38% | +2.14% |
| ONDO/USDT:USDT | below_1h_threshold | +2.32% | +2.08% |
| VIRTUAL/USDT:USDT | below_1h_threshold | +2.31% | +2.07% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
