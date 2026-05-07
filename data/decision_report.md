# Decision Report

- generated_at: 2026-05-07T09:42:36.912517+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3608**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3608, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.13%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.13% | **+0.13%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +5.42% | **+1.36%** |
| LIMIT_9PCT | 3/20 | 15.0% | +6.86% | **+1.03%** |
| LIMIT_BB3S | 7/13 | 53.8% | +1.82% | **+0.98%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.80% | **+0.70%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.56% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +3.06% | **+1.53%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +1.86% | **+0.46%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.00% | **+0.45%** |
| MARKET_LONG | 20/20 | 100.0% | +0.44% | **+0.44%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.48% | **+0.27%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$105.48** / 初期 $100.00 (+5.48%)
- 確定: 102件 (Win 34 / Loss 43 / Flat 25) / skip 67件
- 成長率目線: 平均log +0.000523 / 幾何平均 +0.052% per trade / maxDD +2.48%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TONCOIN/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $105.48

## 4. Latest Market Context

- 更新: 2026-05-07T09:42:33.457544+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.34% price=80914.4
- Funnel: target 771 → liquid 187 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +157.62% | $2,102,299.95 |
| PENGUIN/USDT:USDT | +117.88% | $2,878,337.12 |
| B3/USDT:USDT | +93.00% | $10,615,359.52 |
| DOGS/USDT:USDT | +57.05% | $14,433,928.29 |
| D/USDT:USDT | +51.79% | $1,183,321.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| B3/USDT:USDT | below_1h_threshold | +4.76% | +5.10% |
| EVAA/USDT:USDT | below_1h_threshold | +3.19% | +3.54% |
| D/USDT:USDT | below_1h_threshold | +2.71% | +3.05% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +2.62% | +2.96% |
| NIL/USDT:USDT | below_1h_threshold | +2.45% | +2.79% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
