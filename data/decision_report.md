# Decision Report

- generated_at: 2026-09-03T00:56:17.862597+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13405**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13405, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.79%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.79% | **-0.79%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 14/20 | 70.0% | +2.41% | **+1.69%** |
| LIMIT_6PCT | 10/20 | 50.0% | +2.57% | **+1.28%** |
| LIMIT_BB3S | 7/16 | 43.8% | +2.15% | **+0.94%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_8PCT | 5/20 | 25.0% | +2.34% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +2.52% | **+1.38%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +2.40% | **+1.20%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +2.06% | **+1.03%** |
| LIMIT_9PCT_LONG | 8/20 | 40.0% | +2.41% | **+0.96%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +0.47% | **+0.28%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 198件 (TP 74 / SL 119 / EXP 5)
- 最新: FONE/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$879.96** / 初期 $100.00 (+779.96%)
- 確定: 4996件 (Win 1516 / Loss 1638 / Flat 1842) / skip 4970件
- 成長率目線: 平均log +0.000435 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ARB/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.11% 残高後 $879.96

## 4. Robust Adaptive DryRun ($100)

- 残高: **$184.60** / 初期 $100.00 (+84.60%)
- 確定: 2372件 (Win 671 / Loss 576 / Flat 1125) / skip 4444件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0422 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $184.60

## 5. Causal Adaptive DryRun ($100)

- 残高: **$113.86** / 初期 $100.00 (+13.86%)
- 確定: 2111件 (Win 615 / Loss 830 / Flat 666) / pending 4件 / skip 2763件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000279 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $113.86

## 6. Latest Market Context

- 更新: 2026-09-03T00:56:08.305142+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.35% price=77031.2
- Funnel: target 1044 → liquid 160 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +53.07% | $74,132,608.45 |
| SNOWSTOCK/USDT:USDT | +22.01% | $1,443,267.94 |
| PONS/USDT:USDT | +18.87% | $3,744,959.58 |
| EDGE/USDT:USDT | +15.29% | $1,106,749.08 |
| EGLD/USDT:USDT | +9.82% | $9,563,763.58 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FF/USDT:USDT | below_1h_threshold | +3.96% | +4.31% |
| USELESS/USDT:USDT | below_1h_threshold | +3.46% | +3.81% |
| LIT/USDT:USDT | below_1h_threshold | +2.80% | +3.14% |
| ZRO/USDT:USDT | below_1h_threshold | +2.61% | +2.96% |
| PONS/USDT:USDT | below_1h_threshold | +1.37% | +1.72% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
