# Decision Report

- generated_at: 2026-09-12T20:26:15.268375+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14321**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.25% / filled 20/20。**
- 全期間 MARKET基準: n=14321, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.25%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.25% | **+0.25%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 8/20 | 40.0% | +2.25% | **+0.90%** |
| LIMIT_BB3S | 4/19 | 21.1% | +3.54% | **+0.75%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.59% | **+0.47%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.43% | **+0.41%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.70% | **+1.36%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.32% | **+1.26%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.24% | **+0.87%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.28% | **+0.15%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,080.43** / 初期 $100.00 (+980.43%)
- 確定: 5429件 (Win 1635 / Loss 1760 / Flat 2034) / skip 5453件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STORJ/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $1,080.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$211.99** / 初期 $100.00 (+111.99%)
- 確定: 2839件 (Win 782 / Loss 657 / Flat 1400) / skip 4893件
- 成長率目線: 平均log +0.000265 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1370 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $211.99

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.96** / 初期 $100.00 (+23.96%)
- 確定: 2772件 (Win 820 / Loss 1065 / Flat 887) / pending 5件 / skip 3016件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000453 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $123.96

## 6. Latest Market Context

- 更新: 2026-09-12T20:26:08.076798+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=77139.7
- Funnel: target 1068 → liquid 122 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STORJ/USDT:USDT | +24.70% | $24,890,426.29 |
| LONGXIA/USDT:USDT | +19.21% | $9,357,068.12 |
| RIVER/USDT:USDT | +12.45% | $14,239,424.09 |
| REZ/USDT:USDT | +10.38% | $1,516,055.34 |
| AKE/USDT:USDT | +6.95% | $3,364,542.83 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VVV/USDT:USDT | below_1h_threshold | +1.16% | +1.09% |
| XMR/USDT:USDT | below_1h_threshold | +1.08% | +1.01% |
| ABNBSTOCK/USDT:USDT | below_1h_threshold | +0.97% | +0.90% |
| PENDLE/USDT:USDT | below_1h_threshold | +0.90% | +0.83% |
| UAI/USDT:USDT | below_1h_threshold | +0.73% | +0.66% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
