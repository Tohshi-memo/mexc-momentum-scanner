# Decision Report

- generated_at: 2026-05-29T13:49:46.526088+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5050**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.28% / filled 20/20。**
- 全期間 MARKET基準: n=5050, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+0.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.28% | **+0.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.34% | **+0.47%** |
| ASK | 20/20 | 100.0% | +0.37% | **+0.37%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.36% | **+0.31%** |
| MARKET | 20/20 | 100.0% | +0.28% | **+0.28%** |
| LIMIT_1PCT | 18/20 | 90.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/6 | 50.0% | +3.87% | **+1.94%** |
| MARKET_LONG | 20/20 | 100.0% | +1.27% | **+1.27%** |
| ASK_LONG | 20/20 | 100.0% | +1.09% | **+1.09%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.65% | **+0.49%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$99.09** / 初期 $100.00 (-0.91%)
- 確定トレード: 73件 (TP 22 / SL 48 / EXP 3)
- 最新: NIL/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.09
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.68** / 初期 $100.00 (+25.68%)
- 確定: 740件 (Win 175 / Loss 226 / Flat 339) / skip 871件
- 成長率目線: 平均log +0.000309 / 幾何平均 +0.031% per trade / maxDD +4.72%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CTR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $125.68

## 4. Latest Market Context

- 更新: 2026-05-29T13:49:43.794372+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=73182.9
- Funnel: target 777 → liquid 151 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 92.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ALLO/USDT:USDT | +133.37% | $112,779,789.44 |
| HEI/USDT:USDT | +99.29% | $1,784,282.47 |
| ID/USDT:USDT | +34.86% | $2,403,612.64 |
| DELLSTOCK/USDT:USDT | +30.86% | $10,726,202.28 |
| LAB/USDT:USDT | +28.78% | $90,061,611.34 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PANWSTOCK/USDT:USDT | below_1h_threshold | +3.83% | +3.94% |
| PRL/USDT:USDT | below_1h_threshold | +3.61% | +3.72% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +2.97% | +3.07% |
| ORCLSTOCK/USDT:USDT | below_1h_threshold | +2.14% | +2.25% |
| LIT/USDT:USDT | below_1h_threshold | +1.93% | +2.03% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
