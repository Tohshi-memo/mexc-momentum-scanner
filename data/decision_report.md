# Decision Report

- generated_at: 2026-05-15T01:23:31.201663+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4316**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.36% / filled 20/20。**
- 全期間 MARKET基準: n=4316, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=+1.36%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.36% | **+1.36%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/14 | 35.7% | +4.35% | **+1.55%** |
| ASK | 20/20 | 100.0% | +1.42% | **+1.42%** |
| MARKET | 20/20 | 100.0% | +1.36% | **+1.36%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.72% | **+0.50%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.54% | **+0.43%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/6 | 83.3% | +2.52% | **+2.10%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +1.11% | **+0.28%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +0.50% | **+0.25%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.22% | **+0.08%** |

## 2. $100 Live Portfolio

- 残高: **$96.24** / 初期 $100.00 (-3.76%)
- 確定トレード: 43件 (TP 10 / SL 30 / EXP 3)
- 最新: PLAY/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.24
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.46** / 初期 $100.00 (+20.46%)
- 確定: 368件 (Win 96 / Loss 130 / Flat 142) / skip 509件
- 成長率目線: 平均log +0.000506 / 幾何平均 +0.051% per trade / maxDD +4.21%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIN/USDT:USDT `LIMIT_BB3S` EXPIRED account +0.00% 残高後 $120.46

## 4. Latest Market Context

- 更新: 2026-05-15T01:23:27.963402+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=81402.4
- Funnel: target 760 → liquid 166 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PEAQ/USDT:USDT | +22.75% | $1,960,555.74 |
| GWEI/USDT:USDT | +19.33% | $1,012,468.64 |
| UP/USDT:USDT | +19.11% | $3,775,212.77 |
| TAC/USDT:USDT | +17.90% | $1,919,773.52 |
| FIGSTOCK/USDT:USDT | +14.45% | $3,029,462.76 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PEAQ/USDT:USDT | below_1h_threshold | +3.39% | +3.48% |
| BILL/USDT:USDT | below_1h_threshold | +1.92% | +2.01% |
| GUA/USDT:USDT | below_1h_threshold | +1.63% | +1.72% |
| ASTEROID/USDT:USDT | below_1h_threshold | +1.62% | +1.71% |
| BB/USDT:USDT | below_1h_threshold | +1.29% | +1.38% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
