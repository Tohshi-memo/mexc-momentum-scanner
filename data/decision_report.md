# Decision Report

- generated_at: 2026-05-30T16:10:23.024875+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5137**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.32% / filled 20/20。**
- 全期間 MARKET基準: n=5137, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+2.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.32% | **+2.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.32% | **+2.32%** |
| ASK | 20/20 | 100.0% | +1.83% | **+1.83%** |
| LIMIT_1PCT | 18/20 | 90.0% | +2.03% | **+1.82%** |
| LIMIT_BB3S | 7/17 | 41.2% | +3.88% | **+1.60%** |
| LIMIT_3PCT | 13/20 | 65.0% | +2.03% | **+1.32%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +4.79% | **+3.20%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.06% | **+0.53%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.22% | **+0.44%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.10% | **+0.27%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$98.59** / 初期 $100.00 (-1.41%)
- 確定トレード: 77件 (TP 23 / SL 51 / EXP 3)
- 最新: HEI/USDT:USDT TP_HIT PnL +8.00% 残高後 $98.59
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$123.19** / 初期 $100.00 (+23.19%)
- 確定: 791件 (Win 183 / Loss 242 / Flat 366) / skip 907件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +6.10%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STG/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.16% 残高後 $123.19

## 4. Latest Market Context

- 更新: 2026-05-30T16:10:18.247662+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=73894.3
- Funnel: target 773 → liquid 122 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SKYAI/USDT:USDT | +10.62% | $9,250,365.83 |
| OL/USDT:USDT | +4.85% | $1,565,212.96 |
| RAVE/USDT:USDT | +4.03% | $1,522,934.80 |
| RIVER/USDT:USDT | +2.77% | $3,855,080.12 |
| UB/USDT:USDT | +2.13% | $10,064,419.94 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| OL/USDT:USDT | below_1h_threshold | +4.86% | +4.85% |
| RAVE/USDT:USDT | below_1h_threshold | +4.03% | +4.02% |
| RIVER/USDT:USDT | below_1h_threshold | +2.77% | +2.76% |
| ALLO/USDT:USDT | below_1h_threshold | +2.15% | +2.14% |
| UB/USDT:USDT | below_1h_threshold | +2.13% | +2.12% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
