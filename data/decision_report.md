# Decision Report

- generated_at: 2026-11-23T08:41:36.350243+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19433**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19433, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.14%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.14% | **-1.14%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 18/20 | 90.0% | +1.02% | **+0.91%** |
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.59% | **+0.64%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +3.67% | **+1.84%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +3.42% | **+1.54%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.92% | **+0.86%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.30% | **+0.84%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.98% | **+0.84%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 285件 (TP 103 / SL 174 / EXP 8)
- 最新: BLESS/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,862.59** / 初期 $100.00 (+1762.59%)
- 確定: 7531件 (Win 2164 / Loss 2424 / Flat 2943) / skip 8463件
- 成長率目線: 平均log +0.000388 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ELSA/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $1,862.59

## 4. Robust Adaptive DryRun ($100)

- 残高: **$466.74** / 初期 $100.00 (+366.74%)
- 確定: 5195件 (Win 1385 / Loss 1117 / Flat 2693) / skip 7649件
- 成長率目線: 平均log +0.000297 / 幾何平均 +0.030% per trade / maxDD +4.29%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0697 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ELSA/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $466.74

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7595件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000147 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-23T08:41:21.732548+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=61468.8
- Funnel: target 1086 → liquid 120 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.4 >= 65=1, 4h RSI 80.0 >= 65=1, 4h RSI 73.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SI/USDT:USDT | +91.93% | $1,941,727.09 |
| ELSA/USDT:USDT | +31.15% | $2,343,056.39 |
| BULLA/USDT:USDT | +31.13% | $2,836,736.82 |
| ARIA/USDT:USDT | +24.62% | $2,533,781.59 |
| EVAA/USDT:USDT | +18.26% | $46,784,588.36 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_1h_threshold | +3.11% | +3.05% |
| JUP/USDT:USDT | below_1h_threshold | +1.61% | +1.55% |
| VELVET/USDT:USDT | below_1h_threshold | +1.58% | +1.52% |
| QNT/USDT:USDT | below_1h_threshold | +1.17% | +1.11% |
| LIT/USDT:USDT | below_1h_threshold | +0.98% | +0.92% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
