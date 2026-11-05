# Decision Report

- generated_at: 2026-11-05T00:11:18.612517+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18145**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18145, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.07%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.07% | **-0.07%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +5.85% | **+1.17%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.80% | **+0.56%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.39% | **+0.27%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +2.52% | **+1.76%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +2.12% | **+1.27%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +2.50% | **+1.25%** |
| LIMIT_ATR_LONG | 17/20 | 85.0% | +1.09% | **+0.92%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.70% | **+0.77%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 262件 (TP 96 / SL 158 / EXP 8)
- 最新: SOXS/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,510.57** / 初期 $100.00 (+1410.57%)
- 確定: 6964件 (Win 2015 / Loss 2236 / Flat 2713) / skip 7742件
- 成長率目線: 平均log +0.000390 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SOXS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,510.57

## 4. Robust Adaptive DryRun ($100)

- 残高: **$374.63** / 初期 $100.00 (+274.63%)
- 確定: 4554件 (Win 1223 / Loss 1028 / Flat 2303) / skip 7002件
- 成長率目線: 平均log +0.000290 / 幾何平均 +0.029% per trade / maxDD +4.25%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOXS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $374.63

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6305件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000140 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-05T00:11:08.697054+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.21% price=80632.4
- Funnel: target 1078 → liquid 187 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ELSA/USDT:USDT | +39.52% | $1,900,189.54 |
| APPSTOCK/USDT:USDT | +22.66% | $1,206,586.63 |
| FLUID/USDT:USDT | +12.04% | $3,390,375.48 |
| STX/USDT:USDT | +5.06% | $3,932,889.82 |
| MRNASTOCK/USDT:USDT | +4.46% | $4,378,714.51 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ELSA/USDT:USDT | below_1h_threshold | +3.57% | +3.36% |
| BIRB/USDT:USDT | below_1h_threshold | +1.75% | +1.54% |
| SQQQ/USDT:USDT | below_1h_threshold | +1.33% | +1.13% |
| AIN/USDT:USDT | below_1h_threshold | +0.78% | +0.57% |
| BEAT/USDT:USDT | below_1h_threshold | +0.73% | +0.53% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
