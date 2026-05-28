# Decision Report

- generated_at: 2026-05-28T13:44:35.368790+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4961**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.83% / filled 20/20。**
- 全期間 MARKET基準: n=4961, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+1.83%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.83% | **+1.83%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 16/20 | 80.0% | +2.41% | **+1.93%** |
| ASK | 20/20 | 100.0% | +1.92% | **+1.92%** |
| MARKET | 20/20 | 100.0% | +1.83% | **+1.83%** |
| LIMIT_1PCT | 17/20 | 85.0% | +2.03% | **+1.73%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.88% | **+1.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.34% | **+0.23%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.16% | **+0.23%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.04% | **+0.01%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | -0.57% | **-0.26%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -3.95% | **-0.39%** |

## 2. $100 Live Portfolio

- 残高: **$98.61** / 初期 $100.00 (-1.39%)
- 確定トレード: 71件 (TP 21 / SL 47 / EXP 3)
- 最新: BILL/USDT:USDT TP_HIT PnL +8.00% 残高後 $98.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$126.79** / 初期 $100.00 (+26.79%)
- 確定: 696件 (Win 172 / Loss 220 / Flat 304) / skip 826件
- 成長率目線: 平均log +0.000341 / 幾何平均 +0.034% per trade / maxDD +4.72%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BILL/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $126.79

## 4. Latest Market Context

- 更新: 2026-05-28T13:44:32.766348+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.95% price=72801.2
- Funnel: target 776 → liquid 156 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 95.4 >= 65=1, 4h RSI 87.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SNOWSTOCK/USDT:USDT | +30.16% | $10,833,518.96 |
| XLM/USDT:USDT | +25.79% | $185,870,901.93 |
| ONDSSTOCK/USDT:USDT | +20.19% | $1,122,789.52 |
| PRL/USDT:USDT | +15.96% | $2,402,585.91 |
| NBISSTOCK/USDT:USDT | +9.07% | $2,130,583.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HBAR/USDT:USDT | below_1h_threshold | +2.85% | +3.80% |
| LLYSTOCK/USDT:USDT | below_1h_threshold | +1.71% | +2.66% |
| BEAT/USDT:USDT | below_1h_threshold | +1.58% | +2.52% |
| CRO/USDT:USDT | below_1h_threshold | +1.49% | +2.44% |
| RKLBSTOCK/USDT:USDT | below_1h_threshold | +1.34% | +2.29% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
