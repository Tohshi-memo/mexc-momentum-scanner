# Decision Report

- generated_at: 2026-11-23T12:11:16.904623+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19444**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19444, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.54%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.54% | **-0.54%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 4/20 | 20.0% | +3.41% | **+0.68%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_3PCT | 17/20 | 85.0% | +0.78% | **+0.67%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.67% | **+1.42%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.82% | **+0.53%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +1.60% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 285件 (TP 103 / SL 174 / EXP 8)
- 最新: BLESS/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,868.41** / 初期 $100.00 (+1768.41%)
- 確定: 7542件 (Win 2165 / Loss 2426 / Flat 2951) / skip 8463件
- 成長率目線: 平均log +0.000388 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_FIB1272_LONG` SL_HIT account -0.50% 残高後 $1,868.41

## 4. Robust Adaptive DryRun ($100)

- 残高: **$469.95** / 初期 $100.00 (+369.95%)
- 確定: 5205件 (Win 1386 / Loss 1117 / Flat 2702) / skip 7650件
- 成長率目線: 平均log +0.000297 / 幾何平均 +0.030% per trade / maxDD +4.29%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0608 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_FIB1272` TP_HIT account +0.69% 残高後 $469.95

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7603件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000157 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-23T12:11:05.537427+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=61412.0
- Funnel: target 1088 → liquid 119 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SI/USDT:USDT | +85.37% | $2,329,604.48 |
| BULLA/USDT:USDT | +36.07% | $3,326,604.65 |
| ARIA/USDT:USDT | +34.83% | $4,449,938.45 |
| EVAA/USDT:USDT | +31.95% | $41,880,661.32 |
| ELSA/USDT:USDT | +20.50% | $2,592,200.58 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BULLA/USDT:USDT | below_1h_threshold | +3.60% | +3.58% |
| ELSA/USDT:USDT | below_1h_threshold | +3.54% | +3.53% |
| IDOL/USDT:USDT | below_1h_threshold | +2.79% | +2.77% |
| QNT/USDT:USDT | below_1h_threshold | +1.14% | +1.13% |
| BLESS/USDT:USDT | below_1h_threshold | +1.01% | +0.99% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
