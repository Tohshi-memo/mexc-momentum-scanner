# Decision Report

- generated_at: 2026-06-13T12:35:22.110537+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6578**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6578, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.07%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.07% | **-1.07%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 16/20 | 80.0% | +0.72% | **+0.58%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_ATR | 18/20 | 90.0% | +0.22% | **+0.20%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.01% | **+0.01%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | -0.15% | **-0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +0.75% | **+0.75%** |
| MARKET_LONG | 20/20 | 100.0% | +0.74% | **+0.74%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +1.51% | **+0.53%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +1.26% | **+0.51%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.45% | **+0.36%** |

## 2. $100 Live Portfolio

- 残高: **$97.07** / 初期 $100.00 (-2.93%)
- 確定トレード: 25件 (TP 6 / SL 18 / EXP 1)
- 最新: SPCXSTOCK/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.07
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$164.48** / 初期 $100.00 (+64.48%)
- 確定: 1451件 (Win 389 / Loss 464 / Flat 598) / skip 1688件
- 成長率目線: 平均log +0.000343 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $164.48

## 4. Latest Market Context

- 更新: 2026-06-13T12:35:18.272135+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=63978.0
- Funnel: target 770 → liquid 151 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JCT/USDT:USDT | +52.06% | $7,858,055.45 |
| RIF/USDT:USDT | +28.24% | $3,867,287.31 |
| VVV/USDT:USDT | +18.63% | $7,708,886.21 |
| NOT/USDT:USDT | +16.31% | $2,424,000.99 |
| TAO/USDT:USDT | +16.12% | $154,566,828.58 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JCT/USDT:USDT | below_1h_threshold | +4.66% | +4.59% |
| PYTH/USDT:USDT | below_1h_threshold | +3.34% | +3.27% |
| COAI/USDT:USDT | below_1h_threshold | +2.24% | +2.18% |
| WLD/USDT:USDT | below_1h_threshold | +2.02% | +1.95% |
| NOT/USDT:USDT | below_1h_threshold | +1.83% | +1.77% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
