# Decision Report

- generated_at: 2026-05-20T19:53:55.368944+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4578**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4578, expectancy=-0.11%
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
| LIMIT_FIB1272 | 9/20 | 45.0% | -1.07% | **-0.48%** |
| LIMIT_6PCT | 10/20 | 50.0% | -1.03% | **-0.52%** |
| LIMIT_5PCT | 12/20 | 60.0% | -0.94% | **-0.56%** |
| LIMIT_9PCT | 6/20 | 30.0% | -2.00% | **-0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +2.39% | **+1.92%** |
| LIMIT_BB3S_LONG | 7/13 | 53.8% | +3.36% | **+1.81%** |
| MARKET_LONG | 20/20 | 100.0% | +1.80% | **+1.80%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +3.04% | **+1.52%** |
| ASK_LONG | 20/20 | 100.0% | +1.34% | **+1.34%** |

## 2. $100 Live Portfolio

- 残高: **$96.69** / 初期 $100.00 (-3.31%)
- 確定トレード: 57件 (TP 15 / SL 39 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.69
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$123.87** / 初期 $100.00 (+23.87%)
- 確定: 538件 (Win 137 / Loss 179 / Flat 222) / skip 601件
- 成長率目線: 平均log +0.000398 / 幾何平均 +0.040% per trade / maxDD +4.21%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EDEN/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $123.87

## 4. Latest Market Context

- 更新: 2026-05-20T19:53:49.865625+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.32% price=77620.6
- Funnel: target 759 → liquid 128 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.2 >= 65=1, 4h RSI 81.1 >= 65=1, 4h RSI 81.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EDEN/USDT:USDT | +36.47% | $28,905,882.91 |
| BSB/USDT:USDT | +30.75% | $61,729,756.46 |
| FIDA/USDT:USDT | +21.93% | $8,814,859.40 |
| NIL/USDT:USDT | +20.85% | $2,146,355.55 |
| LAB/USDT:USDT | +10.14% | $46,621,484.29 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEC/USDT:USDT | below_1h_threshold | +4.98% | +4.66% |
| ZEN/USDT:USDT | below_1h_threshold | +4.92% | +4.61% |
| FIGHT/USDT:USDT | below_1h_threshold | +4.52% | +4.20% |
| LIT/USDT:USDT | below_1h_threshold | +4.01% | +3.69% |
| BEAT/USDT:USDT | below_1h_threshold | +3.18% | +2.86% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
