# Decision Report

- generated_at: 2026-09-03T08:06:27.322358+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13459**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13459, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +0.11% | **+0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +3.39% | **+3.39%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.40% | **+1.33%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.45% | **+0.80%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.99% | **+0.59%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.72% | **+0.54%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 199件 (TP 74 / SL 120 / EXP 5)
- 最新: MARSCOIN/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$859.66** / 初期 $100.00 (+759.66%)
- 確定: 5008件 (Win 1516 / Loss 1644 / Flat 1848) / skip 5012件
- 成長率目線: 平均log +0.000430 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BONER/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.36% 残高後 $859.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$184.60** / 初期 $100.00 (+84.60%)
- 確定: 2372件 (Win 671 / Loss 576 / Flat 1125) / skip 4498件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1132 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $184.60

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.01** / 初期 $100.00 (+14.01%)
- 確定: 2154件 (Win 634 / Loss 846 / Flat 674) / pending 2件 / skip 2773件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000313 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $114.01

## 6. Latest Market Context

- 更新: 2026-09-03T08:06:17.095335+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.43% price=77952.6
- Funnel: target 1046 → liquid 152 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MARSCOIN/USDT:USDT | +95.82% | $5,744,516.44 |
| EDGE/USDT:USDT | +42.43% | $3,247,302.70 |
| BR/USDT:USDT | +28.51% | $1,098,584.03 |
| NIULAI/USDT:USDT | +25.87% | $2,256,098.51 |
| CHIP/USDT:USDT | +24.70% | $4,780,546.08 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIULAI/USDT:USDT | below_1h_threshold | +2.41% | +1.99% |
| CHIP/USDT:USDT | below_1h_threshold | +2.22% | +1.79% |
| BR/USDT:USDT | below_1h_threshold | +1.12% | +0.69% |
| XPL/USDT:USDT | below_1h_threshold | +0.94% | +0.52% |
| SUI/USDT:USDT | below_1h_threshold | +0.90% | +0.47% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
