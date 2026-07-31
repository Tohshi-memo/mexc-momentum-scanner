# Decision Report

- generated_at: 2026-07-31T11:11:18.345206+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9993**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.75% / filled 20/20。**
- 全期間 MARKET基準: n=9993, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.75%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.75% | **+0.75%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/15 | 40.0% | +2.60% | **+1.04%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.95% | **+0.76%** |
| MARKET | 20/20 | 100.0% | +0.75% | **+0.75%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.32% | **+0.25%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.30% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.26% | **+1.02%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +6.07% | **+0.91%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.09% | **+0.87%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.67% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$547.70** / 初期 $100.00 (+447.70%)
- 確定: 3573件 (Win 1141 / Loss 1168 / Flat 1264) / skip 2981件
- 成長率目線: 平均log +0.000476 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $547.70

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.81** / 初期 $100.00 (+40.81%)
- 確定: 1278件 (Win 359 / Loss 297 / Flat 622) / skip 2126件
- 成長率目線: 平均log +0.000268 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0679 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MMT/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $140.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$111.31** / 初期 $100.00 (+11.31%)
- 確定: 826件 (Win 269 / Loss 328 / Flat 229) / pending 4件 / skip 635件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000321 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MMT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $111.31

## 6. Latest Market Context

- 更新: 2026-07-31T11:11:09.997219+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=63893.8
- Funnel: target 921 → liquid 173 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KOMA/USDT:USDT | +73.55% | $12,712,440.43 |
| MMT/USDT:USDT | +43.48% | $20,764,088.17 |
| AXTISTOCK/USDT:USDT | +34.78% | $5,375,252.80 |
| GIGGLE/USDT:USDT | +32.29% | $9,366,982.58 |
| BULLA/USDT:USDT | +22.21% | $1,626,470.73 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KIOXIASTOCK/USDT:USDT | below_1h_threshold | +4.97% | +4.95% |
| DEXE/USDT:USDT | below_1h_threshold | +4.08% | +4.07% |
| ETNSTOCK/USDT:USDT | below_1h_threshold | +3.74% | +3.72% |
| SNXX/USDT:USDT | below_1h_threshold | +2.33% | +2.32% |
| KOMA/USDT:USDT | below_1h_threshold | +2.00% | +1.98% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
