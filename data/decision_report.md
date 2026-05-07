# Decision Report

- generated_at: 2026-05-07T17:57:39.674068+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3672**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3672, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-1.65%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.65% | **-1.65%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 11/20 | 55.0% | +1.59% | **+0.88%** |
| LIMIT_6PCT | 6/20 | 30.0% | +2.91% | **+0.87%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.53% | **+0.40%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +0.12% | **+0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +2.46% | **+2.46%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +3.20% | **+2.08%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.46% | **+1.31%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +3.67% | **+1.29%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +2.24% | **+0.90%** |

## 2. $100 Live Portfolio

- 残高: **$99.82** / 初期 $100.00 (-0.18%)
- 確定トレード: 22件 (TP 6 / SL 14 / EXP 2)
- 最新: LAB/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.82
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$110.07** / 初期 $100.00 (+10.07%)
- 確定: 166件 (Win 46 / Loss 57 / Flat 63) / skip 67件
- 成長率目線: 平均log +0.000578 / 幾何平均 +0.058% per trade / maxDD +2.62%
- 次の候補: `LIMIT_6PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SATO/USDT:USDT `LIMIT_6PCT_LONG` EXPIRED account +0.00% 残高後 $110.07

## 4. Latest Market Context

- 更新: 2026-05-07T17:57:33.527149+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.34% price=80032.3
- Funnel: target 767 → liquid 185 → pre 50 → checked 50 → surge 5 → strict 1
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.2 >= 65=1, 4h RSI 87.9 >= 65=1, 4h RSI 71.7 >= 65=1, 4h RSI 74.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +28.62% | $1,188,269.01 |
| JTO/USDT:USDT | +23.47% | $12,211,713.35 |
| B/USDT:USDT | +12.21% | $4,794,490.44 |
| LAB/USDT:USDT | +10.09% | $253,886,357.73 |
| SATO/USDT:USDT | +7.20% | $5,752,993.06 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NOT/USDT:USDT | below_1h_threshold | +3.88% | +3.54% |
| APE/USDT:USDT | below_1h_threshold | +3.37% | +3.03% |
| LUNC/USDT:USDT | below_1h_threshold | +3.28% | +2.94% |
| LIGHT/USDT:USDT | below_1h_threshold | +3.24% | +2.90% |
| LAB/USDT:USDT | below_1h_threshold | +2.81% | +2.47% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
