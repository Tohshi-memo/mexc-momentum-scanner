# Decision Report

- generated_at: 2026-09-12T21:46:19.367952+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14325**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.16% / filled 20/20。**
- 全期間 MARKET基準: n=14325, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.16% | **+1.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.16% | **+1.16%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.62% | **+0.56%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.43% | **+0.50%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| LIMIT_BB3S | 3/19 | 15.8% | +2.06% | **+0.32%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.26% | **+1.07%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.89% | **+0.67%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.37% | **+0.35%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.06% | **+0.04%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.03% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,080.43** / 初期 $100.00 (+980.43%)
- 確定: 5429件 (Win 1635 / Loss 1760 / Flat 2034) / skip 5457件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STORJ/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $1,080.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$212.71** / 初期 $100.00 (+112.71%)
- 確定: 2843件 (Win 784 / Loss 659 / Flat 1400) / skip 4893件
- 成長率目線: 平均log +0.000265 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1410 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LONGXIA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.52% 残高後 $212.71

## 5. Causal Adaptive DryRun ($100)

- 残高: **$124.17** / 初期 $100.00 (+24.17%)
- 確定: 2776件 (Win 822 / Loss 1067 / Flat 887) / pending 3件 / skip 3016件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000450 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LONGXIA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $124.17

## 6. Latest Market Context

- 更新: 2026-09-12T21:46:08.988191+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=77169.6
- Funnel: target 1068 → liquid 124 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STORJ/USDT:USDT | +28.39% | $23,703,805.50 |
| LONGXIA/USDT:USDT | +20.97% | $9,646,783.69 |
| REZ/USDT:USDT | +15.72% | $1,809,811.21 |
| RIVER/USDT:USDT | +12.29% | $15,072,454.65 |
| ILV/USDT:USDT | +11.33% | $1,149,946.06 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STORJ/USDT:USDT | below_1h_threshold | +4.68% | +4.63% |
| LONGXIA/USDT:USDT | below_1h_threshold | +3.42% | +3.37% |
| REZ/USDT:USDT | below_1h_threshold | +2.40% | +2.35% |
| RIVER/USDT:USDT | below_1h_threshold | +2.23% | +2.18% |
| ALCH/USDT:USDT | below_1h_threshold | +1.44% | +1.39% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
