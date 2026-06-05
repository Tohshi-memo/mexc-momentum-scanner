# Decision Report

- generated_at: 2026-06-05T01:41:52.141238+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5691**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.75% / filled 20/20。**
- 全期間 MARKET基準: n=5691, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.75%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.75% | **+0.75%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.91% | **+0.91%** |
| MARKET | 20/20 | 100.0% | +0.75% | **+0.75%** |
| LIMIT_BB3S | 4/18 | 22.2% | +1.87% | **+0.42%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.45% | **+0.40%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.30% | **+0.97%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.24% | **+0.87%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.67% | **+0.80%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +1.09% | **+0.71%** |

## 2. $100 Live Portfolio

- 残高: **$98.05** / 初期 $100.00 (-1.95%)
- 確定トレード: 99件 (TP 30 / SL 66 / EXP 3)
- 最新: MONAD/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.05
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.20** / 初期 $100.00 (+31.20%)
- 確定: 1008件 (Win 239 / Loss 312 / Flat 457) / skip 1244件
- 成長率目線: 平均log +0.000269 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: OPN/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $131.20

## 4. Latest Market Context

- 更新: 2026-06-05T01:41:49.090331+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=63327.1
- Funnel: target 772 → liquid 164 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 96.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +84.64% | $11,943,013.85 |
| HOME/USDT:USDT | +28.47% | $7,549,744.35 |
| OPN/USDT:USDT | +15.14% | $36,883,324.90 |
| AAOISTOCK/USDT:USDT | +9.93% | $1,298,631.34 |
| HEI/USDT:USDT | +9.79% | $5,338,809.26 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +3.36% | +3.48% |
| RIVER/USDT:USDT | below_1h_threshold | +3.28% | +3.39% |
| HEI/USDT:USDT | below_1h_threshold | +3.18% | +3.29% |
| MONAD/USDT:USDT | below_1h_threshold | +2.68% | +2.79% |
| OPG/USDT:USDT | below_1h_threshold | +2.64% | +2.75% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
