# Decision Report

- generated_at: 2026-09-23T06:36:23.428928+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15402**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15402, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.29%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.29% | **-0.29%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +3.88% | **+0.97%** |
| LIMIT_6PCT | 8/20 | 40.0% | +1.92% | **+0.77%** |
| LIMIT_7PCT | 6/20 | 30.0% | +2.54% | **+0.76%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.50% | **+0.25%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.89% | **+1.89%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +2.26% | **+1.70%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.16% | **+1.41%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.71% | **+1.11%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |

## 2. $100 Live Portfolio

- 残高: **$120.32** / 初期 $100.00 (+20.32%)
- 確定トレード: 217件 (TP 79 / SL 133 / EXP 5)
- 最新: LONGXIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.32
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,169.81** / 初期 $100.00 (+1069.81%)
- 確定: 5875件 (Win 1733 / Loss 1883 / Flat 2259) / skip 6088件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LONGXIA/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $1,169.81

## 4. Robust Adaptive DryRun ($100)

- 残高: **$249.25** / 初期 $100.00 (+149.25%)
- 確定: 3356件 (Win 927 / Loss 782 / Flat 1647) / skip 5457件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LONGXIA/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $249.25

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.15** / 初期 $100.00 (+21.15%)
- 確定: 3131件 (Win 920 / Loss 1232 / Flat 979) / pending 5件 / skip 3745件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000188 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LONGXIA/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $121.15

## 6. Latest Market Context

- 更新: 2026-09-23T06:36:12.316866+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=86429.9
- Funnel: target 1061 → liquid 192 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SHROOM/USDT:USDT | +64.64% | $1,246,302.79 |
| LONGXIA/USDT:USDT | +46.73% | $1,472,092.36 |
| NIL/USDT:USDT | +28.60% | $7,719,406.98 |
| SAGA/USDT:USDT | +23.94% | $2,048,100.05 |
| ALLO/USDT:USDT | +19.90% | $2,655,194.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BCH/USDT:USDT | below_1h_threshold | +4.26% | +4.28% |
| SAGA/USDT:USDT | below_1h_threshold | +3.79% | +3.81% |
| CHR/USDT:USDT | below_1h_threshold | +3.02% | +3.04% |
| FOLKS/USDT:USDT | below_1h_threshold | +3.02% | +3.04% |
| NIL/USDT:USDT | below_1h_threshold | +2.84% | +2.86% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
