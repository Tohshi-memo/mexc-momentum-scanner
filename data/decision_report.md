# Decision Report

- generated_at: 2026-06-06T13:41:52.637535+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5834**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5834, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_BB3S | 5/17 | 29.4% | +0.99% | **+0.29%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.46% | **+0.23%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |
| ASK | 20/20 | 100.0% | +0.15% | **+0.15%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.31% | **+1.12%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.33% | **+0.93%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +1.31% | **+0.87%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +2.40% | **+0.84%** |
| ASK_LONG | 20/20 | 100.0% | +0.67% | **+0.67%** |

## 2. $100 Live Portfolio

- 残高: **$99.50** / 初期 $100.00 (-0.50%)
- 確定トレード: 1件 (TP 0 / SL 1 / EXP 0)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.50
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.54** / 初期 $100.00 (+30.54%)
- 確定: 1014件 (Win 239 / Loss 313 / Flat 462) / skip 1381件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ALLO/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $130.54

## 4. Latest Market Context

- 更新: 2026-06-06T13:41:48.995721+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.31% price=60811.2
- Funnel: target 771 → liquid 147 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.4 >= 65=1, 4h RSI 75.1 >= 65=1, 4h RSI 69.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ALLO/USDT:USDT | +123.78% | $61,776,757.53 |
| BLUAI/USDT:USDT | +62.97% | $4,430,012.43 |
| VELVET/USDT:USDT | +49.44% | $3,561,089.52 |
| HEI/USDT:USDT | +36.23% | $3,210,803.76 |
| CLO/USDT:USDT | +31.60% | $2,547,840.10 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_1h_threshold | +3.78% | +4.09% |
| HIGH/USDT:USDT | below_1h_threshold | +3.21% | +3.52% |
| GUA/USDT:USDT | below_1h_threshold | +2.74% | +3.05% |
| ALLO/USDT:USDT | below_1h_threshold | +2.65% | +2.96% |
| HOME/USDT:USDT | below_1h_threshold | +1.59% | +1.89% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
