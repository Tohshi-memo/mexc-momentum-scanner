# Decision Report

- generated_at: 2026-05-13T15:13:26.233134+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4231**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4231, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.48%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.48% | **-0.48%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_BB3S | 8/18 | 44.4% | +0.35% | **+0.15%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.02% | **+0.00%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.00% | **+0.00%** |
| LIMIT_3PCT | 13/20 | 65.0% | -0.20% | **-0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.32% | **+1.12%** |
| ASK_LONG | 20/20 | 100.0% | +0.90% | **+0.90%** |
| MARKET_LONG | 20/20 | 100.0% | +0.74% | **+0.74%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.09% | **+0.55%** |

## 2. $100 Live Portfolio

- 残高: **$97.71** / 初期 $100.00 (-2.29%)
- 確定トレード: 37件 (TP 9 / SL 25 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.78** / 初期 $100.00 (+19.78%)
- 確定: 341件 (Win 94 / Loss 124 / Flat 123) / skip 451件
- 成長率目線: 平均log +0.000529 / 幾何平均 +0.053% per trade / maxDD +4.21%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UB/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.01% 残高後 $119.78

## 4. Latest Market Context

- 更新: 2026-05-13T15:13:22.684127+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.31% price=79476.8
- Funnel: target 765 → liquid 179 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COS/USDT:USDT | +59.93% | $2,057,059.14 |
| LAB/USDT:USDT | +45.07% | $141,657,811.92 |
| TRUTH/USDT:USDT | +30.33% | $4,076,131.15 |
| JCT/USDT:USDT | +27.15% | $1,161,652.77 |
| UB/USDT:USDT | +26.11% | $10,967,903.43 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KITE/USDT:USDT | below_1h_threshold | +2.55% | +2.86% |
| NAORIS/USDT:USDT | below_1h_threshold | +2.12% | +2.44% |
| TRUTH/USDT:USDT | below_1h_threshold | +2.00% | +2.32% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +1.59% | +1.91% |
| RIVER/USDT:USDT | below_1h_threshold | +0.78% | +1.10% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
