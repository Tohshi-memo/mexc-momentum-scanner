# Decision Report

- generated_at: 2026-05-07T16:02:55.367952+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3652**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.46% / filled 20/20。**
- 全期間 MARKET基準: n=3652, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+0.46%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.46% | **+0.46%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +3.27% | **+1.14%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.02% | **+0.97%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.09% | **+0.87%** |
| LIMIT_4PCT | 11/20 | 55.0% | +1.09% | **+0.60%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +2.86% | **+2.00%** |
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

- 残高: **$112.16** / 初期 $100.00 (+12.16%)
- 確定: 146件 (Win 46 / Loss 53 / Flat 47) / skip 67件
- 成長率目線: 平均log +0.000786 / 幾何平均 +0.079% per trade / maxDD +2.62%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SATO/USDT:USDT `LIMIT_FIB1272_LONG` TP_HIT account +1.00% 残高後 $112.16

## 4. Latest Market Context

- 更新: 2026-05-07T16:02:52.185894+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=79860.3
- Funnel: target 771 → liquid 178 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +8.32% | $3,986,768.24 |
| PENGUIN/USDT:USDT | +2.57% | $4,552,699.08 |
| FHE/USDT:USDT | +2.24% | $13,424,239.20 |
| BSB/USDT:USDT | +1.92% | $5,158,329.35 |
| BILL/USDT:USDT | +1.79% | $10,736,096.91 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PENGUIN/USDT:USDT | below_1h_threshold | +2.58% | +2.58% |
| FHE/USDT:USDT | below_1h_threshold | +2.14% | +2.15% |
| BSB/USDT:USDT | below_1h_threshold | +1.86% | +1.86% |
| M/USDT:USDT | below_1h_threshold | +1.48% | +1.48% |
| BILL/USDT:USDT | below_1h_threshold | +1.39% | +1.39% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
