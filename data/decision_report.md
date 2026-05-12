# Decision Report

- generated_at: 2026-05-12T14:17:58.134925+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4127**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4127, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-0.93%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.93% | **-0.93%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | -0.04% | **-0.01%** |
| LIMIT_3PCT | 17/20 | 85.0% | -0.19% | **-0.16%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.81% | **+0.99%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.37% | **+0.82%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.99% | **+0.74%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.33% | **+0.60%** |
| MARKET_LONG | 20/20 | 100.0% | +0.53% | **+0.53%** |

## 2. $100 Live Portfolio

- 残高: **$99.19** / 初期 $100.00 (-0.81%)
- 確定トレード: 34件 (TP 9 / SL 22 / EXP 3)
- 最新: DOGS/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.19
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$116.52** / 初期 $100.00 (+16.52%)
- 確定: 263件 (Win 72 / Loss 89 / Flat 102) / skip 425件
- 成長率目線: 平均log +0.000581 / 幾何平均 +0.058% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SOLV/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $116.52

## 4. Latest Market Context

- 更新: 2026-05-12T14:17:54.658033+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.22% price=80612.2
- Funnel: target 763 → liquid 191 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SAGA/USDT:USDT | +81.70% | $26,761,544.11 |
| GIGA/USDT:USDT | +59.29% | $7,168,546.72 |
| USELESS/USDT:USDT | +42.55% | $10,684,062.76 |
| SOLV/USDT:USDT | +40.79% | $1,824,610.65 |
| SKYAI/USDT:USDT | +40.67% | $39,982,110.97 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GIGA/USDT:USDT | below_1h_threshold | +2.59% | +2.37% |
| PENGUIN/USDT:USDT | below_1h_threshold | +2.24% | +2.02% |
| SAHARA/USDT:USDT | below_1h_threshold | +2.21% | +1.99% |
| NAORIS/USDT:USDT | below_1h_threshold | +1.98% | +1.75% |
| SIREN/USDT:USDT | below_1h_threshold | +1.94% | +1.72% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
