# Decision Report

- generated_at: 2026-07-31T11:01:20.651354+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9992**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.75% / filled 20/20。**
- 全期間 MARKET基準: n=9992, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.75%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.75% | **+0.75%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.75% | **+0.75%** |
| LIMIT_BB3S | 5/15 | 33.3% | +1.52% | **+0.51%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.48% | **+0.36%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | -0.01% | **-0.00%** |
| LIMIT_1PCT | 15/20 | 75.0% | -0.20% | **-0.15%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +6.07% | **+0.91%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.09% | **+0.87%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.87% | **+0.84%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.35% | **+0.67%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$547.70** / 初期 $100.00 (+447.70%)
- 確定: 3573件 (Win 1141 / Loss 1168 / Flat 1264) / skip 2980件
- 成長率目線: 平均log +0.000476 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $547.70

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.81** / 初期 $100.00 (+40.81%)
- 確定: 1278件 (Win 359 / Loss 297 / Flat 622) / skip 2125件
- 成長率目線: 平均log +0.000268 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0897 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MMT/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $140.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$111.51** / 初期 $100.00 (+11.51%)
- 確定: 825件 (Win 269 / Loss 327 / Flat 229) / pending 5件 / skip 635件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000328 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CAP/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $111.51

## 6. Latest Market Context

- 更新: 2026-07-31T11:01:11.917325+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=63893.7
- Funnel: target 921 → liquid 173 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KOMA/USDT:USDT | +70.92% | $12,565,386.87 |
| MMT/USDT:USDT | +55.24% | $19,816,894.39 |
| AXTISTOCK/USDT:USDT | +34.30% | $5,320,106.95 |
| GIGGLE/USDT:USDT | +32.91% | $9,291,270.09 |
| BULLA/USDT:USDT | +22.40% | $1,600,874.57 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KIOXIASTOCK/USDT:USDT | below_1h_threshold | +4.97% | +4.96% |
| ETNSTOCK/USDT:USDT | below_1h_threshold | +3.74% | +3.72% |
| SNXX/USDT:USDT | below_1h_threshold | +2.33% | +2.32% |
| MUU/USDT:USDT | below_1h_threshold | +1.65% | +1.64% |
| AXTISTOCK/USDT:USDT | below_1h_threshold | +1.37% | +1.36% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
