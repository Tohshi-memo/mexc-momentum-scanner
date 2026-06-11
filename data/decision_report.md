# Decision Report

- generated_at: 2026-06-11T17:18:38.229129+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6381**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.49% / filled 20/20。**
- 全期間 MARKET基準: n=6381, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+0.49%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.49% | **+0.49%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.41% | **+0.60%** |
| ASK | 20/20 | 100.0% | +0.59% | **+0.59%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.56% | **+0.50%** |
| MARKET | 20/20 | 100.0% | +0.49% | **+0.49%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.52% | **+0.53%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +0.94% | **+0.38%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.31% | **+0.15%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +0.17% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$150.57** / 初期 $100.00 (+50.57%)
- 確定: 1298件 (Win 333 / Loss 413 / Flat 552) / skip 1644件
- 成長率目線: 平均log +0.000315 / 幾何平均 +0.032% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $150.57

## 4. Latest Market Context

- 更新: 2026-06-11T17:18:35.243377+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=62428.3
- Funnel: target 782 → liquid 154 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SKYAI/USDT:USDT | +11.78% | $10,076,567.66 |
| ESPORTS/USDT:USDT | +9.81% | $9,035,815.13 |
| VELVET/USDT:USDT | +6.66% | $93,035,879.29 |
| UB/USDT:USDT | +5.60% | $1,475,069.52 |
| ZBT/USDT:USDT | +5.38% | $1,125,319.83 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +4.22% | +4.41% |
| STG/USDT:USDT | below_1h_threshold | +3.93% | +4.12% |
| H/USDT:USDT | below_1h_threshold | +3.78% | +3.97% |
| SPACE/USDT:USDT | below_1h_threshold | +2.97% | +3.16% |
| VELVET/USDT:USDT | below_1h_threshold | +2.15% | +2.34% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
