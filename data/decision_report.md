# Decision Report

- generated_at: 2026-05-07T15:37:54.018207+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3649**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.40% / filled 20/20。**
- 全期間 MARKET基準: n=3649, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.40% | **+0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.89% | **+0.71%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +2.46% | **+1.60%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +2.72% | **+1.49%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +2.48% | **+1.49%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +2.62% | **+1.44%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +5.00% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$100.83** / 初期 $100.00 (+0.83%)
- 確定トレード: 20件 (TP 6 / SL 12 / EXP 2)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.83
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$111.05** / 初期 $100.00 (+11.05%)
- 確定: 143件 (Win 45 / Loss 53 / Flat 45) / skip 67件
- 成長率目線: 平均log +0.000733 / 幾何平均 +0.073% per trade / maxDD +2.62%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PENGUIN/USDT:USDT `LIMIT_FIB1272_LONG` TP_HIT account +1.00% 残高後 $111.05

## 4. Latest Market Context

- 更新: 2026-05-07T15:37:48.371843+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.17% price=79994.5
- Funnel: target 771 → liquid 183 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.2 >= 65=1, 4h RSI 80.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B3/USDT:USDT | +89.21% | $10,253,278.38 |
| SATO/USDT:USDT | +77.11% | $3,868,327.18 |
| PENGUIN/USDT:USDT | +63.81% | $4,460,902.11 |
| NIL/USDT:USDT | +55.12% | $5,748,272.94 |
| DOGS/USDT:USDT | +50.38% | $18,084,526.49 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SATO/USDT:USDT | below_1h_threshold | +4.13% | +4.29% |
| NIL/USDT:USDT | below_1h_threshold | +3.18% | +3.35% |
| DOGS/USDT:USDT | below_1h_threshold | +2.65% | +2.82% |
| STRK/USDT:USDT | below_1h_threshold | +2.25% | +2.42% |
| KSM/USDT:USDT | below_1h_threshold | +1.85% | +2.02% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
