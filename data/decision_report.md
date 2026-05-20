# Decision Report

- generated_at: 2026-05-20T19:49:01.058415+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4577**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4577, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=-2.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.80% | **-2.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 4/20 | 20.0% | -1.00% | **-0.20%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | -0.84% | **-0.42%** |
| LIMIT_6PCT | 11/20 | 55.0% | -0.77% | **-0.42%** |
| LIMIT_5PCT | 13/20 | 65.0% | -0.79% | **-0.51%** |
| LIMIT_7PCT | 9/20 | 45.0% | -1.15% | **-0.52%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +2.58% | **+2.06%** |
| MARKET_LONG | 20/20 | 100.0% | +2.00% | **+2.00%** |
| LIMIT_BB3S_LONG | 7/13 | 53.8% | +3.36% | **+1.81%** |
| ASK_LONG | 20/20 | 100.0% | +1.55% | **+1.55%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.17% | **+1.41%** |

## 2. $100 Live Portfolio

- 残高: **$96.69** / 初期 $100.00 (-3.31%)
- 確定トレード: 57件 (TP 15 / SL 39 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.69
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$123.87** / 初期 $100.00 (+23.87%)
- 確定: 538件 (Win 137 / Loss 179 / Flat 222) / skip 600件
- 成長率目線: 平均log +0.000398 / 幾何平均 +0.040% per trade / maxDD +4.21%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EDEN/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $123.87

## 4. Latest Market Context

- 更新: 2026-05-20T19:48:55.480659+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.30% price=77607.9
- Funnel: target 759 → liquid 128 → pre 50 → checked 50 → surge 5 → strict 1
- Surge前reject: below_1h_threshold=44, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.4 >= 65=1, 4h RSI 81.2 >= 65=1, 4h RSI 80.1 >= 65=1, 4h RSI 84.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +46.65% | $61,053,974.85 |
| EDEN/USDT:USDT | +38.23% | $28,727,060.16 |
| FIDA/USDT:USDT | +21.83% | $8,747,570.51 |
| NIL/USDT:USDT | +18.63% | $2,107,039.90 |
| BANANAS31/USDT:USDT | +9.55% | $4,014,529.40 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FIGHT/USDT:USDT | below_relative_strength | +5.28% | +4.98% |
| ZEN/USDT:USDT | below_1h_threshold | +4.72% | +4.42% |
| BEAT/USDT:USDT | below_1h_threshold | +4.32% | +4.02% |
| BANANAS31/USDT:USDT | below_1h_threshold | +3.13% | +2.83% |
| TIA/USDT:USDT | below_1h_threshold | +2.75% | +2.45% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
