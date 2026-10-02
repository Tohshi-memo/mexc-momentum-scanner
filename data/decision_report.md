# Decision Report

- generated_at: 2026-10-02T16:51:33.586953+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16012**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.57% / filled 20/20。**
- 全期間 MARKET基準: n=16012, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.57%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.57% | **+0.57%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +1.93% | **+0.77%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +4.82% | **+0.72%** |
| MARKET | 20/20 | 100.0% | +0.57% | **+0.57%** |
| LIMIT_ATR | 11/20 | 55.0% | +0.92% | **+0.51%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.60% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.33% | **+0.30%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.39% | **+0.24%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | -0.01% | **-0.01%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | -0.10% | **-0.03%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -0.89% | **-0.09%** |

## 2. $100 Live Portfolio

- 残高: **$120.27** / 初期 $100.00 (+20.27%)
- 確定トレード: 229件 (TP 82 / SL 140 / EXP 7)
- 最新: SI/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.27
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,342.32** / 初期 $100.00 (+1242.32%)
- 確定: 6117件 (Win 1807 / Loss 1960 / Flat 2350) / skip 6456件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VVV/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,342.32

## 4. Robust Adaptive DryRun ($100)

- 残高: **$275.42** / 初期 $100.00 (+175.42%)
- 確定: 3605件 (Win 1005 / Loss 844 / Flat 1756) / skip 5818件
- 成長率目線: 平均log +0.000281 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0341 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $275.42

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4174件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000149 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-02T16:51:21.936497+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=85220.1
- Funnel: target 1099 → liquid 173 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LONGXIA/USDT:USDT | +12.15% | $17,487,460.99 |
| MAGMA/USDT:USDT | +3.24% | $3,766,039.80 |
| NIGHT/USDT:USDT | +2.78% | $7,914,819.29 |
| BR/USDT:USDT | +2.68% | $3,377,449.63 |
| SUPER/USDT:USDT | +2.25% | $1,312,130.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MAGMA/USDT:USDT | below_1h_threshold | +3.10% | +3.19% |
| NIGHT/USDT:USDT | below_1h_threshold | +2.81% | +2.90% |
| BR/USDT:USDT | below_1h_threshold | +2.64% | +2.73% |
| SUPER/USDT:USDT | below_1h_threshold | +2.26% | +2.35% |
| GALA/USDT:USDT | below_1h_threshold | +1.58% | +1.67% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
