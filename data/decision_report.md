# Decision Report

- generated_at: 2026-05-19T16:53:49.879799+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4482**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4482, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.96%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.96% | **-0.96%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +2.76% | **+0.97%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.74% | **+0.78%** |
| LIMIT_FIB1272 | 11/20 | 55.0% | +0.56% | **+0.31%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.29% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +6.73% | **+5.05%** |
| MARKET_LONG | 20/20 | 100.0% | +1.36% | **+1.36%** |
| ASK_LONG | 20/20 | 100.0% | +1.16% | **+1.16%** |
| LIMIT_1PCT_LONG | 12/20 | 60.0% | +0.53% | **+0.32%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 55件 (TP 14 / SL 38 / EXP 3)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定: 473件 (Win 124 / Loss 164 / Flat 185) / skip 570件
- 成長率目線: 平均log +0.000412 / 幾何平均 +0.041% per trade / maxDD +4.21%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $121.49

## 4. Latest Market Context

- 更新: 2026-05-19T16:53:44.799374+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.46% price=76840.4
- Funnel: target 764 → liquid 136 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.4 >= 65=1, 4h RSI 83.4 >= 65=1, 4h RSI 81.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EDEN/USDT:USDT | +16.21% | $5,132,132.40 |
| BSB/USDT:USDT | +10.43% | $8,670,270.12 |
| LAB/USDT:USDT | +10.09% | $85,224,680.05 |
| RLS/USDT:USDT | +6.02% | $1,014,666.91 |
| LIT/USDT:USDT | +4.46% | $1,763,382.43 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LIT/USDT:USDT | below_1h_threshold | +4.46% | +3.99% |
| VVV/USDT:USDT | below_1h_threshold | +4.25% | +3.79% |
| PYTH/USDT:USDT | below_1h_threshold | +3.34% | +2.88% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +3.24% | +2.77% |
| DYDX/USDT:USDT | below_1h_threshold | +3.16% | +2.70% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
