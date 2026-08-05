# Decision Report

- generated_at: 2026-08-05T14:31:39.457831+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10411**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.35% / filled 20/20。**
- 全期間 MARKET基準: n=10411, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.35%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.35% | **+1.35%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 17/20 | 85.0% | +2.05% | **+1.74%** |
| MARKET | 20/20 | 100.0% | +1.35% | **+1.35%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.33% | **+1.26%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.38% | **+0.90%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.96% | **+0.74%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +4.53% | **+1.13%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +3.86% | **+0.96%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.03% | **+0.41%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.49% | **+0.22%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.24% | **+0.17%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$605.31** / 初期 $100.00 (+505.31%)
- 確定: 3769件 (Win 1195 / Loss 1236 / Flat 1338) / skip 3203件
- 成長率目線: 平均log +0.000478 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $605.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$143.45** / 初期 $100.00 (+43.45%)
- 確定: 1318件 (Win 373 / Loss 310 / Flat 635) / skip 2504件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0600 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CYS/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $143.45

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.15** / 初期 $100.00 (+18.15%)
- 確定: 1140件 (Win 365 / Loss 442 / Flat 333) / pending 2件 / skip 744件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000184 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $118.15

## 6. Latest Market Context

- 更新: 2026-08-05T14:06:24.217227+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.18% price=64499.8
- Funnel: target 948 → liquid 181 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.6 >= 65=1, 4h RSI 73.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +98.24% | $27,832,529.57 |
| BLESS/USDT:USDT | +87.14% | $60,937,162.61 |
| HFT/USDT:USDT | +83.41% | $4,227,255.77 |
| BICO/USDT:USDT | +30.03% | $16,275,206.17 |
| TAKE/USDT:USDT | +29.32% | $1,880,435.49 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DELLSTOCK/USDT:USDT | below_1h_threshold | +4.71% | +4.54% |
| AMGNSTOCK/USDT:USDT | below_1h_threshold | +4.54% | +4.36% |
| 1000RATS/USDT:USDT | below_1h_threshold | +2.89% | +2.72% |
| NVIDIA/USDT:USDT | below_1h_threshold | +2.79% | +2.61% |
| AALSTOCK/USDT:USDT | below_1h_threshold | +2.36% | +2.19% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
