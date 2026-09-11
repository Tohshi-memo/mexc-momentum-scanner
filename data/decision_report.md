# Decision Report

- generated_at: 2026-09-11T16:31:19.854751+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14236**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.24% / filled 20/20。**
- 全期間 MARKET基準: n=14236, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.24% | **+0.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_BB3S | 3/15 | 20.0% | +1.66% | **+0.33%** |
| LIMIT_5PCT | 5/20 | 25.0% | +1.03% | **+0.26%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.85% | **+0.26%** |
| MARKET | 20/20 | 100.0% | +0.24% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +3.71% | **+2.97%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.07% | **+0.48%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.76% | **+0.46%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.47% | **+0.33%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.37% | **+0.17%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 209件 (TP 78 / SL 126 / EXP 5)
- 最新: RIVER/USDT:USDT SL_HIT PnL -3.59% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,070.23** / 初期 $100.00 (+970.23%)
- 確定: 5394件 (Win 1624 / Loss 1746 / Flat 2024) / skip 5403件
- 成長率目線: 平均log +0.000439 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RIVER/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.68% 残高後 $1,070.23

## 4. Robust Adaptive DryRun ($100)

- 残高: **$206.69** / 初期 $100.00 (+106.69%)
- 確定: 2812件 (Win 771 / Loss 654 / Flat 1387) / skip 4835件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0009 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RIVER/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.52% 残高後 $206.69

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.06** / 初期 $100.00 (+23.06%)
- 確定: 2731件 (Win 807 / Loss 1047 / Flat 877) / pending 6件 / skip 2975件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000158 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $123.06

## 6. Latest Market Context

- 更新: 2026-09-11T16:31:10.265096+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=77648.0
- Funnel: target 1067 → liquid 160 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RIVER/USDT:USDT | +5.04% | $2,357,802.85 |
| STORJ/USDT:USDT | +3.68% | $5,828,380.23 |
| MET/USDT:USDT | +2.53% | $1,622,959.79 |
| POL/USDT:USDT | +2.21% | $4,515,287.04 |
| LAB/USDT:USDT | +1.90% | $3,706,634.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STORJ/USDT:USDT | below_1h_threshold | +3.68% | +3.74% |
| MET/USDT:USDT | below_1h_threshold | +2.53% | +2.59% |
| POL/USDT:USDT | below_1h_threshold | +2.18% | +2.24% |
| LAB/USDT:USDT | below_1h_threshold | +1.98% | +2.04% |
| LSK/USDT:USDT | below_1h_threshold | +1.81% | +1.87% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
