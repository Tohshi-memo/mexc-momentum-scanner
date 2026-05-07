# Decision Report

- generated_at: 2026-05-07T11:12:22.859005+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3619**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.85% / filled 20/20。**
- 全期間 MARKET基準: n=3619, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.85%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.85% | **+0.85%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +0.91% | **+0.87%** |
| MARKET | 20/20 | 100.0% | +0.85% | **+0.85%** |
| ASK | 20/20 | 100.0% | +0.81% | **+0.81%** |
| LIMIT_BB3S | 3/17 | 17.6% | +2.09% | **+0.37%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.34% | **+0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 19/20 | 95.0% | +1.43% | **+1.36%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +2.76% | **+0.83%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.23% | **+0.49%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.59% | **+0.44%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.44% | **+0.42%** |

## 2. $100 Live Portfolio

- 残高: **$100.83** / 初期 $100.00 (+0.83%)
- 確定トレード: 20件 (TP 6 / SL 12 / EXP 2)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.83
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.37** / 初期 $100.00 (+7.37%)
- 確定: 113件 (Win 37 / Loss 45 / Flat 31) / skip 67件
- 成長率目線: 平均log +0.000629 / 幾何平均 +0.063% per trade / maxDD +2.62%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SATO/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $107.37

## 4. Latest Market Context

- 更新: 2026-05-07T11:12:19.243669+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=80903.9
- Funnel: target 771 → liquid 184 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +122.55% | $2,185,526.32 |
| B3/USDT:USDT | +109.82% | $11,447,241.73 |
| PENGUIN/USDT:USDT | +81.28% | $3,522,170.42 |
| DOGS/USDT:USDT | +62.06% | $15,421,448.00 |
| SIREN/USDT:USDT | +41.45% | $14,335,852.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ENA/USDT:USDT | below_1h_threshold | +2.77% | +2.64% |
| XPL/USDT:USDT | below_1h_threshold | +2.47% | +2.34% |
| B3/USDT:USDT | below_1h_threshold | +1.73% | +1.60% |
| ONDO/USDT:USDT | below_1h_threshold | +1.66% | +1.54% |
| SATO/USDT:USDT | below_1h_threshold | +1.63% | +1.50% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
