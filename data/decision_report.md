# Decision Report

- generated_at: 2026-09-15T16:06:25.730575+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14600**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14600, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.89%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.89% | **-0.89%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.38% | **+0.26%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.16% | **+0.97%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.95% | **+0.88%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.05% | **+0.58%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +1.92% | **+0.48%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +0.94% | **+0.47%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,067.64** / 初期 $100.00 (+967.64%)
- 確定: 5502件 (Win 1643 / Loss 1778 / Flat 2081) / skip 5659件
- 成長率目線: 平均log +0.000430 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DELLSTOCK/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $1,067.64

## 4. Robust Adaptive DryRun ($100)

- 残高: **$231.07** / 初期 $100.00 (+131.07%)
- 確定: 3040件 (Win 838 / Loss 718 / Flat 1484) / skip 4971件
- 成長率目線: 平均log +0.000276 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DELLSTOCK/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $231.07

## 5. Causal Adaptive DryRun ($100)

- 残高: **$124.11** / 初期 $100.00 (+24.11%)
- 確定: 2909件 (Win 863 / Loss 1133 / Flat 913) / pending 0件 / skip 3166件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000102 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: POWR/USDT:USDT `MARKET` EXPIRED account +0.10% 残高後 $124.11

## 6. Latest Market Context

- 更新: 2026-09-15T16:06:16.733444+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=76435.3
- Funnel: target 1060 → liquid 156 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LSK/USDT:USDT | +2.66% | $22,141,491.40 |
| AKE/USDT:USDT | +2.63% | $22,278,320.42 |
| BONER/USDT:USDT | +2.08% | $1,054,721.86 |
| BTW/USDT:USDT | +1.97% | $7,436,973.78 |
| POWER/USDT:USDT | +1.69% | $14,196,894.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +2.71% | +2.76% |
| LSK/USDT:USDT | below_1h_threshold | +2.67% | +2.72% |
| BONER/USDT:USDT | below_1h_threshold | +2.39% | +2.44% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +2.08% | +2.13% |
| BTW/USDT:USDT | below_1h_threshold | +1.98% | +2.03% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
