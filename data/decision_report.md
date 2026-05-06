# Decision Report

- generated_at: 2026-05-06T11:32:40.418671+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3446**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3446, expectancy=-0.14%
- 直近20件 MARKET基準: n=20, expectancy=-0.71%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.71% | **-0.71%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.47% | **+0.19%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.00% | **+0.00%** |
| LIMIT_BB3S | 5/13 | 38.5% | -0.31% | **-0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +2.03% | **+0.71%** |
| MARKET_LONG | 20/20 | 100.0% | +0.56% | **+0.56%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +1.40% | **+0.49%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.63% | **+0.47%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +0.90% | **+0.45%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$98.51** / 初期 $100.00 (-1.49%)
- 確定: 8件 (Win 0 / Loss 3 / Flat 5) / skip 0件
- 成長率目線: 平均log -0.001880 / 幾何平均 -0.188% per trade / maxDD +1.49%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BILL/USDT:USDT `LIMIT_BB3S` EXPIRED account +0.00% 残高後 $98.51

## 4. Latest Market Context

- 更新: 2026-05-06T11:32:34.885672+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.51% price=82660.3
- Funnel: target 770 → liquid 202 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BILL/USDT:USDT | +48.83% | $2,545,887.58 |
| IO/USDT:USDT | +47.53% | $12,841,615.52 |
| B3/USDT:USDT | +36.86% | $1,524,123.13 |
| ZEC/USDT:USDT | +34.64% | $764,854,468.41 |
| STORJ/USDT:USDT | +30.21% | $2,826,845.58 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAG/USDT:USDT | below_1h_threshold | +4.57% | +4.06% |
| FHE/USDT:USDT | below_1h_threshold | +3.10% | +2.59% |
| ENA/USDT:USDT | below_1h_threshold | +2.74% | +2.23% |
| NOT/USDT:USDT | below_1h_threshold | +2.08% | +1.58% |
| SPX/USDT:USDT | below_1h_threshold | +1.23% | +0.72% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
