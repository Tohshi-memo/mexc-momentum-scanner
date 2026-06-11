# Decision Report

- generated_at: 2026-06-11T17:44:11.430823+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6384**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6384, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.12% | **-0.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 4/20 | 20.0% | +3.29% | **+0.66%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.21% | **+0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.08% | **+0.65%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.83% | **+0.54%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +1.38% | **+0.48%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +0.79% | **+0.35%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.36% | **+0.25%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$151.52** / 初期 $100.00 (+51.52%)
- 確定: 1301件 (Win 334 / Loss 413 / Flat 554) / skip 1644件
- 成長率目線: 平均log +0.000319 / 幾何平均 +0.032% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $151.52

## 4. Latest Market Context

- 更新: 2026-06-11T17:44:07.087257+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +1.22% price=63308.2
- Funnel: target 782 → liquid 158 → pre 50 → checked 50 → surge 5 → strict 0
- Surge前reject: below_1h_threshold=43, below_relative_strength=2, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.9 >= 65=1, 4h RSI 76.1 >= 65=1, 4h RSI 78.6 >= 65=1, 4h RSI n/a=1, 4h RSI 76.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +20.42% | $96,079,828.96 |
| ESPORTS/USDT:USDT | +19.50% | $10,646,860.86 |
| SKYAI/USDT:USDT | +11.36% | $10,809,526.92 |
| ZBT/USDT:USDT | +6.08% | $1,157,836.16 |
| STG/USDT:USDT | +5.74% | $12,630,646.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VVV/USDT:USDT | below_relative_strength | +5.80% | +4.58% |
| H/USDT:USDT | below_relative_strength | +5.62% | +4.40% |
| OUSTSTOCK/USDT:USDT | below_1h_threshold | +4.86% | +3.64% |
| SKYAI/USDT:USDT | below_1h_threshold | +3.79% | +2.57% |
| SILVER/USDT:USDT | below_1h_threshold | +3.77% | +2.56% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
