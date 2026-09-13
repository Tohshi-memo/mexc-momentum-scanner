# Decision Report

- generated_at: 2026-09-13T02:46:29.537635+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14353**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14353, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.11%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.11% | **-0.11%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 6/20 | 30.0% | +3.28% | **+0.99%** |
| LIMIT_9PCT | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.69% | **+0.69%** |
| LIMIT_7PCT | 8/20 | 40.0% | +1.55% | **+0.62%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.61% | **+0.45%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/12 | 50.0% | +3.66% | **+1.83%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +4.99% | **+1.75%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +3.97% | **+1.59%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.40% | **+1.12%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.86% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,080.43** / 初期 $100.00 (+980.43%)
- 確定: 5430件 (Win 1635 / Loss 1760 / Flat 2035) / skip 5484件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,080.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$218.47** / 初期 $100.00 (+118.47%)
- 確定: 2871件 (Win 795 / Loss 670 / Flat 1406) / skip 4893件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1342 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $218.47

## 5. Causal Adaptive DryRun ($100)

- 残高: **$125.85** / 初期 $100.00 (+25.85%)
- 確定: 2804件 (Win 833 / Loss 1078 / Flat 893) / pending 5件 / skip 3016件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000436 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $125.85

## 6. Latest Market Context

- 更新: 2026-09-13T02:46:13.604092+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=77268.3
- Funnel: target 1068 → liquid 126 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 97.6 >= 65=1, 4h RSI 93.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LSK/USDT:USDT | +143.86% | $68,257,241.54 |
| POWR/USDT:USDT | +49.69% | $1,319,591.01 |
| ZCAT/USDT:USDT | +27.96% | $1,139,569.10 |
| STORJ/USDT:USDT | +20.89% | $19,287,878.70 |
| ALCH/USDT:USDT | +17.99% | $2,690,753.59 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VTHO/USDT:USDT | below_1h_threshold | +2.96% | +2.98% |
| POWR/USDT:USDT | below_1h_threshold | +2.87% | +2.89% |
| STORJ/USDT:USDT | below_1h_threshold | +2.37% | +2.39% |
| STX/USDT:USDT | below_1h_threshold | +1.55% | +1.57% |
| AKE/USDT:USDT | below_1h_threshold | +1.00% | +1.03% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
