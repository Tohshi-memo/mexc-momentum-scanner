# Decision Report

- generated_at: 2026-09-11T07:01:19.418706+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14203**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.42% / filled 20/20。**
- 全期間 MARKET基準: n=14203, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.42%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.42% | **+0.42%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.42% | **+0.42%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.21% | **+0.07%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.04% | **+0.02%** |
| LIMIT_ATR | 13/20 | 65.0% | -0.25% | **-0.16%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +1.61% | **+1.61%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.15% | **+0.86%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.91% | **+0.82%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +1.21% | **+0.18%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | -0.02% | **-0.01%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 208件 (TP 78 / SL 125 / EXP 5)
- 最新: EIGEN/USDT:USDT SL_HIT PnL -3.25% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,065.48** / 初期 $100.00 (+965.48%)
- 確定: 5369件 (Win 1615 / Loss 1736 / Flat 2018) / skip 5395件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RAY/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,065.48

## 4. Robust Adaptive DryRun ($100)

- 残高: **$208.23** / 初期 $100.00 (+108.23%)
- 確定: 2797件 (Win 768 / Loss 650 / Flat 1379) / skip 4817件
- 成長率目線: 平均log +0.000262 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0060 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $208.23

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.87** / 初期 $100.00 (+22.87%)
- 確定: 2706件 (Win 799 / Loss 1035 / Flat 872) / pending 3件 / skip 2964件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000183 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $122.87

## 6. Latest Market Context

- 更新: 2026-09-11T07:01:11.998964+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=77250.6
- Funnel: target 1068 → liquid 164 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIULAI/USDT:USDT | +39.69% | $11,282,407.47 |
| RAY/USDT:USDT | +25.12% | $14,562,071.06 |
| LSK/USDT:USDT | +22.14% | $1,424,077.24 |
| PONS/USDT:USDT | +20.13% | $8,736,098.23 |
| BTW/USDT:USDT | +13.12% | $3,478,007.10 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LSK/USDT:USDT | below_1h_threshold | +1.62% | +1.64% |
| FCXSTOCK/USDT:USDT | below_1h_threshold | +0.94% | +0.95% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +0.53% | +0.54% |
| VVV/USDT:USDT | below_1h_threshold | +0.49% | +0.50% |
| DOT/USDT:USDT | below_1h_threshold | +0.32% | +0.34% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
