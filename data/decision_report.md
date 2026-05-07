# Decision Report

- generated_at: 2026-05-07T10:52:33.664457+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3616**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.78% / filled 20/20。**
- 全期間 MARKET基準: n=3616, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.78%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.78% | **+0.78%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.52% | **+1.45%** |
| MARKET | 20/20 | 100.0% | +0.78% | **+0.78%** |
| ASK | 20/20 | 100.0% | +0.70% | **+0.70%** |
| LIMIT_BB3S | 2/15 | 13.3% | +3.09% | **+0.41%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.73% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.40% | **+0.77%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.23% | **+0.49%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +0.54% | **+0.48%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.72% | **+0.47%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +1.86% | **+0.46%** |

## 2. $100 Live Portfolio

- 残高: **$100.83** / 初期 $100.00 (+0.83%)
- 確定トレード: 20件 (TP 6 / SL 12 / EXP 2)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.83
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.91** / 初期 $100.00 (+7.91%)
- 確定: 110件 (Win 37 / Loss 44 / Flat 29) / skip 67件
- 成長率目線: 平均log +0.000692 / 幾何平均 +0.069% per trade / maxDD +2.62%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIL/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.79% 残高後 $107.91

## 4. Latest Market Context

- 更新: 2026-05-07T10:52:30.547106+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=80798.1
- Funnel: target 771 → liquid 185 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.2 >= 65=1, 4h RSI 70.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +119.81% | $2,195,060.79 |
| B3/USDT:USDT | +107.53% | $11,366,317.67 |
| PENGUIN/USDT:USDT | +90.56% | $3,359,760.35 |
| DOGS/USDT:USDT | +64.64% | $15,312,729.40 |
| NIL/USDT:USDT | +42.30% | $2,136,980.98 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DYDX/USDT:USDT | below_1h_threshold | +4.81% | +4.92% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +4.47% | +4.58% |
| TAG/USDT:USDT | below_1h_threshold | +4.09% | +4.20% |
| B3/USDT:USDT | below_1h_threshold | +4.04% | +4.15% |
| B/USDT:USDT | below_1h_threshold | +3.45% | +3.56% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
