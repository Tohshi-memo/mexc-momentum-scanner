# Decision Report

- generated_at: 2026-07-04T05:37:41.702178+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8222**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8222, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.75%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.75% | **-0.75%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 9/20 | 45.0% | +1.23% | **+0.55%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.44% | **+0.36%** |
| LIMIT_8PCT | 3/20 | 15.0% | +1.14% | **+0.17%** |
| LIMIT_BB3S | 4/18 | 22.2% | +0.64% | **+0.14%** |
| LIMIT_9PCT | 2/20 | 10.0% | +0.29% | **+0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.17% | **+1.17%** |
| ASK_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.64% | **+0.90%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.38% | **+0.69%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |

## 2. $100 Live Portfolio

- 残高: **$102.10** / 初期 $100.00 (+2.10%)
- 確定トレード: 57件 (TP 20 / SL 36 / EXP 1)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$306.60** / 初期 $100.00 (+206.60%)
- 確定: 2539件 (Win 789 / Loss 846 / Flat 904) / skip 2244件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ANSEM/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $306.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.36** / 初期 $100.00 (+6.36%)
- 確定: 618件 (Win 149 / Loss 150 / Flat 319) / skip 1015件
- 成長率目線: 平均log +0.000100 / 幾何平均 +0.010% per trade / maxDD +3.57%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0595 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ANSEM/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $106.36

## 5. Latest Market Context

- 更新: 2026-07-04T05:37:36.236895+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.26% price=62496.6
- Funnel: target 834 → liquid 156 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.8 >= 65=1, 4h RSI 75.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ANSEM/USDT:USDT | +79.94% | $4,557,944.27 |
| TLM/USDT:USDT | +64.26% | $42,262,610.12 |
| HMSTR/USDT:USDT | +41.43% | $3,356,831.38 |
| BAS/USDT:USDT | +31.90% | $4,102,662.79 |
| MAGMA/USDT:USDT | +29.37% | $15,566,265.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HMSTR/USDT:USDT | below_1h_threshold | +4.32% | +4.59% |
| M/USDT:USDT | below_1h_threshold | +3.54% | +3.81% |
| MAGMA/USDT:USDT | below_1h_threshold | +3.08% | +3.34% |
| BAS/USDT:USDT | below_1h_threshold | +2.88% | +3.14% |
| UB/USDT:USDT | below_1h_threshold | +2.67% | +2.93% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
