# Decision Report

- generated_at: 2026-10-28T02:26:27.984956+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17668**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.05% / filled 20/20。**
- 全期間 MARKET基準: n=17668, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.05% | **+2.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.05% | **+2.05%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.75% | **+1.48%** |
| LIMIT_ATR | 9/20 | 45.0% | +1.81% | **+0.81%** |
| LIMIT_3PCT | 10/20 | 50.0% | +1.51% | **+0.76%** |
| LIMIT_2PCT | 13/20 | 65.0% | +1.12% | **+0.73%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +4.00% | **+2.00%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +2.55% | **+1.28%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +1.12% | **+1.12%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |
| LIMIT_5PCT_LONG | 14/20 | 70.0% | +0.20% | **+0.14%** |

## 2. $100 Live Portfolio

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定トレード: 255件 (TP 94 / SL 153 / EXP 8)
- 最新: BTW/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.62
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,532.91** / 初期 $100.00 (+1432.91%)
- 確定: 6760件 (Win 1968 / Loss 2170 / Flat 2622) / skip 7469件
- 成長率目線: 平均log +0.000404 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BULLA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,532.91

## 4. Robust Adaptive DryRun ($100)

- 残高: **$353.54** / 初期 $100.00 (+253.54%)
- 確定: 4197件 (Win 1142 / Loss 965 / Flat 2090) / skip 6882件
- 成長率目線: 平均log +0.000301 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.1138 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PEPE/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $353.54

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5829件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000260 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-28T02:26:13.007568+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=80928.3
- Funnel: target 1083 → liquid 160 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SI/USDT:USDT | +33.57% | $1,178,535.90 |
| BULLA/USDT:USDT | +30.70% | $10,355,410.19 |
| APR/USDT:USDT | +29.65% | $5,802,352.18 |
| EVAA/USDT:USDT | +25.79% | $4,625,113.32 |
| PONS/USDT:USDT | +14.06% | $1,960,600.12 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +3.95% | +3.93% |
| BEAT/USDT:USDT | below_1h_threshold | +2.62% | +2.60% |
| UNITREE/USDT:USDT | below_1h_threshold | +2.48% | +2.46% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +2.39% | +2.37% |
| KORU/USDT:USDT | below_1h_threshold | +2.20% | +2.18% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
