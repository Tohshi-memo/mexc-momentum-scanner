# Decision Report

- generated_at: 2026-06-14T16:42:15.257471+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6682**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.59% / filled 20/20。**
- 全期間 MARKET基準: n=6682, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.59% | **+0.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_ATR | 9/20 | 45.0% | +2.54% | **+1.14%** |
| LIMIT_8PCT | 5/20 | 25.0% | +3.88% | **+0.97%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| MARKET | 20/20 | 100.0% | +0.59% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.12% | **+1.12%** |
| MARKET_LONG | 20/20 | 100.0% | +0.54% | **+0.54%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.01% | **+0.41%** |

## 2. $100 Live Portfolio

- 残高: **$100.99** / 初期 $100.00 (+0.99%)
- 確定トレード: 4件 (TP 2 / SL 2 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.99
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$173.78** / 初期 $100.00 (+73.78%)
- 確定: 1555件 (Win 414 / Loss 492 / Flat 649) / skip 1688件
- 成長率目線: 平均log +0.000355 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EVAA/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $173.78

## 4. Robust Adaptive DryRun ($100)

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定: 65件 (Win 19 / Loss 12 / Flat 34) / skip 28件
- 成長率目線: 平均log -0.000154 / 幾何平均 -0.015% per trade / maxDD +2.00%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0376 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $99.00

## 5. Latest Market Context

- 更新: 2026-06-14T16:42:10.894419+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.19% price=64115.1
- Funnel: target 770 → liquid 128 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| H/USDT:USDT | +11.24% | $106,273,905.01 |
| EVAA/USDT:USDT | +7.49% | $1,782,521.21 |
| EIGEN/USDT:USDT | +3.36% | $1,510,713.66 |
| TRADOOR/USDT:USDT | +3.06% | $9,296,369.52 |
| BANANAS31/USDT:USDT | +2.88% | $1,782,430.24 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EIGEN/USDT:USDT | below_1h_threshold | +3.37% | +3.18% |
| TRADOOR/USDT:USDT | below_1h_threshold | +3.07% | +2.88% |
| BANANAS31/USDT:USDT | below_1h_threshold | +2.89% | +2.70% |
| JTO/USDT:USDT | below_1h_threshold | +2.48% | +2.30% |
| EDGE/USDT:USDT | below_1h_threshold | +2.41% | +2.22% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
