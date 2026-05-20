# Decision Report

- generated_at: 2026-05-20T19:03:46.716857+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4569**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4569, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_6PCT | 8/20 | 40.0% | +0.42% | **+0.17%** |
| LIMIT_7PCT | 6/20 | 30.0% | +0.54% | **+0.16%** |
| LIMIT_5PCT | 11/20 | 55.0% | +0.05% | **+0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.20% | **+2.20%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +2.66% | **+1.86%** |
| ASK_LONG | 20/20 | 100.0% | +1.65% | **+1.65%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.53% | **+1.52%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +3.84% | **+1.34%** |

## 2. $100 Live Portfolio

- 残高: **$96.69** / 初期 $100.00 (-3.31%)
- 確定トレード: 57件 (TP 15 / SL 39 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.69
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$124.50** / 初期 $100.00 (+24.50%)
- 確定: 531件 (Win 137 / Loss 178 / Flat 216) / skip 599件
- 成長率目線: 平均log +0.000413 / 幾何平均 +0.041% per trade / maxDD +4.21%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $124.50

## 4. Latest Market Context

- 更新: 2026-05-20T19:03:43.811832+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=77356.1
- Funnel: target 759 → liquid 126 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.3 >= 65=1, 4h RSI 76.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +99.23% | $45,781,552.95 |
| EDEN/USDT:USDT | +19.92% | $26,506,209.19 |
| JTO/USDT:USDT | +10.10% | $1,363,399.96 |
| LAB/USDT:USDT | +10.07% | $43,101,857.61 |
| NIL/USDT:USDT | +9.54% | $1,643,157.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +1.79% | +1.81% |
| BEAT/USDT:USDT | below_1h_threshold | +1.21% | +1.23% |
| LAB/USDT:USDT | below_1h_threshold | +0.87% | +0.90% |
| JTO/USDT:USDT | below_1h_threshold | +0.80% | +0.82% |
| ZEC/USDT:USDT | below_1h_threshold | +0.67% | +0.70% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
