# Decision Report

- generated_at: 2026-08-01T13:26:16.060851+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10092**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10092, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 18/20 | 90.0% | +1.25% | **+1.12%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.69% | **+0.66%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.86% | **+0.56%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.62% | **+0.40%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +5.86% | **+5.86%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +3.29% | **+0.82%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +1.18% | **+0.71%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.40% | **+0.42%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.28% | **+0.24%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$573.69** / 初期 $100.00 (+473.69%)
- 確定: 3632件 (Win 1158 / Loss 1190 / Flat 1284) / skip 3021件
- 成長率目線: 平均log +0.000481 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UAI/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $573.69

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.81** / 初期 $100.00 (+40.81%)
- 確定: 1279件 (Win 359 / Loss 297 / Flat 623) / skip 2224件
- 成長率目線: 平均log +0.000268 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $140.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$111.15** / 初期 $100.00 (+11.15%)
- 確定: 903件 (Win 286 / Loss 353 / Flat 264) / pending 2件 / skip 656件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000075 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: UAI/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $111.15

## 6. Latest Market Context

- 更新: 2026-08-01T13:26:08.870990+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=63059.3
- Funnel: target 921 → liquid 146 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IDOL/USDT:USDT | +46.13% | $1,051,945.75 |
| EPIC/USDT:USDT | +28.88% | $1,078,254.22 |
| UAI/USDT:USDT | +27.33% | $4,447,189.24 |
| BTW/USDT:USDT | +26.78% | $11,264,852.15 |
| TAKE/USDT:USDT | +24.01% | $1,291,991.55 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UAI/USDT:USDT | below_1h_threshold | +4.59% | +4.60% |
| TAKE/USDT:USDT | below_1h_threshold | +3.92% | +3.94% |
| BTW/USDT:USDT | below_1h_threshold | +3.35% | +3.37% |
| SATS/USDT:USDT | below_1h_threshold | +2.83% | +2.84% |
| MYX/USDT:USDT | below_1h_threshold | +2.60% | +2.61% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
