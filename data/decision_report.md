# Decision Report

- generated_at: 2026-05-20T19:08:49.741875+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4570**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4570, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |
| LIMIT_9PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |
| LIMIT_6PCT | 9/20 | 45.0% | -0.08% | **-0.03%** |
| LIMIT_7PCT | 7/20 | 35.0% | -0.11% | **-0.04%** |
| LIMIT_5PCT | 11/20 | 55.0% | -0.40% | **-0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.80% | **+1.80%** |
| ASK_LONG | 20/20 | 100.0% | +1.65% | **+1.65%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +2.01% | **+1.41%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +3.84% | **+1.34%** |
| LIMIT_BB3S_LONG | 5/11 | 45.5% | +2.60% | **+1.18%** |

## 2. $100 Live Portfolio

- 残高: **$96.69** / 初期 $100.00 (-3.31%)
- 確定トレード: 57件 (TP 15 / SL 39 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.69
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$124.50** / 初期 $100.00 (+24.50%)
- 確定: 532件 (Win 137 / Loss 178 / Flat 217) / skip 599件
- 成長率目線: 平均log +0.000412 / 幾何平均 +0.041% per trade / maxDD +4.21%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $124.50

## 4. Latest Market Context

- 更新: 2026-05-20T19:08:46.958457+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=77352.8
- Funnel: target 759 → liquid 126 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.0 >= 65=1, 4h RSI 77.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +121.59% | $47,896,081.23 |
| EDEN/USDT:USDT | +21.43% | $26,728,634.99 |
| LAB/USDT:USDT | +12.21% | $43,664,190.20 |
| NIL/USDT:USDT | +11.32% | $1,677,150.50 |
| JTO/USDT:USDT | +11.05% | $1,401,324.43 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +2.85% | +2.88% |
| BEAT/USDT:USDT | below_1h_threshold | +2.34% | +2.37% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.32% | +2.35% |
| NIL/USDT:USDT | below_1h_threshold | +2.31% | +2.34% |
| ZEC/USDT:USDT | below_1h_threshold | +1.75% | +1.78% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
