# Decision Report

- generated_at: 2026-09-16T22:46:21.617928+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14744**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14744, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +2.48% | **+0.74%** |
| LIMIT_7PCT | 4/20 | 20.0% | +3.70% | **+0.74%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.47% | **+0.69%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.28% | **+0.26%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +7.56% | **+5.04%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.39% | **+1.04%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.07% | **+1.02%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.54% | **+0.69%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.43% | **+0.64%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,165.60** / 初期 $100.00 (+1065.60%)
- 確定: 5599件 (Win 1679 / Loss 1813 / Flat 2107) / skip 5706件
- 成長率目線: 平均log +0.000439 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BULLA/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,165.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$240.73** / 初期 $100.00 (+140.73%)
- 確定: 3129件 (Win 870 / Loss 746 / Flat 1513) / skip 5026件
- 成長率目線: 平均log +0.000281 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.1108 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $240.73

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.53** / 初期 $100.00 (+23.53%)
- 確定: 2956件 (Win 878 / Loss 1165 / Flat 913) / pending 0件 / skip 3260件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000306 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CNPY/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $123.53

## 6. Latest Market Context

- 更新: 2026-09-16T22:46:09.099060+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.21% price=75779.3
- Funnel: target 1059 → liquid 155 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BATON/USDT:USDT | +36.35% | $2,233,674.11 |
| HNT/USDT:USDT | +34.51% | $3,874,281.10 |
| BULLA/USDT:USDT | +31.05% | $7,714,477.27 |
| LONGXIA/USDT:USDT | +12.96% | $2,889,470.46 |
| POWER/USDT:USDT | +9.72% | $5,168,959.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UAI/USDT:USDT | below_1h_threshold | +3.04% | +3.25% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +2.61% | +2.82% |
| CNPY/USDT:USDT | below_1h_threshold | +2.39% | +2.60% |
| HEI/USDT:USDT | below_1h_threshold | +1.30% | +1.51% |
| ON/USDT:USDT | below_1h_threshold | +0.87% | +1.08% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
