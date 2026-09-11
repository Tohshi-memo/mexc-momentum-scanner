# Decision Report

- generated_at: 2026-09-11T18:26:30.685706+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14245**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.82% / filled 20/20。**
- 全期間 MARKET基準: n=14245, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.82%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.82% | **+0.82%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.82% | **+0.82%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +2.02% | **+0.40%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.01% | **+0.35%** |
| LIMIT_4PCT | 10/20 | 50.0% | +0.04% | **+0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +5.88% | **+3.92%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.31% | **+1.11%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.29% | **+1.04%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.51% | **+0.33%** |
| MARKET_LONG | 20/20 | 100.0% | +0.26% | **+0.26%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 210件 (TP 78 / SL 127 / EXP 5)
- 最新: LAB/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,109.43** / 初期 $100.00 (+1009.43%)
- 確定: 5402件 (Win 1630 / Loss 1748 / Flat 2024) / skip 5404件
- 成長率目線: 平均log +0.000445 / 幾何平均 +0.045% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $1,109.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$209.84** / 初期 $100.00 (+109.84%)
- 確定: 2818件 (Win 775 / Loss 655 / Flat 1388) / skip 4838件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0037 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UAI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $209.84

## 5. Causal Adaptive DryRun ($100)

- 残高: **$124.01** / 初期 $100.00 (+24.01%)
- 確定: 2737件 (Win 811 / Loss 1049 / Flat 877) / pending 5件 / skip 2976件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000295 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $124.01

## 6. Latest Market Context

- 更新: 2026-09-11T18:26:17.765160+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.46% price=77135.6
- Funnel: target 1067 → liquid 161 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.4 >= 65=1, 4h RSI 84.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +26.03% | $5,807,654.02 |
| STORJ/USDT:USDT | +24.02% | $7,137,354.15 |
| BEAT/USDT:USDT | +13.24% | $8,181,725.62 |
| RIVER/USDT:USDT | +2.52% | $3,123,011.01 |
| HNT/USDT:USDT | +2.35% | $1,896,687.22 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RIVER/USDT:USDT | below_1h_threshold | +2.28% | +2.74% |
| MET/USDT:USDT | below_1h_threshold | +1.87% | +2.33% |
| FOLKS/USDT:USDT | below_1h_threshold | +1.14% | +1.60% |
| SOPH/USDT:USDT | below_1h_threshold | +0.98% | +1.44% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +0.75% | +1.21% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
