# Decision Report

- generated_at: 2026-09-11T05:41:07.180966+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14202**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14202, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.04%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.04% | **-0.04%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.21% | **+0.07%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.04% | **+0.02%** |
| MARKET | 20/20 | 100.0% | -0.04% | **-0.04%** |
| LIMIT_ATR | 14/20 | 70.0% | -0.30% | **-0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +1.61% | **+1.61%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.82% | **+1.37%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.41% | **+1.27%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.91% | **+0.59%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.05% | **+0.58%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 208件 (TP 78 / SL 125 / EXP 5)
- 最新: EIGEN/USDT:USDT SL_HIT PnL -3.25% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,065.48** / 初期 $100.00 (+965.48%)
- 確定: 5369件 (Win 1615 / Loss 1736 / Flat 2018) / skip 5394件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RAY/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,065.48

## 4. Robust Adaptive DryRun ($100)

- 残高: **$208.23** / 初期 $100.00 (+108.23%)
- 確定: 2796件 (Win 768 / Loss 650 / Flat 1378) / skip 4817件
- 成長率目線: 平均log +0.000262 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0063 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RAY/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $208.23

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.09** / 初期 $100.00 (+23.09%)
- 確定: 2705件 (Win 799 / Loss 1034 / Flat 872) / pending 2件 / skip 2964件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000202 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: RAY/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $123.09

## 6. Latest Market Context

- 更新: 2026-09-11T05:40:59.541653+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=77118.3
- Funnel: target 1066 → liquid 171 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIULAI/USDT:USDT | +34.36% | $10,559,884.51 |
| RAY/USDT:USDT | +22.38% | $12,647,265.65 |
| PONS/USDT:USDT | +16.58% | $8,628,909.77 |
| CNPY/USDT:USDT | +15.59% | $2,741,321.86 |
| BTW/USDT:USDT | +10.48% | $3,470,975.41 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PONS/USDT:USDT | below_1h_threshold | +2.16% | +2.10% |
| RUNE/USDT:USDT | below_1h_threshold | +1.63% | +1.58% |
| CNPY/USDT:USDT | below_1h_threshold | +1.53% | +1.47% |
| BTR/USDT:USDT | below_1h_threshold | +0.91% | +0.86% |
| HNT/USDT:USDT | below_1h_threshold | +0.87% | +0.82% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
