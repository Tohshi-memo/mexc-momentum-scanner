# Decision Report

- generated_at: 2026-05-10T07:37:41.953496+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3950**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.91% / filled 20/20。**
- 全期間 MARKET基準: n=3950, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.91%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.91% | **+0.91%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.98% | **+0.98%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.96% | **+0.92%** |
| MARKET | 20/20 | 100.0% | +0.91% | **+0.91%** |
| LIMIT_7PCT | 6/20 | 30.0% | +1.67% | **+0.50%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.28% | **+1.28%** |
| ASK_LONG | 20/20 | 100.0% | +0.93% | **+0.93%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.80% | **+0.64%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.02% | **+0.41%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.36% | **+0.13%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.73** / 初期 $100.00 (+7.73%)
- 確定: 197件 (Win 48 / Loss 66 / Flat 83) / skip 314件
- 成長率目線: 平均log +0.000378 / 幾何平均 +0.038% per trade / maxDD +4.09%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAYER/USDT:USDT `LIMIT_5PCT_LONG` EXPIRED account +0.00% 残高後 $107.73

## 4. Latest Market Context

- 更新: 2026-05-10T07:37:38.576109+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=80735.9
- Funnel: target 769 → liquid 165 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.9 >= 65=1, 4h RSI 79.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TROLLSOL/USDT:USDT | +67.48% | $1,284,789.29 |
| LAYER/USDT:USDT | +45.32% | $4,853,724.71 |
| XEC/USDT:USDT | +29.76% | $1,716,123.90 |
| BAS/USDT:USDT | +17.18% | $1,124,415.84 |
| INX/USDT:USDT | +16.34% | $15,864,518.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAYER/USDT:USDT | below_1h_threshold | +4.46% | +4.42% |
| LAB/USDT:USDT | below_1h_threshold | +3.35% | +3.30% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +2.37% | +2.32% |
| XEC/USDT:USDT | below_1h_threshold | +1.98% | +1.93% |
| UNI/USDT:USDT | below_1h_threshold | +1.96% | +1.92% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
