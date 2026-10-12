# Decision Report

- generated_at: 2026-10-12T12:06:23.725360+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16600**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.23% / filled 20/20。**
- 全期間 MARKET基準: n=16600, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.23% | **+0.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.31% | **+0.59%** |
| MARKET | 20/20 | 100.0% | +0.23% | **+0.23%** |
| LIMIT_5PCT | 4/20 | 20.0% | -1.52% | **-0.30%** |
| LIMIT_6PCT | 3/20 | 15.0% | -2.04% | **-0.31%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.12% | **+0.78%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.11% | **+0.72%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.59% | **+0.64%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.66% | **+0.50%** |

## 2. $100 Live Portfolio

- 残高: **$121.72** / 初期 $100.00 (+21.72%)
- 確定トレード: 238件 (TP 89 / SL 142 / EXP 7)
- 最新: BATON/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.72
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,291.75** / 初期 $100.00 (+1191.75%)
- 確定: 6291件 (Win 1845 / Loss 2016 / Flat 2430) / skip 6870件
- 成長率目線: 平均log +0.000407 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RSR/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $1,291.75

## 4. Robust Adaptive DryRun ($100)

- 残高: **$272.12** / 初期 $100.00 (+172.12%)
- 確定: 3639件 (Win 1010 / Loss 855 / Flat 1774) / skip 6372件
- 成長率目線: 平均log +0.000275 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RSR/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $272.12

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4758件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000180 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-12T12:06:12.038541+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=83300.0
- Funnel: target 1089 → liquid 157 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RSR/USDT:USDT | +53.99% | $8,855,169.65 |
| W/USDT:USDT | +46.39% | $39,747,643.96 |
| BATON/USDT:USDT | +24.03% | $3,940,036.74 |
| PYTH/USDT:USDT | +15.30% | $6,696,988.61 |
| ZRO/USDT:USDT | +13.70% | $25,066,104.11 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RSR/USDT:USDT | below_1h_threshold | +4.15% | +4.22% |
| BATON/USDT:USDT | below_1h_threshold | +1.84% | +1.91% |
| SOXS/USDT:USDT | below_1h_threshold | +0.99% | +1.06% |
| PLUME/USDT:USDT | below_1h_threshold | +0.96% | +1.03% |
| MAGIC/USDT:USDT | below_1h_threshold | +0.96% | +1.03% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
