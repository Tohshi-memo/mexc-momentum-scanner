# Decision Report

- generated_at: 2026-06-07T15:29:57.048597+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5971**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5971, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-2.11%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.11% | **-2.11%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_BB3S | 5/15 | 33.3% | +0.68% | **+0.23%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | -0.76% | **-0.19%** |
| LIMIT_4PCT | 16/20 | 80.0% | -0.25% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +4.78% | **+3.11%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +4.86% | **+2.92%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +3.87% | **+2.71%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +6.19% | **+2.17%** |
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +3.44% | **+2.06%** |

## 2. $100 Live Portfolio

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定トレード: 5件 (TP 1 / SL 4 / EXP 0)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.00
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$148.08** / 初期 $100.00 (+48.08%)
- 確定: 1088件 (Win 264 / Loss 328 / Flat 496) / skip 1444件
- 成長率目線: 平均log +0.000361 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $148.08

## 4. Latest Market Context

- 更新: 2026-06-07T15:29:53.788332+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=61927.0
- Funnel: target 768 → liquid 122 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +67.03% | $12,656,777.43 |
| FIDA/USDT:USDT | +63.52% | $9,393,883.21 |
| SIREN/USDT:USDT | +61.01% | $25,177,744.19 |
| LAB/USDT:USDT | +39.24% | $63,272,480.58 |
| ESPORTS/USDT:USDT | +35.20% | $2,899,412.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +3.85% | +3.76% |
| BSB/USDT:USDT | below_1h_threshold | +3.44% | +3.36% |
| NEAR/USDT:USDT | below_1h_threshold | +3.12% | +3.03% |
| ZEST/USDT:USDT | below_1h_threshold | +2.75% | +2.66% |
| WLD/USDT:USDT | below_1h_threshold | +2.43% | +2.34% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
