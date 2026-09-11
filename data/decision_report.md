# Decision Report

- generated_at: 2026-09-11T04:41:18.467859+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14200**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14200, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.34% | **-0.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.21% | **+0.07%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.03% | **+0.02%** |
| MARKET | 20/20 | 100.0% | -0.34% | **-0.34%** |
| LIMIT_ATR | 14/20 | 70.0% | -0.57% | **-0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.32% | **+1.19%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.56% | **+1.17%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.71% | **+1.11%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.69% | **+0.93%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +0.50% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 208件 (TP 78 / SL 125 / EXP 5)
- 最新: EIGEN/USDT:USDT SL_HIT PnL -3.25% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,070.84** / 初期 $100.00 (+970.84%)
- 確定: 5368件 (Win 1615 / Loss 1735 / Flat 2018) / skip 5393件
- 成長率目線: 平均log +0.000442 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PONS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $1,070.84

## 4. Robust Adaptive DryRun ($100)

- 残高: **$208.23** / 初期 $100.00 (+108.23%)
- 確定: 2794件 (Win 768 / Loss 650 / Flat 1376) / skip 4817件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0140 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RAY/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $208.23

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.32** / 初期 $100.00 (+23.32%)
- 確定: 2703件 (Win 799 / Loss 1032 / Flat 872) / pending 4件 / skip 2964件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000235 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: RAY/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $123.32

## 6. Latest Market Context

- 更新: 2026-09-11T04:41:10.160281+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.29% price=77079.8
- Funnel: target 1066 → liquid 170 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIULAI/USDT:USDT | +45.74% | $9,505,937.89 |
| RAY/USDT:USDT | +31.87% | $9,818,270.46 |
| CNPY/USDT:USDT | +15.98% | $2,730,474.14 |
| PONS/USDT:USDT | +15.72% | $8,468,643.33 |
| BTW/USDT:USDT | +11.46% | $3,316,790.51 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JUP/USDT:USDT | below_1h_threshold | +3.16% | +2.87% |
| XMR/USDT:USDT | below_1h_threshold | +3.14% | +2.86% |
| RUNE/USDT:USDT | below_1h_threshold | +2.59% | +2.30% |
| VVV/USDT:USDT | below_1h_threshold | +2.48% | +2.19% |
| HNT/USDT:USDT | below_1h_threshold | +2.45% | +2.16% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
