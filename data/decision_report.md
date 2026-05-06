# Decision Report

- generated_at: 2026-05-06T11:42:26.016747+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3447**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3447, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-0.66%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.66% | **-0.66%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +0.31% | **+0.09%** |
| LIMIT_6PCT | 3/20 | 15.0% | +0.30% | **+0.04%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.10% | **+0.04%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.04% | **-0.00%** |
| LIMIT_4PCT | 14/20 | 70.0% | -0.21% | **-0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +2.03% | **+0.71%** |
| MARKET_LONG | 20/20 | 100.0% | +0.64% | **+0.64%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +1.40% | **+0.49%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +0.90% | **+0.45%** |
| ASK_LONG | 20/20 | 100.0% | +0.43% | **+0.43%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$98.01** / 初期 $100.00 (-1.99%)
- 確定: 9件 (Win 0 / Loss 4 / Flat 5) / skip 0件
- 成長率目線: 平均log -0.002228 / 幾何平均 -0.223% per trade / maxDD +1.99%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LYN/USDT:USDT `LIMIT_BB3S` SL_HIT account -0.50% 残高後 $98.01

## 4. Latest Market Context

- 更新: 2026-05-06T11:42:22.948683+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.33% price=82515.0
- Funnel: target 770 → liquid 203 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.9 >= 65=1, 4h RSI n/a=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IO/USDT:USDT | +44.55% | $12,986,889.53 |
| BILL/USDT:USDT | +43.82% | $2,695,117.29 |
| B3/USDT:USDT | +36.97% | $1,529,250.04 |
| ZEC/USDT:USDT | +34.14% | $767,673,863.92 |
| LAB/USDT:USDT | +29.90% | $123,179,039.08 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FHE/USDT:USDT | below_1h_threshold | +3.86% | +3.52% |
| TAG/USDT:USDT | below_1h_threshold | +2.10% | +1.77% |
| NEAR/USDT:USDT | below_1h_threshold | +1.87% | +1.54% |
| NAORIS/USDT:USDT | below_1h_threshold | +1.48% | +1.15% |
| TAO/USDT:USDT | below_1h_threshold | +1.19% | +0.86% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
