# Decision Report

- generated_at: 2026-08-23T21:41:35.089230+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12473**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12473, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-2.01%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.01% | **-2.01%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_BB3S | 8/14 | 57.1% | +0.92% | **+0.53%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.63% | **+0.29%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/6 | 83.3% | +5.34% | **+4.45%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +4.31% | **+2.59%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +4.93% | **+2.22%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +3.36% | **+1.85%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.65% | **+1.59%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$723.66** / 初期 $100.00 (+623.66%)
- 確定: 4500件 (Win 1374 / Loss 1471 / Flat 1655) / skip 4534件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UNI/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account +0.75% 残高後 $723.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$157.26** / 初期 $100.00 (+57.26%)
- 確定: 1949件 (Win 536 / Loss 469 / Flat 944) / skip 3935件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0087 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UNI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $157.26

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.75** / 初期 $100.00 (+16.75%)
- 確定: 1868件 (Win 551 / Loss 708 / Flat 609) / pending 3件 / skip 2081件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000096 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TUT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $116.75

## 6. Latest Market Context

- 更新: 2026-08-23T21:41:24.422291+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.29% price=77602.9
- Funnel: target 1018 → liquid 169 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TUT/USDT:USDT | +18.46% | $62,652,870.87 |
| BASECAT/USDT:USDT | +13.45% | $2,899,009.04 |
| PENGU/USDT:USDT | +13.02% | $20,167,784.25 |
| 1000RATS/USDT:USDT | +11.75% | $2,182,146.05 |
| BRETT/USDT:USDT | +10.48% | $1,427,440.37 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SPK/USDT:USDT | below_1h_threshold | +3.25% | +2.96% |
| FLOKI/USDT:USDT | below_1h_threshold | +3.01% | +2.71% |
| BASECAT/USDT:USDT | below_1h_threshold | +2.88% | +2.59% |
| MORPHO/USDT:USDT | below_1h_threshold | +2.67% | +2.38% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +2.31% | +2.02% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
