# Decision Report

- generated_at: 2026-05-12T23:32:58.394579+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4168**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.90% / filled 20/20。**
- 全期間 MARKET基準: n=4168, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=+0.90%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.90% | **+0.90%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.90% | **+0.90%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.63% | **+0.79%** |
| ASK | 20/20 | 100.0% | +0.56% | **+0.56%** |
| LIMIT_BB3S | 9/19 | 47.4% | +1.11% | **+0.53%** |
| LIMIT_3PCT | 11/20 | 55.0% | +0.65% | **+0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.73% | **+0.78%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +0.01% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$98.69** / 初期 $100.00 (-1.31%)
- 確定トレード: 35件 (TP 9 / SL 23 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -3.91% 残高後 $98.69
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.18** / 初期 $100.00 (+21.18%)
- 確定: 304件 (Win 88 / Loss 105 / Flat 111) / skip 425件
- 成長率目線: 平均log +0.000632 / 幾何平均 +0.063% per trade / maxDD +4.21%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SATO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $121.18

## 4. Latest Market Context

- 更新: 2026-05-12T23:32:55.158564+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=80585.5
- Funnel: target 758 → liquid 184 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +11.71% | $111,181,731.35 |
| AKT/USDT:USDT | +11.44% | $2,491,802.43 |
| VIC/USDT:USDT | +10.57% | $6,213,673.35 |
| PEAQ/USDT:USDT | +9.70% | $2,090,125.90 |
| TRUMPOFFICIAL/USDT:USDT | +9.38% | $26,760,379.47 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CHIP/USDT:USDT | below_1h_threshold | +2.80% | +2.84% |
| UB/USDT:USDT | below_1h_threshold | +1.87% | +1.90% |
| ZEC/USDT:USDT | below_1h_threshold | +1.52% | +1.56% |
| NAORIS/USDT:USDT | below_1h_threshold | +1.33% | +1.37% |
| TRUMPOFFICIAL/USDT:USDT | below_1h_threshold | +1.32% | +1.36% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
