# Decision Report

- generated_at: 2026-08-01T21:21:18.636673+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10121**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10121, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.94% | **+0.78%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +2.00% | **+1.60%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.19% | **+1.53%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.28% | **+1.48%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.26% | **+1.47%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.00% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$571.50** / 初期 $100.00 (+471.50%)
- 確定: 3643件 (Win 1159 / Loss 1191 / Flat 1293) / skip 3039件
- 成長率目線: 平均log +0.000478 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $571.50

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.81** / 初期 $100.00 (+40.81%)
- 確定: 1280件 (Win 359 / Loss 297 / Flat 624) / skip 2252件
- 成長率目線: 平均log +0.000267 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $140.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$112.10** / 初期 $100.00 (+12.10%)
- 確定: 930件 (Win 295 / Loss 363 / Flat 272) / pending 3件 / skip 659件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000263 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $112.10

## 6. Latest Market Context

- 更新: 2026-08-01T21:21:11.434373+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.17% price=62737.7
- Funnel: target 922 → liquid 133 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| 1000RATS/USDT:USDT | +22.07% | $18,899,182.82 |
| UAI/USDT:USDT | +22.02% | $13,626,674.27 |
| AKE/USDT:USDT | +21.77% | $32,805,011.93 |
| BLESS/USDT:USDT | +16.84% | $4,005,651.09 |
| TAG/USDT:USDT | +8.20% | $1,874,563.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GIGGLE/USDT:USDT | below_1h_threshold | +2.99% | +2.82% |
| BLESS/USDT:USDT | below_1h_threshold | +2.29% | +2.12% |
| UAI/USDT:USDT | below_1h_threshold | +2.14% | +1.97% |
| MMT/USDT:USDT | below_1h_threshold | +1.38% | +1.21% |
| XPL/USDT:USDT | below_1h_threshold | +1.02% | +0.85% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
