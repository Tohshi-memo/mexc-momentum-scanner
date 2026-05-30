# Decision Report

- generated_at: 2026-05-30T11:05:00.665063+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5120**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.11% / filled 20/20。**
- 全期間 MARKET基準: n=5120, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+1.11%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.11% | **+1.11%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.14% | **+1.14%** |
| MARKET | 20/20 | 100.0% | +1.11% | **+1.11%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.90% | **+0.76%** |
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/5 | 100.0% | +1.81% | **+1.81%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.09% | **+0.82%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +0.87% | **+0.70%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.34% | **+0.60%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +0.55% | **+0.49%** |

## 2. $100 Live Portfolio

- 残高: **$98.10** / 初期 $100.00 (-1.90%)
- 確定トレード: 75件 (TP 22 / SL 50 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$126.64** / 初期 $100.00 (+26.64%)
- 確定: 775件 (Win 182 / Loss 234 / Flat 359) / skip 906件
- 成長率目線: 平均log +0.000305 / 幾何平均 +0.030% per trade / maxDD +4.72%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ALLO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $126.64

## 4. Latest Market Context

- 更新: 2026-05-30T11:04:57.877912+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=73609.3
- Funnel: target 773 → liquid 131 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +58.64% | $1,012,876.70 |
| NFP/USDT:USDT | +38.95% | $2,939,065.36 |
| LAB/USDT:USDT | +28.33% | $123,691,324.85 |
| HEI/USDT:USDT | +27.89% | $18,033,148.65 |
| H/USDT:USDT | +24.97% | $2,434,131.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +1.31% | +1.32% |
| H/USDT:USDT | below_1h_threshold | +0.75% | +0.75% |
| ALLO/USDT:USDT | below_1h_threshold | +0.64% | +0.65% |
| BEAT/USDT:USDT | below_1h_threshold | +0.60% | +0.61% |
| BASED/USDT:USDT | below_1h_threshold | +0.49% | +0.49% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
