# Decision Report

- generated_at: 2026-05-07T01:37:35.534112+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3527**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.28% / filled 20/20。**
- 全期間 MARKET基準: n=3527, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+0.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.28% | **+0.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.28% | **+0.28%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.91% | **+0.27%** |
| LIMIT_9PCT | 3/20 | 15.0% | +1.72% | **+0.26%** |
| ASK | 20/20 | 100.0% | +0.23% | **+0.23%** |
| LIMIT_7PCT | 4/20 | 20.0% | +1.10% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.21% | **+2.10%** |
| ASK_LONG | 20/20 | 100.0% | +1.43% | **+1.43%** |
| MARKET_LONG | 20/20 | 100.0% | +1.43% | **+1.43%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.75% | **+1.31%** |
| LIMIT_BB3S_LONG | 2/5 | 40.0% | +2.73% | **+1.09%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$102.14** / 初期 $100.00 (+2.14%)
- 確定: 22件 (Win 8 / Loss 8 / Flat 6) / skip 66件
- 成長率目線: 平均log +0.000964 / 幾何平均 +0.096% per trade / maxDD +2.48%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DOGS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $102.14

## 4. Latest Market Context

- 更新: 2026-05-07T01:37:31.713534+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.23% price=81150.3
- Funnel: target 770 → liquid 189 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.7 >= 65=1, 4h RSI 76.4 >= 65=1, 4h RSI 76.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +122.93% | $1,028,445.59 |
| DOGS/USDT:USDT | +57.64% | $6,415,463.46 |
| FHE/USDT:USDT | +25.00% | $15,954,880.04 |
| PENGUIN/USDT:USDT | +24.06% | $1,045,090.30 |
| LAB/USDT:USDT | +12.72% | $256,395,685.09 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NOT/USDT:USDT | below_1h_threshold | +2.90% | +2.68% |
| TONCOIN/USDT:USDT | below_1h_threshold | +2.34% | +2.11% |
| BILL/USDT:USDT | below_1h_threshold | +1.04% | +0.82% |
| M/USDT:USDT | below_1h_threshold | +0.87% | +0.65% |
| SILVER/USDT:USDT | below_1h_threshold | +0.83% | +0.60% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
