# Decision Report

- generated_at: 2026-05-08T03:32:51.270112+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3728**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.40% / filled 20/20。**
- 全期間 MARKET基準: n=3728, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+1.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.62% | **+1.45%** |
| LIMIT_3PCT | 14/20 | 70.0% | +2.02% | **+1.41%** |
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +3.37% | **+1.35%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.26% | **+1.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.62% | **+0.34%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +0.97% | **+0.19%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +0.27% | **+0.05%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.02% | **+0.01%** |

## 2. $100 Live Portfolio

- 残高: **$98.83** / 初期 $100.00 (-1.17%)
- 確定トレード: 24件 (TP 6 / SL 16 / EXP 2)
- 最新: PENGUIN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.83
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 190件 (Win 48 / Loss 64 / Flat 78) / skip 99件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.043% per trade / maxDD +3.48%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PENGUIN/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-08T03:32:47.490395+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.17% price=79583.4
- Funnel: target 771 → liquid 184 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.3 >= 65=1, 4h RSI 71.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +31.99% | $2,107,888.57 |
| NOT/USDT:USDT | +20.42% | $10,965,444.87 |
| LAB/USDT:USDT | +20.33% | $212,044,812.78 |
| TST/USDT:USDT | +19.42% | $6,304,374.47 |
| DYDX/USDT:USDT | +16.61% | $12,247,035.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NOT/USDT:USDT | below_1h_threshold | +2.53% | +2.36% |
| PENDLE/USDT:USDT | below_1h_threshold | +2.44% | +2.27% |
| CHIP/USDT:USDT | below_1h_threshold | +2.42% | +2.25% |
| ZBT/USDT:USDT | below_1h_threshold | +2.38% | +2.21% |
| STRK/USDT:USDT | below_1h_threshold | +2.09% | +1.92% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
