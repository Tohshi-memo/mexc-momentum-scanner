# Decision Report

- generated_at: 2026-07-13T08:16:11.445776+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8626**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.93% / filled 20/20。**
- 全期間 MARKET基準: n=8626, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.93%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.93% | **+2.93%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.93% | **+2.93%** |
| LIMIT_1PCT | 18/20 | 90.0% | +2.65% | **+2.39%** |
| LIMIT_2PCT | 15/20 | 75.0% | +2.28% | **+1.71%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.51% | **+0.98%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.49% | **+0.62%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/6 | 83.3% | +0.53% | **+0.45%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -0.33% | **-0.07%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -2.30% | **-0.35%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | -0.73% | **-0.40%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -4.00% | **-0.40%** |

## 2. $100 Live Portfolio

- 残高: **$101.20** / 初期 $100.00 (+1.20%)
- 確定トレード: 91件 (TP 30 / SL 59 / EXP 2)
- 最新: ANSEM/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.20
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$321.39** / 初期 $100.00 (+221.39%)
- 確定: 2795件 (Win 876 / Loss 923 / Flat 996) / skip 2392件
- 成長率目線: 平均log +0.000418 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: XEC/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $321.39

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.11** / 初期 $100.00 (+5.11%)
- 確定: 645件 (Win 152 / Loss 159 / Flat 334) / skip 1392件
- 成長率目線: 平均log +0.000077 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ANSEM/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $105.11

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.36** / 初期 $100.00 (+0.36%)
- 確定: 31件 (Win 13 / Loss 18 / Flat 0) / pending 1件 / skip 62件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000685 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: XEC/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $100.36

## 6. Latest Market Context

- 更新: 2026-07-13T08:16:04.148040+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=63028.5
- Funnel: target 863 → liquid 144 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| XEC/USDT:USDT | +27.62% | $3,971,743.40 |
| DODO/USDT:USDT | +25.95% | $7,107,029.75 |
| JCT/USDT:USDT | +23.91% | $1,069,694.59 |
| KITE/USDT:USDT | +15.31% | $1,702,476.55 |
| JTO/USDT:USDT | +8.44% | $2,146,992.20 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VELVET/USDT:USDT | below_1h_threshold | +3.62% | +3.50% |
| BILL/USDT:USDT | below_1h_threshold | +3.61% | +3.49% |
| DODO/USDT:USDT | below_1h_threshold | +3.42% | +3.30% |
| JTO/USDT:USDT | below_1h_threshold | +1.59% | +1.47% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +1.48% | +1.36% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
