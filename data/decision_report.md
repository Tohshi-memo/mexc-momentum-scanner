# Decision Report

- generated_at: 2026-05-28T13:14:36.657388+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4960**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.32% / filled 20/20。**
- 全期間 MARKET基準: n=4960, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+1.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.32% | **+1.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 16/20 | 80.0% | +1.82% | **+1.45%** |
| ASK | 20/20 | 100.0% | +1.35% | **+1.35%** |
| MARKET | 20/20 | 100.0% | +1.32% | **+1.32%** |
| LIMIT_3PCT | 14/20 | 70.0% | +1.70% | **+1.19%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.35% | **+1.15%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.34% | **+0.23%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.16% | **+0.23%** |
| LIMIT_BB3S_LONG | 3/6 | 50.0% | +0.46% | **+0.23%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.04% | **+0.01%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | -0.69% | **-0.27%** |

## 2. $100 Live Portfolio

- 残高: **$97.63** / 初期 $100.00 (-2.37%)
- 確定トレード: 70件 (TP 20 / SL 47 / EXP 3)
- 最新: PRL/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.63
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$126.79** / 初期 $100.00 (+26.79%)
- 確定: 695件 (Win 172 / Loss 220 / Flat 303) / skip 826件
- 成長率目線: 平均log +0.000342 / 幾何平均 +0.034% per trade / maxDD +4.72%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: XLM/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $126.79

## 4. Latest Market Context

- 更新: 2026-05-28T13:14:34.458727+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.23% price=73328.3
- Funnel: target 777 → liquid 154 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SNOWSTOCK/USDT:USDT | +34.97% | $9,881,848.30 |
| XLM/USDT:USDT | +19.64% | $157,880,123.10 |
| PRL/USDT:USDT | +15.02% | $2,356,351.98 |
| NBISSTOCK/USDT:USDT | +13.14% | $2,080,794.39 |
| ONDSSTOCK/USDT:USDT | +12.30% | $1,104,149.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +2.81% | +3.04% |
| BEAT/USDT:USDT | below_1h_threshold | +2.05% | +2.28% |
| XLM/USDT:USDT | below_1h_threshold | +1.85% | +2.08% |
| FUTUSTOCK/USDT:USDT | below_1h_threshold | +0.93% | +1.16% |
| MYX/USDT:USDT | below_1h_threshold | +0.85% | +1.08% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
