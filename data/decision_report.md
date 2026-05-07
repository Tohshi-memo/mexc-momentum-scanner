# Decision Report

- generated_at: 2026-05-07T06:42:37.368401+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3581**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.47% / filled 20/20。**
- 全期間 MARKET基準: n=3581, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.47%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.47% | **+0.47%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.87% | **+0.78%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| ASK | 20/20 | 100.0% | +0.50% | **+0.50%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +1.54% | **+1.54%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +2.81% | **+0.98%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.89% | **+0.71%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.72% | **+0.69%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.22** / 初期 $100.00 (+7.22%)
- 確定: 75件 (Win 28 / Loss 30 / Flat 17) / skip 67件
- 成長率目線: 平均log +0.000930 / 幾何平均 +0.093% per trade / maxDD +2.48%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SATO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $107.22

## 4. Latest Market Context

- 更新: 2026-05-07T06:42:33.556869+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.27% price=81269.8
- Funnel: target 770 → liquid 187 → pre 50 → checked 50 → surge 4 → strict 0
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.2 >= 65=1, 4h RSI 82.5 >= 65=1, 4h RSI 81.2 >= 65=1, 4h RSI 69.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +259.35% | $1,830,667.67 |
| B3/USDT:USDT | +77.37% | $9,683,092.63 |
| DOGS/USDT:USDT | +71.38% | $12,650,986.25 |
| PENGUIN/USDT:USDT | +70.14% | $1,439,477.88 |
| FHE/USDT:USDT | +30.18% | $17,159,433.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FHE/USDT:USDT | below_1h_threshold | +3.72% | +3.44% |
| IO/USDT:USDT | below_1h_threshold | +2.71% | +2.44% |
| VIRTUAL/USDT:USDT | below_1h_threshold | +2.67% | +2.39% |
| GIGGLE/USDT:USDT | below_1h_threshold | +2.55% | +2.27% |
| TONCOIN/USDT:USDT | below_1h_threshold | +2.16% | +1.89% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
