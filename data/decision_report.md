# Decision Report

- generated_at: 2026-07-12T02:26:13.503426+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8560**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.47% / filled 20/20。**
- 全期間 MARKET基準: n=8560, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.47%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.47% | **+0.47%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +5.55% | **+1.39%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| MARKET | 20/20 | 100.0% | +0.47% | **+0.47%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +2.09% | **+1.77%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.47% | **+1.32%** |
| MARKET_LONG | 20/20 | 100.0% | +0.85% | **+0.85%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +1.34% | **+0.34%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +0.25% | **+0.07%** |

## 2. $100 Live Portfolio

- 残高: **$103.05** / 初期 $100.00 (+3.05%)
- 確定トレード: 85件 (TP 30 / SL 54 / EXP 1)
- 最新: CASHCAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.05
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$317.87** / 初期 $100.00 (+217.87%)
- 確定: 2748件 (Win 866 / Loss 921 / Flat 961) / skip 2373件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: T/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $317.87

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.11** / 初期 $100.00 (+5.11%)
- 確定: 643件 (Win 152 / Loss 159 / Flat 332) / skip 1328件
- 成長率目線: 平均log +0.000078 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $105.11

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.17** / 初期 $100.00 (-0.83%)
- 確定: 26件 (Win 9 / Loss 17 / Flat 0) / pending 0件 / skip 3件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000298 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: T/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $99.17

## 6. Latest Market Context

- 更新: 2026-07-12T02:26:07.176719+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=64095.4
- Funnel: target 863 → liquid 147 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SXT/USDT:USDT | +23.00% | $13,180,498.75 |
| CASHCAT/USDT:USDT | +17.19% | $2,108,391.82 |
| T/USDT:USDT | +10.46% | $12,524,939.97 |
| FHE/USDT:USDT | +9.05% | $1,462,679.62 |
| BILL/USDT:USDT | +8.57% | $1,308,869.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| T/USDT:USDT | below_1h_threshold | +4.75% | +4.77% |
| SXT/USDT:USDT | below_1h_threshold | +3.25% | +3.27% |
| B3/USDT:USDT | below_1h_threshold | +3.12% | +3.14% |
| US/USDT:USDT | below_1h_threshold | +2.51% | +2.53% |
| TAC/USDT:USDT | below_1h_threshold | +2.33% | +2.35% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
