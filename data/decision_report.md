# Decision Report

- generated_at: 2026-05-20T19:39:07.512483+00:00
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

- 更新: 2026-05-20T19:39:01.726277+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.22% price=77548.5
- Funnel: target 759 → liquid 127 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=45, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.1 >= 65=1, 4h RSI 81.0 >= 65=1, 4h RSI 79.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EDEN/USDT:USDT | +36.17% | $28,517,795.06 |
| FIDA/USDT:USDT | +23.18% | $8,490,779.59 |
| BSB/USDT:USDT | +23.03% | $59,072,559.90 |
| NIL/USDT:USDT | +16.36% | $2,022,194.06 |
| LAB/USDT:USDT | +10.77% | $45,359,576.40 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEC/USDT:USDT | below_relative_strength | +5.03% | +4.81% |
| BEAT/USDT:USDT | below_1h_threshold | +4.26% | +4.03% |
| FIGHT/USDT:USDT | below_1h_threshold | +3.89% | +3.67% |
| TIA/USDT:USDT | below_1h_threshold | +3.37% | +3.14% |
| ZEN/USDT:USDT | below_1h_threshold | +3.35% | +3.12% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
