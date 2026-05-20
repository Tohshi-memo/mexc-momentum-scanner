# Decision Report

- generated_at: 2026-05-20T14:49:02.077691+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4549**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.66% / filled 20/20。**
- 全期間 MARKET基準: n=4549, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.66%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.66% | **+0.66%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.12% | **+1.06%** |
| ASK | 20/20 | 100.0% | +0.67% | **+0.67%** |
| MARKET | 20/20 | 100.0% | +0.66% | **+0.66%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.29% | **+0.39%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.51% | **+0.35%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +0.30% | **+0.12%** |
| MARKET_LONG | 20/20 | 100.0% | +0.09% | **+0.09%** |
| ASK_LONG | 20/20 | 100.0% | +0.05% | **+0.05%** |

## 2. $100 Live Portfolio

- 残高: **$96.69** / 初期 $100.00 (-3.31%)
- 確定トレード: 57件 (TP 15 / SL 39 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.69
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$123.58** / 初期 $100.00 (+23.58%)
- 確定: 511件 (Win 134 / Loss 175 / Flat 202) / skip 599件
- 成長率目線: 平均log +0.000414 / 幾何平均 +0.041% per trade / maxDD +4.21%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SAGA/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.11% 残高後 $123.58

## 4. Latest Market Context

- 更新: 2026-05-20T14:48:58.985534+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.27% price=77383.5
- Funnel: target 763 → liquid 131 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.4 >= 65=1, 4h RSI 68.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +85.29% | $2,788,589.88 |
| FIDA/USDT:USDT | +60.91% | $5,899,313.18 |
| EDEN/USDT:USDT | +31.63% | $23,731,200.20 |
| BANANAS31/USDT:USDT | +26.51% | $3,132,873.02 |
| LIT/USDT:USDT | +24.51% | $10,745,214.90 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +4.36% | +4.09% |
| ZEC/USDT:USDT | below_1h_threshold | +4.09% | +3.82% |
| UP/USDT:USDT | below_1h_threshold | +3.51% | +3.24% |
| ONDO/USDT:USDT | below_1h_threshold | +3.43% | +3.16% |
| PENGU/USDT:USDT | below_1h_threshold | +2.73% | +2.46% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
