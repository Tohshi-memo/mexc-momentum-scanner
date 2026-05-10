# Decision Report

- generated_at: 2026-05-10T19:58:09.660693+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3986**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3986, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-0.94%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.94% | **-0.94%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.79% | **+0.36%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_BB3S | 5/13 | 38.5% | +0.02% | **+0.01%** |
| LIMIT_4PCT | 12/20 | 60.0% | -0.28% | **-0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.99% | **+1.79%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +2.35% | **+1.65%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +1.56% | **+0.86%** |
| MARKET_LONG | 20/20 | 100.0% | +0.72% | **+0.72%** |
| ASK_LONG | 20/20 | 100.0% | +0.72% | **+0.72%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.80** / 初期 $100.00 (+8.80%)
- 確定: 199件 (Win 49 / Loss 66 / Flat 84) / skip 348件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +4.09%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TROLLSOL/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $108.80

## 4. Latest Market Context

- 更新: 2026-05-10T19:58:06.195606+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=81350.9
- Funnel: target 769 → liquid 171 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.6 >= 65=1, 4h RSI 78.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +30.14% | $1,505,863.63 |
| TROLLSOL/USDT:USDT | +24.93% | $3,858,457.85 |
| ALCH/USDT:USDT | +22.29% | $2,571,052.20 |
| B/USDT:USDT | +16.67% | $2,108,566.27 |
| SUI/USDT:USDT | +12.91% | $628,983,159.25 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JUP/USDT:USDT | below_1h_threshold | +2.85% | +2.71% |
| SPX/USDT:USDT | below_1h_threshold | +2.28% | +2.13% |
| ENS/USDT:USDT | below_1h_threshold | +2.23% | +2.09% |
| APT/USDT:USDT | below_1h_threshold | +2.21% | +2.07% |
| B/USDT:USDT | below_1h_threshold | +2.14% | +2.00% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
