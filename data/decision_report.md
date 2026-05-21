# Decision Report

- generated_at: 2026-05-21T13:08:59.216213+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4628**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.59% / filled 20/20。**
- 全期間 MARKET基準: n=4628, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=+0.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.59% | **+0.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/18 | 33.3% | +3.04% | **+1.01%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.68% | **+0.65%** |
| MARKET | 20/20 | 100.0% | +0.59% | **+0.59%** |
| LIMIT_5PCT | 4/20 | 20.0% | +2.71% | **+0.54%** |
| ASK | 20/20 | 100.0% | +0.45% | **+0.45%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.16% | **+0.40%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.53% | **+0.26%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +0.42% | **+0.17%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.23% | **+0.08%** |
| MARKET_LONG | 20/20 | 100.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$95.73** / 初期 $100.00 (-4.27%)
- 確定トレード: 59件 (TP 15 / SL 41 / EXP 3)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.73
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定: 546件 (Win 138 / Loss 185 / Flat 223) / skip 643件
- 成長率目線: 平均log +0.000355 / 幾何平均 +0.036% per trade / maxDD +4.21%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PROVE/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $121.41

## 4. Latest Market Context

- 更新: 2026-05-21T13:08:56.822990+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=77299.2
- Funnel: target 766 → liquid 135 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EDEN/USDT:USDT | +45.43% | $32,598,181.54 |
| PROVE/USDT:USDT | +42.57% | $5,985,055.94 |
| NEX/USDT:USDT | +42.55% | $1,092,194.09 |
| FIDA/USDT:USDT | +38.77% | $13,381,979.03 |
| ROAM/USDT:USDT | +31.69% | $2,277,721.56 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +3.89% | +3.81% |
| FIDA/USDT:USDT | below_1h_threshold | +1.39% | +1.32% |
| BEAT/USDT:USDT | below_1h_threshold | +0.89% | +0.82% |
| PYTH/USDT:USDT | below_1h_threshold | +0.75% | +0.68% |
| LIT/USDT:USDT | below_1h_threshold | +0.67% | +0.60% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
