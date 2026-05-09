# Decision Report

- generated_at: 2026-05-09T23:57:39.209036+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3925**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.98% / filled 20/20。**
- 全期間 MARKET基準: n=3925, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.98%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.98% | **+0.98%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.27% | **+1.14%** |
| ASK | 20/20 | 100.0% | +1.09% | **+1.09%** |
| MARKET | 20/20 | 100.0% | +0.98% | **+0.98%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.77% | **+0.62%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.19% | **+0.60%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.70% | **+0.38%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.65% | **+0.33%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | -0.02% | **-0.02%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.73** / 初期 $100.00 (+7.73%)
- 確定: 196件 (Win 48 / Loss 66 / Flat 82) / skip 290件
- 成長率目線: 平均log +0.000380 / 幾何平均 +0.038% per trade / maxDD +4.09%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $107.73

## 4. Latest Market Context

- 更新: 2026-05-09T23:57:36.060182+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=80661.9
- Funnel: target 769 → liquid 175 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| INX/USDT:USDT | +31.55% | $8,551,479.90 |
| SATO/USDT:USDT | +16.34% | $5,451,204.02 |
| JASMY/USDT:USDT | +15.25% | $13,926,990.39 |
| BILL/USDT:USDT | +13.86% | $39,535,237.88 |
| BANK/USDT:USDT | +11.62% | $1,165,278.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BRETT/USDT:USDT | below_1h_threshold | +2.64% | +2.72% |
| OFC/USDT:USDT | below_1h_threshold | +2.03% | +2.11% |
| UNI/USDT:USDT | below_1h_threshold | +1.12% | +1.20% |
| PTB/USDT:USDT | below_1h_threshold | +0.97% | +1.05% |
| JASMY/USDT:USDT | below_1h_threshold | +0.87% | +0.96% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
